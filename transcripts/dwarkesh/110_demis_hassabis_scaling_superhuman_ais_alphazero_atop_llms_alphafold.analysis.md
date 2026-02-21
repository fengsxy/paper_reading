---
date: 2024-01-01
layout: default
type: analysis
series: dwarkesh
episode: 110
guest: ""
title: "Demis Hassabis — Scaling, superhuman AIs, AlphaZero atop LLMs, AlphaFold - Analysis"
source_url: "https://www.youtube.com/watch?v=qTogNUV3CAI"
transcript_url: /transcripts/dwarkesh/110_demis_hassabis_scaling_superhuman_ais_alphazero_atop_llms_alphafold/
permalink: /transcripts/dwarkesh/110_demis_hassabis_scaling_superhuman_ais_alphazero_atop_llms_alphafold.analysis/
---

# Analysis: Demis Hassabis — Scaling, superhuman AIs, AlphaZero atop LLMs, AlphaFold

## 0. 3-5 句摘要

DeepMind CEO Demis Hassabis 描绘了通往 AGI 的路线图：大型语言模型作为"世界模型"的基础层，AlphaZero 式的规划和搜索机制叠加在上面。他认为当前 LLM "几乎不合理地有效"——它们隐式学到了概念、抽象甚至某种程度的物理世界理解，这超出了几乎所有人的预期。但 Hassabis 坚持认为 LLM 本身"必要但可能不充分"，需要结合 RL 自我对弈、规划搜索和多模态感知才能达到 AGI。他还深入讨论了 AlphaFold 如何在两年内解决了蛋白质折叠问题（从50年未解到几乎完全解决），以及为什么科学发现是 AI 最有价值的应用方向。

## 1. 反共识/非显然观点

- **[00:00] AGI 可能在十年内实现**：Hassabis 作为该领域最资深的从业者之一，明确表示"如果在十年内出现 AGI 级系统，我不会感到惊讶"。
- **[06:22] LLM + AlphaZero 式搜索是最可能的 AGI 路径**：不是纯 scaling，也不是纯 RL，而是两者的结合——LLM 提供世界模型，AlphaZero 式搜索在其上进行规划。这与"只需要更大的 Transformer"和"需要全新架构"两种极端观点都不同。
- **[07:41] 更好的世界模型 = 更少的搜索**：AlphaZero 只搜索数万个位置就能击败搜索数百万位置的暴力系统，而人类大师只需搜索数百个。这暗示 AGI 的关键不是更多计算，而是更好的内部模型。
- **[17:02] LLM 的能力"几乎不合理地有效"**：Hassabis 承认即使是 scaling 假说的提出者也对 LLM 走到这一步感到惊讶——纯语言训练竟然能产生某种形式的概念理解和世界模型。
- **[17:58] RLHF 可能提供了意外的"接地"**：人类标注者本身是"接地的"（grounded in reality），他们的反馈可能将某种现实世界的理解传递给了模型——这是一个有趣的哲学假说。

## 2. 关键洞察

- 神经科学对 AI 的贡献是"方向性灵感"而非具体算法：强化学习、经验回放、注意力机制都源于对大脑的理解，但不是一对一的映射
- AlphaFold 的成功模式可以推广：识别一个有明确验证标准的科学问题→用 AI 搜索解空间→在两年内从"50年未解"到"基本解决"。这个模式适用于药物发现、材料科学等领域
- "虚拟大脑分析"（virtual brain analytics）是一个被严重低估的研究方向——用计算神经科学的技术来分析 AI 模型的内部表征
- Hassabis 的赌注是"50% scaling + 50% 新发明"——这比纯 scaling 派和纯创新派都更务实
- 多模态（视频、音频、物理交互）将提供真正的"接地"——纯语言模型的接地是意外的副产品，多模态接地将是系统性的

## 3. Takeaway

- AGI 最可能的形态不是"超大 LLM"也不是"纯 RL agent"，而是两者的结合——LLM 作为世界模型基础，搜索和规划作为推理引擎
- AI 对科学发现的加速可能是比"AI 替代人类工作"更重要的影响——AlphaFold 在两年内解决了50年的问题，这种加速如果推广到其他领域将是变革性的
