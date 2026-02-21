---
layout: default
type: analysis
series: dwarkesh
episode: 84
guest: ""
title: "John Schulman (OpenAI Cofounder) — Reasoning, RLHF, & plan for 2027 AGI - Analysis"
source_url: "https://www.youtube.com/watch?v=Wo95ob_s_NI"
transcript_url: /transcripts/dwarkesh/84_john_schulman_openai_cofounder_reasoning_rlhf_plan_for_2027_agi/
permalink: /transcripts/dwarkesh/84_john_schulman_openai_cofounder_reasoning_rlhf_plan_for_2027_agi.analysis/
---

# Analysis: John Schulman (OpenAI Cofounder) — Reasoning, RLHF, & plan for 2027 AGI

## 0. 3-5 句摘要

John Schulman 坦诚地讨论了 AGI 时间线和安全策略。他认为长时间跨度 RL（long-horizon RL）是下一个关键能力解锁——让模型在数小时甚至数天的任务中保持连贯。最惊人的表态是：如果 AGI 比预期更早到来，OpenAI 会放慢脚步甚至暂停。他对"AGI 之后怎么办"坦率回答"我没有好的答案"。对话还揭示了 post-training 中惊人的泛化现象：30个示例就能修复整类行为问题。

## 1. 反共识/非显然观点

- **[17:33] 如果 AGI 比预期更早到来会放慢**：Schulman 明确表示会暂停进一步训练和大规模部署，与"竞赛到底"叙事形成对比。但他承认博弈论使多方协调极其困难。
- **[09:29] 长时间跨度 RL 可能是 AGI 的关键解锁**：当前模型核心缺陷不是知识不足而是无法在长任务中保持连贯。一旦成功，模型可能迅速接近人类同事水平。
- **[15:27] 30个示例修复整类行为**：早期 ChatGPT 会假装能发邮件叫 Uber，仅约30个示例就修复了所有类似问题——模型内部已有正确表征，只需极少数据激活。

## 2. 关键洞察

- Post-training 泛化惊人：英语微调→西班牙语改善；文本微调→多模态改善
- "品味"和"处理模糊性"可能是 AGI 前最后瓶颈
- 渐进式部署比不连续跳跃安全得多——Schulman 明确偏好这种路径
- 防御纵深：模型对齐 + 外部监控 + 模拟测试三层防线

## 3. Takeaway

- 连 OpenAI 联合创始人都无法明确说出"AGI 之后还缺什么"，这意味着准备工作应该现在就开始。
