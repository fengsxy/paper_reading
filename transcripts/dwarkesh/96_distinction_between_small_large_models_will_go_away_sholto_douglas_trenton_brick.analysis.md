---
layout: default
type: analysis
series: dwarkesh
episode: 96
guest: ""
title: "Distinction between small & large models will go away – Sholto Douglas & Trenton Bricken - Analysis"
source_url: "https://www.youtube.com/watch?v=AOt0GwY8IvU"
transcript_url: /transcripts/dwarkesh/96_distinction_between_small_large_models_will_go_away_sholto_douglas_trenton_brick/
permalink: /transcripts/dwarkesh/96_distinction_between_small_large_models_will_go_away_sholto_douglas_trenton_brick.analysis/
---

# Analysis: Distinction between small & large models will go away — Sholto Douglas & Trenton Bricken

## 0. 3-5 句摘要

Sholto Douglas 和 Trenton Bricken 预测大小模型之间的区分将逐渐消失。核心论点是：随着蒸馏技术和架构改进，小模型将越来越接近大模型的能力，而大模型的推理成本将持续下降。他们讨论了 Mixture of Experts、稀疏激活等技术如何让"大模型"在推理时只使用一小部分参数。最终，用户不会关心模型大小，只关心延迟、成本和能力的组合。

## 1. 反共识/非显然观点

- **[00:00] 模型大小将变得无关紧要**：当前"8B vs 70B vs 405B"的分类方式将被淘汰。未来的区分将是"任务复杂度"而非"模型大小"——简单任务用轻量推理，复杂任务用重量推理，但底层可能是同一个模型的不同模式。
- **[01:30] 蒸馏的极限远未到达**：当前蒸馏技术只是初步的，未来小模型可能在特定领域达到大模型90%以上的能力，使得"必须用大模型"的场景越来越少。

## 2. 关键洞察

- Mixture of Experts 模糊了"模型大小"的定义——一个万亿参数模型可能每次推理只激活100亿参数
- 推理成本的下降速度可能比训练成本下降更快
- 端侧推理（手机、眼镜）将成为重要的部署场景，推动小模型的持续优化
- 模型能力的"民主化"不仅来自开源，还来自蒸馏和量化技术

## 3. Takeaway

- 不要基于当前的模型大小分类做长期规划。未来的 AI 部署将更像"按需调用不同强度的智能"，而非"选择一个固定大小的模型"。
