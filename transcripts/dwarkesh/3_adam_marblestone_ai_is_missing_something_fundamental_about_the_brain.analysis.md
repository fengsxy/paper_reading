---
date: 2024-01-01
layout: default
type: analysis
series: dwarkesh
episode: 3
guest: ""
title: "Adam Marblestone – AI is missing something fundamental about the brain"
source_url: "https://www.youtube.com/watch?v=_9V_Hbe-N1A"
transcript_url: /transcripts/dwarkesh/3_adam_marblestone_ai_is_missing_something_fundamental_about_the_brain/
permalink: /transcripts/dwarkesh/3_adam_marblestone_ai_is_missing_something_fundamental_about_the_brain.analysis/
---

# Analysis: Adam Marblestone – AI is missing something fundamental about the brain

## 0. 3-5 句摘要

Adam Marblestone（FRO 倡导者、E11bio 联合创始人）提出了一个核心框架：大脑由"学习子系统"（皮层，类似通用推理引擎）和"引导子系统"（皮层下区域，类似奖励函数+注意力调控）两部分组成，当前 LLM 主要复制了前者而几乎完全忽略了后者。他认为引导子系统的复杂性远超学习子系统——下丘脑的细胞类型比皮层多得多，因为每个本能反应（蜘蛛恐惧、社交奖励等）都需要基因预布线的专用电路。对话深入探讨了连接组学（connectomics）如何以低十亿美元级投资揭示大脑的架构和学习规则，以及 Lean 形式化证明如何通过 RLVR 加速数学和软件验证。Marblestone 的 AI 时间线偏向 10 年以上，理由是 LLM 的范式与大脑的模型基础 RL 仍然"诡异地不同"。

## 1. 反共识/非显然观点

- **引导子系统的基因复杂度远超学习子系统** [31:00-33:00]：皮层下区域有数千种特化细胞类型（每种对应一个本能回路），而皮层的细胞类型相对少且重复——这意味着进化在"奖励函数"上投入的基因资源远多于"通用学习算法"。这与 AI 社区将大部分精力放在扩展学习算法（scaling laws）而忽视奖励设计的做法形成鲜明对比。

- **纸夹最大化器可能真的可行，因为智能所需的最小驱动集远小于人类社会本能** [58:00-59:10]：Marblestone 引用 Steve Byrnes 的观点指出，让系统变"聪明"所需的引导信号（好奇心、探索欲）远少于让它具备人类伦理所需的信号。LLM 的预训练可能进一步降低了这个门槛——你不需要社交本能就能从文本中学习语言。

- **理解大脑应该关注架构和学习规则，而非解释单个神经元** [1:04:46-1:06:18]：Marblestone 认为试图找到"金门大桥电路"是徒劳的——就像你不会通过解读权重矩阵来理解 LLM 为什么智能。真正有价值的是描述大脑的"架构、损失函数、学习规则、初始化"，就像我们描述 transformer 一样。

## 2. 关键洞察

- 大脑的能效优势可能来自硬件-算法协同设计：低电压随机神经元天然适合采样，共置存储与计算消除了数据搬运瓶颈，这些是当前 GPU 架构无法复制的 [52:00-53:15]。
- 连接组学从电子显微镜转向光学显微镜可能带来类似基因组测序的成本暴跌——E11bio 的目标是将小鼠全脑连接组从数十亿美元降至数千万美元 [1:11:52-1:12:30]。
- Lean 形式化证明 + LLM 的 RLVR 可能彻底改变数学和软件验证：证明正确性成为完美的 RL 信号，类似 AlphaGo 的可验证搜索 [1:25:00-1:26:06]。
- 人类大脑的快速膨胀可能主要靠"复制已有皮层模块"而非发明新架构——从小鼠到人类的差异可能只需少量基因改变 [37:00-37:08]。

## 3. Takeaway

- 如果你在做 AI alignment 研究，Marblestone 的框架暗示：与其只关注 RLHF 的奖励模型，不如研究大脑引导子系统的多层级结构——模型无关 RL、TD 学习、皮层内的模型基础推理可能需要不同的对齐策略。
- 对于 AI 基础设施投资者：连接组学和形式化验证是两个可能被严重低估的领域，前者可能揭示全新的架构灵感，后者可能成为 AI 安全的基础设施层。
