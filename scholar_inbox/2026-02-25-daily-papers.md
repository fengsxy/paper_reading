---
layout: default
title: '每日论文 2026-02-25'
date: 2026-02-25
categories: scholar_inbox
---

# 每日论文精选 — 2026-02-25

来源：YDC Search (arxiv 2602.*)，聚焦 dLLM / discrete diffusion / information theory。

---

## 1. Adaptation to Intrinsic Dependence in Diffusion Language Models
- arXiv: [2602.20126](https://arxiv.org/abs/2602.20126) (Feb 23)
- DLM 的 token 间依赖建模问题。当前 DLM 假设 token 独立解码，这篇分析了内在依赖如何影响生成质量，并提出自适应方法。

## 2. T3D: Few-Step Diffusion Language Models via Trajectory Transfer
- arXiv: [2602.12262](https://arxiv.org/abs/2602.12262) (Feb 13)
- 少步 dLLM 生成。通过轨迹迁移把多步扩散压缩到几步，解决 dLLM 推理慢的问题。跟 Yu 的加速方向直接相关。

## 3. Diffusion-State Policy Optimization for Masked Diffusion LMs
- arXiv: [2602.06462](https://arxiv.org/abs/2602.06462) (Feb 9)
- 把 RL 引入 masked diffusion LM。因为 dLLM 是多步解码，传统 RLHF 不直接适用，这篇设计了针对扩散状态的 policy optimization。

## 4. Just on Time: Token-Level Early Stopping for Diffusion LMs
- arXiv: [2602.11133](https://arxiv.org/abs/2602.11133) (Feb 11)
- 逐 token 的 early stopping：有些 token 早就确定了，不需要跑完所有去噪步。跟 Yu 的 remask 方向有交集——都在思考"哪些 token 需要更多计算"。

## 5. Search or Accelerate: Confidence-Switched Position Decoding
- arXiv: [2602.10953](https://arxiv.org/abs/2602.10953) (Feb 11)
- 根据置信度动态决定每个位置是继续搜索还是加速提交。又一篇在做"自适应计算分配"的工作。

## 6. Balancing Understanding and Generation in Discrete Diffusion
- arXiv: [2602.01362](https://arxiv.org/abs/2602.01362) (Feb 1)
- MDLM 擅长理解，UDLM 擅长生成，这篇试图统一两者。跟 Sahoo et al. 的 Duo 工作相关。

## 7. Embedding Inversion via Conditional Masked Diffusion
- arXiv: [2602.11047](https://arxiv.org/abs/2602.11047) (Feb 18)
- 用 masked diffusion 做 embedding 反演——从 embedding 恢复原始 token。并行解码而非自回归。

## 8. Refining the Information Bottleneck via Adversarial Information
- arXiv: [2602.06549](https://arxiv.org/abs/2602.06549) (Feb 9)
- 对抗式 Information Bottleneck，学习解耦表征。跟 Greg 的信息论方向相关。

---

与 Yu 研究最相关的：#2 (few-step)、#4 (early stopping)、#5 (confidence-switched) 都在做"自适应计算"，跟 remask 的思路有交集。#6 直接对标 Sahoo et al. 的 Duo。#8 是 IB 新工作，Greg 可能感兴趣。
