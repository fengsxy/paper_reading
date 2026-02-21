---
date: 2024-01-01
layout: default
type: analysis
series: dwarkesh
episode: 112
guest: "Demis Hassabis"
title: "Scaling LLMs further is an artform – Demis Hassabis - Analysis"
source_url: "https://www.youtube.com/watch?v=666XgM38jJE"
transcript_url: /transcripts/dwarkesh/112_scaling_llms_further_is_an_artform_demis_hassabis_google_deepmind_ceo/
permalink: /transcripts/dwarkesh/112_scaling_llms_further_is_an_artform_demis_hassabis_google_deepmind_ceo.analysis/
---

# Analysis: Scaling LLMs further is an artform – Demis Hassabis

## 0. 3-5 句摘要

Demis 揭示了 scaling 的一个被低估的现实：scaling laws 不是"重复同一个 recipe 在更大规模上"——每次 scale up 都需要调整超参数、处理新的分布式计算挑战、并且发现某些外推预测在新规模上不再成立。他用"art form"来形容这个过程，强调需要中间数据点来校正预测。最关键的洞察是：training loss 可以预测，但 downstream capabilities 不一定跟着 loss 线性变化——这解释了为什么 emergent abilities 看起来像 step functions。

## 1. 反共识/非显然观点

- **"Scaling 是艺术而非工程"** [00:44]：大多数人认为 scaling 就是"更多 GPU + 更多数据"。Demis 说每次 scale up 都需要重新调整 recipe，而且某些预测在新规模上会失效。这意味着 scaling 的人才瓶颈比算力瓶颈更严重。

- **"Loss 可预测但 capabilities 不可预测"** [01:46]：GPT-4 技术报告说可以用少 10000 倍的 compute 预测 training loss，但 Demis 指出 loss 到 MMLU 等实际能力的映射不是线性的。这是 emergent abilities 争论的核心。

- **"一个数量级是每次 scale up 的实际上限"** [01:20]：不是因为钱不够，而是因为超过一个数量级的外推太不可靠——你需要中间数据点来校正。

## 2. 可学习的点（可迁移的方法论）

- **"50% scaling + 50% invention"的资源分配** [02:33]：Demis 描述了 DeepMind 的策略——一半精力用于 scaling 当前最佳方案，一半精力用于发明下一代架构和算法。这种"exploit + explore"的平衡对任何研究组织都有参考价值。

- **"中间数据点"的价值** [00:56]：在任何需要外推的领域，不要试图一步跳到终点——收集中间数据点来校正你的预测模型。

## 3. 提问技巧（采访方法）

- **引用竞争对手的数据** [01:33]：Dwarkesh 引用 GPT-4 技术报告的 loss 预测来追问 Demis，让 DeepMind CEO 不得不回应 OpenAI 的方法论。

## 4. 可进一步验证/挖坑

- **"Loss → capabilities"映射的系统研究**：是否有系统性的研究量化了 training loss 和 downstream capabilities 之间的非线性关系？这对预测下一代模型的能力至关重要。
