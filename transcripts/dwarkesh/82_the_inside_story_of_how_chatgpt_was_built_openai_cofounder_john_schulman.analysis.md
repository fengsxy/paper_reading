---
date: 2024-01-01
layout: default
type: analysis
series: dwarkesh
episode: 82
guest: ""
title: "The inside story of how ChatGPT was built – OpenAI cofounder John Schulman - Analysis"
source_url: "https://www.youtube.com/watch?v=ERpNuLzKmJY"
transcript_url: /transcripts/dwarkesh/82_the_inside_story_of_how_chatgpt_was_built_openai_cofounder_john_schulman/
permalink: /transcripts/dwarkesh/82_the_inside_story_of_how_chatgpt_was_built_openai_cofounder_john_schulman.analysis/
---

# Analysis: The inside story of how ChatGPT was built – OpenAI cofounder John Schulman

## 0. 3-5 句摘要

John Schulman 揭示了 ChatGPT 诞生的内部故事：它并非一个精心策划的产品发布，而是在 GPT-4 完成训练后被"遗忘"的一个副项目。ChatGPT 基于 GPT-3.5 构建，关键创新不是模型本身，而是"对话"这个交互范式——它让人类标注员和模型都更容易理解"好的输出"应该是什么样子。Schulman 透露，仅约30个示例就足以教会模型理解自身能力边界（如不能发邮件），这展示了惊人的泛化能力。ChatGPT 的成功本质上是一个 UX 创新而非模型创新。

## 1. 反共识/非显然观点

- **[00:00] ChatGPT 差点被 GPT-4 的光芒掩盖**：GPT-4 在2022年8月完成训练后，团队的注意力转向了 GPT-4 的指令微调，ChatGPT 项目一度被搁置。最终它被推出更多是因为"已经做了，不如发布看看"。
- **[04:50] "对话"范式的真正价值是降低了标注难度**：指令跟随模型的任务定义模糊（"以有帮助的方式补全文本"），而对话范式让标注员直觉地理解"一个有帮助的机器人应该怎样"——这不是技术突破，而是人机交互设计的突破。
- **[05:35] 任何人都可以用公开 API 做出类似产品**：Schulman 承认如果 GPT-3.5 的微调 API 当时可用，外部开发者通过迭代式监督微调也能做出"相当接近"的产品——ChatGPT 的护城河不在于技术独占。
- **[15:27] 30个示例就能教会模型理解自身局限**：早期 ChatGPT 会假装能发邮件或叫 Uber，仅用约30个示例就修复了这个问题，且泛化到了所有未训练过的能力边界——这暗示模型内部已有某种"自我认知"的潜在能力。

## 2. 关键洞察

- ChatGPT 的成功是"对的产品形态+对的时机"的结果，而非技术突破——GPT-3.5 的能力已经足够，缺的是让用户和模型都能理解的交互范式
- 迭代式微调（让人类编辑模型输出而非从头写）比纯人类数据训练更有效，因为模型可能无法完美拟合人类写作风格，但可以学会改进自己的输出
- 跨语言泛化是 post-training 最令人惊讶的特性之一：仅用英语数据训练，模型自动在西班牙语等其他语言上表现良好

## 3. Takeaway

- 产品创新有时比技术创新更重要：ChatGPT 的核心贡献不是更强的模型，而是找到了让人类直觉理解 AI 能力的交互方式
- 极少量的高质量示例可以触发惊人的泛化——这暗示大模型内部已经"知道"很多东西，post-training 更像是"激活"而非"教授"
