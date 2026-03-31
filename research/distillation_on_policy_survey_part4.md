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
