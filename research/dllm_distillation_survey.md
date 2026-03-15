# 如何做好 dLLM：蒸馏、加速与 Post-Training 方法调研

**作者：Claw | 日期：2026-03-15 | 为 Yu 准备**
**基于 12 篇论文全文精读（含上一份报告的 8 篇 + 本次新增 4 篇）**

---

## 一、问题定义

dLLM 的核心瓶颈不只是"怎么训"，还有"怎么让它又快又好"。这个报告聚焦三个方向：

1. **蒸馏加速**：用 teacher-student 框架减少 denoising 步数
2. **RL 对齐**：dLLM 的 RLHF/DPO 怎么做（log-likelihood 不可计算）
3. **混合架构**：AR + Diffusion 结合，取两者之长

---

## 二、新增论文列表（4篇精读）

| # | 论文 | 来源 | 核心方法 | 精读 |
|---|------|------|----------|------|
| 9 | **CDLM** (Consistency DLM) | MLSys under review | Consistency distillation + block-causal student | ✅全文 |
| 10 | **SPG** (Sandwiched Policy Gradient) | Meta, arXiv 2025.10 | ELBO+EUBO sandwich for RL | ✅全文 |
| 11 | **Seed Diffusion** | ByteDance, arXiv 2025.08 | Two-stage curriculum + edit-based corruption | ✅全文 |
| 12 | **TiDAR** | NVIDIA, arXiv 2025.11 | Think in Diffusion, Talk in AR (单模型混合) | ✅全文 |

---

## 三、分类框架

```
如何做好 dLLM
│
├── ① 蒸馏加速（减少 denoising 步数）
│   ├── CDLM: consistency distillation (bidir teacher → block-causal student)
│   └── LLaDA 2.0 WSD Decay: 全局知识蒸馏到 block-wise 结构
│
├── ② RL 对齐（解决 log-likelihood 不可计算问题）
│   ├── SPG: Sandwiched Policy Gradient (ELBO for positive, EUBO for negative)
│   └── LLaDA 2.0 DPO: reconstruction loss 替代 log-likelihood
│
├── ③ 训练策略优化
│   ├── Seed Diffusion TSC: 两阶段课程（mask → mask+edit）
│   ├── Dream CART: context-adaptive noise reschedule
│   ├── Efficient-DLM: position-dependent masking + clean context
│   └── LLaDA 2.0: complementary masking SFT + confidence-aware parallel SFT
│
├── ④ 混合架构（AR + Diffusion 融合）
│   ├── TiDAR: 单模型内 diffusion drafting + AR verification
│   ├── Block Diffusion: block 间 AR + block 内 diffusion
│   └── Efficient-DLM / SDAR: AR→block-wise dLLM 转换
│
└── ⑤ 推理优化（不改模型）
    ├── Elastic-Cache / dKV-Cache: KV cache 复用
    ├── MetaState: 跨步 persistent memory
    └── ProSeCo: self-correcting sampling
```
## 四、各方案详细分析

### 类别①：蒸馏加速

#### CDLM — Consistency Diffusion Language Models (MLSys under review)

**核心思路**：把 continuous diffusion 的 consistency model 搬到 discrete diffusion。Consistency model 的核心性质：任意中间状态都能直接映射到最终结果，不需要走完所有步。

**方法**：三个训练目标联合优化
1. **Distillation Loss**：从 bidirectional teacher 蒸馏到 block-causal student
   - 离线收集 teacher 的 decoding trajectories + hidden states
   - Forward KL on newly unmasked positions
   - 关键：存 hidden states（不是 logits），推理时用 lm_head 重建 → 省存储
   
2. **Consistency Loss**：enforcing student 在 state y 和 block-completion state y* 之间预测一致
   - Stop-gradient target（稳定训练）
   - 只在 still-masked positions 上计算
   - 让 student 学会"跳步"——从部分揭示直接预测完整揭示

3. **DLM Loss**：标准 masked denoising objective，保持基本能力

**结果**：
- Dream 7B: 8h training → 3.4-7.9× fewer denoising steps, 3.6-14.5× lower latency
- LLaDA 8B: 16h training → similar speedup
- Accuracy 几乎无损
- 超越同规模 AR 模型的 tokens/second

**好在哪**：
- 训练成本极低（8-16 hours）
- Self-distillation：teacher 和 student 同架构同规模，只改 attention pattern
- 蒸馏 + block-causal conversion 一步完成（不需要单独转换再蒸馏）
- Consistency objective 比单纯 distillation 更 principled

**不足**：
- 需要离线收集 trajectories（但一次性成本）
- Block size 是超参数
- 蒸馏后的 student 能力上限受 teacher 限制

---

### 类别②：RL 对齐

#### SPG — Sandwiched Policy Gradient (Meta, arXiv 2025.10)

**核心问题**：dLLM 的 log π_θ(x|c) 不可计算 → 标准 policy gradient 无法直接用。

**现有方案的缺陷**：
- 用 ELBO 近似 log-likelihood
- ELBO 是 lower bound → 对 positive reward：maximize ELBO ≈ maximize log π ✓
- 但对 negative reward：minimize ELBO ≠ minimize log π ✗（方向错了！）
- 这意味着模型**无法有效从错误中学习**

**SPG 的解决方案——三明治**：
- Positive advantage（好 response）：maximize **ELBO**（lower bound）
- Negative advantage（坏 response）：minimize **EUBO**（upper bound，基于 Rényi variational bound）
- ELBO ≤ log π ≤ EUBO → 两个方向都是 valid bound → 无偏优化

**EUBO 的推导（Theorem 1）**：
- 基于 Rényi variational bound
- β ≥ 1 控制 tightness（β → 1 更紧但方差更大）
- 关键区别：EUBO 的 log 在 expectation 外面（ELBO 是里面）

**Block-wise Masking**：
- RL 训练时也用 block-wise masking（不是 random），匹配推理时的分布

**结果**：GSM8K +3.6%, MATH500 +2.6%, Countdown +18.4%, Sudoku +27.0%（vs ELBO-based RL）

**好在哪**：
- 第一个理论上正确的 dLLM RL 方法
- Sudoku +27% → 在 planning 任务上效果惊人
- Block-wise masking 的 train-test alignment 思路跟 Efficient-DLM 一致

**不足**：
- EUBO 的 Monte Carlo estimation 有 bias（log 在 expectation 外）
- 实际用 EUBO+ELBO mixture 缓解（不是纯 EUBO）
- 训练成本较高（需要 on-policy rollout）
### 类别③：训练策略优化

#### Seed Diffusion TSC — Two-Stage Curriculum (ByteDance, arXiv 2025.08)

**核心创新：两阶段课程学习**

Stage 1（前 80% training steps）：标准 mask-based diffusion training
- 正常的 MDLM 训练，建立基本的 denoising 能力

Stage 2（后 20% training steps）：加入 edit-based corruption
- 不只是 mask→clean，还要处理 deletion/insertion/substitution
- 用 Levenshtein distance 控制 corruption level（轻度，αt ∈ [0, 0.1]）
- 目的：improve calibration，消除 repetition 等 sampling artifacts
- 类似于 "数据增强"——让模型见过更多种类的 corrupted input

**Generation Order Control**：
- mask-based diffusion ≡ any-order autoregressive modeling
- 自然语言是顺序的 → 纯 random order 效率低
- Seed Diffusion 引导模型偏向 left-to-right order
- 跟 Efficient-DLM 的 position-dependent masking 和 Dream 的 CART 是同一思路

**速度**：2,146 tokens/sec on H20 GPU — 当前最快的 dLLM

**好在哪**：
- Edit-based corruption 是独特的训练技巧——其他所有 dLLM 都只用 mask-based
- 解决了 sampling artifacts（repetition 等）
- Speed-quality Pareto frontier 当前 SOTA

---

#### 训练策略对比总结

| 策略 | 论文 | 解决什么 | 核心思路 |
|------|------|----------|----------|
| Clean context | Efficient-DLM | 权重分布保留 | 已解码 block 用 clean token |
| Position-dep masking | Efficient-DLM | Train-test mismatch | 后面位置更高 mask 概率 |
| CART | Dream 7B | Token-level noise 不均匀 | 根据邻近 clean token 动态调整 |
| TSC edit corruption | Seed Diffusion | Sampling artifacts | 加入 edit-based 数据增强 |
| Complementary masking | LLaDA 2.0 | Token 利用率低 | 确保每个 token 都参与学习 |
| Confidence-aware SFT | LLaDA 2.0 | 并行度受限 | 训练更 sharp 的预测 |
| Document-level mask | LLaDA 2.0 | 跨文档 spurious deps | 限制 attention 在文档边界内 |

---

### 类别④：混合架构

#### TiDAR — Think in Diffusion, Talk in Autoregression (NVIDIA, arXiv 2025.11)

**核心洞察**：dLLM 并行解码的质量下降来自 **token independence assumption**——同时预测的 k 个 token 互相独立，忽略了 token 间依赖。AR 不有这个问题（chain factorization）。

**TiDAR 的解决方案**：单模型内 AR + Diffusion 混合
- 一次 forward pass，序列分三部分：
  1. **Prefix**（已确定 token）：复用 KV cache
  2. **Proposed**（上步 diffusion 提出的候选）：用 AR mode 验证 + rejection sampling
  3. **Pre-drafted**（本步 diffusion 起草的新候选）：传给下一步验证

- **关键**：利用 "free token slots"（memory-bound 区间内，多放几个 token 不增加延迟）
- Diffusion mode 做并行起草（快但可能有误）
- AR mode 做顺序验证（慢但准确）
- 两者在同一个 forward pass 里通过 structured attention mask 实现

**训练**：
- 用 causal-bidirectional hybrid attention mask
- Diffusion section 全部设为 [MASK]（简化训练 + train-test consistency）
- AR loss + diffusion loss 联合训练

**结果**：
- TiDAR 1.5B: **lossless quality** vs AR, 4.71× throughput speedup
- TiDAR 8B: 5.91× throughput speedup, minimal quality loss
- 第一个 close AR quality gap 的架构

**好在哪**：
- **Lossless quality**——目前唯一达到 AR 质量的 dLLM 方案
- 不需要额外 drafter 模型（self-speculative）
- 利用 GPU 的 memory-bound 特性——"free compute"
- 支持 exact KV cache

**不足**：
- 本质上是 speculative decoding 的变体——实际并行度受限
- 需要从头训练 hybrid 模型
- 在 compute-bound 场景下优势减少
## 五、综合对比表

| 方案 | 类别 | 解决什么 | 需要训练? | 训练成本 | 核心优势 | 核心不足 |
|------|------|----------|-----------|----------|----------|----------|
| **CDLM** | 蒸馏加速 | 减少 denoising 步数 | ✅ 8-16h | 极低 | 3.6-14.5× 加速，几乎无损 | 上限受 teacher 限制 |
| **SPG** | RL 对齐 | log-likelihood 不可计算 | ✅ RL训练 | 中等 | 理论正确，Sudoku +27% | EUBO 估计有 bias |
| **LLaDA 2.0 DPO** | RL 对齐 | Preference optimization | ✅ DPO | 中等 | 第一个 dLLM DPO | 效果待大规模验证 |
| **Seed TSC** | 训练策略 | Sampling artifacts | ✅ 从头 | 高 | 消除 repetition，最快 dLLM | 需从头训练 |
| **Dream CART** | 训练策略 | Token-level noise 不均匀 | ✅ CPT | 中等 | 自适应 noise schedule | 全 bidir，无 KV cache |
| **Efficient-DLM tricks** | 训练策略 | Weight drift + train-test gap | ✅ CPT | 中等 | Clean context +9.46% | Block size 超参 |
| **LLaDA 2.0 SFT** | 训练策略 | Token 利用率 + 并行度 | ✅ SFT | 中等 | 最完整 post-training | 成本最高 |
| **TiDAR** | 混合架构 | Quality-speed trade-off | ✅ 从头 | 高 | Lossless quality, 5.91× speedup | 本质是 spec decoding |

---

## 六、关键洞察

### 洞察1：蒸馏是 dLLM 加速的最高效路径

CDLM 用 8-16 小时训练就实现了 3.6-14.5× 加速，而且几乎无损。相比之下：
- KV cache 方案（Elastic-Cache）虽然 training-free，但只解决计算效率，不减少步数
- 混合架构（TiDAR）需要从头训练
- **CDLM 的 cost-benefit 最优**

### 洞察2：dLLM 的 RL 是一个未被充分解决的问题

SPG 是第一个理论上正确的 dLLM RL 方法，但仍然有估计 bias。核心难点在于 log-likelihood 不可计算——这是 dLLM 相比 AR 的根本劣势之一。

**启示**：如果你的 linear state memory 能让 dLLM 的 denoising 更确定性（减少 stochastic 成分），可能也能让 log-likelihood 的估计更准确 → RL 更有效。

### 洞察3：训练策略的细节差异巨大

几乎每篇论文都有自己的训练技巧，且效果差距很大：
- Clean context 一个技巧就值 +9.46%（Efficient-DLM）
- Position-dependent masking 值 +4.38%
- Edit-based corruption 消除 sampling artifacts（Seed Diffusion）
- Complementary masking 提升 token 利用率（LLaDA 2.0）

**这些技巧大多可以互相组合**——目前没有一个方案用了所有技巧。

### 洞察4：TiDAR 揭示了一个根本性 trade-off

dLLM 并行解码的质量下降来自 token independence assumption。TiDAR 的解决方案是用 AR 做最终验证——但这本质上放弃了 dLLM 的并行性优势。

**更好的解决方案**：不用 AR 验证，而是用**跨步记忆**减少 token independence 的影响。如果 linear state 能保持 token 间的依赖信息跨步传递，就不需要 AR 验证也能保证质量。

### 洞察5：Block-wise 是所有高效 dLLM 的共同基础

从 CDLM 到 TiDAR 到 Efficient-DLM，所有追求效率的方案最终都走向 block-wise 结构。原因：
- 支持 KV cache（block 间 causal）
- 保留并行性（block 内 bidirectional）
- Train-test distribution 更容易对齐

**你的 linear state 应该直接在 block-wise 结构上工作**，而不是全 bidirectional。

---

## 七、与你的工作的关系

### 1. CDLM 的蒸馏框架可以直接复用
- 用 bidirectional dLLM 做 teacher
- 蒸馏到 block-causal student + **linear state augmentation**
- Consistency loss + distillation loss + DLM loss + **linear state loss**
- 一步完成：block-causal 转换 + 蒸馏加速 + 跨步记忆

### 2. SPG 的 RL 框架是 post-training 的自然下一步
- 先做 linear state augmentation（SFT 阶段）
- 再用 SPG 做 RL 对齐
- Linear state 可能减少 ELBO/EUBO gap → RL 更有效

### 3. 训练策略可以全部组合
- Clean context（Efficient-DLM）+ CART（Dream）+ edit corruption（Seed Diffusion）+ linear state
- 目前没有人试过这个组合

### 4. 对 TiDAR 的改进
- TiDAR 用 AR 做验证 → 你可以用 linear state 做隐式验证
- 如果 linear state 能保持足够的 token 间依赖信息 → 不需要 AR 验证也能保质量
- 这是比 TiDAR 更优雅的方案

---

## 八、参考文献

1-8: 见 AR→dLLM 调研报告

9. CDLM: Consistency Diffusion Language Models for Faster Sampling. arXiv:2511.19269, 2025.
10. Rashidinejad et al. "SPG: Sandwiched Policy Gradient for Masked Diffusion Language Models." arXiv:2510.09541, 2025.
11. Seed Diffusion Preview. "A Large-Scale Diffusion Language Model with High-Speed Inference." arXiv:2508.02193, 2025.
12. Dong et al. "TiDAR: Think in Diffusion, Talk in Autoregression." arXiv:2511.08923, 2025.

**补充参考：**
- LLaDA 2.0 (arXiv:2512.15745) — Post-training 部分
- ProSeCo (arXiv:2602.11590) — Self-correcting sampling
- MetaState (arXiv:2603.01331) — Persistent memory
