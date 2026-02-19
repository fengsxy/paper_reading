---
layout: default
type: analysis
series: dwarkesh
episode: 18
guest: "Dwarkesh Patel"
title: "Why I don't think AGI is right around the corner - Analysis"
source_url: "https://www.youtube.com/watch?v=nyvmYnz6EAg"
transcript_url: /transcripts/dwarkesh/18_why_i_don_t_think_agi_is_right_around_the_corner/
permalink: /transcripts/dwarkesh/18_why_i_don_t_think_agi_is_right_around_the_corner.analysis/
---

# Analysis: Why I don't think AGI is right around the corner

## 0. 3-5 句摘要

Dwarkesh 在这期独白中基于自己 100+ 小时使用 LLM 工具的亲身经验，论证了为什么 AGI 不会很快到来。核心论点是：LLM 缺乏持续学习能力——你无法像培训人类员工一样给模型高层反馈让它逐步改进，只能不断调整 system prompt，这就像"每次换一个新学生来读你的萨克斯风教学笔记"。他同时承认这个瓶颈可能被"模型自己为自己构建 RL 环境"的方式突破，但认为这需要的不仅是更聪明的模型，而是一种全新的学习范式。

## 1. 反共识/非显然观点

- **"Fortune 500 不用 LLM 不是因为管理层保守"** [00:16]：Dwarkesh 反驳了"企业采用慢是因为官僚"的叙事——真正的原因是 LLM 在实际工作流中只有 5/10 的水平，而且无法通过反馈改进。

- **"人类的价值不在于 raw intellect 而在于持续学习"** [02:03]：LLM 的 baseline 可能比普通人高，但人类员工的真正价值是"build up context, interrogate failures, pick up small improvements"——这些 LLM 完全做不到。

- **"萨克斯风类比"** [02:15]：你不可能通过写越来越详细的说明书来教一个从未吹过萨克斯风的人演奏 Charlie Parker——但这正是我们"教" LLM 的唯一方式。

## 2. 可学习的点（可迁移的方法论）

- **"100 小时实际使用 > 100 小时理论分析"** [00:41]：Dwarkesh 的判断来自亲身尝试构建 LLM 工具，而非阅读论文。这种"先用再评"的方法论对任何技术评估都有价值。

- **"模型自建 RL 环境"作为突破方向** [03:24]：如果模型能根据高层反馈自己设计练习题和验证环境，持续学习问题就可能被解决。这把问题从"架构限制"转化为"元学习能力"。

## 3. 提问技巧（采访方法）

- **用个人经验锚定抽象讨论**：Dwarkesh 没有引用论文或 benchmark，而是用自己尝试让 LLM 重写 transcript、识别 clip、协作写文章的具体经历来支撑论点。

## 4. 可进一步验证/挖坑

- **"5/10"评分是否在快速改善**：Dwarkesh 在 2025 年 7 月给 LLM 打 5/10。到 2026 年，同样的任务是否已经到了 7/10 或 8/10？

- **持续学习的实际进展**：test-time fine-tuning、long context learning、tool-augmented self-improvement 是否已经部分解决了 Dwarkesh 描述的问题？
