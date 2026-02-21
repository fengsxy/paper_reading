---
date: 2024-01-01
layout: default
type: analysis
series: dwarkesh
episode: 6
guest: "Ilya Sutskever"
title: "Ilya Sutskever — We're moving from the age of scaling to the age of research - Analysis"
source_url: "https://www.youtube.com/watch?v=aR20FWCCjAs"
transcript_url: /transcripts/dwarkesh/6_ilya_sutskever_we_re_moving_from_the_age_of_scaling_to_the_age_of_research/
permalink: /transcripts/dwarkesh/6_ilya_sutskever_we_re_moving_from_the_age_of_scaling_to_the_age_of_research.analysis/
---

# Analysis: Ilya Sutskever — We're moving from the age of scaling to the age of research

## 0. 3-5 句摘要

这是 Ilya Sutskever 离开 OpenAI 创立 SSI（Safe Superintelligence Inc.）后的一次深度对话，核心论点是 AI 正在从"scaling 时代"回归"研究时代"——不是因为 scaling 失败了，而是因为当前的 scaling recipe（pre-training + RL）在泛化能力上存在根本性缺陷。Ilya 用一个精妙的类比说明了问题：一个练了 10000 小时竞赛编程的学生 vs 一个只练了 100 小时但有"it factor"的学生，后者在职业生涯中表现更好——当前模型更像前者，RL 训练让它们在 eval 上表现惊人但在真实世界中脆弱。他提出了几个关键的研究方向：value function（让模型在长推理链中获得中间反馈而非只在终点获得奖励）、情感作为 value function 的类比（引用了一个失去情感处理能力后无法做决策的脑损伤案例）、以及模型泛化能力远不如人类这一"超级明显"但未被解决的根本问题。整个对话的底层张力是：Ilya 显然知道很多他不能说的东西，但他通过精心选择的类比和暗示传达了对当前 AI 发展路径的深层担忧。

## 1. 反共识/非显然观点

- **"Scaling 时代已经结束，我们回到了研究时代"** [19:06]：这是整期对话的标题论点。Ilya 认为 2012-2020 是研究时代，2020-2025 是 scaling 时代，现在又回到了研究时代——但这次有大计算机。关键不是"scaling 不 work"，而是当前的 scaling recipe 已经不是最高效的资源使用方式。这与"只要继续 scale 就行"的主流叙事直接矛盾。

- **"RL 训练可能让模型变得过于单一和狭隘"** [03:02]：Ilya 提出了一个"whimsical"但深刻的假说——RL 训练在让模型变强的同时，也让它们变得"unaware"。这解释了为什么模型能在 coding competition 上超人但会在 vibe coding 中交替引入两个 bug。这不是能力不足，而是某种认知结构的扭曲。

- **"真正的 reward hacking 是人类研究者太关注 eval"** [05:03]：Dwarkesh 的总结精准地捕捉了 Ilya 的第二个假说——eval 性能和真实世界性能的脱节不是因为模型在 hack reward，而是因为人类研究者在设计 RL 环境时不自觉地从 eval 中取灵感，导致模型过拟合到 eval 的分布上。

- **"情感是进化给人类的 value function，而且因为简单所以鲁棒"** [12:33]：Ilya 引用了一个失去情感处理能力的脑损伤患者——他在测试中表现正常但无法做任何日常决策。Ilya 的推论是：情感的"简单性"恰恰是它的优势，因为简单的 value function 在分布外情况下更鲁棒。这对 AI 的 reward design 有直接启示。

- **"Pre-training 没有人类类比"** [09:33]：Ilya 明确否定了两个常见类比——"pre-training 像人类前 18 年的学习"和"pre-training 像进化"。他认为两者都有部分相似性，但人类用极少数据学到的东西"somehow much more deeply"。这暗示当前的 pre-training paradigm 可能在根本层面上缺少某些东西。

## 2. 可学习的点（可迁移的方法论）

- **"两个学生"框架用于评估能力 vs 泛化** [06:07]：Ilya 的竞赛编程类比是一个可以广泛应用的思维工具——当你看到一个系统在 benchmark 上表现惊人时，问自己：它是"10000 小时学生"还是"100 小时学生"？前者的能力来自过拟合，后者来自泛化。这个区分对评估任何 AI 系统的真实能力都有价值。

- **Value function 作为"短路"长推理链的工具** [14:43]：Ilya 用下棋丢子的例子解释了 value function 的核心价值——你不需要下完整盘棋才知道丢子是坏的。在 AI 的长推理链中，value function 可以在中间步骤就提供反馈，而不是等到最终答案。这把 RL 的计算效率从 O(trajectory length) 降到了 O(1) per step。

- **"语言影响思维"在 ML 研究中的应用** [19:45]：Ilya 指出"scaling"这个词本身就是一个强大的思维工具——它告诉人们该做什么。这个观察可以推广：在研究中，找到正确的"一个词"来描述你的方向，可能比具体的技术细节更重要，因为它会引导整个社区的注意力。

- **复杂性-鲁棒性 trade-off** [17:41]：Ilya 提出了一个优雅的框架——复杂的东西在特定情况下很有用，但简单的东西在广泛情况下都有用。这解释了为什么进化选择了"简单"的情感系统而非复杂的推理系统作为人类的 value function。这个 trade-off 对 AI 系统设计有直接指导意义。

## 3. 提问技巧（采访方法）

- **用"两种解读"结构化模糊回答** [05:09]：当 Ilya 给出一个可以多种解读的回答时，Dwarkesh 主动提出"有两种理解方式"——一种是"扩大 RL 环境的多样性"，另一种是"为什么泛化本身不 work"。这种技巧帮助嘉宾澄清自己的真实意思，也帮助听众理解讨论的层次。

- **用嘉宾的类比反问嘉宾** [07:42]：Dwarkesh 在 Ilya 给出"两个学生"类比后追问"那第二个学生在做 100 小时 fine-tuning 之前在做什么？"——这迫使 Ilya 给出了"it factor"这个回答，暴露了他的框架中最模糊但也最重要的部分。

- **区分"sample efficiency"和"teachability"** [25:20]：Dwarkesh 把"为什么模型需要这么多数据"和"为什么模型这么难教"区分为两个独立问题。这种分解让讨论更精确，也让 Ilya 能分别回应每个问题。

- **"这是不是就是 X？"的确认式提问** [05:03]：Dwarkesh 说"我喜欢这个想法——真正的 reward hacking 是人类研究者太关注 eval"。这种用一句话总结嘉宾观点的技巧既确认了理解，也给了嘉宾修正的机会。

## 4. 可进一步验证/挖坑

- **"It factor"的可操作化**：Ilya 说第二个学生有"it factor"但没有进一步定义。这是整个讨论中最关键的未解问题——如果我们能理解"it factor"是什么，就能设计出更好的训练方法。可能的方向：meta-learning、curiosity-driven exploration、或某种形式的"认知多样性"训练。

- **Eval 过拟合的量化**：Ilya 的假说——RL 环境设计受 eval 启发导致过拟合——是可以经验检验的。方法：比较模型在"受 eval 启发的 RL 环境"和"完全独立设计的 RL 环境"上训练后的泛化差异。

- **Value function 在长推理链中的实际效果**：Ilya 预测 value function 会被广泛使用。截至 2026 年初，o1/o3/R1 系列是否已经在使用 value function？如果是，泛化问题是否有改善？

- **"情感 = 简单 value function"假说的 interpretability 验证**：如果 Ilya 是对的，那么在 RLHF 训练后的模型中，应该能找到类似"情感"的简单 value function features。Anthropic 的 dictionary learning 工作是否能检测到这种结构？

- **Pre-training 泛化 vs RL 泛化的根本差异**：Ilya 暗示 pre-training 的泛化和 RL 的泛化可能有本质不同。如果 pre-training 的主要优势只是"数据量大"而非"泛化好"，那么 synthetic data 的 pre-training 可能不会带来预期的改善。
