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
