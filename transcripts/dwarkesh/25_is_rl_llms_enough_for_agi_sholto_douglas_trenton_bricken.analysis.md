---
layout: default
type: analysis
series: dwarkesh
episode: 25
guest: ""
title: "Is RL + LLMs enough for AGI? — Sholto Douglas & Trenton Bricken - Analysis"
source_url: "https://www.youtube.com/watch?v=64lXQP6cs5M"
transcript_url: /transcripts/dwarkesh/25_is_rl_llms_enough_for_agi_sholto_douglas_trenton_bricken/
permalink: /transcripts/dwarkesh/25_is_rl_llms_enough_for_agi_sholto_douglas_trenton_bricken.analysis/
---

# Analysis: Is RL + LLMs enough for AGI? — Sholto Douglas & Trenton Bricken

## 0. 3-5 句摘要

Anthropic 研究员 Sholto Douglas 和 Trenton Bricken 与 Dwarkesh 深入讨论了 RL + LLM 是否足以实现 AGI。Sholto 认为当前 LLM 已具备足够的概念理解基础，只要能构建正确的反馈循环（feedback loop），几乎所有领域都会被攻克——计算机使用、白领工作自动化在 2-5 年内几乎是"过度确定"的。Trenton 从机械可解释性（mechanistic interpretability）角度展示了模型内部已有真正的概念推理能力（如 I-don't-know 电路、代码漏洞特征），并强调 interp 对 AI 安全的关键作用。两人还深入分析了 DeepSeek 的研究品味、推理计算瓶颈、以及一个令人不安的"人类肉体机器人"过渡期场景。

## 1. 反共识/非显然观点

- **RL 的"反馈循环"才是关键瓶颈，而非模型能力本身**：Sholto 认为计算机使用之所以落后于编程，不是因为模型不够聪明，而是因为更难构建有效的 RL 反馈循环。一旦反馈循环到位，领域就会被攻克。
- **AI 实验室远非完美机器**：内部资源分配极度紧张，研究员倾向于优先攻克自己认为"聪明"的任务（数学、竞赛编程），而非经济价值最高的任务（报税、计算机使用）。这解释了能力发展的不均匀性。
- **Moravec 悖论是"假的"**：机器人之所以落后，主要是因为缺乏等价于 GitHub 的物理世界训练数据，而非物理操作本身更难。如果有全人类日常动作的 MoCap 数据，机器人进展会与软件工程同步。
- **"人类肉体机器人"过渡期**：在 AI 能做所有白领工作但机器人尚未成熟的窗口期（约十年），人类最大的比较优势可能是作为 AI 指挥下的物理执行者——戴着 AirPods 和 AR 眼镜按指令搬东西。
- **即使算法进步完全停滞，当前技术也足以自动化白领工作**：只要有足够的正确数据和 RL 环境，现有算法套件就够用，因为经济激励太大了。
- **推理计算将成为 2027-28 年的主要瓶颈**：即使有 1 亿个 H100 等效算力，按每个 H100 ≈ 100 个人类思考速度计算，也只相当于 100 亿"人类等效"——远不够实现全面自动化。

## 2. 可学习的点（可迁移的方法论）

- **"产品指数"思维**：Sholto 提出产品设计需要领先模型能力几个月——Cursor 在 Claude 3.5 Sonnet 时 hit PMF，Windsurf 更激进地押注 agentic 工作流。下一波是完全异步的、不在 IDE 中的代码生成。启示：做产品要预判能力曲线，而非适配当前能力。
- **DeepSeek 的研究品味分析法**：Sholto 通过"对比 base transformer 和 DeepSeek v2/v3 的 diff"来理解其设计哲学——每个架构选择都能追溯到具体的硬件约束（H800 的 flops vs 内存带宽、出口管制后的算力变化）。这是一种"约束驱动的逆向工程"方法论。
- **Generator-Verifier Gap 的实际应用**：未来瓶颈不是"AI 能否完成任务"，而是"人类能否高效验证 100 个 agent 的输出"。启示：投资于自动化评估和摘要系统比投资于更强的生成能力更有杠杆。
- **对待 AI 应像对待新员工**：人们对 AI 失败的容忍度远低于对新员工的容忍度（几分钟 vs 几周），这导致严重的能力低估。异步工作形态会大幅改善这一问题。

## 3. 提问技巧（采访方法）

- **具体化预测追问**：Dwarkesh 不满足于"计算机使用会变好"这种模糊预测，而是追问"明年五月能否在 Photoshop 中连续添加三个特效？""能否可靠地报税？"——迫使嘉宾给出可验证的具体时间线。
- **引入第三方观点制造张力**：引用 Eray 和 Tom 的悲观论点（"我们离解决长上下文、连贯 agency 还很远"）来挑战 Sholto 的乐观立场，制造有建设性的辩论。
- **"逃生舱"技巧**：在嘉宾给出强预测后，主动帮他们设置"如果错了怎么解释"的条件（"如果明年还没有 robust 的计算机使用 agent，是不是就是 bust timeline？"），这既增加了预测的信息量，也让嘉宾更愿意给出大胆判断。
- **类比挑战法**：用 AlphaGo/AlphaZero 的历史类比（"当时也觉得是 baby AGI，结果不是"）来挑战 LLM 的 AGI 潜力，迫使嘉宾解释"这次为什么不同"。

## 4. 可进一步验证/挖坑

- **Sholto 的具体预测可追踪**：2025 年 5 月 Photoshop 三步操作、2026 年底可靠报税、"一年内个人行政事务逃逸速度"——这些都是可在时间到达后验证的硬预测。
- **"10 bits/s 人类思考速度"论文**：Sholto 引用了一篇关于人类信息处理速度仅 10 bits/s 的论文，用于计算 H100 vs 人类的等效比。值得找到原文验证其方法论和适用范围。
- **DeepSeek 的 multi-token prediction**：Meta 发表了论文但没在 Llama 中使用，DeepSeek 却采用了——这个差异的原因值得深挖（是 Meta 发现大规模无效，还是 DeepSeek 迭代更快？）。
- **Emergent Misalignment 现象**：在代码漏洞数据上微调 ChatGPT 导致模型"变成纳粹"——这个结果的可复现性和机制值得关注，尤其是 interp 工具能否事前检测这类 persona 漂移。
- **RL scaling laws for board games (Andy Jones)**：Sholto 推荐的研究方向，可作为理解 RL 效率的入口。
- **国家级 AI 准备度**：Sholto 建议各国建立"白领工作自动化 benchmark"（类似 SWE-bench 但覆盖所有职业），这个政策建议是否有国家在执行？

