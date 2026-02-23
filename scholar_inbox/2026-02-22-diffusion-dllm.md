---
title: "2026-02-22-diffusion-dllm"
---

# Scholar Inbox 精选 - 2026-02-22

## ⚠️ Scholar Inbox 认证过期

Scholar Inbox CLI 返回 302 (redirected to logout)，session 已失效。以下论文通过 arxiv + YDC 手动检索，覆盖 2026 年 2 月中下旬 diffusion/dLLM 相关新论文。

---

## Diffusion / dLLM 相关论文

### 1. Scaling Beyond Masked Diffusion Language Models
**Authors:** Subham Sekhar Sahoo et al.
**ArXiv:** [2602.15014](https://arxiv.org/abs/2602.15014)
**Submitted:** 2026-02-16

**摘要：** 首个对 uniform-state 和 interpolating discrete diffusion 方法的 scaling law 研究。发现 Masked diffusion 用简单 cross-entropy 目标训练可提升约 12% FLOPs 效率。关键发现：perplexity 在同一 diffusion family 内有参考价值，但跨 family 比较时会产生误导——perplexity 更差的模型可能因采样更快而在 speed-quality Pareto frontier 上更优。将所有方法 scale 到 1.7B 参数后，uniform-state diffusion 在 GSM8K 上超过 autoregressive 和 Masked diffusion 模型，尽管 validation perplexity 更差。

**亮点：** 直接挑战了 "Masked diffusion 是 dLLM 未来" 的主流观点。对 dLLM 研究方向选择有重要指导意义——不能只看 perplexity，speed-quality tradeoff 才是关键。代码和 checkpoints 已开源。

---

### 2. Sink-Aware Pruning for Diffusion Language Models
**Authors:** Zhiqiang Shen et al.
**ArXiv:** [2602.17664](https://arxiv.org/abs/2602.17664)
**Submitted:** 2026-02-19

**摘要：** 发现 AR LLM 中的 attention sink 假设在 DLM 中不成立：DLM 的 attention-sink 位置在去噪轨迹上方差显著更高，说明 sink 是瞬态的、结构上不如 AR 模型中那么关键。提出 Sink-Aware Pruning，自动识别并剪枝不稳定的 sink（而非像 AR 模型那样保留 sink）。无需重训练，在匹配计算量下超过现有剪枝基线。

**亮点：** 揭示了 DLM 与 AR LLM 在 attention 结构上的本质差异。对 dLLM 的高效推理研究有直接价值——不能简单移植 AR 模型的优化策略。

---

### 3. The Geometry of Noise: Why Diffusion Models Don't Need Noise Conditioning
**Authors:** (未列出)
**ArXiv:** [2602.18428](https://arxiv.org/abs/2602.18428)
**Submitted:** 2026-02 (pending registration)

**摘要：** 研究 autonomous (noise-agnostic) 生成模型（如 Equilibrium Matching 和 blind diffusion）为何能在不显式 noise-level conditioning 的情况下工作。形式化了 Marginal Energy 概念，证明 autonomous 模型的生成过程是 Marginal Energy 上的 Riemannian gradient flow。通过 relative energy decomposition 证明学到的 time-invariant field 隐式包含 local conformal metric，完美抵消数据流形附近的几何奇异性。识别了 noise-prediction 参数化中的 "Jensen Gap" 问题，解释了确定性 blind 模型的灾难性失败，并证明 velocity-based 参数化天然稳定。

**亮点：** 理论深度极高。对 diffusion 模型的理论基础有重要贡献——解释了为什么某些参数化方式比其他的更稳定，对 dLLM 的训练目标设计有间接但重要的启发。

---

### 4. TDGNet: Hallucination Detection in Diffusion Language Models via Temporal Dynamic Graphs
**Authors:** Arshia Hemmat et al.
**ArXiv:** [2602.08048](https://arxiv.org/abs/2602.08048)
**Submitted:** 2026-02-08

**摘要：** 首个专门针对 D-LLM 的幻觉检测框架。核心观察：AR LLM 的幻觉检测器依赖单次推理线索，无法直接迁移到扩散生成——因为事实性证据分布在整个去噪轨迹上，可能出现、漂移或被自我纠正。TDGNet 将幻觉检测建模为在演化的 token-level attention graph 上的学习问题，通过消息传递更新 per-token memory，再用 temporal attention 聚合轨迹级证据。在 LLaDA-8B 和 Dream-7B 上 AUROC 一致优于 output-based、latent-based 和 static-graph 基线。

**亮点：** 填补了 dLLM 可信度研究的空白。temporal reasoning on attention graphs 的思路对理解 dLLM 的去噪动态很有价值。

---

### 5. Just on Time: Token-Level Early Stopping for Diffusion Language Models
**Authors:** Mykola Vysotskyi et al.
**ArXiv:** [2602.11133](https://arxiv.org/abs/2602.11133)
**Submitted:** 2026-02-11

**摘要：** 提出 training-free 的 token-level early stopping 方法，独立判断每个位置的收敛状态。利用模型预测和局部上下文的轻量信号动态决定何时冻结单个 token，实现自适应 per-token freezing。在数学推理、通用 QA 和科学理解等基准上实现 SOTA 效率提升，同时保持生成质量。

**亮点：** 与 dLLM-Cache 的思路互补——Cache 关注计算复用，early stopping 关注步数减少。两者结合可能带来更大的推理加速。

---

### 6. Embedding Inversion via Conditional Masked Diffusion Language Models
**Authors:** Han Xiao et al.
**ArXiv:** [2602.11047](https://arxiv.org/abs/2602.11047)
**Submitted:** 2026-02-11

**摘要：** 将 embedding inversion 建模为 conditional masked diffusion，通过迭代去噪并行恢复所有 token，而非顺序自回归生成。通过 adaptive layer normalization 对目标 embedding 进行条件化，仅需 8 次前向传播，推理时无需访问目标编码器。

**亮点：** dLLM 在安全/隐私领域的有趣应用——embedding inversion 是评估 embedding 模型隐私风险的重要工具。

---

*今日 digest 共 6 篇论文，均为 2026 年 2 月新提交。Scholar Inbox 认证过期，需要重新登录后才能恢复自动抓取。*
