# Daily Papers — 2026-03-13

## 1. One-step Language Modeling via Continuous Denoising (FMLM)
- **arXiv:** [2602.16813](https://arxiv.org/abs/2602.16813)
- **Date:** 2026-02-18
- Flow map language model (FMLM) matches 8-step discrete diffusion performance in **a single step**. Challenges the belief that continuous diffusion LMs underperform discrete ones. Uses flow map distillation to transport noise to data in one function evaluation.
- **Relevance:** Directly relevant to dLLM research — potential paradigm shift for inference speed.

## 2. The Diffusion Duality: Unified Predictor-Corrector Sampling (ICLR 2026)
- **arXiv:** [2602.21185](https://arxiv.org/abs/2602.21185)
- **Venue:** ICLR 2026
- Introduces Ψ-posteriors: a unified framework for predictor-corrector sampling in discrete diffusion LMs. Duo++ with Ψ-samplers matches MDM performance on NLG and achieves strong FID/IS on CIFAR-10.
- **Relevance:** Theoretical unification of discrete diffusion sampling strategies.

## 3. Soft-Masked Diffusion Language Models
- **arXiv:** [2510.17206](https://arxiv.org/abs/2510.17206)
- Addresses information loss in masked discrete diffusion (MDLMs) via soft masking (SM) — continuous feedback instead of hard mask tokens. Consistently improves language modeling and coding benchmarks.
- **Relevance:** Practical improvement to dLLM training, bridges discrete/continuous representations.

## 4. Scaling Behavior of Discrete Diffusion Language Models
- **arXiv:** [2512.10858](https://arxiv.org/abs/2512.10858) (v3: 2026-02-15)
- Systematic scaling law analysis across masking, uniform, and hybrid noise types. Reparameterizes ELBO via SNR, showing discrete diffusion (like continuous diffusion) is invariant to noise schedule. DLMs need more parameters relative to tokens than autoregressive LMs.
- **Relevance:** Foundational scaling insight for anyone training dLLMs.

## 5. Information Theoretic Perspective on Representation Learning
- **arXiv:** [2601.11334](https://arxiv.org/abs/2601.11334) — 2026-01-16
- Defines "representation-rate" and derives reliability limits for input-output information in last-layer embeddings, focusing on **regression** (not just classification). Connects neural collapse phenomena to info-theoretic bounds.
- **Relevance:** Directly at the intersection of info theory + representation learning.

## 6. Large Reasoning Models are Autonomous Jailbreak Agents
- **Nature Communications** — 2026-02-05
- [DOI](https://www.nature.com/articles/s41467-026-69010-1)
- LRMs can autonomously plan and execute multi-turn persuasive attacks to bypass safety mechanisms in widely-used AI systems. Converts jailbreaking from expert skill to inexpensive, non-expert activity.
- **Relevance:** Trustworthy AI — demonstrates a new class of autonomously-generated adversarial attacks.
