# Daily Papers - 2026-03-11

## Diffusion Models & Representation Learning

### Information-Theoretic Diffusion
- **URL:** https://arxiv.org/abs/2302.03792
- **Authors:** Xianghao Kong, Greg Ver Steeg (your advisor!)
- **Key Insight:** New mathematical foundation for diffusion models using I-MMSE relations from information theory. Enables unified framework for continuous and discrete probabilities with same regression objective.
- **Relevance:** Directly connects to your research interests (diffusion + info theory). Ver Steeg's work.

### Why Diffusion Models Don't Memorize: Implicit Dynamical Regularization
- **URL:** https://arxiv.org/html/2505.17638v2
- **Date:** 2025-10-28
- **Key Insight:** Identifies two distinct timescales in training dynamics: early generalization phase vs. late memorization phase. Training dynamics act as implicit regularization preventing memorization.
- **Relevance:** Theoretical understanding of generalization in diffusion models.

### InfoDiffusion: Representation Learning Using Information Maximizing Diffusion Models
- **URL:** https://arxiv.org/abs/2306.08757
- **Key Insight:** Augments diffusion models with low-dimensional latent variables via mutual information regularization. Achieves disentangled representations while retaining high sample quality.
- **Relevance:** Combines diffusion + representation learning + information theory (all your interests).

### SODA: Bottleneck Diffusion Models for Representation Learning
- **URL:** https://arxiv.org/abs/2311.17901
- **Key Insight:** Self-supervised diffusion with tight bottleneck between encoder and decoder. Novel view synthesis as self-supervised objective for learning visual semantics.
- **Relevance:** Representation learning via diffusion with architectural constraints.

## Large Language Models

### Microsoft BitNet: 100B Param 1-Bit Model for Local CPUs
- **URL:** https://github.com/microsoft/BitNet
- **Key Insight:** 1-bit quantization enabling 100B parameter models to run on consumer CPUs. Major efficiency breakthrough.
- **Relevance:** Extreme model compression, democratizing LLM access.

### Will LLMs Scaling Hit the Wall? Breaking Barriers via Distributed Intelligence
- **URL:** https://arxiv.org/html/2503.08223v1
- **Date:** 2025-03-11 (today!)
- **Key Insight:** Public text data exhaustion by 2026-2028. Semiconductor bottlenecks (TSMC 5nm fully booked until 2026). Proposes distributed intelligence as solution.
- **Relevance:** Critical analysis of scaling limits and future directions.

### On-Device Large Language Models for Sequential Recommendation
- **URL:** https://arxiv.org/html/2601.09306v1
- **Conference:** WSDM 2026
- **Key Insight:** SVD-based low-rank compression + novel tokenization normalization for stable on-device LLM inference. Addresses privacy and latency for recommender systems.
- **Relevance:** Practical deployment of compressed LLMs.

### Challenges and Research Directions for Large Language Model Inference Hardware
- **URL:** https://arxiv.org/abs/2601.05047
- **Date:** 2026-02-06
- **Key Insight:** Autoregressive decode makes inference fundamentally different from training. Primary challenges are memory and interconnect, not compute.
- **Relevance:** Hardware bottlenecks for LLM deployment.
