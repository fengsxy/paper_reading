# Daily Papers — 2026-03-14

## Diffusion Models & Generation

### 1. EndoCoT: Scaling Endogenous Chain-of-Thought Reasoning in Diffusion Models
- **arXiv:** [2603.12252](https://arxiv.org/abs/2603.12252)
- 将 CoT 推理内化到 diffusion model 内部，而非依赖外部 LLM 指导。探索 diffusion model 自身的推理能力扩展。
- **关注理由:** 直接结合 diffusion + reasoning，可能对 dLLM 推理能力研究有启发。

### 2. One Model, Many Budgets: Elastic Latent Interfaces for Diffusion Transformers
- **arXiv:** [2603.12245](https://arxiv.org/abs/2603.12245)
- 提出弹性潜在接口，让单个 DiT 模型在不同计算预算下运行，无需重新训练多个模型。
- **关注理由:** DiT 效率优化，实用性强。

### 3. CoDAR: Continuous Diffusion with Contextual AutoRegressive Decoder
- **来源:** [bansky-cl/diffusion-nlp-paper-arxiv](https://github.com/bansky-cl/diffusion-nlp-paper-arxiv)
- 解决连续 DLM 的 token rounding 瓶颈：用 AR decoder cross-attend denoised embedding 做 contextualized rounding，在 LM1B/OpenWebText 上逼近离散 DLM 性能。
- **关注理由:** 连续 vs 离散 diffusion LM 的核心问题，提出实用的 hybrid 方案。

### 4. Coevolutionary Continuous Discrete Diffusion
- **OpenReview:** [mwAkJJ4NBD](https://openreview.net/forum?id=mwAkJJ4NBD)
- 分析为什么连续 diffusion LM 落后于离散版本，提出协同进化框架。与 looped transformers / continuous CoT 的理论优势相关。
- **关注理由:** 直接关于 dLLM 架构选择的核心问题。

## Efficient Attention & Training

### 5. IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse
- **arXiv:** [2603.12201](https://arxiv.org/abs/2603.12201)
- 跨层复用稀疏注意力索引，加速长序列推理。
- **关注理由:** Attention 效率，对大模型推理有普遍意义。

### 6. The Curse and Blessing of Mean Bias in FP4-Quantized LLM Training
- **arXiv:** [2603.10444](https://arxiv.org/abs/2603.10444)
- 分析 FP4 量化训练中均值偏差的双面效应，理论+实证。
- **关注理由:** LLM 训练效率，information-theoretic 视角分析量化误差。

## RL & Reward Modeling

### 7. Trust Your Critic: Robust Reward Modeling and RL for Faithful Image Editing
- **arXiv:** [2603.12247](https://arxiv.org/abs/2603.12247)
- 鲁棒奖励建模用于图像编辑/生成的忠实性，结合 RL 和 diffusion generation。
