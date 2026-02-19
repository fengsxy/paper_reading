---
layout: default
type: analysis
series: dwarkesh
episode: 111
guest: "Demis Hassabis"
title: "The Fastest Way to AGI: LLMs + Tree Search – Demis Hassabis - Analysis"
source_url: "https://www.youtube.com/watch?v=eqXfhejDeqA"
transcript_url: /transcripts/dwarkesh/111_the_fastest_way_to_agi_llms_tree_search_demis_hassabis_google_deepmind_ceo/
permalink: /transcripts/dwarkesh/111_the_fastest_way_to_agi_llms_tree_search_demis_hassabis_google_deepmind_ceo.analysis/
---

# Analysis: The Fastest Way to AGI: LLMs + Tree Search – Demis Hassabis

## 0. 3-5 句摘要

Demis 提出了他对 AGI 最可能路径的判断：LLM 作为世界模型 + Alpha Zero 式的规划/搜索。LLM 是"必要但可能不充分"的——它们提供了对世界的理解，但缺少将理解转化为行动计划的搜索机制。他用 Alpha Zero vs Deep Blue 的对比说明了"更好的模型 = 更高效的搜索"——Alpha Zero 只看数万个位置就能超过看数百万个位置的 Deep Blue，因为它有更好的世界模型。这暗示 AGI 的计算成本可能比人们想象的低。

## 1. 反共识/非显然观点

- **"LLM 是必要但不充分的"** [00:22]：Demis 是少数公开说"仅靠 LLM 不够"的顶级 AI 领导者。他认为还需要 Alpha Zero 式的规划和搜索。

- **"更好的模型让搜索更便宜"** [02:56]：人类棋手只看几百个位置就能做出世界级决策，因为他们的"模型"比 Alpha Zero 更好。这意味着 AGI 的推理成本可能随着模型改善而大幅下降。

- **"纯 RL 理论上可行但不实际"** [01:25]：Demis 承认从零开始的 Alpha Zero 式方法理论上可以达到 AGI，但"为什么不利用已有的知识？"——这是一个务实的工程判断。

## 2. 可学习的点（可迁移的方法论）

- **"模型质量 vs 搜索量"的 trade-off** [03:08]：Deep Blue（差模型 + 大量搜索）→ Alpha Zero（好模型 + 中等搜索）→ 人类（最好模型 + 最少搜索）。这个 trade-off 曲线对理解 test-time compute 的价值有直接指导意义。

- **"reward function 是真实世界 RL 的核心挑战"** [04:49]：游戏有内置的 reward function（赢/输），但真实世界没有。如何定义正确的目标函数是从游戏 AI 到通用 AI 的关键瓶颈。

## 3. 提问技巧（采访方法）

- **"这需要多少 compute？"** [02:32]：Dwarkesh 直接追问实际的计算成本，把理论讨论拉回工程现实。

## 4. 可进一步验证/挖坑

- **o1/o3 是否验证了"LLM + 搜索"路径**：OpenAI 的 o1/o3 系列本质上就是"LLM + 某种形式的搜索"。它们的成功是否验证了 Demis 的预测？

- **reward function 问题的进展**：constitutional AI、RLHF、process reward models 是否部分解决了"真实世界 reward function"的问题？
