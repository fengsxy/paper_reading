---
layout: default
type: analysis
series: dwarkesh
episode: 9
guest: "Andrej Karpathy"
title: "Andrej Karpathy — We're summoning ghosts, not building animals - Analysis"
source_url: "https://www.youtube.com/watch?v=48pxVdmkMIE"
transcript_url: /transcripts/dwarkesh/9_andrej_karpathy_we_re_summoning_ghosts_not_building_animals/
permalink: /transcripts/dwarkesh/9_andrej_karpathy_we_re_summoning_ghosts_not_building_animals.analysis/
---

# Analysis: Andrej Karpathy — "We're summoning ghosts, not building animals"

## 0. 3-5 句摘要

Karpathy 在这次对话中提出了一个核心隐喻：我们不是在"建造动物"，而是在"召唤幽灵"——LLM 是纯数字的、模仿人类的灵体，而非具有生物基础的智能体。他认为"agent 年"是过度炒作，更准确的说法是"agent 十年"，因为让 AI 真正像员工一样可靠地完成端到端任务还需要大量工程工作。最有洞察力的观点是关于"知识 vs 认知核心"的分离：pre-training 同时灌入了知识和智能，但知识可能反而在拖累模型，未来需要找到方法剥离知识、保留纯粹的认知能力。他还分享了 NanoChat 项目的教育哲学：不要写博客、不要做 slides，直接写代码、让它跑起来，这是唯一真正学到东西的方式。

## 1. 反共识/非显然观点

- **"幽灵而非动物"——LLM 的本体论定位** [00:17]：Karpathy 认为当前 AI 不是在复制生物智能，而是在创造一种全新的数字存在形式。这不是语义游戏——它直接影响你对 AI 能力边界的预期。幽灵可以瞬间复制、没有物理约束，但也没有具身经验。

- **知识可能在拖累智能** [14:00]：这是整场对话中最反直觉的观点。Karpathy 认为 pre-training 灌入的海量知识实际上让模型过度依赖记忆而非推理，导致它们在"数据分布之外"的任务上表现差。他建议未来需要"剥离知识、保留认知核心"。这与"更多数据 = 更好"的主流范式直接矛盾。

- **Pre-training 是"劣质版进化"** [12:51]：进化给了人类学习的算法，而非知识本身。Pre-training 则同时给了知识和算法，但两者纠缠在一起。Karpathy 认为这是一个需要解决的问题，而非特性。

- **In-context learning 可能就是一种梯度下降** [15:39]：虽然不是显式的梯度下降，但 Karpathy 认为 in-context learning 在功能上可能等价于某种形式的参数更新。这个观点模糊了"训练"和"推理"之间的界限。

- **所有改进因素"惊人地均等"** [26:45]：从 ImageNet 到现在，数据、硬件、软件、算法的贡献大致相当，没有哪个单一因素占主导。这意味着押注单一技术路线（比如只押 scaling）可能是错误的。

## 2. 可学习的点（可迁移的方法论）

- **"不要写博客，写代码"** [00:34]：Karpathy 的学习哲学极其明确——slides 和博客是知识的幻觉，只有亲手写代码并让它跑起来才能真正理解。这对任何技术学习者都适用。

- **"右屏参考，左屏从零写"** [29:06]：他建议学习 NanoChat 的方式是把代码放在右边屏幕，左边从零开始写，允许参考但不允许复制粘贴。这种"有参考的从零构建"是一种非常高效的学习方法。

- **"chunk growing"作为编程方法论** [29:25]：真正的代码不是从上到下线性写的，而是从多个小块开始，逐步生长和连接。这个过程本身包含了大量隐性知识，而最终代码库无法体现这些。

- **用"十年 vs 一年"来校准预期** [01:20]：当行业在炒作某个时间线时，把它乘以 10 通常更接近现实。这是一个简单但有效的去泡沫启发式。

## 3. 提问技巧（采访方法）

- **用对方的框架内部制造张力** [13:05]：Dwarkesh 在 Karpathy 说"pre-training 像进化"之后，立刻指出"进化给的是算法不是知识，但 pre-training 给的是知识"，迫使 Karpathy 深入解释这个类比的局限性。这种"在你的框架内找矛盾"的技巧非常有效。

- **把抽象概念锚定到具体经验** [27:34]：当讨论变得抽象时，Dwarkesh 把话题拉回到 Karpathy 刚发布的 NanoChat 项目，问"你刚写完所有代码，有什么意外发现？"用具体经验来验证抽象理论。

- **开场用对方自己的话** [00:51]：直接引用 Karpathy 的"decade of agents"推文作为开场，让对方解释自己的立场，而非从零开始建立语境。

## 4. 可进一步验证/挖坑

- **"知识拖累智能"假说的实验验证**：如果 Karpathy 是对的，那么在相同参数量下，用更少但更高质量的数据训练的模型应该在 OOD（out-of-distribution）任务上表现更好。这可以通过对比实验验证。

- **In-context learning 的机制研究**：Karpathy 暗示 ICL 可能是某种隐式梯度下降。这个方向已经有一些理论工作（如 Akyürek et al. 2022），值得追踪后续进展。

- **NanoChat 作为教育工具的效果**：8000 行代码覆盖完整 pipeline 的教育效果如何？可以追踪社区反馈和衍生项目。

- **"所有因素均等改进"是否会被打破**：如果未来某个单一突破（比如新架构）导致不成比例的进步，Karpathy 的"均等改进"观察就需要修正。
