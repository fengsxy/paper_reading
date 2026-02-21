---
date: 2024-01-01
layout: default
type: analysis
series: dwarkesh
episode: 83
guest: ""
title: "Why GPT-4 is much smarter than it was a year ago – OpenAI cofounder John Schulman - Analysis"
source_url: "https://www.youtube.com/watch?v=JclnqKZBTUU"
transcript_url: /transcripts/dwarkesh/83_why_gpt_4_is_much_smarter_than_it_was_a_year_ago_openai_cofounder_john_schulman/
permalink: /transcripts/dwarkesh/83_why_gpt_4_is_much_smarter_than_it_was_a_year_ago_openai_cofounder_john_schulman.analysis/
---

# Analysis: Why GPT-4 is much smarter than it was a year ago – OpenAI cofounder John Schulman

## 0. 3-5 句摘要

John Schulman 透露了一个令人惊讶的事实：当前 GPT-4 的 ELO 评分比发布时高出约100分，而这些提升大部分来自 post-training 而非预训练。他描述了 post-training 作为一种"护城河"的特性——它需要大量隐性知识、组织知识和多轮迭代的 R&D 积累，不是简单可以复制的。同时他承认较小的玩家可能通过蒸馏、克隆输出或使用他人模型作为评判器来缩小差距，但这些做法违反服务条款且有尊严成本。

## 1. 反共识/非显然观点

- **[00:44] GPT-4 的大部分进步来自 post-training 而非预训练**：发布后 ELO 提升100分，主要归功于数据质量、数据量、迭代收集新标注数据等 post-training 改进——这意味着"更大的预训练模型"不是唯一的进步路径。
- **[01:41] Post-training 是一种真正的护城河**：它需要大量熟练人员、隐性知识和组织知识的积累，不是简单的工程问题。这与"谁有最多 GPU 谁就赢"的叙事形成对比。
- **[03:14] 小玩家通过蒸馏和输出克隆在追赶**：Schulman 暗示一些较小的 AI 公司正在使用竞争对手的模型输出来训练自己的模型——这是一个公开的秘密。
- **[03:41] 好的 post-training 研究者需要"全栈视野"**：从 RL 算法到数据收集到标注流程，需要对整个栈有好奇心，同时兼具经验主义和第一性原理思维。

## 2. 关键洞察

- Post-training 的改进是多个独立轴向的叠加效应：数据质量、数据量、迭代次数、标注类型变化——每个单独看起来不大，但叠加后相当于显著的"有效计算量增加"
- 模型生成的输出质量可能已经高于互联网上大部分内容——这为"模型自我训练"提供了第一性原理的论据
- Post-training 的复杂性意味着 AI 竞争不仅仅是算力竞赛，更是组织能力和人才密度的竞赛

## 3. Takeaway

- AI 模型的进步越来越多地来自"训练后"的精细调优而非"训练前"的暴力扩展——这改变了 AI 竞争的格局，从纯算力竞赛转向工程和研究能力的竞赛
