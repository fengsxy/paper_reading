# Daily Papers — 2026-03-24

> 周二 arxiv cs.LG 169 篇新投稿。以下 5 篇与研究方向高度相关。

## Diffusion Language Models

### 1. Confidence-Based Decoding is Provably Efficient for Diffusion Language Models
- **Link:** https://arxiv.org/abs/2603.22248 (Mar 24, 2026 — **今日新出**)
- **Authors:** Changxiao Cai, Gen Li
- **要点:** 为 DLM 的 confidence-based 解码策略提供了理论保证。解决了 DLM 区别于 AR 模型的核心问题：解码顺序和每步生成 token 数的选择。证明了基于置信度的策略在效率上是 provably optimal 的，cross-listed cs.IT。
- **与研究相关:** 直接关联 dLLM 推理效率的理论基础，信息论交叉。

### 2. Generalized Discrete Diffusion from Snapshots (GDDS)
- **Link:** https://arxiv.org/abs/2603.21342 (Mar 24, 2026 — **今日新出**)
- **Authors:** Oussama Zekri, Théo Uscidda, Nicolas Boullé, Anna Korba
- **要点:** 提出统一框架支持任意 noising process 的离散扩散建模，覆盖所有现有离散扩散方法，同时允许更灵活的 corruption dynamics 设计。基于 uniformization 的前向过程。
- **与研究相关:** 离散扩散的理论统一框架，可能为 dLLM 训练提供新视角。

## Representation Learning & Interpretability

### 3. Probing the Latent World: Emergent Discrete Symbols in Latent Representations
- **Link:** https://arxiv.org/abs/2603.20327 (Mar 24, 2026 — **今日新出**)
- **Authors:** Liu Hung Ming
- **要点:** 提出 AI Mother Tongue (AIM) 框架，在冻结的 V-JEPA 2 encoder 上将连续 latent vectors 量化为离散符号序列，无需任务监督。发现 JEPA latent space 高度紧凑——不同动作类别共享核心表征，语义差异编码为分布变化而非类别边界。
- **与研究相关:** 连续→离散表征的 probe 方法，representation geometry 分析。

### 4. DSPA: Dynamic SAE Steering for Data-Efficient Preference Alignment
- **Link:** https://arxiv.org/abs/2603.21461 (Mar 24, 2026 — **今日新出**)
- **Authors:** James Wedgwood, Aashiq Muhamed, Mona Diab, Virginia Smith
- **要点:** 用 Sparse Autoencoder 实现推理时对齐，无需更新模型权重。通过 preference triples 计算条件差异映射，解码时仅修改 token-active latents。在 Gemma-2/Qwen3 上提升 MT-Bench，且比 RAHF-SCIT 减少 4.47× alignment FLOPs。发现偏好方向主要由话语和风格信号主导。
- **与研究相关:** 表征层面的对齐操控，mechanistic interpretability。

## Information Theory & AI Safety

### 5. Kolmogorov Complexity Bounds for LLM Steganography
- **Link:** https://arxiv.org/abs/2603.21567 (Mar 24, 2026 — **今日新出**)
- **Authors:** Andrii Shportko
- **要点:** 证明任何保语义隐写方案必须使 stegotext 的 Kolmogorov 复杂度严格增加：K(M₂) ≥ K(M₁) + K(P) - O(log n)。这意味着 AI 系统间的隐蔽通信通道在信息论上存在不可消除的检测信号。
- **与研究相关:** 信息论 + AI safety 的优雅交叉，与 trustworthy AI 直接相关。

### 值得留意但次优先

- **SSAM:** Training-free 模型合并框架，通过奇异子空间对齐合并不同模态 MLLM (2603.21584)
- **RSA-FT:** 通过 reward sharpness-aware fine-tuning 缓解扩散模型 RLHF 中的 reward hacking
- **What Do World Models Learn:** 对 IRIS/DIAMOND 世界模型内部表征的 probing 研究 (2603.21546)
