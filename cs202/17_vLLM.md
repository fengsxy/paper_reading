---
layout: default
title: "vLLM"
description: "PagedAttention"
parent: CS 202 论文解读
nav_order: 17
---

# vLLM: Efficient Memory Management for Large Language Model Serving with PagedAttention

**Kwon et al., SOSP 2023**

---

## 1. 论文背景与动机

大语言模型（LLM）的推理服务正在成为现代 AI 基础设施中最关键的环节之一。当用户向 ChatGPT 这样的服务发送请求时，模型需要逐 token 地生成回复，而在这个自回归（autoregressive）生成过程中，每一步都需要访问之前所有 token 的 key 和 value 向量——这就是所谓的 KV cache。

KV cache 的内存管理是 LLM serving 的核心瓶颈。以一个 13B 参数的 OPT 模型为例，单个请求的 KV cache 可能占用数百 MB 到数 GB 的 GPU 显存。问题在于：请求的输出长度是事先未知的，这意味着系统必须为每个请求预分配一块连续的显存空间来存放 KV cache。在实践中，现有系统（如 FasterTransformer、Orca 等）采用的策略是按照模型允许的最大序列长度预分配内存，这导致了严重的内存浪费。

作者通过分析发现，现有 LLM serving 系统中 KV cache 的内存浪费主要来自三个方面：

- **内部碎片（Internal Fragmentation）**：为请求预分配的连续内存块中，实际生成的 token 数往往远小于最大长度，大量预留空间被浪费。
- **外部碎片（External Fragmentation）**：不同请求的 KV cache 大小各异，频繁的分配和释放导致显存中出现大量无法利用的小空闲块。
- **预留浪费（Reservation Waste）**：由于无法预知输出长度，系统倾向于过度预留，进一步加剧浪费。

实测数据显示，在现有系统中，实际有效利用的 KV cache 内存仅占总分配量的 20.4%–38.2%。这意味着超过 60% 的宝贵 GPU 显存被白白浪费了。显存利用率直接决定了系统能同时处理多少请求（即 batch size），而 batch size 又直接影响吞吐量。因此，KV cache 的内存管理效率是提升 LLM serving 性能的关键杠杆。

## 2. 核心设计与关键创新

vLLM 的核心洞察极为精妙：KV cache 的内存管理问题，本质上与操作系统中的虚拟内存管理问题高度相似。操作系统通过分页（paging）机制，将进程的连续虚拟地址空间映射到不连续的物理内存页上，从而消除了外部碎片并实现了灵活的内存管理。vLLM 将这一经典思想引入 GPU 显存管理，提出了 **PagedAttention** 算法。

### PagedAttention

PagedAttention 的核心思想是将每个请求的 KV cache 分割成固定大小的 **block**（类比 OS 中的页），每个 block 存储固定数量 token 的 key 和 value 向量。这些 block 不需要在物理显存中连续存放——就像虚拟内存页不需要对应连续的物理页框一样。

系统维护一个 **block table**（类比页表），记录每个请求的逻辑 block 到物理 block 的映射关系。当 attention 计算需要访问某个 token 的 KV 向量时，通过 block table 查找其实际物理位置。这个查找过程被集成到了 attention kernel 中，开销极小。

### KV Cache Manager

vLLM 引入了一个集中式的 KV cache manager，负责物理 block 的分配和回收。其工作方式类似 OS 的物理内存分配器：

- 维护一个 **free block pool**，按需为请求分配物理 block。
- 请求生成新 token 时，仅在当前 block 填满后才分配新 block，实现了按需分配（demand paging 的思想）。
- 请求完成后，其占用的所有物理 block 被回收到 free pool。

这种设计彻底消除了内部碎片（最多浪费最后一个 block 的部分空间）和外部碎片（所有 block 大小相同，任何空闲 block 都可被任何请求使用）。

### Copy-on-Write（写时复制）

在 beam search、parallel sampling 等场景中，多个候选序列共享相同的前缀（prompt 部分的 KV cache 完全相同）。vLLM 借鉴 OS 中 fork() 的 copy-on-write 机制：共享前缀的多个序列指向相同的物理 block，仅当某个序列需要修改（即在该 block 上追加不同的 token）时，才复制出一个新的物理 block。这大幅减少了 beam search 等场景下的内存开销。

### 调度与抢占

当 GPU 显存不足以容纳所有活跃请求时，vLLM 支持请求级别的抢占（preemption）。被抢占的请求的 KV cache block 可以被 swap 到 CPU 内存（类比 OS 的 swap），待显存空闲后再 swap 回来继续生成。这使得系统能够在高负载下优雅降级，而非简单拒绝新请求。

## 3. 重要的技术细节

### Block 大小的选择

Block 大小是一个关键的设计参数。太小的 block 会增加 block table 的开销和 attention kernel 中的间接寻址次数；太大的 block 则会增加最后一个 block 的内部碎片。论文通过实验发现 block size = 16 tokens 是一个较好的平衡点。

### Attention Kernel 的修改

标准的 attention 实现假设 KV cache 在内存中连续存放。PagedAttention 需要修改 attention kernel，使其能够根据 block table 从不连续的物理位置读取 KV 向量。具体来说，kernel 在计算 attention score 时，对每个 block 独立计算 partial softmax，然后合并结果。这个修改对计算效率的影响很小，因为 attention 计算本身是 memory-bound 的，额外的间接寻址开销可以被内存访问延迟掩盖。

### 分布式执行

在 tensor parallelism 场景下，vLLM 采用单一的 KV cache manager 控制所有 GPU worker 的 block 分配。由于所有 worker 处理相同的输入，它们的 KV cache 分配模式完全一致，因此只需一个集中式 manager 即可，无需复杂的分布式协调。

### 与 Continuous Batching 的结合

vLLM 在 Orca 提出的 iteration-level scheduling（continuous batching）基础上进一步优化。每次迭代后，已完成的请求立即释放其 block，新请求可以立即加入 batch。PagedAttention 使得这种动态 batching 更加高效，因为新请求只需分配少量初始 block，而非预留整个最大长度的连续空间。

## 4. 优缺点分析

### 优点

1. **显著提升吞吐量**：通过近乎最优的内存利用率，vLLM 能够支持 2–4 倍于现有系统的 batch size，从而将吞吐量提升 2–4 倍，在复杂解码场景（如 beam search）下提升可达 2.2 倍。

2. **设计优雅，概念清晰**：将 OS 虚拟内存的经典抽象直接映射到 GPU 显存管理，概念简洁，易于理解和实现。这种跨领域的类比是系统研究中最有力的设计方法之一。

3. **通用性强**：PagedAttention 不依赖特定的模型架构或解码算法，可以与各种 LLM 和采样策略配合使用。

4. **工程实现完整**：vLLM 不仅是一篇论文，更是一个完整的开源系统，迅速成为 LLM serving 的事实标准。

### 缺点

1. **Attention kernel 开销**：虽然论文声称间接寻址开销很小，但在某些 GPU 架构和 workload 下，非连续内存访问可能影响 cache locality，导致一定的性能损失。

2. **Block 大小固定**：固定的 block 大小可能不适合所有场景。短请求可能浪费最后一个 block 的空间，而极长请求的 block table 可能变得较大。

3. **CPU swap 的延迟**：当发生抢占需要将 KV cache swap 到 CPU 时，PCIe 带宽成为瓶颈，可能导致被抢占请求的恢复延迟较高。

4. **单机设计**：论文主要关注单节点（可能多 GPU）的场景，对于跨节点的分布式 serving 场景讨论较少。

## 5. 历史影响与后续发展

vLLM 的影响是深远且即时的。论文发表于 SOSP 2023，而其开源实现在论文发表前就已经在工业界广泛采用。截至目前，vLLM 已成为 LLM serving 领域最流行的开源框架之一，被众多公司和研究机构用于生产环境。

从学术角度看，vLLM 展示了操作系统经典概念在新兴领域的强大生命力。虚拟内存、分页、copy-on-write 这些诞生于 1960–1970 年代的思想，在 2023 年的 GPU 显存管理中焕发了新的活力。这提醒我们，系统设计的基本原则具有跨时代的普适性。

后续工作在多个方向上扩展了 vLLM 的思想：prefix caching（跨请求共享公共前缀的 KV cache）、speculative decoding 的集成、更细粒度的内存管理（如 token-level 而非 block-level）、以及跨节点的分布式 KV cache 管理。PagedAttention 的思想也被集成到了 NVIDIA 的 TensorRT-LLM 等商业框架中。

vLLM 是一个教科书级的系统研究案例：识别实际瓶颈，从经典理论中汲取灵感，提出简洁优雅的解决方案，并通过完整的工程实现产生实际影响。对于操作系统课程的学生来说，它完美地展示了 OS 抽象的力量——你在课堂上学到的页表和虚拟内存，正在驱动当今最前沿的 AI 系统。
