---
layout: default
type: analysis
series: dwarkesh
episode: 109
guest: "Demis Hassabis"
title: "Multimodality: The Next Big Step – Demis Hassabis - Analysis"
source_url: "https://www.youtube.com/watch?v=bFwWkyZ7yMo"
transcript_url: /transcripts/dwarkesh/109_multimodality_the_next_big_step_demis_hassabis_google_deepmind_ceo/
permalink: /transcripts/dwarkesh/109_multimodality_the_next_big_step_demis_hassabis_google_deepmind_ceo.analysis/
---

# Analysis: Multimodality: The Next Big Step – Demis Hassabis

## 0. 3-5 句摘要

Demis 描述了多模态作为通向 AGI 的关键一步——不仅仅是"能处理图片和文字"，而是通过视频、触觉、动作等多种模态的关联学习来实现真正的"grounding"。他认为当系统开始理解"我的行动如何影响世界"时，就获得了 RL agent 式的主动学习能力。关于机器人数据瓶颈，他同意 Ilya 的判断但指出大型多模态模型的迁移学习正在缓解这个问题——"token 可以是动作、文字、像素，都一样"。

## 1. 反共识/非显然观点

- **"多模态不是功能叠加而是能力涌现"** [00:49]：Demis 认为真正的多模态系统会出现跨模态的正迁移——"你因为理解了视频所以语言变得更好"。这与"多模态只是多个单模态模型拼在一起"的简单理解不同。

- **"多模态是 grounding 的一种形式"** [01:05]：这是一个重要的哲学立场——Demis 认为通过多模态学习获得的物理世界理解是"proper grounding"，而不仅仅是统计关联。

## 2. 可学习的点（可迁移的方法论）

- **"token 统一"框架** [02:13]：把所有模态都视为 token——动作是 token，文字是 token，像素是 token。这个统一框架简化了多模态系统的设计。

## 3. 提问技巧（采访方法）

- **引用其他嘉宾的观点** [01:40]：Dwarkesh 引用 Ilya 关于机器人数据瓶颈的观点来追问 Demis，让两位 AI 领袖的观点形成对话。

## 4. 可进一步验证/挖坑

- **跨模态正迁移的量化**：Demis 说"语言因为视频变得更好"。这个效应有多大？是否有 ablation 研究量化了多模态训练对单模态性能的提升？
