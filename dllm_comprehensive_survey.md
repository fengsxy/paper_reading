# dLLM 全面调研 (2026-02-15)

基于 Scholar Inbox semantic search 的全面调研，覆盖 remask、soft mask、reasoning、acceleration、theory 等方向。

---

## 一、Remask / Self-Correction 方向 (~25 篇)

### 核心 Remask 论文

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2509.23653 | Don't Settle Too Early: Self-Reflective Remasking (RemeDi) | ArXiv | Remasking as fundamental mechanism, SFT+RL |
| 2602.04096 | CoRe: Context-Robust Remasking | ArXiv 2026 | Context-robust remasking 策略 |
| 2503.00307 | Remasking with Inference-Time Scaling | NeurIPS 2025 | 更多 compute → 更好 remask |
| 2602.09501 | Where-to-Unmask: Ground-Truth-Guided Unmasking Order | ArXiv 2026 | 学习最优 unmask 顺序 |
| 2512.09106 | Learning Unmasking Policies | ArXiv | 学习 unmasking policy |
| 2507.08018 | R3: Review, Remask, Refine | ArXiv | Process-guided block diffusion |

### Self-Correction 论文

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2602.11590 | Learn from Your Mistakes: Self-Correcting MDMs (ProSeCo) | ArXiv 2026 | Progressive self-correction, 2-3x faster |
| 2512.15596 | Corrective Diffusion Language Models | ArXiv | 分析为什么标准 MDLM 不能 self-correct |
| 2510.01384 | Fine-Tuning MDM for Provable Self-Correction | ArXiv | 有理论保证的 self-correction |
| 2601.06428 | Teach DLM to Learn from Their Own Mistakes | ArXiv 2026 | 教模型从错误中学习 |
| 2602.02927 | Training-Free Self-Correction for Multimodal MDMs | ArXiv 2026 | 不需要训练的 self-correction |
| 2510.19871 | From Denoising to Refining (ReDiff) | ArXiv | VLM 的 corrective framework |

### Decoding 策略

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2602.10953 | SOAR: Confidence-Switched Position Beam Search | ArXiv 2026 | Training-free, adaptive search |
| 2512.02044 | Beyond Confidence: Adaptive and Coherent Decoding | ArXiv | 不只是 confidence |
| 2512.12168 | Diffusion LM Inference with MCTS | ArXiv | Monte Carlo Tree Search |
| 2601.20339 | Joint Search in Generation Order and Token Space | ArXiv 2026 | 同时搜索顺序和 token |
| 2510.18165 | Saber: Backtracking Enhanced Remasking | ArXiv | Backtracking + adaptive acceleration |

### 相关机制分析

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2511.21338 | Masks Can Be Distracting | ArXiv | Context comprehension 问题 |
| 2510.03289 | Why Mask Diffusion Does Not Work | ArXiv | 分析 mask diffusion 的问题 |
| 2601.04205 | STDD: Spatio-Temporal Dynamics-Driven Token Refinement | ArXiv | 时空动态驱动的 refinement |

---

## 二、Soft Mask / Continuous 方向 (~20 篇)

### Soft Mask 核心论文

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2510.17206 | Soft-Masked Diffusion Language Models | ArXiv | Blend mask embedding with top-k predictions |
| 2304.04746 | A Cheaper and Better DLM with Soft-Masked Noise | EMNLP 2023 | 早期 soft mask 工作 |
| 2601.07351 | Beyond Hard Masks: EvoToken-DLM | ArXiv 2026 | Evolving soft token distributions |
| 2601.22954 | Residual Context Diffusion (RCD) | ArXiv 2026 | Residual context injection |

### Continuous / Latent Diffusion

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2212.09462 | Latent Diffusion for Language Generation | NeurIPS 2023 | Latent space diffusion for text |
| 2502.11564 | Continuous Diffusion Model for Language Modeling | NeurIPS 2025 | Continuous diffusion for discrete data |
| 2601.16220 | Towards Latent Diffusion Suitable For Text | ArXiv 2026 | 改进 latent diffusion for text |
| 2506.21170 | Compressed and Smooth Latent Space for Text Diffusion | NeurIPS 2025 | 更好的 latent space |
| 2505.18853 | Smoothie: Smoothing Diffusion on Token Embeddings | ArXiv | Embedding space smoothing |

### Embedding Space Diffusion

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2211.04236 | Self-conditioned Embedding Diffusion | ArXiv | Embedding space diffusion |
| 2212.09412 | Empowering Diffusion on Embedding Space | NAACL 2024 | Embedding space generation |
| 2402.19097 | TEncDM: Diffusion in LM Encoding Space | AAAI 2025 | 在 encoder space 做 diffusion |

### Token Evolution

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2601.04854 | Token Maturation: Continuous Token Dynamics | ArXiv 2026 | Continuous token evolution |
| 2601.21768 | Zonkey: Hierarchical DLM with Differentiable Tokenization | ArXiv 2026 | Differentiable tokenization |

---

## 三、Reasoning 方向 (~20 篇)

### Chain-of-Thought in Diffusion

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2402.07754 | Diffusion of Thought: CoT in DLMs | NeurIPS 2024 | 第一个 CoT for diffusion |
| 2505.10446 | Reinforcing Diffusion Chain of Lateral Thought | NeurIPS 2025 | DCoLT, RL 强化 |
| 2510.27469 | Diffuse Thinking: DLMs as Thought Proposers | ArXiv | DLM 作为 thought proposer |
| 2510.09544 | Beyond Surface Reasoning: True Long CoT Capacity | ArXiv | 长 CoT 能力分析 |
| 2601.22035 | Thinking Out of Order (Yu's paper) | ArXiv 2026 | Order robustness, complexity-based ordering |

### Latent Reasoning

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2507.06203 | A Survey on Latent Reasoning | ArXiv | Latent reasoning 综述 |
| 2505.16782 | Reasoning Beyond Language: Latent CoT Survey | ArXiv | Latent CoT 综述 |
| 2412.06769 | Training LLM to Reason in Continuous Latent Space | ArXiv | Continuous latent reasoning |
| 2509.26314 | Latent Thinking Optimization | ArXiv | Latent reasoning 优化 |
| 2510.25741 | Scaling Latent Reasoning via Looped LMs | ArXiv | Looped models for latent reasoning |
| 2602.08100 | Emergent Search and Backtracking in Latent Reasoning | ArXiv 2026 | Latent reasoning 中的 search |
| 2502.05171 | Scaling Test-Time Compute with Latent Reasoning | NeurIPS 2025 | Recurrent depth approach |

### RL for Reasoning

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2509.21474 | d2: Improved Techniques for Training Reasoning DLMs | ArXiv | 新 policy gradient for masked DLMs |
| 2510.08554 | Group Diffusion Policy Optimization | ArXiv | Group-based policy optimization |
| 2510.04019 | Principled and Tractable RL for Reasoning with DLMs | ArXiv | Principled RL approach |
| 2602.08905 | Efficient and Stable RL for DLMs | ArXiv 2026 | 稳定的 RL 训练 |
| 2507.08838 | wd1: Weighted Policy Optimization | ArXiv | Weighted policy optimization |

---

## 四、Acceleration 方向 (~25 篇)

### 系统级加速

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2510.08666 | dInfer: Efficient Inference Framework | ArXiv | 推理框架 |
| 2505.22618 | Fast-dLLM: KV Cache + Parallel Decoding | ArXiv | Training-free, KV cache |
| 2505.21467 | FlashDLM: KV Caching + Guided Diffusion | ArXiv | KV cache + guidance |
| 2512.17077 | Taming Memory Footprint Crisis | ArXiv | 内存优化 |
| 2508.02193 | Seed Diffusion: High-Speed Inference | ArXiv | 大规模高速推理 |

### Parallel Decoding

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2601.15593 | Parallelism and Generation Order: Limits and Potential | ArXiv 2026 | 分析并行的极限 |
| 2601.12247 | Plan, Verify and Fill: Structured Parallel Decoding | ArXiv 2026 | 结构化并行 |
| 2602.06953 | DAWN: Dependency-Aware Fast Inference | ArXiv 2026 | 依赖感知推理 |
| 2509.25188 | Learning to Parallel: Learnable Parallel Decoding | ArXiv | 学习并行策略 |
| 2510.07081 | Local Determinism Propagation | ArXiv | 局部确定性传播 |

### Consistency / Distillation

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2511.19269 | CDLM: Consistency Diffusion LMs | ArXiv | Consistency model for DLM |
| 2408.05636 | Speculative Diffusion Decoding | NAACL 2025 | Speculative decoding |
| 2508.09192 | Faster-Than-AR via Discrete Diffusion Forcing | ArXiv | Diffusion forcing |

### 其他加速方法

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2602.06412 | Stopping Computation for Converged Tokens | ArXiv 2026 | Early stopping |
| 2601.17917 | Streaming-dLLM: Suffix Pruning + Dynamic Decoding | ArXiv 2026 | Streaming 生成 |
| 2602.02159 | Focus-dLLM: Confidence-Guided Context Focusing | ArXiv 2026 | Long context 加速 |
| 2506.10848 | SlowFast Sampling: Three Golden Principles | ArXiv | SlowFast 采样 |
| 2602.08404 | TEAM: Expert Activation for MoE DLM | ArXiv 2026 | MoE 加速 |

---

## 五、Theory / Analysis 方向 (~15 篇)

### 理论分析

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2505.21400 | Convergence Theory: Information-Theoretic Perspective | ArXiv | 信息论视角的收敛理论 |
| 2502.09622 | Theoretical Benefit and Limitation of DLM | NeurIPS 2025 | 理论优势和局限 |
| N/A | Breaking AR's Sampling Bottleneck: Provable Acceleration | NeurIPS 2025 | 可证明的加速 |
| 2601.22450 | Tuning Implicit Regularizer via k-Parity | ArXiv 2026 | 隐式正则化 |

### Information Theory

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2310.09031 | MINDE: MI Neural Diffusion Estimation | ICLR 2024 | MI 估计 |
| 2310.07972 | Interpretable Diffusion via Information Decomposition | ICLR 2024 | 信息分解 |
| 2302.03792 | Information-Theoretic Diffusion | ICLR 2023 | 信息论 diffusion |
| 2509.20609 | MMG: MI Estimation via MMSE Gap | ArXiv | MMSE gap 估计 MI |

### Survey

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2508.10875 | A Survey on Diffusion Language Models | ArXiv | 最新综述 |
| 2506.13759 | Discrete Diffusion in LLMs and MLLMs: A Survey | ArXiv | Discrete diffusion 综述 |
| 2601.14041 | Top 10 Open Challenges | ArXiv 2026 | 10 大挑战 |
| 2303.06574 | Diffusion Models for Non-AR Text Generation: Survey | ArXiv | 早期综述 |

---

## 六、Training 方向 (~15 篇)

### Training Objectives

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2406.07524 | Simple and Effective MDLM (MDLM) | NeurIPS 2024 | Effective training recipe |
| 2305.18619 | Likelihood-Based DLMs | NeurIPS 2023 | Likelihood-based training |
| 2509.05056 | Frequency-Informed Training | ArXiv | Frequency-informed masking |
| 2510.03280 | Training Optimal Large DLMs | ArXiv | 最优训练 |

### Scaling / Adaptation

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2410.17891 | Scaling DLMs via Adaptation from AR Models | ICLR 2025 | AR → Diffusion adaptation |
| 2410.18514 | Scaling up Masked Diffusion on Text | ICLR 2025 | Scaling masked diffusion |
| 2509.24389 | LLaDA-MoE: Sparse MoE DLM | ArXiv | MoE for DLM |

### Alignment

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2510.23658 | Aligning DLMs via Unpaired Preference Optimization | ArXiv | Unpaired preference |
| 2509.20863 | WeFT: Weighted Entropy-driven Fine-Tuning | ArXiv | Entropy-driven fine-tuning |
| 2512.09675 | d-TreeRPO: Reliable Policy Optimization | ArXiv | Tree-based RPO |

---

## 七、Test-Time Scaling 方向 (~10 篇)

| arXiv | 标题 | 会议 | 核心贡献 |
|-------|------|------|----------|
| 2512.02008 | The Art of Scaling Test-Time Compute | ArXiv | 综述 |
| N/A | Scaling LLM Test-Time Compute Optimally | ICLR 2025 | 最优 scaling |
| 2408.00724 | Inference Scaling Laws | ICLR 2025 | Compute-optimal inference |
| 2509.04474 | Benchmark of Speculative Decoding for Test-Time Scaling | ArXiv | Speculative decoding benchmark |
| 2504.14047 | Think Deep, Think Fast: Verifier-free Methods | ArXiv | Verifier-free |
| 2506.22376 | OptScale: Probabilistic Optimality | ArXiv | Probabilistic optimality |

---

## Gap 分析总结

### 方向 A: Remask-based Reasoning

**已有工作：**
- Remask 策略：RemeDi, CoRe, Saber (backtracking)
- Self-correction：ProSeCo, Corrective DLM, Provable Self-Correction
- Decoding：SOAR, MCTS, Joint Search

**Gap 1: Remask timing 没有理论基础**
- 现有工作用 confidence 决定 remask
- 没人研究 **optimal remask timing 的理论**
- 信息论视角：什么时候需要更多信息？

**Gap 2: Remask 和 Reasoning 的因果关系不清楚**
- 大家说 remask 帮助 reasoning，但 **为什么**？
- 是 error correction？还是 iterative refinement 本身？
- 没有 mechanistic understanding

**Gap 3: 训练方法都是 heuristic**
- RemeDi: SFT + RL
- Corrective DLM: post-training with synthetic errors
- **没有 principled training objective for remask**

**Gap 4: 没有 information-theoretic 视角**
- Remask 本质是 "重新获取信息"
- 没人用 MI/entropy 指导 remask

---

### 方向 B: Hard → Soft Mask

**已有工作：**
- Soft mask：Soft-Masked DLM (embedding blend), EvoToken (distribution evolution)
- Continuous：Latent Diffusion, Continuous Diffusion, TEncDM
- Residual：RCD (residual context injection)

**Gap 1: Soft mask 定义不统一**
- Embedding blending vs Distribution evolution vs Residual injection
- **没有统一框架**

**Gap 2: Soft mask 和加速的关系不清楚**
- 为什么 soft 更快？
- 是因为保留了更多信息？还是减少了 steps？
- **没有理论分析**

**Gap 3: Soft mask 和 latent reasoning 的关系是空白** ⭐⭐⭐
- **完全没人研究！**
- Soft mask 保留的 "中间信息" 是什么？
- 这些信息对 reasoning 有什么帮助？
- 能否用 MI 量化？

**Gap 4: 没有 training-free hard → soft 转换**
- EvoToken 从头训练
- RCD 需要 fine-tuning
- **能否 training-free 把 LLaDA 转成 soft mask？**

---

## 最有价值的研究方向

### 1. Soft Mask 和 Latent Reasoning 的关系 (最推荐)

**为什么重要：**
- 完全空白，没人做
- 有理论深度（information theory）
- 和 Greg 的背景契合
- 可以 build on Yu 的 "Thinking Out of Order"

**具体问题：**
- Soft mask 是否等价于在 latent space 做 diffusion？
- Soft mask 保留的 "中间信息" 能否用 MI 量化？
- 这些中间信息对 reasoning 有什么帮助？

### 2. Information-Theoretic Remask

**为什么重要：**
- 现有 remask 都是 heuristic
- 信息论可以提供 principled guidance
- 和 Greg 的背景契合

**具体问题：**
- 什么时候 remask？→ 当 MI(token; context) 低时
- Remask 多少？→ 取决于 uncertainty
- 如何训练？→ MI-based objective

### 3. Training-Free Hard → Soft Conversion

**为什么重要：**
- 实用价值高
- 可以直接用 LLaDA
- 不需要重新训练

**具体问题：**
- 如何在 inference 时把 hard mask 转成 soft？
- 需要什么 architectural changes？
- 性能 trade-off 是什么？
