# Daily Paper Review — 2026-04-12

**Paper**: Lost in Diffusion: Uncovering Hallucination Patterns and Failure Modes in Diffusion Large Language Models
**arXiv ID**: 2604.10556v1
**Date**: 2026-04-12
**Tag**: dLLM / Hallucination / Reliability

---

## 1. Task

**问题形式化**：

dLLM 作为一种 promising non-autoregressive 范式，其 **faithfulness（忠实性）**——尤其是 hallucination 问题——几乎没有被系统研究过。

论文做了第一个 **controlled comparative study**，系统比较 dLLM 和 AR 模型在 hallucination 上的差异。

核心发现：

> 在控制 architecture、scale 和 pre-training weights 的条件下，**dLLM 表现出比 AR 模型更高的 hallucination 倾向**。

同时识别出 dLLM 独有的 **distinct failure modes**：

1. **Premature Termination**：生成在完全 denoise 之前提前结束
2. **Incomplete Denoising**：某些 token 未被充分去噪，停留在 noisy 状态
3. **Context Intrusion**：不相关的 context 信息渗入生成内容

---

## 2. Challenge

| 方法 | 困境 |
|------|------|
| Perplexity / 传统 NLG 评估 | 无法捕捉 hallucination 的结构性模式 |
| AR hallucination 研究 | 不适用于 dLLM，因为 generation dynamics 本质不同 |
| 没有 dLLM-specific 的分析框架 | 需要新的方法论来理解 dLLM 的 hallucination 机制 |

**根本问题**：dLLM 的 iterative denoising 过程如何导致 hallucination？与 AR 的机制有何本质不同？

---

## 3. Insight & Novelty

### 3.1 Insight

**核心发现 1**：dLLM 确实比 AR 更容易 hallucinate。

> 控制了 architecture、scale、pre-training weights 后，dLLM 的 hallucination 率系统性高于 AR。
> 这说明 dLLM 的生成机制本身（而非模型大小或数据质量）更容易导致 hallucination。

**核心发现 2**：inference-time compute 揭示了不同的 dynamics。

> AR 的 quasi-autoregressive generation 在早期 compute 后就饱和了，无法继续改善。
> **dLLM 的 non-sequential decoding 解锁了持续改善的潜力**——这与 H/S 假说相关：dLLM 可以在后期仍能 refine S（soft）阶段的内容。

**核心发现 3**：三种 dLLM 特有的 failure modes。

> **Premature Termination**：某些 token 在未完全收敛时被过早锁定（对应 H 阶段提前到来）
> **Incomplete Denoising**：部分 token 停留在中间状态（对应 S/H 临界区的不确定性）
> **Context Intrusion**：bidirectional attention 导致无关 context 渗入（dLLM 独有，AR 不存在）

### 3.2 Novelty

**创新点 1**：首个 dLLM hallucination 的 controlled comparative study
- **解决的问题**：dLLM 的 hallucination 是否比 AR 更严重
- **受启发于**：AR 的 hallucination 研究 → 迁移到 dLLM，控制变量实验设计
- **具体设计**：控制 architecture/scale/weights，comparative evaluation

**创新点 2**：识别三种 dLLM-specific failure modes
- **解决的问题**：dLLM hallucination 的机制是什么
- **受启发于**：dLLM 的 iterative denoising 结构 → 发现 premature termination、incomplete denoising、context intrusion
- **具体设计**：对去噪轨迹做分析，定位三种 failure 的发生位置

**创新点 3**：发现 non-sequential decoding 的持续改善潜力
- **解决的问题**：为什么 dLLM 在推理时间充分时可能超越 AR
- **受启发于**：H/S 的 S 阶段持续 refine → dLLM 的后期 denoising 仍能改善
- **具体设计**：在多个 compute budget 下测量 dLLM vs AR 的性能曲线

---

## 4. Potential Flaw

### 4.1 情境局限

- **评估数据集**：hallucination 评测的数据集可能偏向特定 domain，未覆盖全场景
- **模型覆盖**：只在特定 dLLM 上验证，不同架构的 hallucination 模式可能不同
- **与 reasoning 任务的结合**：reasoning 场景的 hallucination 可能更严重，但未系统测试

### 4.2 数据问题

- **低质量训练数据**：如果训练数据本身有 noise，dLLM 的 hallucination 可能更严重，但未单独分析
- **长序列场景**：三种 failure modes 在长文本生成中可能叠加，导致错误率非线性增长

### 4.3 值得挖掘的方向

**最值得做的**：dLLM hallucination 的 **trajectory-level 干预**。

> 既然三种 failure modes 已经被定位（premature termination、incomplete denoising、context intrusion），
> 那就可以设计针对性的干预：
> - Premature termination → 用 VSB（self-containedness check）防止过早 commit
> - Incomplete denoising → 用 T2M（remask 机制）强制重新去噪
> - Context intrusion → 用 attention masking 或 guidance 来阻断无关 context
>
> 这是一个完整的 dLLM faithfulness 修复 pipeline，与 VSB、T2M 等解码策略形成完整闭环。

---

## 5. Motivation

**General idea 推导路径**（第一性原理）：

> AR 模型生成 token 时，每次只考虑前文，错误是单向传播的——一旦某个 token 错了，后面全错。
>
> dLLM 不同：所有 token 同时迭代生成，bidirectional context 既可以传播正确信息，也可以传播错误信息。
>
> **那问题来了：bidirectional attention 会让 hallucination 更容易发生吗？**
>
> ——是的。因为 AR 的错误是单向的，dLLM 的错误是全局传播的。
>
> 但反过来说：**dLLM 在推理时间充分时，non-sequential decoding 也意味着 global refinement 是可能的**。AR 在 early stop 后无法再改善，dLLM 可以继续 denoise。
>
> 所以 dLLM hallucination 的本质是：**双向传播 + 全局 refinement 的权衡**。如果推理时间不够充分，错误还没被修复就被锁定了；如果时间足够，dLLM 实际上比 AR 更能 self-correct。
