## 四、各类方案详细分析

### 类别①：全双向转换

#### DiffuLLaMA (ICLR 2025)

**核心发现**：AR 和 diffusion 的 loss 在特定 masking schedule 下**精确数学等价**——不是近似。这是 AR→dLLM 转换可行的理论基础。

**三个关键技术**：
1. **Attention Mask Annealing**：不是简单 linear interpolation，而是 log-space 分阶段退火。先 anneal 对角线附近（局部），再扩展到远处（全局）。前 10% steps 保持纯 causal，最后 10% 完全 bidirectional。
2. **Shift Operation**：保留 AR 的 position i 预测 token i+1 模式（不改为预测 token i），最大化保留权重分布。
3. **Time-Embedding-Free**：不加 time embedding 反而更好——基于 RADD 的发现：absorbing diffusion 的 concrete score 与时间无关。

**实验细节**：
- DiffuGPT-127M 转换后**超越了 GPT2-127M**（AR→diffusion 后变好了！）
- DiffuLLaMA-7B 在 commonsense reasoning 上接近 LLaMA2-7B
- 但 GSM8K 差距明显（reasoning 最难转换）
- 训练成本：~200B tokens（AR 预训练的 10%）
- 从 AR 的 final LR 开始训练（不重新 warmup）

**好在哪**：第一个系统性证明 AR→dLLM 可行，有严格的数学基础

**不足**：全 bidirectional → 无 KV cache → 推理慢；200B tokens 仍不算便宜

---

#### Dream 7B (HKU, arXiv 2025.08)

**核心创新是 CART（Context-Adaptive Token-Level Noise Rescheduling）**：
- 标准训练：所有 masked token 共享一个全局 noise level → suboptimal
- CART：根据每个 masked token 周围的 clean token 数量，用 geometric distribution 动态调整其 effective noise level
- 近处的 clean token 贡献大 → 该 masked token 的 effective noise 应更低
- 公式：w(t, x_t, n) = 1/2 * Σ 1[x_t^i ≠ MASK] * Geo(p, |n-i|-1)

**关键数据**：
- 只用 0.6T tokens（LLaDA 的 1/4），就全面超越 LLaDA-8B → AR 初始化极其有效
- Planning 任务碾压式优势：Sudoku 81.0 vs Qwen2.5 的 21.0（4倍！）
- Trip planning 17.8 vs Qwen2.5 的 3.6（5倍！）
- **Planning 优势是 dLLM 范式的固有优势**：能同时看到整个序列，做全局规划而非贪心

**不足**：全 bidirectional → 无 KV cache；与 AR 原版在 reasoning 上仍有差距

---

#### RND1 (Radical Numerics, arXiv 2025.10)

**最简单的方案**：直接切 causal → bidirectional，不用 annealing。

**关键发现**：Layer-specific learning rates 是关键
- Dense layers（attention/FFN）用低 LR → 防止 catastrophic forgetting
- 新增的 diffusion-specific layers 用高 LR → 快速学习
- 约束 dense layers 的更新幅度 → 保留知识密集型能力

**规模**：30B MoE（3B active），从 Qwen3-30B-A3B 转换。发布时最大开源 base DLM。

**不足**：全 bidirectional → 无 KV cache

---

### 类别②：块级混合转换

#### Efficient-DLM (NVIDIA Song Han 组, arXiv 2025.12)

**Table 1 是全文最重要的实验**（Abstract 里完全看不到）：

| 方案 | 12-task 平均 |
|------|-------------|
| Full bidir + shift | 18.10（崩溃）|
| Full bidir - shift | 19.29（仍崩）|
| Block-wise + noisy context + shift | 28.23 |
| Block-wise + **clean context** + shift | 37.69 |
| Block-wise + **clean context** - shift | **38.41**（最优）|

**三个关键发现**：

1. **Clean context 比 noisy context 重要 9.46%**——block-wise 训练时，已解码的 block 应该用 clean token 作为 context（不加噪声）。这是全文最大的单一改进。

2. **Block-wise 下不需要 token shift**——跟 DiffuLLaMA 的结论相反！原因：block-wise + clean context 已足够保留权重分布，shift 反而增加任务难度。

3. **Position-Dependent Token Masking**：
   - 训练时 uniform masking vs 推理时 block-wise 从左到右 → train-test mismatch
   - 解决：w_i(t) = exp[β(1-t)i]，后面位置更高 mask 概率
   - 在高并行度（TPF=5.6）下提升 4.38%

**Weight Drift 可视化（Figure 2e）**：
- Full bidir: attention 层和 FFN 层 drift 都大
- Block-wise + clean context: **两者都小** → 定量证明权重分布保留最好

**训练动态**：10B tokens 够基本转换，50B 不错，100B 最优

**最终结果（8B）**：比 Dream 7B 高 +5.4% accuracy，4.5× throughput

---

#### SDAR (上海AI Lab, arXiv 2025.10)

**最重要的实验（Section 4）**：同架构(2B)、同数据(1T)、同超参公平对比 AR vs MDLM
- AR-2B-Chat 在几乎所有 benchmark 上大幅超越 MDLM-2B-Chat
- 原因：AR 直接优化 NLL，每个 token 都参与梯度；MDLM 优化 NELBO（loose bound），只有 masked tokens 参与 loss
- **结论：AR 训练效率远高于 MDLM → 先训 AR 再转换是正确路线**

**转换极其轻量**：
- 只用 30-50B tokens（预训练的 3-5%，比 DiffuLLaMA 便宜 4-7 倍）
- 不需要 annealing、不需要 shift、不需要原始预训练数据
- 直接做 block-wise 适配

**规模最大**：1.7B, 4B, 8B (dense) + 30B MoE

**关键结果**：SDAR-30B-A3B-Sci 在 GPQA、ChemBench 上**超越 AR 原版** → diffusion 的 iterative refinement 确实提供了 AR 没有的推理能力

**与 Efficient-DLM 的区别**：
- SDAR 不用 clean context（训练时 context 是 noisy 的）
- SDAR 不用 position-dependent masking
- 更便宜但 accuracy 可能不如 Efficient-DLM
- **两者可以结合：SDAR 的低成本 + Efficient-DLM 的 clean context 和 pos-dep masking**
