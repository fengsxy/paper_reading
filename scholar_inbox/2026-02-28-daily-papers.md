# 每日论文精选 - 2026-02-28

**主题:** Diffusion Language Models / Discrete Diffusion / Information Theory

---

## 1. dLLM: Simple Diffusion Language Modeling

**arXiv:** [2602.22661](https://arxiv.org/abs/2602.22661)  
**作者:** Zhanhui Zhou, Lingjie Chen, Hanghang Tong, Dawn Song  
**日期:** 2026-02-26  
**关键词:** dLLM, Framework, Unified, Open-source

尽管 diffusion language models 发展迅速，很多模型都收敛到了一组共享组件，但这些组件分散在各种 ad-hoc 代码库中，难以复现和扩展。dLLM 提供了一个统一的开源框架，标准化了 diffusion language modeling 的训练、推理和评估核心组件，同时保持足够的灵活性支持新方法和架构。

**与 Yu 研究的关联:** 做 discrete diffusion 研究的基础设施级工作，值得关注作为实验平台。

---

## 2. Test-Time Scaling with Diffusion Language Models via Reward-Guided Stitching

**arXiv:** [2602.22871](https://arxiv.org/abs/2602.22871)  
**作者:** Roy Miles, Aysim Toker, Andreea-Maria Oncescu, Songcen Xu, Jiankang Deng, Ismail Elezi  
**日期:** 2026-02-26  
**关键词:** Test-time scaling, Reasoning, Reward-guided, Stitching

提出用 diffusion LM 做 test-time scaling 的新思路：生成多条 chain-of-thought 后，不是简单选最好的或投票，而是在 step 级别做 reward-guided stitching——从不同 trace 中拼接最优片段，再用 AR solver 生成最终答案。模块化地分离了探索（diffusion）、评估和求解，在数学推理 benchmark 上效果显著，尤其在难题上收益最大。

**与 Yu 研究的关联:** Diffusion model 在 reasoning 上的新应用范式，test-time compute 方向。

---

## 3. Adaptation to Intrinsic Dependence in Diffusion Language Models

**arXiv:** [2602.20126](https://arxiv.org/abs/2602.20126)  
**作者:** Yunxiao Zhao et al.  
**日期:** 2026-02-23  
**关键词:** Unmasking schedule, Token dependence, Theory

DLM 的 unmasking schedule（决定 token 解码顺序和数量）如何影响生成质量？这篇从理论角度分析了这个问题，研究 schedule 如何适应 token 之间的内在依赖结构。填补了 DLM 理论理解的重要空白。

**与 Yu 研究的关联:** DLM 的理论分析，与 information-theoretic 方法有潜在交叉。

---

## 4. Is Your Diffusion Sampler Actually Correct?

**arXiv:** [2602.19619](https://arxiv.org/abs/2602.19619)  
**作者:** Luhan Tang et al.  
**日期:** 2026-02-23  
**关键词:** Sampler evaluation, Oracle framework, dLLM, Correctness

提出 sampler-centric oracle 评估框架：用精确的 HMM 后验替换学习到的 denoiser，隔离 sampler 本身引入的误差。关键发现：即使在 oracle denoiser 下，few-step discrete diffusion sampler 在分布层面也不是正确的，transition-level mismatch 只有当步数接近序列长度时才消失。

**与 Yu 研究的关联:** 对 discrete diffusion 采样正确性的严格分析，理论研究必读。

---

## 5. Discrete Diffusion Models Exploit Asymmetry to Solve Lookahead Planning Tasks

**arXiv:** [2602.19980](https://arxiv.org/abs/2602.19980)  
**作者:** Itamar Trainin, Shauli Ravfogel, Omri Abend, Amir Feder  
**日期:** 2026-02-23  
**关键词:** Planning, Lookahead, NAR vs AR, Sample efficiency

比较 AR 和 NAR（discrete diffusion）模型在 lookahead planning 任务上的表现。两者都能达到完美准确率，但 NAR 模型需要指数级更少的训练样本和更浅的架构，而 AR 模型常常需要特定的 curriculum 才能收敛。揭示了 diffusion 模型利用非对称性的独特机制。

**与 Yu 研究的关联:** 理解 diffusion model 相比 AR 的根本优势，对研究方向选择有启发。

---

## 6. Sharp Convergence Rates for Masked Diffusion Models

**arXiv:** [2602.22505](https://arxiv.org/abs/2602.22505)  
**作者:** Yuchen Liang et al.  
**日期:** 2026-02-26  
**关键词:** Convergence theory, Masked diffusion, Euler sampler, First-Hitting Sampler

为 masked (absorbing-rate) discrete diffusion 建立了 sharp 收敛速率。分析了 Euler method 和 First-Hitting Sampler (FHS) 两种采样器，给出了精确的理论保证。

**与 Yu 研究的关联:** Discrete diffusion 的理论基础，与 efficient sampling 的 2602.15008 互补。

---

## 7. DiSPO: Diffusion-State Policy Optimization for Masked Diffusion Language Models

**arXiv:** [2602.06462](https://arxiv.org/abs/2602.06462)  
**作者:** Daisuke Oba, Hiroki Furuta, Naoaki Okazaki  
**日期:** 2026-02-09  
**关键词:** RLHF, Credit assignment, Policy optimization, Masked diffusion

Masked diffusion LM 通过多步 denoising 生成，但只在最终输出上给 reward 会导致 credit assignment 粗糙。DiSPO 提出直接优化中间 filling 决策的 plug-in credit-assignment 层，解决了 diffusion LM 做 RLHF 的核心难题。

**与 Yu 研究的关联:** Diffusion LM + alignment/RLHF 的交叉方向，trustworthy AI 相关。

---

## 总结

本周 discrete diffusion language model 领域异常活跃。几个值得注意的趋势：
1. **框架统一化** — dLLM 框架的出现说明领域正在走向成熟
2. **理论深化** — 多篇论文从收敛速率、采样正确性、unmasking schedule 等角度建立理论基础
3. **新应用范式** — test-time scaling (stitching)、planning、RLHF 等方向的探索
4. **AR vs NAR 的根本差异** — lookahead planning 的结果暗示 diffusion model 有独特的计算优势
