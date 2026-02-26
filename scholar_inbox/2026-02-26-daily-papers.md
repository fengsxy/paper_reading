---
layout: default
title: '每日论文 2026-02-26'
date: 2026-02-26
categories: scholar_inbox
---

# 每日论文精选 — 2026-02-26

来源：YDC Search (arxiv 2602.*)，聚焦 dLLM / discrete diffusion / information theory / representation learning。

---

## 1. IDLM: Inverse-distilled Diffusion Language Models
- arXiv: [2602.19066](https://arxiv.org/abs/2602.19066) (Feb 22)
- dLLM 推理加速的新路线：把连续扩散模型的 Inverse Distillation 技术迁移到离散设定。通过梯度稳定的松弛方法支持有效训练，在多个 DLM 上实现 4x-64x 步数压缩，同时保持 teacher 模型的 entropy 和生成 perplexity。跟 T3D 的蒸馏加速方向互补，但走的是 inverse distillation 路线。

## 2. Discrete Diffusion with Sample-Efficient Estimators for Conditionals
- arXiv: [2602.20293](https://arxiv.org/abs/2602.20293) (Feb 23)
- 提出新的离散扩散框架：不再近似离散 score function，而是直接把 single-site conditional probabilities 作为反向扩散的基本对象，用 NeurISE 方法高效估计。配合 round-robin noising/denoising 动态。理论视角新颖，把条件概率而非 score 作为核心。

## 3. Scaling Beyond Masked Diffusion Language Models
- arXiv: [2602.15014](https://arxiv.org/abs/2602.15014) (Feb 16)
- 首个 uniform-state 和 interpolating 离散扩散方法的 scaling law 研究。发现 masked diffusion 用简单 cross-entropy 目标可提升约 12% FLOPs 效率。关键洞察：perplexity 在同一扩散家族内有参考价值，但跨家族比较会误导——likelihood scaling 差的模型可能因采样更快而在 speed-quality Pareto 前沿更优。

## 4. Reasoning with Latent Tokens in Diffusion Language Models
- arXiv: [2602.03769](https://arxiv.org/abs/2602.03769) (Feb 3)
- 揭示 dLLM 推理能力的关键机制：扩散模型训练时联合预测所有未知 token（包括当前步不会解码的），这种"联合推理"是推理能力的来源。消融实验证实去掉联合预测会加速推理但降低性能。提出用 latent token 来保留联合推理能力同时提升效率。

## 5. AnCoder: Anchored Code Generation via Discrete Diffusion Models
- arXiv: [2602.17688](https://arxiv.org/abs/2602.17688) (Feb 5)
- 用 AST 结构引导离散扩散做代码生成。现有 dLLM 不尊重编程语言的刚性结构，容易生成无法执行的代码。AnchorTree 框架优先解码语法/语义关键 token（关键字、标识符），建立结构骨架再填充细节。dLLM 在代码领域的有趣应用。

## 6. Efficient Sampling with Discrete Diffusion: Sharp and Adaptive Guarantees
- arXiv: [2602.15008](https://arxiv.org/abs/2602.15008) (Feb 16)
- 离散扩散采样效率的理论分析。在 CTMC 框架下研究 τ-leaping 采样器，证明 uniform 离散扩散的迭代复杂度为 Õ(d/ε)，消除了对词表大小 S 的线性依赖，并证明对维度 d 的线性依赖不可避免。同时给出 masking 过程的自适应保证。

## 7. Radial-VCReg: More Informative Representation Learning Through Radial Gaussianization
- arXiv: [2602.14272](https://arxiv.org/abs/2602.14272) (Feb 15)
- 自监督学习的信息最大化方向。现有方法（如 VCReg）只正则化一二阶统计量，无法真正实现最大熵。提出 radial Gaussianization 方法，通过更高阶的统计约束来学习更具信息量的表示。信息论 + 表示学习的交叉。

## 8. WaterVIB: Learning Minimal Sufficient Watermark Representations via Variational Information Bottleneck
- arXiv: [2602.21508](https://arxiv.org/abs/2602.21508) (Feb 25)
- 用 Variational Information Bottleneck 理论做鲁棒水印。现有水印方法把水印与高频纹理纠缠，容易被 AIGC 重生成攻击破坏。WaterVIB 强制模型学习消息的最小充分统计量，理论上保证水印信息嵌入到语义层而非纹理层。VIB 在安全领域的实际应用。

---

*筛选标准：与 diffusion language model / discrete diffusion / information theory / representation learning 直接相关，优先选取理论贡献或方法创新显著的工作。*
