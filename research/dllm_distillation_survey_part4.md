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
