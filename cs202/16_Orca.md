---
layout: default
title: "Orca"
description: "分布式共享对象"
parent: CS 202 论文解读
nav_order: 16
---

# Orca: A Distributed Serving System for Transformer-Based Generative Models

**论文信息：** Gyeong-In Yu, Joo Seong Jeong, Geon-Woo Kim, Soojeong Kim, Byung-Gon Chun, OSDI 2022

---

## 1. 论文背景与动机

2022 年，大型语言模型（LLM）正处于爆发的前夜。GPT-3 已经展示了大规模 Transformer 模型的惊人能力，但如何高效地部署和服务这些模型，仍然是一个严峻的工程挑战。

Transformer 生成模型的推理过程有一个独特的特征：自回归生成（autoregressive generation）。模型每次 forward pass 只生成一个 token，然后将这个 token 追加到输入序列中，再进行下一次 forward pass，如此循环直到生成完整的输出。这意味着生成一个 100 token 的回复需要 100 次 forward pass，每次的计算量还随序列长度递增。

当时主流的 serving 系统（如 NVIDIA Triton、FasterTransformer）采用的是 request-level scheduling（请求级调度）：将多个请求组成一个 batch，这个 batch 中的所有请求从头到尾一起执行。一个 batch 的执行时间由最慢的请求决定——如果 batch 中有一个请求需要生成 500 个 token，而其他请求只需要 50 个 token，那些早已完成的请求必须"陪跑"到最慢的请求结束，GPU 在这段时间内做的是无用功。

这个问题在实际部署中非常严重。不同请求的输出长度差异巨大（从几个 token 到几千个 token），request-level batching 导致：

- **GPU 利用率低下：** 短请求完成后 GPU 空转等待长请求。
- **延迟不可控：** 短请求的延迟被长请求拖累。
- **吞吐量受限：** 新请求必须等待当前 batch 完全结束才能开始处理。

Orca 的核心动机就是打破 request-level scheduling 的限制，实现更细粒度的调度。

## 2. 核心设计与关键创新

### Iteration-Level Scheduling（迭代级调度）

Orca 最核心的创新是将调度粒度从 request level 细化到 iteration level。具体来说：

在每次 forward pass（即每个 iteration）结束后，调度器重新评估当前 batch 的组成：
- 已经生成完 EOS token（结束标记）的请求立即从 batch 中移除，释放资源。
- 等待队列中的新请求可以立即加入 batch，填补空出的位置。

这意味着 batch 的组成是动态变化的——不再是一组请求从头到尾绑定在一起，而是每个 iteration 都可能有请求加入或离开。这从根本上消除了"短请求陪跑长请求"的问题。

### Selective Batching（选择性批处理）

Iteration-level scheduling 带来了一个新的技术挑战：batch 中不同请求处于不同的生成阶段。有些请求刚刚加入，需要处理完整的 prompt（可能有数百个 token）；有些请求已经生成了很多 token，每次只需要处理一个新 token。

在传统的 batching 中，batch 内所有请求的输入长度必须相同（通过 padding 对齐）。但在 Orca 中，不同请求的输入长度差异巨大，简单的 padding 会造成严重的计算浪费。

Orca 的解决方案是 selective batching：根据 Transformer 每一层的计算特性，选择性地决定是否对该层进行 batching。

**Attention 层：** 每个请求的 attention 计算依赖于该请求自己的 KV cache（历史 key-value 对），不同请求之间没有数据依赖。因此 attention 层不进行 batching，而是逐个请求独立计算。

**非 Attention 层（FFN、LayerNorm 等）：** 这些层的计算是 token-wise 的，不同请求的 token 可以拼接成一个大 batch 一起计算，充分利用 GPU 的并行能力。

这种选择性的 batching 策略既避免了 padding 的浪费，又保留了 batching 带来的 GPU 利用率提升。

### 调度器设计

Orca 的调度器在每个 iteration 开始前执行以下逻辑：

1. **检查完成：** 扫描当前 batch，移除已生成 EOS 的请求。
2. **准入控制：** 根据当前 GPU 内存使用情况（主要是 KV cache 占用），决定可以加入多少新请求。
3. **请求选择：** 从等待队列中选择请求加入 batch。可以使用 FCFS（先来先服务）或其他策略。
4. **执行：** 对更新后的 batch 执行一次 forward pass。

准入控制是关键——KV cache 的内存占用随序列长度线性增长，如果 batch 中的请求过多或序列过长，可能导致 GPU 内存溢出。调度器需要动态估算内存需求并做出保守的准入决策。

## 3. 重要的技术细节

### KV Cache 管理

在自回归生成中，每个请求需要维护一个 KV cache，存储之前所有 token 在每一层 attention 中的 key 和 value 向量。KV cache 的大小与序列长度成正比，对于大模型来说，这是 GPU 内存的主要消耗者。

Orca 需要高效地管理动态变化的 KV cache：
- 新请求加入时，分配 KV cache 空间。
- 请求完成时，释放 KV cache 空间。
- 每个 iteration 后，为每个请求的 KV cache 追加新的 key-value 对。

论文中 Orca 使用预分配的连续内存块来管理 KV cache，按请求的最大可能长度预分配。这种方式简单但存在内存碎片问题——后来的 vLLM 论文（2023）通过 PagedAttention 机制解决了这个问题。

### Prompt 处理（Prefill）与生成（Decode）的分离

当一个新请求加入 batch 时，它首先需要处理完整的 prompt（prefill 阶段），然后才能进入逐 token 生成的 decode 阶段。Prefill 阶段的计算量远大于 decode 阶段（因为需要一次性处理所有 prompt token），这会导致该 iteration 的延迟显著增加，影响 batch 中其他正在 decode 的请求。

Orca 的处理方式是将 prefill 和 decode 混合在同一个 iteration 中执行。通过 selective batching，prefill 请求的大量 token 和 decode 请求的单个 token 可以在非 attention 层中一起 batch 处理，而在 attention 层中独立计算。这种混合执行在一定程度上缓解了 prefill 对 decode 延迟的影响，但并未完全解决——后续的 Sarathi（2023）和 Splitwise（2024）等工作进一步优化了 prefill-decode 的调度。

### 分布式执行

对于超大模型（参数量超过单 GPU 内存），Orca 支持模型并行（model parallelism）。论文主要讨论了 pipeline parallelism（流水线并行）：将模型的不同层分配到不同的 GPU 上，请求在 GPU 之间流水线式地传递。

Iteration-level scheduling 与 pipeline parallelism 的结合需要仔细设计：每个 GPU 上的 micro-batch 组成可能不同，调度器需要协调所有 GPU 上的请求状态。Orca 通过一个集中式的调度器来管理全局状态，各 GPU 上的 worker 按调度器的指令执行。

### 性能评估

论文在 GPT-2（1.5B 参数）和一个 341B 参数的内部模型上进行了评估。关键结果：

- **吞吐量：** 在相同延迟约束下，Orca 的吞吐量比 FasterTransformer 高 36.9 倍（在请求输出长度差异大的场景下）。即使在输出长度相对均匀的场景下，也有数倍的提升。
- **延迟：** Orca 显著降低了短请求的尾延迟（P99 延迟），因为短请求不再被长请求拖累。
- **GPU 利用率：** 通过动态 batch 管理，GPU 的计算利用率大幅提升。

36.9 倍的吞吐量提升数字非常惊人，但需要注意这是在极端场景下（输出长度从 1 到 512 均匀分布）的结果。在更现实的工作负载下，提升幅度会小一些，但仍然非常显著。

## 4. 优缺点分析

### 优点

- **思想简洁而深刻：** Iteration-level scheduling 的核心思想非常直观——既然生成是逐 token 进行的，调度也应该逐 iteration 进行。这种"调度粒度匹配计算粒度"的思想具有普遍意义。
- **性能提升巨大：** 在实际工作负载下，吞吐量提升数倍到数十倍，这对于降低 LLM 部署成本至关重要。
- **工程可行性强：** Orca 的设计不需要修改模型架构，只需要修改 serving 框架的调度逻辑，易于集成到现有系统中。
- **开创性：** 作为第一篇系统性地研究 LLM serving 调度问题的论文，Orca 定义了这个领域的问题框架和基本术语。

### 缺点

- **KV cache 管理粗糙：** 预分配连续内存块的方式导致内存利用率不高，限制了 batch size 的上限。这个问题后来被 vLLM 的 PagedAttention 解决。
- **Prefill-Decode 干扰：** 混合执行 prefill 和 decode 会导致 decode 请求的延迟抖动。论文没有深入讨论这个问题的解决方案。
- **调度策略简单：** 论文主要使用 FCFS 调度，没有考虑请求优先级、公平性、SLO（服务级别目标）等实际部署中的重要需求。
- **缺乏对 tensor parallelism 的讨论：** 论文主要讨论 pipeline parallelism，但实际部署中 tensor parallelism（将单层的计算分布到多个 GPU）更为常用。
- **评估模型规模有限：** 论文发表时最大的评估模型为 341B 参数，而当今主流模型（如 Llama 3 405B、GPT-4）的规模和架构特征可能带来新的挑战。

## 5. 历史影响与后续发展

Orca 是 LLM serving 系统领域的开山之作。它发表于 OSDI 2022，恰好赶上了 ChatGPT 引爆的 LLM 浪潮。论文提出的 iteration-level scheduling 和 selective batching 已经成为所有现代 LLM serving 系统的标准设计。

**vLLM（2023）：** UC Berkeley 的 vLLM 在 Orca 的基础上，通过 PagedAttention 解决了 KV cache 的内存碎片问题。PagedAttention 将 KV cache 分成固定大小的页（page），按需分配和释放，类似操作系统的虚拟内存管理。vLLM 继承了 Orca 的 iteration-level scheduling（在 vLLM 中称为 continuous batching），并成为最流行的开源 LLM serving 框架之一。

**Continuous Batching 的普及：** Orca 提出的 iteration-level scheduling 在工业界被广泛采用，通常被称为 continuous batching。TensorRT-LLM（NVIDIA）、TGI（Hugging Face）、DeepSpeed-FastGen（Microsoft）等主流 serving 框架都实现了这一机制。可以说，continuous batching 已经成为 LLM serving 的事实标准。

**Prefill-Decode 分离：** Orca 未能完美解决的 prefill-decode 干扰问题催生了一系列后续工作。Sarathi（2023）提出了 chunked prefill，将长 prompt 分成小块与 decode 交错执行。Splitwise（2024）和 DistServe（2024）则提出将 prefill 和 decode 分配到不同的 GPU 上，彻底消除干扰。

**投机解码（Speculative Decoding）：** 另一个重要的后续方向是投机解码——用一个小模型快速生成候选 token 序列，然后用大模型并行验证。这与 Orca 的 iteration-level scheduling 正交，可以结合使用。

**对系统研究的启示：** Orca 的成功说明了一个重要的系统设计原则：当工作负载的特征发生根本性变化时（从传统的 batch inference 到自回归生成），调度策略也必须相应地重新设计。简单地复用旧的调度框架会导致巨大的效率损失。这个教训对于任何面临新型工作负载的系统设计者都具有参考价值。

Orca 论文的历史地位类似于 MapReduce 之于大数据处理——它不一定是技术上最完美的方案，但它第一个清晰地定义了问题、提出了核心抽象、并用实验证明了其有效性。后续的所有 LLM serving 优化工作，都是在 Orca 建立的框架上进行的。
