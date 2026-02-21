---
date: 2024-01-01
layout: default
type: analysis
series: dwarkesh
episode: 138
guest: "Ilya Sutskever"
title: "Ilya Sutskever (OpenAI Chief Scientist) — Why next-token prediction could surpass human intelligence - Analysis"
source_url: "https://www.youtube.com/watch?v=Yf1o0TQzry8"
transcript_url: /transcripts/dwarkesh/138_ilya_sutskever_openai_chief_scientist_why_next_token_prediction_could_surpass_hu/
permalink: /transcripts/dwarkesh/138_ilya_sutskever_openai_chief_scientist_why_next_token_prediction_could_surpass_hu.analysis/
---

# Analysis: Ilya Sutskever (OpenAI Chief Scientist) — Why next-token prediction could surpass human intelligence

## 一句话

Ilya Sutskever 在这期对话中展示了一种罕见的思维方式：他不是在预测未来，而是在解释为什么 next-token prediction 的本质远比表面看起来深刻——预测下一个 token 意味着理解产生这些 token 的底层现实，这个洞察是理解当前 AI 范式天花板（或者说没有天花板）的关键。

## 关键洞察

- **[06:37] Next-token prediction 可以超越人类表现**：Ilya 直接挑战了"模仿只能达到人类水平"的直觉。他的论证是：如果 base model 足够聪明，你可以问它"一个拥有超凡洞察力的人会怎么做"——这个人不需要真实存在，neural net 可以 extrapolate 出这样一个人的行为。这不是简单的模仿，而是对人类行为底层模式的深度理解后的外推。

- **[07:45] 预测 token 的本质是理解现实**：这是整期最深刻的一个点。Ilya 说"predicting the next token well means that you understand the underlying reality that led to the creation of that token"。表面上是统计，但要真正压缩这些统计信息，你必须理解是什么样的世界产生了这些数据。这个框架把 language modeling 从"pattern matching"提升到了"world modeling"。

- **[05:05] Reliability 是唯一可能让 AI 令人失望的因素**：被问到如果 2030 年 AI 经济价值不大的最佳解释是什么，Ilya 几乎排除了所有可能性，只留下一个：reliability。模型技术上成熟但不够可靠，用户仍需反复检查输出，这会严重限制经济价值。这个判断到今天依然精准。

- **[17:34] Alignment 的终极方案：用小模型监督大模型**：Ilya 描述了一个愿景——用一个小的、被充分理解的 neural net 来研究和验证一个大的、不被理解的 neural net 的行为。这比单纯的 RLHF 更根本，指向了 alignment 研究的一个核心方向：可解释性 + 自动化验证。

- **[10:41] 模型不是推理差，是不被允许"出声思考"**：Ilya 指出当时模型在 multi-step reasoning 上的弱点不是能力问题，而是格式问题——它们被迫在内部完成推理而不能 think out loud。这个观察直接预言了后来 chain-of-thought prompting 和 reasoning models 的成功。

## Takeaway

- **评估 AI 能力时，区分"能力缺失"和"表达方式受限"**：很多时候模型看起来做不到某件事，可能只是没有被给予正确的输出格式或足够的推理空间。在设计 prompt 和 workflow 时，给模型"出声思考"的空间（chain-of-thought）可以显著提升表现。

- **Reliability 是 AI 产品化的核心瓶颈**：如果你在构建 AI 产品，与其追求更强的能力，不如优先解决可靠性——让用户不需要反复检查输出，这才是真正释放经济价值的关键。

## 延伸

- **人物**：Geoffrey Hinton（Ilya 的导师，提出 Forward-Forward Algorithm）、Dwarkesh Patel（主持人，擅长追问 AI 研究者的深层思考）
- **概念**：Scaling Laws（Kaplan et al., 2020）、RLHF（Reinforcement Learning from Human Feedback）、Emergent Properties in LLMs
- **论文**：「Language Models are Few-Shot Learners」(GPT-3, Brown et al., 2020)、「Training language models to follow instructions with human feedback」(InstructGPT, Ouyang et al., 2022)
- **话题**：AI alignment 的多层防御策略、next-token prediction 作为 world model 的哲学含义、AI 对人类意义感的影响（Ilya 提到 AGI 可以成为最好的冥想老师）、台湾半导体供应链风险对 AI 发展的影响
