---
title: "2026-02-24-diffusion-dllm"
---

# Scholar Inbox 精选 - 2026-02-24

## ⚠️ Scholar Inbox 认证过期

Scholar Inbox CLI 返回 302 (redirected to logout)，session 已失效。以下论文通过 arxiv + YDC 手动检索，覆盖 2026 年 2 月最新 diffusion/dLLM 相关论文。

---

## Diffusion / dLLM 相关论文

### 1. Adaptation to Intrinsic Dependence in Diffusion Language Models ⭐ NEW
**Authors:** (多位作者)
**ArXiv:** [2602.20126](https://arxiv.org/abs/2602.20126)
**Submitted:** 2026-02-23

**摘要：** DLM 理论分析的重要进展。研究 DLM 如何自适应数据的内在依赖结构，显著改进了此前的收敛理论，并为低复杂度分布推导出实质性的采样加速。揭示了 DLM 对内在数据结构的自适应性，为理解 dLLM 的采样效率提供了理论基础。

**亮点：** 昨天（2/23）刚发布的最新论文。理论贡献扎实，对理解 dLLM 为什么在某些分布上采样更快有直接指导意义。与 Scaling Beyond Masked Diffusion 的实验发现形成理论-实验互补。

---

### 2. Prompt Optimization Via Diffusion Language Models
**Authors:** Shiyu Wang et al.
**ArXiv:** [2602.18449](https://arxiv.org/abs/2602.18449)
**Submitted:** 2026-01-30

**摘要：** 提出基于 DLM 的 prompt 优化框架，利用 masked denoising 迭代优化 system prompt。通过 conditioning on interaction traces（用户查询、模型响应、反馈信号），DLM 在 prompt 空间中进行去噪搜索。将 prompt engineering 从手工调优转变为可微分的扩散优化过程。

**亮点：** dLLM 的新颖应用方向——不是用 dLLM 做生成，而是用 dLLM 的去噪能力做 prompt 搜索。思路新颖，对 dLLM 的应用范式有启发。

---

### 3. DLLM Agent: See Farther, Run Faster
**Authors:** Huiling Zhen, Weizhe Lin et al.
**ArXiv:** [2602.07451](https://arxiv.org/abs/2602.07451)
**Submitted:** 2026-02-07

**摘要：** 首个系统研究 dLLM 在 agentic multi-step decision making 中表现的工作。核心问题：dLLM 的并行解码和双向上下文能否在 agent 场景中带来优势？实验表明 dLLM agent 在需要全局规划的任务上表现出独特优势——"看得更远，跑得更快"。

**亮点：** dLLM + Agent 是一个被严重低估的方向。双向注意力天然适合需要全局信息的规划任务，这篇论文提供了首批实证。

---

### 4. DLLM-Searcher: Adapting Diffusion Large Language Model for Search Agents
**Authors:** Jiahao Zhao et al.
**ArXiv:** [2602.07035](https://arxiv.org/abs/2602.07035)
**Submitted:** 2026-02-03

**摘要：** 将 dLLM 适配为搜索 Agent。提出 P-ReAct 框架，利用 dLLM 的并行解码在等待工具响应时同步"思考"，实现约 15% 的推理加速且几乎无性能损失。实验证明 DLLM-Searcher 性能可比主流 LLM-based search agents。

**亮点：** 与 DLLM Agent 互补，聚焦搜索场景。P-ReAct 的"边等边想"策略巧妙利用了 dLLM 的并行特性，是 dLLM 在实际应用中的效率优势的好例证。

---

### 5. DAWN: Dependency-Aware Fast Inference for Diffusion LLMs
**Authors:** (多位作者)
**ArXiv:** [2602.06953](https://arxiv.org/abs/2602.06953)
**Submitted:** 2026-02-06

**摘要：** 解决 dLLM 推理中的 quality-speed tradeoff。现有方法直接并行 unmask 多个 token 会导致质量显著下降。DAWN 通过建模 token 间的依赖关系，智能决定哪些 token 可以安全并行生成、哪些需要串行处理，实现依赖感知的快速推理。

**亮点：** 推理加速是 dLLM 落地的关键瓶颈之一。DAWN 的依赖建模思路比简单的 confidence-based 方法更有原则性。

---

### 6. Diffusion-State Policy Optimization for Masked Diffusion Language Models
**Authors:** Daisuke Oba et al.
**ArXiv:** [2602.06462](https://arxiv.org/abs/2602.06462)
**Submitted:** 2026-02-06

**摘要：** 解决 dLLM RLHF 的核心难题：masked diffusion 通过多步去噪生成，仅从最终 reward 学习会导致粗糙的 credit assignment。DiSPO 提出 diffusion-state level 的策略优化，在中间去噪步骤上进行细粒度的 reward 分配。

**亮点：** dLLM 的 alignment/RLHF 是一个关键但研究不足的方向。DiSPO 的 diffusion-state credit assignment 思路对 dLLM post-training 有重要参考价值。

---

### 7. Balancing Understanding and Generation in Discrete Diffusion Models
**Authors:** Yue Liu, Yuzhong Zhao et al.
**ArXiv:** [2602.01362](https://arxiv.org/abs/2602.01362)
**Submitted:** 2026-02-01

**摘要：** 研究离散生成建模中两种范式的分歧能力：absorbing mode (M2T) 擅长理解，uniform noise (T2T) 擅长生成。提出 stationary noise kernel 统一两种模式，在理解和生成之间取得平衡。HuggingFace 评论指出该工作与 LLaDA2.1 高度相关。

**亮点：** 对 dLLM 的 noise schedule 设计有直接指导意义。理解 vs 生成的 tradeoff 是 dLLM 架构设计的核心问题之一。

---

### 8. Self-Rewarding Sequential Monte Carlo for Masked Diffusion Language Models
**Authors:** Ziwei Luo et al.
**ArXiv:** [2602.01849](https://arxiv.org/abs/2602.01849)
**Submitted:** 2026-02-02

**摘要：** 提出 self-rewarding SMC 算法，无需额外训练或 reward 模型即可改善 MDLM 的采样质量。核心观察：现有 MDLM 依赖条件独立假设进行采样，忽略了 token 间依赖。SMC 通过将并行推理能力转化为更好的采样质量，实现 inference-time scaling。

**亮点：** Training-free 的 inference-time scaling 方法，与 Scaling Beyond Masked Diffusion 中关于 sampling 策略重要性的发现一致。实用价值高。

---

### 9. Advancing Block Diffusion Language Models for Test-Time Scaling
**Authors:** Yi Lu et al.
**ArXiv:** [2602.09555](https://arxiv.org/abs/2602.09555)
**Submitted:** 2026-02-10

**摘要：** 首个系统探索 Block Diffusion LM 在 test-time scaling 设置下的工作。现有 BDLM 在 test-time scaling 方面探索有限，且面临更严重的解码质量退化。提出改进方案使 BDLM 在推理时能有效利用更多计算资源。

**亮点：** Test-time compute scaling 是当前 LLM 研究的热点（o1/o3 范式），将其引入 dLLM 是自然且重要的方向。

---

### 10. Focus-dLLM: Accelerating Long-Context Diffusion LLM Inference via Confidence-Guided Context Focusing
**Authors:** (多位作者)
**ArXiv:** [2602.02159](https://arxiv.org/abs/2602.02159)
**Submitted:** 2026-02-02

**摘要：** 解决 dLLM 长上下文推理效率问题。发现 token confidence 在相邻去噪步骤间高度相关，据此设计 past confidence-guided indicator 预测下一步 unmask 区域，配合 sink-aware dynamic token pruning 实现高效稀疏注意力。Training-free 框架，16K 上下文解码显著加速。

**亮点：** 与 Sink-Aware Pruning (2602.17664) 形成互补——Focus-dLLM 聚焦长上下文场景的动态剪枝，后者研究通用的 sink 行为差异。两者共同推进 dLLM 高效推理。

---

*今日 digest 共 10 篇论文，均为 2026 年 2 月新提交。涵盖理论分析、推理加速、Agent 应用、RLHF alignment 等多个方向。Scholar Inbox 认证仍然过期，需要重新登录后才能恢复自动抓取。*
