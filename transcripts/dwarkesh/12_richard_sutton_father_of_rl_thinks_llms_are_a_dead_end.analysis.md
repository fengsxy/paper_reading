---
layout: default
type: analysis
series: dwarkesh
episode: 12
guest: ""
title: "Richard Sutton (Father of RL) thinks LLMs are a dead end - Analysis"
source_url: "https://www.youtube.com/watch?v=LNRxMHsJGJE"
transcript_url: /transcripts/dwarkesh/12_richard_sutton_father_of_rl_thinks_llms_are_a_dead_end/
permalink: /transcripts/dwarkesh/12_richard_sutton_father_of_rl_thinks_llms_are_a_dead_end.analysis/
---

# Analysis: Richard Sutton (Father of RL) thinks LLMs are a dead end

## 0. 3-5 句摘要

强化学习之父 Richard Sutton 提出了一个挑衅性的核心论点：LLM 是"死胡同"，因为它们本质上是在模仿人类文本而非学习世界模型。Sutton 认为真正的智能需要"grounded"的世界模型——agent 必须通过与环境的交互来学习因果关系，而不是从文本中提取统计相关性。他将当前的 LLM 热潮类比为 AI 历史上反复出现的"知识工程"诱惑——每次人们都试图将人类知识直接编码进系统，而非让系统自己学习。对话深入探讨了 Sutton 著名的"苦涩教训"（The Bitter Lesson）：长期来看，利用计算的通用方法总是胜过利用人类知识的特定方法。

## 1. 反共识/非显然观点

- **LLM 的"理解"是虚假的，因为它们没有 grounding** [08:00-09:30]：Sutton 认为 LLM 对"火是热的"的"理解"与一个真正被火烫过的 agent 的理解有本质区别——前者是统计关联，后者是因果模型。这挑战了"scaling 就能涌现真正理解"的主流观点。
- **搜索（search）是智能的核心，而非模式匹配** [15:00-16:30]：Sutton 坚持认为 AlphaGo 式的"学习+搜索"范式比纯 LLM 的"学习+生成"范式更接近真正的智能。搜索允许系统在行动前"想象"多种可能性并评估后果——这正是 LLM 缺乏的。

## 2. 关键洞察

- "苦涩教训"的核心不是"更多计算总是更好"，而是"利用计算的通用方法总是胜过利用人类知识的特定方法"——这意味着即使 LLM 在短期内表现出色，长期赢家可能是更通用的学习范式。
- Sutton 对 AI 时间线持保守态度，认为 AGI 可能需要数十年——因为我们还没有找到正确的"学习世界模型"的算法。
- 当前 RL 的最大瓶颈不是算法而是"奖励信号"——在现实世界中定义正确的奖励函数比在棋盘游戏中困难几个数量级。

## 3. Takeaway

- Sutton 的批评提供了一个有价值的"压力测试"：如果 LLM 真的只是在做模式匹配而非建立世界模型，那么它们在需要因果推理的任务上将遇到根本性的天花板。关注 LLM 在物理推理、反事实推理等任务上的表现，可以帮助判断 Sutton 是否正确。
