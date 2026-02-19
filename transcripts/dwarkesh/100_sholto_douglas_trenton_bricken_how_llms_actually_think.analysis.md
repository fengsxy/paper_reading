---
layout: default
type: analysis
series: dwarkesh
episode: 100
guest: "Sholto Douglas, Trenton Bricken"
title: "Sholto Douglas & Trenton Bricken — How LLMs actually think - Analysis"
source_url: "https://www.youtube.com/watch?v=UTuuTTnjxMQ"
transcript_url: /transcripts/dwarkesh/100_sholto_douglas_trenton_bricken_how_llms_actually_think/
permalink: /transcripts/dwarkesh/100_sholto_douglas_trenton_bricken_how_llms_actually_think.analysis/
---

# Analysis: Sholto Douglas & Trenton Bricken — How LLMs Actually Think

## 0. 3-5 句摘要

这期对话汇集了 Google DeepMind 的 Sholto Douglas（pre-training/系统优化）和 Anthropic 的 Trenton Bricken（mechanistic interpretability），围绕"LLM 内部到底在做什么"展开了一场罕见的跨实验室深度讨论。核心论点是：模型通过 superposition 在有限维度中编码远超神经元数量的 features，而 dictionary learning（稀疏自编码器）可以将这些 features 解纠缠出来，为理解和控制模型行为提供了一条可行路径。Sholto 从系统-算法交叉的视角强调了"理解全栈约束"对 ML 研究的重要性，而 Trenton 则展示了 interpretability 如何从学术好奇心走向实际安全工具——包括检测欺骗电路、ablation 修复、以及 feature splitting 的层级搜索策略。两人都对 feature universality（不同模型学到相同 features）持乐观态度，认为这为跨模型安全审计提供了基础。对话最后触及了一个深刻的张力：alignment 成功得"太好"可能比失败更危险——谁来控制这些精细调控工具？

## 1. 反共识/非显然观点

- **"Associations all the way down"可能就是智能的全部** [1:10:00 区间]：Trenton 认为不存在某个神秘的"推理模块"，智能可能就是 features 之间的关联链条不断组合。这与直觉上"推理需要某种特殊机制"的看法相悖。他承认自己找不到一个能证伪这个框架的替代假说，这本身既是信心的来源也是隐忧。

- **非传统路径入行可能比 PhD 更有优势** [1:46:00]：Sholto 作为前麦肯锡顾问、击剑运动员，被 James Bradbury 作为"实验"招入 Google——实验内容是"高 agency + 顶级导师配对"能否 bootstrap 出顶级研究者。结果是肯定的，而且他认为没有被某个子领域"锁定"反而让他能看到跨领域的 pattern。这挑战了"必须读 PhD"的学术正统。

- **Feature splitting 允许深度优先搜索，而非暴力枚举** [2:40:33]：Trenton 提出了一个关键的可扩展性论点——你不需要一次性把模型投射到百万维空间来找到 anthrax feature，可以先用低维投射找到 biology feature 的方向，然后沿着那个方向递归展开。这把 interpretability 的计算成本从 O(n) 降到了类似 O(log n) 的搜索。

- **Google 内部的"去办公室"alpha** [1:51:44]：Sholto 直言，在 Google 这样的大组织里，"每天去办公室"本身就是一种惊人的竞争优势——因为你会成为和 Sergey Brin、Jeff Dean 一起 pair programming 的那个人。这是一个反远程工作叙事的观点，但他也强调不应该滥用这种接近权。

- **Alignment 成功可能比失败更危险** [3:03:22]：Dwarkesh 提出了一个尖锐的问题——如果 interpretability 真的成功了，谁来控制"loyalty feature 被调高"这种操作？Trenton 承认这是一个真实的担忧，但认为当前的参与者"极其善意"。这个回答本身就暴露了一个脆弱假设。

## 2. 可学习的点（可迁移的方法论）

- **系统约束决定算法设计空间** [1:47:33]：Sholto 的核心方法论——深入理解系统层面（硬件、编译器、推理约束）如何约束算法选择。很少有人能同时桥接这两端，但能做到的人在 pre-training 和芯片设计两边都极有价值。这个"约束树"思维可以应用到任何工程决策中。

- **"制造运气"的策略** [1:56:43]：两人都强调了 agency 的重要性——Sholto 通过独立做项目被注意到，Trenton 通过去会议和随机交谈遇到了 Tristan Hume。共同点是：把自己放在"运气更可能发生"的位置上，而不是等待正式渠道。

- **用异常检测替代标签依赖** [2:34:41]：Trenton 指出 dictionary learning 的一个关键优势——它是无监督的，所以你可以先找到所有 features，然后用异常检测（"这个 feature 从没见过它 fire"）来标记可疑行为，而不需要预先知道你在找什么。这比 linear probe 的"你必须先知道标签"要强大得多。

- **"Caring an unbelievable amount"作为竞争优势** [2:03:06]：Sholto 引用 LeBron 的例子——进入联盟后发现很多人在达到财务稳定后就放松了。在 AI 研究中也是如此：关心整个 stack（而不只是自己的问题）、主动修复不属于自己职责的东西，这种态度本身就是稀缺资源。

## 3. 提问技巧（采访方法）

- **用"反事实"逼出框架边界** [2:09:54]：Dwarkesh 反复追问"什么发现会让你觉得这个方向是错的？"——这是一种极好的提问技巧，因为它迫使研究者暴露自己框架的可证伪性（或缺乏可证伪性）。Trenton 的回答"我找不到替代假说"本身就是重要信息。

- **用具体例子锚定抽象讨论** [2:12:54]：当讨论变得过于抽象（"什么是 feature？"）时，Dwarkesh 用"bird vs. period at end of hyperlink vs. love"这样的具体例子把讨论拉回地面，迫使 Trenton 给出更精确的定义。

- **跨嘉宾交叉提问** [1:53:49]：Dwarkesh 在 Sholto 讲完自己的故事后问 Trenton "does this map onto your experience?"——这种技巧让两位嘉宾的经历形成对比和互补，而不是各说各的。

- **挑战乐观叙事的暗面** [3:03:22]：在整期都在讨论 interpretability 的美好前景后，Dwarkesh 在最后抛出"你担心 alignment 成功得太好吗？"——这种在对话高潮时翻转视角的技巧非常有效。

## 4. 可进一步验证/挖坑

- **Feature universality 的边界在哪里**：base64 feature 在不同模型间有高 cosine similarity，但这是否适用于更高层的抽象 features（如 deception、theory of mind）？如果高层 features 不具有 universality，跨模型安全审计的前提就不成立。

- **Feature splitting 的几何结构是否语义一致**：Trenton 承认还没有深入研究 feature 的几何组织——anthrax feature 是否真的在 biology feature 附近？如果语义树和几何结构不一致（anthrax 在 coffee 子树下），整个深度优先搜索策略就会失效。

- **Sleeper agents 的 dictionary learning 检测**：Trenton 提到正在用 dictionary learning 检测 sleeper agents 中的隐藏触发器。这个方向的成功与否对 interpretability 的实际安全价值是一个关键测试。

- **"Quanta theory of neural scaling"的可证伪预测**：如果所有模型在相似数据上学到相同 features 且顺序一致，那么 curriculum learning 应该有效——但 Sholto 说实际上 curriculum learning 的效果不明确。这个矛盾值得深挖。

- **MoE 模型中的 expert specialization**：Sholto 提到 Vision Transformer 的 MoE 有清晰的类别专门化，但 Mixtral 论文没有发现类似现象。用 dictionary learning 对 Mixtral 的 experts 做 interpretability 分析是一个明确的开放研究方向。
