---
layout: default
type: analysis
series: dwarkesh
episode: 6
guest: "Ilya Sutskever"
title: "Ilya Sutskever — We're moving from the age of scaling to the age of research - Analysis"
source_url: "https://www.youtube.com/watch?v=1yvBqasHLZs"
transcript_url: /transcripts/dwarkesh/6_ilya_sutskever_we_re_moving_from_the_age_of_scaling_to_the_age_of_research/
permalink: /transcripts/dwarkesh/6_ilya_sutskever_we_re_moving_from_the_age_of_scaling_to_the_age_of_research.analysis/
---

# Analysis: Ilya Sutskever — "We're moving from the age of scaling to the age of research"

## 0. 3-5 句摘要

Ilya Sutskever 在这次对话中传递了一个核心信号：纯粹的 scaling 时代正在结束，接下来的突破将来自真正的研究创新而非简单地堆算力。他对当前模型的"eval 表现 vs 经济影响"之间的巨大鸿沟感到困惑——模型在基准测试上表现惊人，但实际经济影响远远落后。最深刻的讨论围绕"value function"和"情感"展开：他认为人类的情感本质上是一种进化硬编码的 value function，而当前 RL 训练缺少这种中间信号，导致模型在长链推理中效率极低。他还暗示自己在 SSI 的研究方向涉及某种"不能公开讨论的 ML 想法"，这本身就是一个强信号。

## 1. 反共识/非显然观点

- **"Takeoff 感觉很正常"是最令人不安的观察** [00:14]：Ilya 指出我们正在投入 GDP 的 1% 到 AI 上，但这件事"感觉没什么大不了的"。他认为这种正常感本身就是不正常的——人类对指数变化的适应速度远超预期，这意味着即使进入奇点，大多数人可能也不会"感觉到"。

- **Eval 表现和经济影响的脱节是一个谜** [01:44]：模型在越来越难的 eval 上得高分，但经济影响"戏剧性地落后"。Ilya 没有给出解释，但他承认这个矛盾让他困惑。这暗示当前的 eval 体系可能在衡量错误的东西。

- **情感是进化硬编码的 value function** [13:00]：这不是比喻——Ilya 认为人类的情感系统在功能上就是一个 value function，它让人类能在不等到最终结果的情况下评估中间状态。当前 RL 缺少这种机制，导致训练效率极低（必须跑完整个 trajectory 才能获得信号）。

- **人类在数学/编程上的能力证明学习算法是通用的** [28:15]：数学和编程是进化史上不存在的技能，但人类能快速学会。这说明人类的学习能力不是特定领域的进化适应，而是某种更基础的通用机制。这对"AI 需要领域特定训练"的观点是一个挑战。

- **"不是所有 ML 想法都能公开讨论"** [31:37]：Ilya 在被追问"如何重新概念化模型训练"时，明确说他有很多想法但不能分享。这暗示 SSI 的研究方向可能涉及训练范式的根本性变革。

## 2. 可学习的点（可迁移的方法论）

- **用"value function"框架理解人类决策** [14:43]：Ilya 把 RL 中的 value function 概念映射到人类认知上，解释了为什么人类能在不完成整个任务的情况下判断"我走错了"。这个框架可以应用到任何需要中间反馈的学习场景。

- **"短路等待"作为效率原则** [15:12]：在 RL 中，value function 让你不需要等到游戏结束就知道丢了一个棋子是坏事。在现实决策中，能越早获得中间信号，学习效率越高。

- **区分"进化先验"和"通用学习"** [28:52]：当评估某个能力时，先问"这个能力在进化史上有多长的选择压力？"如果很短（如编程），那么人类在这方面的能力更可能来自通用学习机制而非特定适应。

## 3. 提问技巧（采访方法）

- **用"连接到你之前说的"制造深度** [12:33]：Dwarkesh 反复把新话题连接回 Ilya 之前的观点（"to connect to your question about pre-training"），让对话形成递归深入而非平行跳跃。

- **在对方说"我不能说"时不放弃** [31:27]：当 Ilya 暗示有不能公开的想法时，Dwarkesh 继续追问"how do we need to reconceptualize"，虽然没得到直接答案，但迫使 Ilya 给出了更多间接线索。

- **用具体论文挑战抽象观点** [15:52]：Dwarkesh 引用 DeepSeek R1 论文中"trajectory 空间太大导致 value function 难学"的观点来挑战 Ilya 对 value function 的乐观态度。Ilya 的回应（"这是对深度学习缺乏信心"）本身就很有信息量。

## 4. 可进一步验证/挖坑

- **"Scaling 时代结束"的可验证性**：如果 Ilya 是对的，未来 1-2 年内应该看到：(1) 纯 scaling 的边际收益递减加速；(2) 方法论创新（而非规模）驱动的突破增多。

- **Eval vs 经济影响的鸿沟是否会收窄**：追踪 AI 在标准 eval 上的分数 vs 实际 GDP 贡献的比值变化。如果持续扩大，说明 eval 体系有根本性问题。

- **SSI 的研究方向**：Ilya 不能公开讨论的 ML 想法是什么？从他在对话中反复强调的 value function、情感、通用学习算法来推断，SSI 可能在研究某种结合了进化启发式 value function 的新训练范式。

- **人类 value function 的鲁棒性 vs AI 的脆弱性**：Ilya 指出人类 value function "除了成瘾之外非常鲁棒"。这暗示 AI 的 reward hacking 问题可能需要从生物学中寻找解决方案。
