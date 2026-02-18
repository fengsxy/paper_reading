# Scholar Inbox 精选 - 2026-02-17

## Diffusion / dLLM 相关论文（已验证）

---

### 1. Continuous Diffusion Models Can Obey Formal Syntax
**ArXiv:** [2602.12468](https://arxiv.org/abs/2602.12468) ✅

**摘要：** 扩散语言模型在结构化输出（比如正则/JSON schema）上的一个关键痛点是“采样容易跑出语法”。这篇工作给出一种无需训练的引导式采样：构造一个可微的“满足正则约束的概率估计”，用其梯度在采样时把输出推回合法区域，从而显著提高约束满足率。

**亮点：** 把“形式语法约束”变成一个能直接用于采样引导的信号，适合迁移到各种结构化生成场景。

---

### 2. dVoting: Fast Voting for dLLMs
**ArXiv:** [2602.12153](https://arxiv.org/abs/2602.12153) ✅
**Code:** https://github.com/fscdc/dVoting

**摘要：** 利用 dLLM 的“任意位置生成”特性做 test-time scaling：先生成候选，再做一致性分析定位不确定 token，局部重生成并迭代投票优化。作者报告在 GSM8K/MATH500/ARC-C 等任务上都有可观提升。

**亮点：** 给 dLLM 提供一种很自然的推理增强范式：并行生成 + 局部修补，而不是像自回归那样只能线性扩展。

---

### 3. Can I Have Your Order? Monte-Carlo Tree Search for Slot Filling Ordering in Diffusion Language Models
**ArXiv:** [2602.12586](https://arxiv.org/abs/2602.12586) ✅

**摘要：** 针对 dLLM 的“slot filling/任意位置补全”带来的一个自由度：先填哪些位置、后填哪些位置。作者用 MCTS 在推理时搜索填充顺序，目标是提升最终输出质量。

**亮点：** 把“生成顺序”从固定策略变成可搜索的决策变量，本质是在 dLLM 上做一种结构化的 test-time planning。

---

### 4. T3D: Few-Step Diffusion Language Models via Trajectory Self-Distillation with Direct Discriminative Optimization
**ArXiv:** [2602.12262](https://arxiv.org/abs/2602.12262) ✅

**摘要：** 目标是让 dLLM 用更少步数达到更好的生成质量。方法上强调“轨迹蒸馏（trajectory self-distillation）”与直接判别优化，把多步采样的有效轨迹压缩成更短的推理路径。

**亮点：** 若成立，能显著改善 dLLM 的推理成本与延迟，是 dLLM 工程落地必须解决的问题之一。

---

### 5. DiffuRank: Effective Document Reranking with Diffusion Language Models
**ArXiv:** [2602.12528](https://arxiv.org/abs/2602.12528) ✅

**摘要：** 把扩散语言模型用于 reranking：通过扩散式生成/评分机制对候选文档重排序，以提高检索质量。

**亮点：** 给 dLLM 找到一个“排序/评估型”任务入口，可能比纯生成更容易形成稳健优势。

---

### 6. Formalizing the Sampling Design Space of Diffusion-Based Generative Models via Adaptive Solvers and Wasserstein-Bounded Objectives
**ArXiv:** [2602.12624](https://arxiv.org/abs/2602.12624) ✅

**摘要：** 从更理论/算法的角度把扩散采样中的 solver 设计空间做形式化，讨论自适应 solver 与带 Wasserstein 上界的目标如何影响采样质量与效率。

**亮点：** 这类工作往往会“慢热”，但可能给后续的采样加速、误差界、以及工程上稳定的 solver 选择提供统一框架。

