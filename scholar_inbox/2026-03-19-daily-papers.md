# Daily Papers — 2026-03-19

## 1. One-step Language Modeling via Continuous Denoising (ICLR 2026?)
- **Authors:** Google DeepMind
- **Link:** https://arxiv.org/abs/2602.16813
- **Date:** 2026-02-18
- **Summary:** Flow map language model (FMLM) that outperforms discrete diffusion models and matches 8-step distilled dLLMs in a single step. Challenges the belief that continuous diffusion LMs underperform discrete ones. Compatible with few-step distillation via flow matching.
- **Relevance:** Directly relevant to dLLM/diffusion LM research. One-step generation is a significant efficiency breakthrough.

## 2. ReFusion: A Diffusion Large Language Model with Parallel Generation
- **Authors:** —
- **Link:** https://arxiv.org/abs/2512.13586
- **Date:** 2026-03-05 (v2)
- **Summary:** Large-scale diffusion LLM with parallel token generation. Builds on the LLaDA/dLLM line of work with focus on practical parallel decoding.
- **Relevance:** Extends practical dLLM architectures with parallel generation capabilities.

## 3. The Diffusion Duality (ICLR 2026)
- **Authors:** —
- **Link:** https://arxiv.org/abs/2602.21185
- **Date:** 2026-02 (published at ICLR 2026)
- **Summary:** Unified predictor-corrector sampling framework for discrete diffusion LMs via Ψ-posteriors. Duo++ with Ψ-samplers matches MDM performance on NLG and improves FID/IS on CIFAR-10. Covers both uniform and absorbing noise priors.
- **Relevance:** Theoretical + practical advance in dLLM sampling — directly in Yu's research area.

## 4. Scaling Behavior of Discrete Diffusion Language Models
- **Authors:** Dimitri von Rütte et al. (ETH Zürich)
- **Link:** https://arxiv.org/abs/2512.10858
- **Date:** 2026-02-15 (v3)
- **Summary:** Systematic scaling law analysis for discrete diffusion LMs (masking, uniform, hybrid noise). Finds dLLMs need more parameters relative to tokens vs. AR models. Reparameterizes ELBO in terms of SNR, closing gap to continuous diffusion theory.
- **Relevance:** Critical for understanding dLLM compute-optimal training. Info-theoretic angle (SNR/ELBO) ties to Yu's interests.

## 5. Generalization of Diffusion Models Arises with a Manifold-like Support of the Data Distribution
- **Authors:** —
- **Link:** https://arxiv.org/abs/2512.20963
- **Date:** 2026-02-10
- **Summary:** Theoretical analysis of when and why diffusion models generalize. Connects generalization to manifold structure of data support.
- **Relevance:** Representation learning + diffusion theory intersection.

## 6. Diffusion-State Policy Optimization for Masked Diffusion Language Models
- **Authors:** —
- **Link:** Referenced in Awesome-DLMs list
- **Date:** 2026-02-06
- **Summary:** Applies policy optimization (RL-style) to masked diffusion LMs. Adapts RLHF-like techniques to the dLLM paradigm.
- **Relevance:** Bridging alignment/RLHF and dLLMs — relevant to trustworthy AI + dLLM intersection.

---

*Note: Most results are from Feb–Mar 2026 window. YDC search does not surface arxiv papers from the last 24h reliably; these represent the latest findable work in dLLM/diffusion/representation learning.*
