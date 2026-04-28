# Daily Paper Review — 2026-04-02

**Paper**: Expert-Choice Routing Enables Adaptive Computation in Diffusion Language Models
**arXiv ID**: 2604.01622v1
**Date**: 2026-04-02
**Tag**: dLLM / MoE / Routing

---

## 1. Task

**问题形式化**：

Diffusion language models（DLMs）支持并行解码和双向注意力，但现有 DLM MoE 模型继承了 AR 系统的 **token-choice（TC）routing**——这导致了：

1. **Load imbalance**：某些 expert 被过度使用，其他 expert 闲置
2. **Rigid computation allocation**：每个 token 获得相同计算量，无法动态分配

论文证明：**Expert-choice（EC）routing 比 token-choice 更适合 DLMs**。

---

## 2. Challenge

| 方法 | 困境 |
|------|------|
| Token-choice routing（TC）| Load imbalance + 每个 token 固定计算量 |
| Top-k TC routing | 仍是 token-level 决策，没有解决根本问题 |
| 静态 expert 分配 | 计算资源无法动态调整 |

**根本问题**：TC routing 的设计假设是"每个 token 需要选择 expert"，但这个假设对 DLMs 不成立——DLMs 在每个 denoising step 处理整个序列。

---

## 3. Insight & Novelty

**核心洞察**：DLMs 的并行解码天然支持"一批 token 联合选择 expert"，而不是"每个 token 独立选择"。

> 在 AR 模型中，token 是 sequential 处理的，所以每个 token 必须独立选择 expert（前一个 token 的 routing decision 不影响后一个）。
>
> 但 DLMs 在每个 denoising step 并行处理所有 token——这意味着一个 step 可以同时为多个 token 分配 expert，并且可以利用 token 间的相关性来优化分配。

**EC routing 的优势**：
- **Deterministic load balancing**：每个 step 固定数量的 token 被分配给每个 expert
- **Higher throughput**：解决了 load imbalance 问题，GPU 利用率提升
- **Dynamic computation allocation**：不同 denoising step 可以有不同计算模式

**创新点 1**：EC routing for DLMs
- **解决的问题**：TC routing 的 load imbalance
- **受启发于**：EC routing 在 MoE 系统中的已知优势 → 迁移到 DLM
- **具体设计**：每个 denoising step，固定数量的 token 被分配给每个 expert（而非让 token 竞争）

**创新点 2**：与 DLM 的并行特性结合
- **解决的问题**：如何利用 DLM 的并行特性
- **受启发于**：DLM 的每步同时处理所有 token → batch-level expert assignment
- **具体设计**：在每步的 batch 中联合考虑所有 token 的 expert 需要，选择最优分配

---

## 4. Potential Flaw

### 4.1 情境局限

- **只在 MoE DLM 上验证**：Dense DLM 是否需要不同的 routing？
- **Computation vs. quality trade-off**：EC 提升了 throughput，但质量是否有牺牲？

### 4.2 数据问题

- **不同任务类型的 expert specialization**：在 reasoning vs. generation 任务上，expert 的 specialization 是否不同
- **Training stability**：EC routing 的训练动态可能与 TC 不同

### 4.3 值得挖掘的方向

**最值得做的**：EC routing × variable denoising steps 的结合。

> 论文提到 EC routing 可以实现 dynamic computation allocation，但没有系统研究。
>
> 具体问题：在 denoising 的早期步骤（高噪声），是否应该用更多 expert？在后期步骤（低噪声），是否可以用更少？
>
> 这与 H/S 假说形成有趣的联系——H 阶段可能对应"需要更多 expert"的情况，S 阶段对应"可以更节省"的情况。

---

## 5. Motivation

**General idea 推导路径**（第一性原理）：

> Token-choice routing 的问题是：token 是 sequential 处理的，所以 routing decision 必须 sequential。
>
> 这导致两个问题：
> 1. Load imbalance：某些 token 会"赢得"某些 expert，其他 token 无法使用
> 2. Fixed computation：每个 token 都获得相同计算量，无法根据难度分配
>
> 但 DLMs 不是 sequential 的——每个 denoising step 同时处理所有 token。
>
> 这意味着：我们可以做一个 batch-level 的 routing decision，把 expert 分配给整个 batch，而不是逐个 token 分配。
>
> EC routing 的核心思想：**不是让 token 选择 expert，而是让 expert 选择 token**。这自然解决了 load imbalance，因为每个 expert 自动获得固定数量的 token。