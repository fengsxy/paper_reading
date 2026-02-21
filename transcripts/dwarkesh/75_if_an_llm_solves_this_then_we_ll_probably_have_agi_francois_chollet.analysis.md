---
date: 2024-01-01
layout: default
type: analysis
series: dwarkesh
episode: 75
guest: ""
title: "If an LLM solves this then we'll probably have AGI – Francois Chollet - Analysis"
source_url: "https://www.youtube.com/watch?v=wZ0ToxtXz5g"
transcript_url: /transcripts/dwarkesh/75_if_an_llm_solves_this_then_we_ll_probably_have_agi_francois_chollet/
permalink: /transcripts/dwarkesh/75_if_an_llm_solves_this_then_we_ll_probably_have_agi_francois_chollet.analysis/
---

# Analysis: If an LLM solves this then we'll probably have AGI – Francois Chollet

## 0. 3-5 句摘要

Francois Chollet 阐述了 ARC 基准测试的核心设计哲学：如果一个LLM能在不依赖大量类似训练数据的情况下达到80%的ARC得分，那我们可能确实在通往AGI的路上。他将智能定义为"未来情境空间中的路径搜索算法"——与记忆化（memorization）有本质区别。Chollet 承认ARC不是完美基准，但四年来它一直抵抗住了记忆化攻击。对话的核心张力在于：Dwarkesh 认为人类学习也依赖大量训练（数年的数学教育），Chollet 则坚持人类的样本效率和即时适应能力是质的不同。

## 1. 反共识/非显然观点

- **[00:00] ARC的真正测试条件**：Chollet 明确表示，即使LLM达到80%，也要看是怎么达到的——如果是通过训练数百万个类似ARC的任务来"暴力覆盖"任务空间，那仍然是记忆化而非智能。真正的测试是模型在未见过类似任务的情况下的表现。
- **[01:24] "如果你能暴力破解所有需要智能的事情，那智能有什么用？"**：Chollet 的回答是——如果世界是静态分布的，确实可以用纯记忆替代智能。但现实世界持续变化，这正是智能存在的原因。昆虫用硬编码行为程序就能生存，但人类需要通用智能来应对不可预测的环境。
- **[03:14] 人类学习也是记忆化？**：Dwarkesh 挑战说人类学数学也需要多年训练，Chollet 承认推理需要记忆作为建筑材料，但区分了"获取程序模板并套用"和"即时合成新程序"两种能力。

## 2. 关键洞察

- 智能是"未来情境空间中的路径搜索"——类似RTS游戏中的战争迷雾寻路，你必须在不完全信息下找到最优路径
- ARC 四年来抵抗住了记忆化攻击，说明它确实在测量某种不同于现有基准的能力
- 测试时微调（test-time fine-tuning）是当前最有效的ARC方法，这暗示"主动推理"而非"静态推理"是关键缺失能力
- 百万美元奖金的设置参考了 Vesuvius Challenge 的成功——那个奖被一个听播客的22岁年轻人赢得
- 记忆和推理不是对立的——有效推理需要记忆作为原材料，但纯记忆不等于推理

## 3. Takeaway

- 评估AI能力时，不仅要看结果（得分多少），更要看过程（怎么达到的）。同样的分数可以来自完全不同的能力机制，区分这两者是理解AI进展的关键。

