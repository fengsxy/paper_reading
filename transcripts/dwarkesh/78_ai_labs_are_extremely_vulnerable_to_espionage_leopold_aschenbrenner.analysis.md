---
date: 2024-01-01
layout: default
type: analysis
series: dwarkesh
episode: 78
guest: "Leopold Aschenbrenner"
title: "AI Labs are extremely vulnerable to espionage – Leopold Aschenbrenner - Analysis"
source_url: "https://www.youtube.com/watch?v=667IffkMDmU"
transcript_url: /transcripts/dwarkesh/78_ai_labs_are_extremely_vulnerable_to_espionage_leopold_aschenbrenner/
permalink: /transcripts/dwarkesh/78_ai_labs_are_extremely_vulnerable_to_espionage_leopold_aschenbrenner.analysis/
---

# Analysis: AI Labs are extremely vulnerable to espionage – Leopold Aschenbrenner

## 0. 3-5 句摘要

Leopold 在这个片段中详细论证了 AI 实验室的安全水平与其保护的资产价值之间的巨大落差。核心论点是：当前 AI 实验室的安全等级是"startup 级别"——DeepMind 自己承认在其安全框架中处于"Level 0"（最低级），而 Google 员工只需把代码复制到 Apple Notes 导出为 PDF 就能绕过监控。Leopold 区分了两种威胁：权重窃取（直接复制"核弹"）和算法秘密窃取（每年 0.5 OOM 的算法进步意味着保护秘密等于保护 10-100x 的算力优势）。他引用苏联 GRU 间谍学院的毕业考试——必须在莫斯科招募一名苏联科学家泄密（被招募者面临死刑）——来说明国家级间谍活动的强度远超硅谷的想象。

## 1. 反共识/非显然观点

- **"算法秘密比算力更重要"** [04:16]：大多数人关注 GPU 竞赛，但 Leopold 认为每年 0.5 OOM 的算法进步意味着几年的秘密保护等于 10-100x 的算力优势。保护秘密比建更多集群更有战略价值。

- **"DeepMind 自评安全等级为零"** [02:30]：这不是 Leopold 的攻击，而是 DeepMind 自己在 Frontier Safety Framework 中的自我评估。全球最有价值的 AI 研究机构承认自己对国家级攻击毫无防御能力。

- **"聪明人系统性地低估间谍活动"** [00:00]：Leopold 认为这是一个认知偏差——技术人员倾向于认为"如果我不会做间谍，别人也不会"，但国家级间谍机构有完全不同的能力和意愿水平。

## 2. 可学习的点（可迁移的方法论）

- **"威胁模型分层"** [03:17]：Leopold 区分了权重窃取（直接复制终端产品）和秘密窃取（获取训练方法），两者的防御策略完全不同。权重窃取需要物理安全和网络隔离，秘密窃取需要人员安全和信息分隔。

- **"安全投资需要提前期"** [03:56]：如果 AGI 在 2027 年到来，安全基础设施需要现在就开始建设——"不是做一些访问控制就行"，而是需要多年的系统性投入。

## 3. 提问技巧（采访方法）

- **用具体场景测试抽象威胁** [03:08]：Dwarkesh 问"是不是只要拿对 U 盘插到三峡大坝旁边的数据中心就行？"——这种把抽象威胁具象化的技巧让听众立刻理解问题的严重性。

## 4. 可进一步验证/挖坑

- **AI 实验室安全的实际改善**：Leopold 在 2024 年中说实验室安全是 Level 0。截至 2026 年，是否有实验室达到了 Level 2 或更高？

- **已知的 AI 间谍案件**：Leopold 提到了 Google 员工窃取代码去中国的案件。此后是否有更多类似案件被公开？这些案件的规模和频率是评估威胁的关键数据。
