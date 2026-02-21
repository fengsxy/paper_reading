---
date: 2024-01-01
layout: default
type: analysis
series: dwarkesh
episode: 86
guest: ""
title: "LLMs will hit the data wall if they can't generalize – OpenAI cofounder John Schulman - Analysis"
source_url: "https://www.youtube.com/watch?v=V6X_tLCxsZk"
transcript_url: /transcripts/dwarkesh/86_llms_will_hit_the_data_wall_if_they_can_t_generalize_openai_cofounder_john_schul/
permalink: /transcripts/dwarkesh/86_llms_will_hit_the_data_wall_if_they_can_t_generalize_openai_cofounder_john_schul.analysis/
---

# Analysis: LLMs will hit the data wall if they can't generalize — OpenAI cofounder John Schulman

## 0. 3-5 句摘要

John Schulman 回应了"LLM 已经触及天花板"的叙事，认为不应从 GPT-4 发布后缺乏明显更强模型就推断停滞——训练新一代模型需要大量准备时间。他承认数据墙是真实挑战，但预期预训练的性质会随时间改变而非简单撞墙。最有价值的洞察是关于泛化的讨论：基础模型已经在预训练中见过了所有 FFmpeg 文档和 bash 脚本，因此即使 post-training 中没有编程示例，也能在编程领域产生合理行为。

## 1. 反共识/非显然观点

- **[00:43] 不要从时间间隔推断停滞**：GPT-4 之后没有明显更强的模型不代表触及天花板，训练和准备新一代模型本身就需要很长时间。
- **[03:24] 你甚至不需要编程数据来获得编程能力**：仅训练通用 helpfulness 偏好模型，即使不包含任何 STEM 数据，也能在编程领域产生合理行为——泛化比人们想象的更强。
- **[01:55] 在 GPT-4 规模上做消融实验几乎不可能**：关于代码训练是否提升推理能力的问题，Schulman 坦承无法在 GPT-4 规模做科学实验，只能在 GPT-2/3 规模做近似测试。

## 2. 关键洞察

- 数据墙不是悬崖而是斜坡——预训练的方法会逐渐演变以适应数据限制
- 基础模型的预训练知识远比人们意识到的更丰富，post-training 更多是"激活"而非"教授"
- 不同模态和领域之间存在大量正向迁移，但在当前规模下难以做严格的科学验证
- 标注员不需要每个领域的专家——泛化能力填补了特定领域数据的缺口

## 3. Takeaway

- 在评估 AI 进展时，区分"没有发布"和"没有进步"至关重要。训练周期的长度本身就是一个重要但常被忽略的变量。
