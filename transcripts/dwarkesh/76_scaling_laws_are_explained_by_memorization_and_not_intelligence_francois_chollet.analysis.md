---
layout: default
type: analysis
series: dwarkesh
episode: 76
guest: ""
title: "Scaling laws are explained by memorization and not intelligence – Francois Chollet - Analysis"
source_url: "https://www.youtube.com/watch?v=rl7B-LHiaNo"
transcript_url: /transcripts/dwarkesh/76_scaling_laws_are_explained_by_memorization_and_not_intelligence_francois_chollet/
permalink: /transcripts/dwarkesh/76_scaling_laws_are_explained_by_memorization_and_not_intelligence_francois_chollet.analysis/
---

# Analysis: Scaling laws are explained by memorization and not intelligence – Francois Chollet

## 0. 3-5 句摘要

François Chollet 提出了一个尖锐的论点：LLM 的 scaling laws 衡量的是记忆能力的提升而非智能的提升。他区分了两种"推理"——从记忆中检索已有程序模板（program fetching）vs 即时合成新程序（on-the-fly program synthesis），认为 LLM 只做前者。Chollet 指出当前所有 LLM 基准测试本质上都是记忆型测试，即使是看似需要推理的数学题，也只需要从有限的解题模板库中匹配正确模板。他承认记忆和技能对实际应用极其有用，但坚持认为这与真正的通用智能（面对全新问题时即时适应的能力）是根本不同的。

## 1. 反共识/非显然观点

- **[00:00] 通用智能不是"特定技能的规模化"**：Chollet 的核心论点是 generality ≠ specificity scaled up。无论你记忆了多少技能，如果不能面对全新问题即时学习，就不是通用智能。这直接挑战了"足够大的模型=AGI"的主流叙事。
- **[02:07] LLM 做的是"程序检索"而非"程序合成"**：LLM 维护着一个巨大的解题程序模板库，面对新问题时只是匹配最合适的模板——这看起来像推理，但本质上是记忆检索。真正的推理需要从已有程序片段即时组装新程序。
- **[01:22] 所有 LLM 基准测试都是记忆型测试**：即使是 GSM-8K 这样的数学推理基准，也只需要有限的解题模板就能达到95%正确率。Scaling laws 的"性能提升"本质上是记忆容量的提升。
- **[03:59] 两种"推理"的定义之争**：Chollet 承认如果把"从模板库中匹配并执行"也算推理，那 LLM 确实在推理。但他认为更有意义的定义是"面对没有现成模板的问题时合成新程序"——这才是智能的核心。

## 2. 关键洞察

- 技能（skill）和智能（intelligence）的区别是根本性的：技能是在已知分布上的表现，智能是面对分布外问题时的适应能力
- 人类学习数学也需要大量训练（从前代数到微积分），但人类能做到的关键区别是：用少量新信息即时适应全新类型的问题
- ARC 基准测试在发布4年后仍然抵抗了 LLM 的记忆攻击，但 Chollet 承认如果生成足够多的变体（数亿个任务），暴力覆盖任务空间也能"作弊"得高分
- 即使 Chollet 的论点完全正确（LLM 只是记忆而非智能），这并不意味着 LLM 没有巨大的实用价值——大多数人类工作也是在"静态分布"上执行已知技能

## 3. Takeaway

- "模型越来越强"和"模型越来越智能"可能是两个完全不同的命题——前者可以通过扩大记忆实现，后者可能需要根本不同的架构
- 在评估 AI 进展时，区分"在已知问题类型上的表现"和"面对全新问题类型的适应能力"至关重要
