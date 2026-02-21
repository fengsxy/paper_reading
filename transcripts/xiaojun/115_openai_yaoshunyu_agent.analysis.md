---
layout: default
type: analysis
series: xiaojun
episode: 115
date: 2026-02-20
guest: 姚顺雨
org: OpenAI
title: "EP115 姚顺雨（OpenAI）- 分析"
source_url: https://www.youtube.com/watch?v=gQgKkUsx5q0
permalink: /transcripts/xiaojun/115_openai_yaoshunyu_agent.analysis/
---

# 访谈分析笔记

## 摘要
1. 姚顺雨是OpenAI研究员，清华姚班→普林斯顿PhD，研究Agent已6年，代表作包括ReAct、WebShop、Tree of Thought等。
2. 他提出AI主线程已进入"下半场"（The Second Half）：方法论已统一（类似牛顿力学时刻），瓶颈从"怎么做"转向"做什么"——即任务定义和环境设计。
3. 语言是人类为实现泛化而发明的工具，比其他模态更本质；语言Agent的核心优势是推理能力带来的泛化。
4. 创业公司的机会在于创造不同于ChatGPT的交互方式（如Cursor），而非复制助手形态；Super App会形成路径依赖，给差异化留出空间。
5. 下一步关键研究方向：Long-term Memory、Intrinsic Reward（内生奖励）、Multi-Agent协作。

## 反共识/非显然观点
1. 做客服比做软件工程更难——对AI而言，coding有清晰reward和环境，客服需要极高reliability，这颠覆了人类社会的难度排序。
2. OpenAI内部在GPT-1时期也没有形成共识，GPT-1第二作者（姚顺雨导师）当时对scaling持怀疑态度；伊利亚的核心贡献不是具体技术而是"all in"的决策。
3. 创业公司应该担心的是模型没有溢出能力（而非溢出太多），因为溢出=机会。
4. 大多数AI公司还没有形成数据飞轮，主要靠模型变好的溢出能力；MidJourney是少数成功案例（清晰的人类偏好reward）。
5. 技术发展同时加剧中心化和去中心化：贫富差距拉大，但阶级跨越的可能性也在增加，网络多样性也在增长。
6. 评估Agent不应只看pass@1或pass@100，还需要"pass@k̄"（k次全部成功的概率），即reliability维度被严重忽视。
7. 开源AI做好是非常non-trivial的事，DeepSeek的成功有"小概率慈善家"的因素。
8. Agent的"最强"没有统一定义——不同交互方式下有不同的智能边界，不是单一模型决定的。

## 可学习的点
1. **Method-Task Fit**：做研究最难的不是方法，而是找到能证明方法价值的任务——类似创业的Product-Market Fit。
2. **Reward设计原则**：基于结果而非过程、基于规则而非人/模型偏好，这是RL成功的关键（math/coding的reward就是答案对不对）。
3. **交叉学科视角**：ReAct之所以能做出来，是因为打通了NLP和RL的边界；只待在单一社区很难做出通用性工作。
4. **从人身上借鉴的正确方式**：观察"人能做什么机器不能"（客观事实），但解决方案不必照抄人脑机制，可以从第一性原理设计。
5. **Context是当前AI创造经济价值的真正瓶颈**：模型推理已经很强，但缺少人脑中那些"写不下来"的隐性context。
6. **Memory作为商业壁壘**：如果ChatGPT有了强大的长期记忆，用户粘性会质变——这可能是研究优势转化为商业优势的关键路径。
7. **环境即最外层Memory**：冯诺伊曼的洞见——外部世界永远是memory hierarchy的最外层，MCP本质上也是在hack用户的context。

## 提问技巧
1. **反直觉追问**："你说你是很乖的学生，但我从你文章里读到反叛精神"——用矛盾制造张力，引出真实自我。
2. **具体化抽象概念**："你说泛化了，有什么跡象让你感觉是真的泛化而不是training data里已有的？"
3. **角色扮演提问**："如果你是Cursor的CEO/微信的老板/伯克希尔CEO，你会怎么做？"——迫使受访者跳出研究者视角。
4. **快问快答收尾**：食物、地点、必读书、关键bet——轻松节奏中暴露个人偏好和价值观。
5. **双主持人配合**：广秘从技术角度追问（context vs reasoning），张小珺从商业/人文角度切入，形成立体访谈。

## 可进一步验证/挖坑
1. **Long-term Memory的技术路线**：姚顺雨暗示OpenAI在做相关工作但不能分享细节——值得持续追踪。
2. **"不同交互方式需要不同pre-training"**：这意味着未来可能出现专门为非chatbot形态训练的基础模型。
3. **Intrinsic Reward的实现**：从物理世界的好奇心到文字世界的内在激励，这个跨越的具体方案尚不明确。
4. **"我在做something"**：姚顺雨暗示可能在准备创业或新项目，值得关注后续动态。
5. **pass@k̄ metric**：TopBench论文提出的reliability评估框架，可能改变Agent评估的范式。
6. **Super App之外的交互方式**：Canvas/Artifacts方向被提及但承认"很难"，具体形态仍在探索中。
