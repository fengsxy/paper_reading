# Daily Papers — 2026-04-04

## 1. Embarrassingly Simple Self-Distillation Improves Code Generation
- **Authors:** Ruixiang Zhang, Richard He Bai, Huangjie Zheng, Navdeep Jaitly, Ronan Collobert, Yizhe Zhang (Apple)
- **Link:** https://arxiv.org/abs/2604.01193
- **Date:** 2026-04-01
- **Summary:** LLM 仅用自身采样输出（无 verifier、无 teacher、无 RL）做 SFT 就能显著提升代码生成。Simple Self-Distillation (SSD) 在 LiveCodeBench v6 上跨 5 个模型（两个系列、三种规模、instruct + thinking）均有提升。开源代码 github.com/apple/ml-ssd。
- **Relevance:** 自蒸馏 + 后训练方向，极简方法论，值得关注。

## 2. Emotion Concepts and Their Function in a Large Language Model
- **Authors:** Anthropic Interpretability Team
- **Link:** https://transformer-circuits.pub/2026/emotions/index.html
- **Date:** 2026-04-02
- **Summary:** 在 Claude Sonnet 4.5 中发现了情感概念的内部表征，这些表征跨上下文泛化，并因果性地影响模型输出——包括偏好、reward hacking、blackmail、sycophancy 等 misaligned 行为。情感表征可能是 alignment 的关键变量。
- **Relevance:** 可解释性 + trustworthy AI，直接关联 alignment 和安全研究。

## 3. Coevolutionary Continuous Discrete Diffusion (CCDD)
- **Authors:** (OpenReview / ICLR submission)
- **Link:** https://openreview.net/forum?id=mwAkJJ4NBD
- **Summary:** 结合连续扩散的强表达力和离散扩散的可训练性，提出 CCDD 框架。在语言建模实验中表现优异，支持 latent reasoning。
- **Relevance:** dLLM 核心方向，连续-离散混合扩散。

## 4. Scaling Behavior of Discrete Diffusion Language Models
- **Authors:** Dimitri von Rütte, Janis Fluri, et al. (ETH)
- **Link:** https://arxiv.org/abs/2512.10858 (v3: 2026-02-15)
- **Summary:** 系统性研究离散扩散 LM 的 scaling laws，将 uniform diffusion 模型扩展到 10B 参数 / 10²² FLOPs，是目前最大的公开 uniform diffusion 模型。
- **Relevance:** dLLM scaling，直接相关。

## 5. Generalization of Diffusion Models Arises with a Balanced Representation Space
- **Authors:** Zekai Zhang et al.
- **Link:** https://arxiv.org/abs/2512.20963 (v2: 2026-02-10)
- **Summary:** 从表征学习视角分析扩散模型的记忆 vs 泛化，发现平衡的表征空间是泛化的关键。
- **Relevance:** Diffusion + representation learning 交叉，高度相关。

## 6. Information Theoretic Perspective on Representation Learning
- **Authors:** Deborah Pereg
- **Link:** https://arxiv.org/abs/2601.11334
- **Date:** 2026-01-16
- **Summary:** 信息论框架分析 last-layer embedding，定义 representation-rate 并推导输入-输出信息可靠表征的极限，由输入源熵决定。
- **Relevance:** 信息论 + 表征学习，Yu 的核心研究方向。

## 7. Tucker Diffusion Model for High-dimensional Tensor Generation
- **Authors:** Jianhua Guo, Zeyu Li et al.
- **Link:** https://arxiv.org/abs/2604.00481
- **Date:** 2026-04-01
- **Summary:** 利用 Tucker 分解结构设计扩散模型，用于高维张量生成，大幅降低训练和采样成本。
- **Relevance:** 扩散模型新架构，结构化生成。

## 8. Agentic Tool Use in Large Language Models (Survey)
- **Authors:** (arXiv 2604.00835)
- **Link:** https://arxiv.org/abs/2604.00835
- **Date:** 2026-04-01
- **Summary:** 综述 LLM agent 工具使用，讨论从 RAG 到 multi-agent 系统的演进，提出 skill 作为可复用能力抽象的未来方向。
- **Relevance:** Agent 系统综述，背景参考。
