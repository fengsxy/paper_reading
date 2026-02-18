# 研究方向调研 (2026-02-15)

Yu 当前的两个项目相关论文调研。

---

## 项目 1: Slot-Lift (图像生成最优路径)

### 核心参考论文

#### Align Your Steps (ICML 2024)
- **arXiv:** 2404.14507
- **作者:** NVIDIA (Amirmojtaba Sabour, Sanja Fidler, Karsten Kreis)
- **核心思想:** 用 stochastic calculus 优化 diffusion 的 sampling schedule
- **方法:** 找到 solver-specific, model-specific, dataset-specific 的最优 schedule
- **结果:** 在 few-step synthesis 上显著优于 hand-crafted schedules
- **项目页:** https://research.nvidia.com/labs/toronto-ai/AlignYourSteps/

**和 Slot-Lift 的关系：** 这是直接相关的工作。Yu 想用 heat error map 估计最优路径，Align Your Steps 用 stochastic calculus 做类似的事。

---

### 相关论文

#### 1. ART for Diffusion Sampling (2026.01)
- 用 Reinforcement Learning 学习 timestep schedule
- 和 Align Your Steps 的 optimization 方法不同

#### 2. BézierFlow (2025.12)
- 用 Bézier curves 参数化 stochastic interpolant schedulers
- 15 分钟训练，2-3x 性能提升 (≤10 NFEs)

#### 3. Hierarchical Schedule Optimization (2025.11)
- 分层优化 schedule
- Fast and robust sampling

#### 4. An Elementary Approach to Scheduling (2601.13602)
- 理论分析 noise scheduling 和 time discretization 的影响
- 用 multivariate Gaussian 简化模型推导 closed-form KL divergence

#### 5. Latent Forcing (2602.11401)
- **核心思想:** Reorder diffusion trajectory for pixel-space generation
- 在 raw images 上达到 latent diffusion 的效率
- **和 Slot-Lift 相关：** 也是关于 "reordering trajectory"

#### 6. Dynamic Classifier-Free Guidance (2509.16131)
- 动态 CFG scheduling（不是 static guidance scale）
- 不同 prompts 需要不同的 guidance schedule

---

### Slot-Lift 的独特点

现有工作主要关注：
1. **Timestep schedule optimization** — 什么时候 denoise
2. **Solver optimization** — 怎么 denoise

Yu 的想法：
- 用 **heat error map** 在不同噪声尺度下估计 error
- 找到 **最优生成路径**
- 有两个 t（可能是 start/end 或 intermediate points）

**潜在创新点：**
- Error-guided path optimization（不只是 timestep，而是整个 trajectory）
- 可视化 error landscape，找到 optimal path

---

## 项目 2: dLLM Remask 算法

### 方向 A: Remask-based Reasoning

#### 核心论文

##### 1. On Powerful Ways to Generate (2510.06190)
- **核心发现:** any-order 不比 AR 更强，**any-process (remask, insert, delete) 才是真正优势**
- 提出 self-correction, length-variable editing, adaptive parallelism
- **关键引用:** "these capabilities enable scalability to significantly harder reasoning problems"

##### 2. Learn from Your Mistakes: Self-Correcting MDMs (2602.11590)
- **ProSeCo:** Progressive Self-Correction
- 训练模型同时做 unmasking 和 correction
- 在 unmasking steps 之间加 corrective refinement steps
- **结果:** 2-3x faster sampling, ~1.3x improvement on benchmarks

##### 3. Don't Settle Too Early: Self-Reflective Remasking / RemeDi (2509.23653)
- 不要过早 commit
- **Remasking as fundamental mechanism** — 不只是纠错
- 关键挑战：如何 identify potential errors in inputs

##### 4. Fine-Tuning Masked Diffusion for Provable Self-Correction (2510.01384)
- **Provable** self-correction — 有理论保证
- 不需要 overhaul MDM architecture

##### 5. Corrective Diffusion Language Models (2512.15596)
- 标准 MDLM training 不能 reliably induce self-correction
- 模型不能 identify unreliable tokens
- Confidence-guided refinement 失效

##### 6. Training-Free Self-Correction for Multimodal MDMs (2602.02927)
- **Training-free** 方法
- 现有 self-correction 方法需要额外训练

##### 7. d2: Improved Techniques for Training Reasoning DLMs (2509.21474)
- 用 RL 提升 DLM reasoning
- 新的 policy gradient algorithm for masked DLMs

##### 8. Remasking Discrete Diffusion Models with Inference-Time Scaling (2025.02, updated 2026.02)
- Inference-time scaling for remasking
- 更多 compute → 更好的 remasking 决策

##### 9. CORE: Context-Robust Remasking (2026.02)
- 标准 MDM decoding 的问题
- Context-robust 的 remasking 策略

##### 10. Stop the Flip-Flop: Context-Preserving Verification (2026.02)
- 解决 parallel diffusion decoding 的 flip-flop 问题
- Context-preserving verification

##### 11. Prism: Hierarchical Search and Self-Verification (2026.02)
- Test-time scaling for discrete diffusion LMs
- Hierarchical search + self-verification

##### 12. Saber: Adaptive Acceleration and Backtracking Enhanced Remasking (2510.18165)
- **Backtracking:** 允许回退到之前的状态
- Adaptive acceleration
- 针对 code generation（强结构约束）

---

### 方向 B: Hard Mask → Soft Mask

#### 核心论文

##### 1. Soft-Masked Diffusion Language Models (2510.17206) ⭐ 新发现
- **直接相关！** 专门讨论 soft mask for dLLM
- Parallel generation + built-in self-correction

##### 2. A Cheaper and Better Diffusion LM with Soft-Masked Noise (EMNLP 2023, 2304.04746)
- **早期工作** — soft mask 的先驱
- Gaussian noise 不能很好处理 discrete corruption
- Soft-masked noise 更适合语言

##### 3. Beyond Hard Masks: EvoToken-DLM (2601.07351)
- **核心思想:** 用 evolving soft token distributions 替代 hard binary masks
- Progressive transition from masked states to discrete outputs
- **Continuous trajectory supervision:** 训练目标和 iterative probabilistic updates 对齐
- **项目页:** https://aim-uofa.github.io/EvoTokenDLM

##### 4. Residual Context Diffusion (RCD) (2601.22954)
- **问题:** Remasking 丢弃 low-confidence tokens，浪费计算
- **解决:** 把 discarded token representations 转为 contextual residuals，注入下一步
- **结果:** 5-10 points accuracy improvement, 4-5x fewer denoising steps on AIME
- **关键:** 只需 ~1B tokens 就能把标准 dLLM 转为 RCD

##### 5. Continuous Diffusion Model for Language Modeling (NeurIPS 2025, 2502.11564)
- Discrete diffusion 不能充分利用 iterative refinement
- **Continuous diffusion for discrete data** — 信号在 discrete state transitions 中丢失

##### 6. Simple and Effective Masked Diffusion LMs (NeurIPS 2024, 2406.07524)
- MDLM 的 effective training recipe
- 证明 simple masked diffusion 比之前认为的更强

##### 7. Discrete Diffusion Survey (2506.13759)
- 系统性 survey of dLLMs and dMLLMs
- Multi-token parallel decoding paradigm

##### 8. Top 10 Open Challenges (2601.14041)
- 提到 **latent thinking** 作为关键方向
- Multi-scale tokenization, active remasking

---

### Remask 和 Latent Reasoning 的关系

**现有理解：**
- Hard mask: token 要么 masked 要么 unmasked，binary
- Soft mask: token 有 continuous probability，可以 partially masked
- Latent reasoning: 在 latent space 做推理，不直接操作 discrete tokens

**潜在联系：**
1. Soft mask 保留更多中间信息 → 类似 latent representation
2. Remask 允许 "reconsider" → 类似 iterative refinement in latent space
3. RCD 的 residual context → 显式保留 latent information

**研究问题：**
- Soft mask 是否等价于在 latent space 做 diffusion？
- 能否设计一个 unified framework 连接 soft mask 和 latent reasoning？

---

## 总结：两个项目的交叉点

| 维度 | Slot-Lift (图像) | dLLM Remask (语言) |
|------|------------------|-------------------|
| 核心问题 | 最优生成路径 | 最优 remask 策略 |
| 方法 | Error map → optimal path | Confidence → remask decision |
| 理论基础 | Stochastic calculus | Information theory? |
| 关键论文 | Align Your Steps | RCD, EvoToken-DLM |

**潜在统一视角：**
- 两者都在问 "什么时候 commit，什么时候 refine"
- 图像：在哪个 noise level commit
- 语言：在哪个 token position commit
- 能否用统一的 information-theoretic framework？

---

## 建议的下一步

### Slot-Lift
1. 复现 Align Your Steps
2. 设计 heat error map 的计算方法
3. 比较 error-guided path vs AYS optimized schedule

### dLLM Remask
1. 读 RCD 和 EvoToken-DLM 的代码
2. 在 LLaDA 上实验 soft mask
3. 分析 soft mask 和 reasoning 能力的关系
