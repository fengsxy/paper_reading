---
date: 2024-01-01
layout: default
type: analysis
series: dwarkesh
episode: 77
guest: ""
title: "Francois Chollet — Why the biggest AI models can't solve simple puzzles - Analysis"
source_url: "https://www.youtube.com/watch?v=UakqL6Pj9xo"
transcript_url: /transcripts/dwarkesh/77_francois_chollet_why_the_biggest_ai_models_can_t_solve_simple_puzzles/
permalink: /transcripts/dwarkesh/77_francois_chollet_why_the_biggest_ai_models_can_t_solve_simple_puzzles.analysis/
---

# Analysis: Francois Chollet — Why the biggest AI models can't solve simple puzzles

## 0. 3-5 句摘要

Francois Chollet 在这集综合访谈中完整阐述了他对LLM局限性的核心论点：最大的AI模型在ARC这样的简单视觉推理测试上表现糟糕，因为ARC的每个谜题都是全新的，无法通过记忆化解决。他宣布了百万美元ARC奖金（其中50万给首个达到85%的团队），并详细解释了为什么当前最好的方法（Jack Cole的测试时微调）本质上是在弥补LLM缺失的"主动推理"能力。Chollet 还批评了OpenAI关闭前沿研究发表的做法，认为这让AGI进展倒退了5-10年，因为LLM"吸走了房间里所有的氧气"，让所有人都只做LLM研究。

## 1. 反共识/非显然观点

- **[01:07] ARC是AI的IQ测试**：与所有现有基准不同，ARC被设计为抗记忆化——每个谜题都是新的，只需要4-5岁儿童的核心知识（基本物理、计数、对称性），但LLM在上面的表现远不如普通人。Amazon Mechanical Turk工人（普通人）得分约85%。
- **[15:37] 不做测试时微调=1-2%的得分**：Jack Cole的方法之所以有效，关键不是模型大小或预训练数据，而是对每个测试问题进行即时微调。去掉这一步，得分从35%暴跌到1-2%。这证明LLM缺失的核心能力是"主动推理"。
- **[00:23] OpenAI让AGI倒退5-10年**：不是因为技术方向错误，而是因为关闭前沿研究发表导致整个领域只做LLM，其他可能通向AGI的研究路径被资源饥饿。

## 2. 关键洞察

- ARC只需要"核心知识"（物理直觉、物体概念、计数、几何、拓扑、对称性），这些知识LLM肯定拥有——问题不在知识而在推理机制
- 多模态模型不会自动解决ARC，因为ARC的网格很小（不像图像那样需要视觉处理），LLM完全可以处理序列化的网格数据
- 测试时微调是向LLM添加"主动推理"的一种方式，这个方向比单纯扩大模型更有前途
- 技能（skill）和智能（intelligence）的混淆是当前AI领域最大的概念错误
- 百万美元奖金的激励设计参考了Vesuvius Challenge的成功模式

## 3. Takeaway

- 当一个系统在"简单"任务上失败而在"困难"任务上成功时，说明它使用了与人类根本不同的机制。这种不对称性是诊断系统真实能力的最佳信号。

