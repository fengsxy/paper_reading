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
