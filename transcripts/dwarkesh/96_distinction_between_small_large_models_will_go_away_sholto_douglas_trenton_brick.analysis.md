---
date: 2024-01-01
layout: default
type: analysis
series: dwarkesh
episode: 96
guest: ""
title: "Distinction between small & large models will go away – Sholto Douglas & Trenton Bricken - Analysis"
source_url: "https://www.youtube.com/watch?v=AOt0GwY8IvU"
transcript_url: /transcripts/dwarkesh/96_distinction_between_small_large_models_will_go_away_sholto_douglas_trenton_brick/
permalink: /transcripts/dwarkesh/96_distinction_between_small_large_models_will_go_away_sholto_douglas_trenton_brick.analysis/
---

# Analysis: Distinction between small & large models will go away – Sholto Douglas & Trenton Bricken

## 0. 3-5 句摘要

Sholto Douglas 和 Trenton Bricken 预测了 AI 模型生态的根本性变化：大模型与小模型的区分将消失，取而代之的是"动态计算包"——根据任务需求自动分配计算量。同样，微调（fine-tuning）可能被无限上下文窗口取代。他们还纠正了一个流行误解：AI agent 没有起飞不是因为长时间跨度任务的困难，而是因为可靠性的"九"不够——当单步成功率从99%提升到99.9%时，100步链式任务的成功率从36%跃升到90%。这意味着 agent 的突破可能是阶跃函数而非渐进提升。

## 1. 反共识/非显然观点

- **[00:00] 模型大小的区分将消失**：当前"8B/70B/405B"的分层模型生态是暂时的。未来将是一个动态计算系统，根据任务复杂度自动分配资源——就像云计算的弹性伸缩。
- **[01:02] Agent 失败的原因是可靠性而非长时间跨度**：Douglas 明确反驳了"agent 因为无法处理长时间任务而失败"的流行叙事。真正的瓶颈是单步可靠性——即使每步99%可靠，100步后只剩36%成功率。
- **[01:21] Agent 突破将是阶跃函数**：当模型能力跨过某个可靠性阈值时，agent 将突然从"不可用"变为"可用"——不是渐进改善，而是相变。
- **[04:31] "AI 公司"可能就是一个模型而非一群 agent**：长上下文+通用能力意味着一个模型可以同时处理前端、后端、设计等所有任务，不需要像人类公司那样分工——专业化的经济学逻辑（Hayekian knowledge problem）对 AI 不适用。

## 2. 关键洞察

- 可靠性的"九"比原始能力更重要：从99%到99.9%的提升在单次任务上几乎不可察觉，但在链式任务上是质变
- 长上下文窗口的突破速度超出所有人预期——不到一年前100K上下文还被认为不可能（"二次注意力成本"的口头禅），现在已经是标准配置
- 端到端 RL 训练（用最终结果信号训练整个系统）是终极目标，但需要模型先足够好以偶尔获得奖励——这是一个鸡生蛋的问题
- 近期 AI 系统将更像"人类监督下的 agent 协作"而非"端到端自主系统"——人类的角色是提供可靠性保障

## 3. Takeaway

- AI 的经济影响可能呈阶跃函数而非线性增长——当可靠性跨过某个阈值时，大量当前"不可自动化"的工作将突然变得可自动化
- 评估 AI 进展的正确指标不是基准测试分数，而是"在不同时间跨度任务上的成功率"——分钟级、小时级、天级任务的自动化率才是真正的经济影响指标
