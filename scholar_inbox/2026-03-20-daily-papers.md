# Daily Papers — 2026-03-20

## Discrete Diffusion & Language Models

### 1. Scaling Behavior of Discrete Diffusion Language Models
- **Authors:** Dimitri von Rütte, Janis Fluri, Omead Pooladzandi, Bernhard Schölkopf, Thomas Hofmann, Antonio Orvieto
- **Link:** https://arxiv.org/abs/2512.10858 (v3, Feb 2026)
- **Key:** Uniform diffusion LMs outscale both masked diffusion and autoregressive models in compute- and data-bound scaling. Scaled to 10B params / 10²² FLOPs. Reformulates discrete diffusion ELBO via SNR, bridging continuous diffusion theory.

### 2. Coevolutionary Continuous Discrete Diffusion (CCDD)
- **Link:** https://openreview.net/forum?id=mwAkJJ4NBD
- **Key:** Combines continuous diffusion's expressivity with discrete diffusion's trainability. Proposes architectures and training/sampling techniques showing strong empirical results on real-world language tasks. Addresses the theory gap around latent reasoning with looped transformers.

### 3. Consistency Diffusion Language Models (CDLM)
- **Authors:** Minseo Kim, Chenfeng Xu, et al. (SNU / UC Berkeley / Together AI)
- **Link:** https://www.together.ai/blog/consistency-diffusion-language-models (Feb 2026)
- **Key:** Post-training recipe enabling exact block-wise KV caching + consistency-based step reduction for DLMs. Up to 14.5× latency speedup on math/coding tasks. Makes DLM inference practical.

### 4. LADR: Locality-Aware Dynamic Rescue for Text-to-Image Diffusion
- **Link:** https://arxiv.org/abs/2603.13450 (Mar 2026)
- **Key:** Accelerates discrete diffusion multimodal models by exploiting 2D spatial redundancy in visual tokens during iterative decoding.

### 5. MetaState: Persistent Working Memory for Discrete Diffusion Language Models
- **Link:** Referenced in VILA-Lab/Awesome-DLMs (Mar 2, 2026)
- **Key:** Introduces persistent working memory mechanism for dLLMs, addressing the stateless nature of iterative refinement.

## Representation Learning & Information Theory

### 6. Information Theoretic Perspective on Representation Learning
- **Authors:** Deborah Pereg
- **Link:** https://arxiv.org/abs/2601.11334 (Jan 2026)
- **Key:** IT framework analyzing last-layer embeddings for regression. Defines "representation-rate" and derives reliability limits via Shannon-McMillan AEP. Connects mutual information at each layer to generalization gap.

### 7. Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis
- **Link:** https://arxiv.org/abs/2603.06507 (Mar 2026)
- **Key:** Strong semantic representations improve convergence and generation quality of flow matching models. Self-supervised approach for multi-modal generation.

## Tutorials & Surveys

### 8. An Introduction to Flow Matching and Diffusion Models
- **Link:** https://arxiv.org/abs/2506.02070 (updated Mar 18, 2026)
- **Key:** Comprehensive tutorial unifying flow matching and diffusion frameworks across modalities (images, video, molecules, music). Good reference for understanding the FM↔diffusion connection.
