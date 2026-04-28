# Daily Paper Review — 2026-04-15

**Paper**: Diffusion Language Models for Speech Recognition
**arXiv ID**: 2604.14001v1
**Date**: 2026-04-15
**Tag**: dLLM / Speech / ASR

---

## 1. Task

**问题形式化**：

Diffusion Language Models 因其 bidirectional attention 和 parallel text generation 能力成为 AR 模型的有力替代。但如何将其用于 **Speech Recognition（ASR）** 仍未被充分探索。

论文提出：

1. MDLM（Masked Diffusion Language Model）和 USDM（Uniform-state Diffusion Model）用于 **rescoring ASR hypotheses** 的完整指南
2. 一种新的 **joint-decoding 方法**：结合 CTC（framewise probabilities）和 USDM（labelwise probabilities）

---

## 2. Challenge

| 方法 | 困境 |
|------|------|
| AR ASR | 单向生成，无法利用完整未来上下文 |
| CTC alone | 独立于语言模型，缺少语言理解 |
| 直接用 LM rescoring | AR LM 和 diffusion LM 的特性不同，不能直接迁移 |

---

## 3. Insight & Novelty

**创新点 1**：MDLM 和 USDM 的 rescoring 完整指南
- **解决的问题**：如何将 dLLM 用于 ASR
- **具体设计**：在每个 decoding step 结合 CTC framewise probabilities 和 USDM labelwise probabilities

**创新点 2**：Joint-decoding 结合 CTC 和 USDM
- **解决的问题**：CTC 和 diffusion LM 如何协同
- **具体设计**：在每个 decoding step 融合声学信息和语言知识，生成同时利用两种信息的 candidates

---

## 4. Potential Flaw

- **计算成本**：diffusion LM 的 iterative denoising 比 AR 慢，可能不适合实时 ASR
- **与 E2E ASR 的比较未充分进行**：主要验证了 rescoring，未直接与 end-to-end 模型比较

---

## 5. Motivation

USDM 的 bidirectional attention 允许在每个 step 同时利用完整上下文，CTC 提供 frame-level 声学信息。两者的结合是自然的——diffusion LM 提供了 AR 模型无法提供的全局语言理解。
