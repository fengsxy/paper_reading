# 知识蒸馏与 On-Policy Distillation 调研报告

**作者：Claw | 日期：2026-03-15 | 为 Yu 准备**
**基于 19 篇论文精读（含前两份报告的 12 篇 + 本次新增 7 篇）**

---

## 一、问题定义

知识蒸馏是让小模型从大模型学习的核心方法。在 dLLM 语境下，蒸馏有两层含义：

1. **经典 KD**：大 teacher → 小 student（压缩模型）
2. **Step Distillation**：多步 teacher → 少步 student（加速推理）
3. **Paradigm Distillation**：AR teacher → dLLM student（转换范式）

On-Policy Distillation 是近年最重要的进展：让 student 在**自己生成的数据**上学习，而非 teacher 的数据。

---

## 二、论文列表（7篇新增精读）

| # | 论文 | 来源 | 核心方法 | 精读 |
|---|------|------|----------|------|
| 13 | **MiniLLM** | ICLR 2024, Microsoft | Reverse KL + on-policy policy gradient | ✅全文 |
| 14 | **GKD** | ICLR 2024, Google DeepMind | Generalized divergence + on-policy student data | ✅论文 |
| 15 | **EOPD** | arXiv 2026.03, IBM+KAIST | Entropy-aware 混合 forward+reverse KL | ✅全文 |
| 16 | **Reopold** | arXiv 2026.03, ICML submission | RL 视角诊断 + relaxed distillation | ✅全文 |
| 17 | **Progressive Distillation** | ICLR 2022, Salimans & Ho | 迭代 halving 步数 | ✅方法 |
| 18 | **Consistency Models** | ICML 2023, Song et al. | Self-consistency → one-step generation | ✅方法 |
| 19 | **OPSD** (Self-Distilled Reasoner) | arXiv 2026.01, CMU | On-policy self-distillation 无需外部 teacher | ✅Abstract+Blog |

---

## 三、分类框架

```
知识蒸馏方法
│
├── ① Off-Policy Distillation（在 teacher 数据上学）
│   ├── SeqKD: SFT on teacher generations（最简单）
│   ├── Standard KD: Forward KL on teacher distribution
│   └── 局限：distribution mismatch（student 推理时的分布 ≠ 训练时的分布）
│
├── ② On-Policy Distillation（在 student 数据上学）
│   ├── MiniLLM: Reverse KL + policy gradient
│   ├── GKD: Generalized divergence + on-policy student sampling
│   ├── EOPD: Entropy-aware forward+reverse KL hybrid
│   ├── Reopold: RL-aware relaxed distillation（reward clipping + dynamic sampling）
│   └── OPSD: Self-distillation（student = teacher）
│
├── ③ Step Distillation（减少 diffusion 步数）
│   ├── Progressive Distillation: 迭代 halving（N → N/2 → N/4）
│   ├── Consistency Distillation: 任意步 → 1步映射
│   └── CDLM: Consistency model for discrete diffusion
│
└── ④ Paradigm Distillation（AR → dLLM 转换）
    ├── DiffuLLaMA / Efficient-DLM / SDAR（见前份报告）
    └── 本质上也是蒸馏：AR teacher 的知识 → dLLM student
```
## 四、各方案详细分析

### 类别①：Off-Policy Distillation（基线）

**SeqKD**：在 teacher 生成的 response 上做 SFT。最简单但效果最差——student 推理时生成的分布和训练时看到的分布不一样（exposure bias）。

**Standard KD (Forward KL)**：在每个 token 位置最小化 teacher 和 student 分布的 forward KL。问题：forward KL 是 mode-covering 的——强迫 student 覆盖 teacher 的所有 mode（包括低概率区域），导致 student 分布过于 diffuse。

**核心局限**：训练在 teacher 的数据上，但推理在 student 的数据上 → **distribution mismatch** → 错误累积。

---

### 类别②：On-Policy Distillation（核心方向）

#### MiniLLM (Microsoft/Tsinghua, ICLR 2024) — 奠基工作

**核心洞察**：用 **reverse KL** 替代 forward KL，在 **student 自己生成的数据**上训练。

**为什么 reverse KL 更好**：
- Forward KL: E_{teacher}[log(teacher/student)] → mode-covering → student 在低概率区域浪费概率
- Reverse KL: E_{student}[log(student/teacher)] → mode-seeking → student 集中在 teacher 的高概率区域
- 对 LLM 来说，模式精确 > 覆盖全面（生成一个好答案 > 覆盖所有可能答案）

**三个稳定训练的技巧**：
1. **Single-Step Decomposition**：把序列级 reverse KL 分解为 token 级，减少梯度方差
2. **Teacher-Mixed Sampling**：α 概率用 teacher 采样 + (1-α) 用 student 采样（防止 student 走太偏）
3. **Length Normalization**：防止 reward hacking（student 学会生成短/重复文本以获得高 reward）

**关键结果**：
- 120M→13B 全面超越 SeqKD 和标准 KD
- Student 在某些任务上**超越 teacher**——因为 on-policy 训练减少了 exposure bias
- Calibration 更好（ECE 更低）

**好在哪**：第一个系统性的 LLM on-policy distillation 方案，建立了 distillation ≈ RL 的联系

**不足**：reverse KL 的 mode-seeking 导致多样性下降（后续工作的改进点）

---

#### GKD — Generalized Knowledge Distillation (Google DeepMind, ICLR 2024)

**核心创新**：泛化 divergence 选择 + on-policy student data

**关键设计**：
- 不限于 KL divergence，支持 JSD、TVD、forward KL、reverse KL 等
- 训练时用 student 自己的 output（on-policy），teacher 只提供 token-level probability
- 可以无缝嵌入 RLHF pipeline（先 GKD 蒸馏 → 再 RLHF 对齐）

**结果**：在 summarization 和 translation 上显著优于标准 KD

**好在哪**：统一框架，灵活选择 divergence

---

#### EOPD — Entropy-Aware On-Policy Distillation (IBM+KAIST, arXiv 2026.03)

**核心发现**：reverse KL 在 **高 entropy token 上失败**。

**问题诊断**：
- Teacher 对某些 token 不确定（多种合理选择 → 高 entropy）
- Reverse KL 强迫 student 只选一个 mode → 丢失了 teacher 的 uncertainty
- 量化：蒸馏后 student 只保留 **6.8%** 的高 entropy tokens（teacher 是 18.5%）
- Toy experiment 验证：高 entropy 下 reverse KL 的 top-10 predictions 无法收敛

**EOPD 的解决方案**：
```
L_EOPD = L_OPD(reverse KL) + I[H_t > τ] × L_FKL(forward KL)
```
- 低 entropy token（teacher 确定）：只用 reverse KL（精确匹配）
- 高 entropy token（teacher 不确定）：加上 forward KL（保留多样性）
- τ = entropy threshold

**结果**：
- Qwen3-0.6B: Pass@8 +1.37, Qwen3-1.7B: +2.39, Qwen3-4B: **+5.05**
- 模型越大提升越大
- 关键：提升主要来自多样性保持 → Pass@K 提升远大于 Greedy

**好在哪**：发现了 reverse KL 的盲区（高 entropy token），提出了优雅的修复

**与 dLLM 的直接关系**：dLLM 的 masked token prediction 本质上就是高 entropy 场景——多个 masked token 同时预测，teacher 的 uncertainty 更高。EOPD 的思路直接适用。

---

#### Reopold — Relaxed On-Policy Distillation (arXiv 2026.03, ICML submission)

**核心洞察**：On-Policy Distillation **精确等价于** Policy Gradient RL。

**证明（Remark 3.1）**：
- Stop-gradient 后，distillation objective = policy gradient objective
- Teacher-student log-likelihood ratio = token-level reward
- 梯度在期望意义下完全相同
- Stop-gradient 作为 control variate 减少方差 → 免费的改进

**三大挑战（RL 视角诊断）**：

| 挑战 | 表现 | 原因 |
|------|------|------|
| Heavy-tailed negative rewards | 梯度爆炸 | Student 生成 teacher 不喜欢的 token |
| Near-zero rewards | 浪费计算 | 大多数 token student 和 teacher 一致 |
| Entropy collapse | 过早收敛 | Student 快速丧失多样性 |

**Reopold 三个解决方案**：
1. **Mixture-based reward clipping**：截断极端负 reward（logλ/(1-λ)），防止梯度爆炸
2. **Token-level dynamic sampling**：只在高信息量 token 上学习（M_{i,t} mask 选择性学习）
3. **两阶段训练**：
   - Stage 1 (exploration)：基于 reward 选择性学习
   - Stage 2 (refinement)：基于 entropy 选择性学习

**结果**：
- 比标准 on-policy distillation **6.7-12× 更高 sample efficiency**
- 7B student 匹配 32B teacher（visual reasoning）
- 比 GRPO 等 RL 方法也更高效

**好在哪**：最深入的理论分析，把 distillation 和 RL 完全统一
### 类别③：Step Distillation（减少 diffusion 步数）

#### Progressive Distillation (Salimans & Ho, ICLR 2022) — 经典方法

**核心方法**：
1. Teacher 用 N 步生成 → 训练 student 用 N/2 步匹配 teacher 的两步输出
2. Student 成为新 teacher → 再训 N/4 步的 student
3. 迭代直到 1-4 步

**关键设计**：student 的一步 = teacher 的两步。每次迭代减半步数。

**在 dLLM 中的应用**：
- 直接类比：teacher 用 T 步 denoise → student 用 T/2 步
- 但 discrete diffusion 比 continuous 更难蒸馏：离散采样不可微，无法直接用 L2 loss
- CDLM（Paper 9）是这个思路在 discrete diffusion 上的实现

---

#### Consistency Models (Song et al., ICML 2023) — 经典方法

**核心思想**：定义 consistency function f(x_t, t) → x_0：同一 trajectory 上的任意中间状态都映射到**同一个** x_0。

**两种训练方式**：
1. **Consistency Distillation (CD)**：从预训练 diffusion model 蒸馏。用 teacher 的 ODE trajectory 做训练信号。
2. **Consistency Training (CT)**：直接训练，不需要 teacher。用 adjacent states 的一致性约束。

**与 dLLM 的关系**：
- CDLM（Paper 9）直接搬了 CD 到 discrete diffusion
- CT 方向在 dLLM 中**还未被探索**——潜在研究机会
- Discrete space 中 "self-consistency" 需要重新定义（离散 token 没有连续 ODE trajectory）

---

#### CDLM — Consistency DLM（Paper 9，前报告已详述）

三个 loss 联合训练：Distillation + Consistency + DLM
- 8-16h 训练 → 3.6-14.5× latency reduction
- Bidir teacher → block-causal student（蒸馏 + 转换一步完成）
- 当前 dLLM 加速的最高效方案

---

### 类别④：Self-Distillation

#### OPSD — Self-Distilled Reasoner (CMU, arXiv 2026.01)

**核心创新：不需要外部 teacher**

**方法**：
1. Model 自己生成 solution
2. 用 privileged info（ground truth answer）筛选正确 solution
3. 在正确 solution 上做 on-policy self-distillation（自己的正确输出作为 teacher signal）
4. 迭代 self-improvement

**结果**：4-5× inference speedup on parallel-structured reasoning tasks

**与 dLLM 的关系**：
- dLLM 天然支持 self-distillation：多步 denoise（完整 trajectory）→ 少步 denoise（student）
- 不需要外部 AR teacher
- 利用 dLLM 自己的 iterative refinement 能力做 self-improvement
## 五、综合对比表

| 方案 | 类别 | Data Source | Divergence | 核心优势 | 核心不足 |
|------|------|------------|------------|----------|----------|
| **SeqKD** | Off-Policy | Teacher 生成 | N/A (SFT) | 最简单 | Exposure bias，效果差 |
| **Standard KD** | Off-Policy | Teacher 分布 | Forward KL | 利用 soft label | Mode-covering，分布 diffuse |
| **MiniLLM** | On-Policy | Student 生成 | Reverse KL | 首个 on-policy LLM KD，超越 teacher | Mode-seeking，多样性下降 |
| **GKD** | On-Policy | Student 生成 | 任意 divergence | 统一框架，兼容 RLHF | 未专门解决高 entropy 问题 |
| **EOPD** | On-Policy | Student 生成 | Entropy-aware 混合 | 保留 teacher 不确定性，Pass@K 大涨 | 需要设定 entropy threshold τ |
| **Reopold** | On-Policy | Student 生成 | Reverse KL + RL tricks | 理论最深，6.7-12× sample efficiency | 复杂度高（两阶段 + 多超参） |
| **OPSD** | Self-Distill | Self 生成 | Self KL | 不需要外部 teacher | 需要 ground truth 做筛选 |
| **Prog. Distill** | Step Distill | Teacher trajectory | L2 / KL | 经典，迭代 halving | 不适用于 discrete（不可微） |
| **Consistency** | Step Distill | Teacher ODE | Consistency loss | 一步生成，理论优雅 | Discrete 版本（CT）未探索 |
| **CDLM** | Step Distill (dLLM) | Teacher trajectory | Distill+Consist+DLM | 8h 训练，14.5× 加速 | 上限受 teacher 限制 |

---

## 六、关键洞察

### 洞察1：On-Policy Distillation 本质上就是 RL

Reopold 严格证明了：stop-gradient 后，on-policy distillation 的梯度 = policy gradient 的梯度。Teacher-student log-likelihood ratio = token-level reward。

**这意味着**：所有 RL 的技巧（PPO clipping、reward shaping、entropy bonus、advantage estimation）都可以直接搬到 distillation 中。反过来，distillation 比 RL 更高效（10× less compute than GRPO），因为 teacher 提供了 dense token-level signal（vs RL 只有 sparse sequence-level reward）。

### 洞察2：Forward KL 和 Reverse KL 各有所长，应该混合使用

| KL 方向 | 行为 | 适用场景 |
|---------|------|----------|
| Forward KL | Mode-covering（覆盖所有 mode） | Teacher 不确定时（高 entropy token） |
| Reverse KL | Mode-seeking（集中在主 mode） | Teacher 确定时（低 entropy token） |

EOPD 证明了：在高 entropy token 上用 forward KL + 低 entropy token 上用 reverse KL → Pass@8 最高 +5.05。

**对 dLLM 的启示**：dLLM 的 masked token prediction 天然是高 entropy 场景，应该优先用 forward KL 或混合策略。

### 洞察3：Token-level 选择性学习是关键

Reopold 和 EOPD 都发现：**不是所有 token 都值得学习**。
- Near-zero reward tokens → 浪费计算（Reopold 过滤）
- 低 entropy tokens → student 已经学好了（EOPD 跳过 forward KL）
- 极端负 reward tokens → 有害信号（Reopold 截断）

**集中资源在"有信息量"的 token 上**，比均匀学习所有 token 高效得多。

### 洞察4：Step Distillation 在 dLLM 中严重不足

Continuous diffusion 有丰富的 step distillation 工具（Progressive Distillation、Consistency Models、DDIM 等），但 discrete diffusion 几乎只有 CDLM 一个。原因：
- 离散采样不可微 → 不能用 L2 loss
- 离散 state space 没有 ODE trajectory → Consistency 的 self-consistency 难定义
- **这是一个巨大的研究空白**

### 洞察5：Self-Distillation 是 dLLM 的天然优势

dLLM 的 iterative refinement 过程天然包含 teacher-student 关系：
- 多步 denoise（完整执行）= teacher
- 少步 denoise（跳步执行）= student
- 不需要外部 AR teacher，dLLM 自己就能做 self-distillation
- 这跟 OPSD 的 self-improvement loop 完美契合

---

## 七、与你的 dLLM 工作的关系

### 1. Linear State Memory + On-Policy Distillation

你的 linear state 可以**降低蒸馏难度**：
- 跨步信息保持 → student 每步拿到更好的初始化 → 需要更少步数达到相同质量
- 相当于 teacher 的知识通过 linear state "预加载"到 student 中

### 2. Entropy-Aware 思路直接适用

dLLM 的 masked prediction = 高 entropy 场景 → EOPD 的 entropy-aware 混合策略直接可用：
- 对 high-confidence tokens（已揭示且稳定）：reverse KL
- 对 low-confidence tokens（新揭示或不确定）：forward KL
- Linear state 可以提供 confidence signal（state 中积累的信息 → 当前预测的可靠度）

### 3. CDLM + Linear State 联合方案

CDLM 做 step distillation + linear state 做信息保持：
- CDLM 蒸馏减少步数（3.6-14.5×）
- Linear state 补偿步数减少带来的信息损失
- 预期效果：更少步 + 同等或更好质量

### 4. Self-Distillation Loop

dLLM 的天然 self-distillation + linear state self-improvement：
- Round 1: dLLM + linear state，T 步 denoise
- 收集 trajectory，训 T/2 步的 student
- Linear state 在少步模式下更关键（每步信息损失更大，memory 更重要）
- 迭代直到最优 step-quality trade-off

---

## 八、参考文献

1-12: 见前两份报告

13. Gu et al. "MiniLLM: Knowledge Distillation of Large Language Models." ICLR 2024. arXiv:2306.08543.
14. Agarwal et al. "On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes (GKD)." ICLR 2024. arXiv:2306.13649.
15. Min et al. "Entropy-Aware On-Policy Distillation of Language Models." arXiv:2603.07079, 2026.
16. Park et al. "Reopold: Scaling Reasoning Efficiently via Relaxed On-Policy Distillation." arXiv:2603.11137, 2026.
17. Salimans & Ho. "Progressive Distillation for Fast Sampling of Diffusion Models." ICLR 2022. arXiv:2202.00512.
18. Song et al. "Consistency Models." ICML 2023. arXiv:2303.01469.
19. Qu et al. "Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models." arXiv:2601.18734, 2026.

**精读笔记**：见 `research/ar_to_dllm_reading_notes.md`（19篇论文完整精读笔记）
