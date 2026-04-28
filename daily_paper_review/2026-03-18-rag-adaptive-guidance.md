# Daily Paper Review — 2026-03-18

**Paper**: Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models
**arXiv ID**: 2603.17677v1
**Date**: 2026-03-18
**Tag**: dLLM / RAG / Knowledge Conflict

---

## 1. Task

**问题形式化**：

Retrieval-Augmented Generation（RAG）通过引入外部知识来提升事实准确性。但当 retrieved context 是 noisy、unreliable 或与模型内部知识冲突时，会引入 **retrieval-prior conflicts**，降低生成质量。

这个问题在 AR 模型上已被广泛研究，但在 masked diffusion language models（MDLMs）上基本未被探索。

**目标**：提出一种 adaptive guidance 方法，让 MDLM 能够在 RAG 场景中智能处理 knowledge conflicts。

---

## 2. Challenge

| 方法 | 困境 |
|------|------|
| 无冲突时的 RAG | 工作正常 |
| Noisy retrieved context | 引入错误信息 |
| 与模型 parametric knowledge 冲突 | 不知道该信哪个 |
| 对 MDLM 的适用性未知 | 现有方法都是为 AR 设计的 |

---

## 3. Insight & Novelty

**核心洞察**：MDLM 的 iterative denoising 过程天然适合处理 knowledge conflicts——每个 denoising step 都可以作为"检查点"，评估 retrieved context 的可靠性。

> 关键发现：在 denoising 的早期（高噪声），retrieved context 可能更有用（因为模型自己的预测不可靠）；在后期（低噪声），模型的 parametric knowledge 可能更可靠。
>
> 这意味着：**guidance strength 应该随 denoising step 动态调整**。

**创新点 1**：Step-dependent guidance strength
- **解决的问题**：固定 guidance strength 无法适应 denoising 阶段的变化
- **受启发于**：Denoising trajectory 的特性 → 早期依赖 retrieval，后期依赖 parametric knowledge
- **具体设计**：在每个 step 根据噪声水平调整 guidance weight

**创新点 2**：Conflict detection mechanism
- **解决的问题**：如何判断 retrieved context 是否与模型 knowledge 冲突
- **受启发于**：Denoising dynamics → 冲突时模型的预测会在两种信息来源之间摇摆
- **具体设计**：通过监测 denoising trajectory 的波动来检测冲突

---

## 4. Potential Flaw

- **Retrieval quality 的依赖**：如果 retrieval 本身很差，adaptive guidance 可能还是会失败
- **只验证了 MDLM**：Block-wise dLLM 的适用性未知

---

## 5. Motivation

**General idea**：MDLM 的迭代特性让它能够动态选择"相信外部知识还是内部知识"——早期噪声大时更依赖 retrieval，后期模型自己的预测变得更可靠时减少对 retrieval 的依赖。