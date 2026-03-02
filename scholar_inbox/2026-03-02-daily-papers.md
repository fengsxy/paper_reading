# 每日论文精选 - 2026-03-02

**主题:** Diffusion Language Models / Discrete Diffusion / Information Theory / Trustworthy AI

---

## 1. Discrete Diffusion Models Exploit Asymmetry to Solve Lookahead Planning Tasks

**arXiv:** [2602.19980](https://arxiv.org/abs/2602.19980)  
**作者:** Itamar Trainin, Shauli Ravfogel, Omri Abend, Amir Feder  
**日期:** 2026-02-23  
**关键词:** dLLM, Planning, Lookahead, NAR vs AR

研究 AR 与 NAR（discrete diffusion）模型在 lookahead planning 任务上的机制差异。关键发现：虽然两类模型都能达到完美准确率，但 NAR 模型所需训练样本指数级更少，且需要更浅的架构。AR 模型在没有特定 curriculum 调整时经常无法收敛。揭示了 discrete diffusion 在需要全局规划的任务上的结构性优势。

**与 Yu 研究的关联:** 直接关于 dLLM 的能力边界分析，对理解 diffusion vs autoregressive 的本质差异有重要意义。

---

## 2. Balancing Understanding and Generation in Discrete Diffusion Models

**arXiv:** [2602.01362](https://arxiv.org/abs/2602.01362)  
**作者:** Yue Liu et al.  
**日期:** 2026-02-01  
**关键词:** MDLM, UDLM, Understanding vs Generation, Unified

指出 discrete generative modeling 的两大范式存在能力分化：Masked Diffusion LM (MDLM) 擅长语义理解和 zero-shot 泛化，Uniform-noise Diffusion LM (UDLM) 擅长 few-step 生成质量，但两者都无法在两个维度上同时表现优异。提出统一方案平衡理解与生成。

**与 Yu 研究的关联:** MDLM vs UDLM 的系统性对比，对选择 diffusion noise schedule 有直接指导意义。

---

## 3. The Diffusion Duality, Chapter II: Ψ-Samplers and Efficient Curriculum

**arXiv:** [2602.21185](https://arxiv.org/abs/2602.21185)  
**作者:** Justin Deschenaux et al.  
**日期:** 2026-02-24  
**关键词:** Uniform-state diffusion, Ψ-Sampler, Curriculum, Self-correction

Uniform-state discrete diffusion 模型因自纠错能力在 few-step 生成和 guidance 场景中优于 AR 和 Masked diffusion。但 ancestral sampler 在步数增加时质量会饱和。本文提出 Ψ-Sampler 和高效 curriculum 策略来突破这一瓶颈。

**与 Yu 研究的关联:** 改进 discrete diffusion 采样质量的前沿工作，与采样理论直接相关。

---

## 4. Efficient Sampling with Discrete Diffusion Models: Sharp and Adaptive Guarantees

**arXiv:** [2602.15008](https://arxiv.org/abs/2602.15008)  
**作者:** Daniil Dmitriev, Zhihan Huang, Yuting Wei  
**日期:** 2026-02-16  
**关键词:** Sampling theory, τ-leaping, KL divergence, Sharp bounds

为 score-based discrete diffusion（CTMC 框架）建立了严格的采样效率理论。对 uniform 和 masking 两种 noising process 都给出了 KL 散度下的 sharp 收敛保证。Uniform discrete diffusion 的 τ-leaping 算法达到 Õ(d/ε) 迭代复杂度，消除了对词表大小 S 的线性依赖，并证明了对维度 d 的线性依赖是不可避免的下界。

**与 Yu 研究的关联:** Discrete diffusion 采样理论的重要进展，information-theoretic 风格的分析。

---

## 5. Discrete Diffusion with Sample-Efficient Estimators for Conditionals

**arXiv:** [2602.20293](https://arxiv.org/abs/2602.20293)  
**作者:** Karthik Elamvazhuthi, Abhijith Jayakumar, Andrey Y. Lokhov  
**日期:** 2026-02-23  
**关键词:** Conditional estimation, NeurISE, Round-robin dynamics

提出新的 discrete denoising diffusion 框架：不再近似 discrete score function，而是将 single-site conditional probabilities 作为参数化 reverse diffusion 的基本对象，结合 round-robin noising/denoising 动力学。使用 Neural Interaction Screening Estimator (NeurISE) 来高效估计这些条件概率。

**与 Yu 研究的关联:** 从条件概率角度重新构建 discrete diffusion，与 information-theoretic 方法有天然联系。

---

## 6. Quantifying Dimensional Independence in Speech: An Information-Theoretic Framework for Disentangled Representation Learning

**arXiv:** [2602.20592](https://arxiv.org/abs/2602.20592)  
**作者:** Bipasha Kashyap et al.  
**日期:** 2026-02-24  
**关键词:** Mutual information, Disentanglement, Speech, Information theory

提出 information-theoretic 框架量化语音特征中跨维度的统计依赖性，整合了 bounded neural MI 估计与非参数验证。不同于通过下游任务间接评估 disentanglement，本文直接测量特征维度间的互信息。

**与 Yu 研究的关联:** Information theory + representation learning 的直接交叉，MI 估计方法可借鉴。

---

## 7. Directional Concentration Uncertainty: A Representational Approach to UQ for Generative Models

**arXiv:** [2602.13264](https://arxiv.org/abs/2602.13264)  
**作者:** Souradeep Chattopadhyay et al.  
**日期:** 2026-02-04  
**关键词:** Uncertainty quantification, von Mises-Fisher, Trustworthy AI, Generative models

提出 Directional Concentration Uncertainty (DCU)，基于 von Mises-Fisher 分布测量生成模型多次输出的 embedding 几何分散度来量化不确定性。无需任务特定启发式，通过连续 embedding 空间中的集中度度量捕获不确定性。

**与 Yu 研究的关联:** Trustworthy AI + generative model 的交叉，用几何/统计方法做 UQ，与 information-theoretic 视角互补。

---

*筛选标准: 与 diffusion models、discrete diffusion / dLLM、information theory、representation learning、trustworthy AI 直接相关的 2026 年 2 月论文。*
