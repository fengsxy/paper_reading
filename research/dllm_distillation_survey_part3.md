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
