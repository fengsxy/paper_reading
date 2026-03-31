### 类别⑤：混合架构（两者兼顾）

#### Block Diffusion / BD3-LM (ICLR 2025 Oral)

**核心洞察**：纯 dLLM 无法用 KV cache（双向注意力），纯 AR 无法并行。把序列分成 block，block 间 AR、block 内 diffusion，就能两全。

**方法**：
- 序列分成固定大小的 block
- Block 间：自回归地从左到右生成（前一个 block 作为 context）
- Block 内：masked diffusion 并行去噪
- 前面 block 的 KV 可以直接 cache（已完全 decode，不会再变）

**好在哪**：
- KV cache 自然可用（block 间是因果的）
- 支持任意长度生成（不再需要固定序列长度）
- 在 language modeling benchmark 上 SOTA（diffusion 模型中）
- 错误不会跨 block 传播（每个 block 独立 denoise）

**不足**：
- Block 内仍然有标准 dLLM 的两个问题
- Block 边界处的连贯性依赖 AR 的上下文传递
- Block 大小是超参数，影响 speed-quality trade-off

---

#### Gated DeltaNet (ICLR 2025) — 作为 MetaState Updater 的替代

**这不是 dLLM 论文**，但它是你方案的核心组件。

**核心思想**：结合 gating（自适应遗忘）和 delta rule（精确记忆修改），得到一个线性时间的序列模型。

**Delta Rule 更新**：
```
S_t = (1 - β_t * k_t * k_t^T) * S_{t-1} + β_t * v_t * k_t^T
```
- β_t: 学习率（学习的）
- k_t: key（要写入的地址）
- v_t: value（要写入的内容）
- 先"擦除"旧的 k_t 对应的记忆，再写入新的 v_t

**加上 Gating**：
```
S_t = α_t ⊙ S_{t-1} + β_t * v_t * k_t^T
```
- α_t: 遗忘门（scalar 或 channel-wise）
- 控制保留多少旧记忆

**为什么适合替代 GRU**：
1. **可并行**：chunk-wise 并行算法，O(L) 但高度 GPU 友好
2. **精确记忆修改**：delta rule 的 "擦除-写入" 比 GRU 的 "混合" 更精确
3. **已在大规模验证**：Qwen3.5 用 Gated DeltaNet 做 3:1 hybrid（3层 GDN : 1层 full attention）
4. **信息容量更大**：state 是 d×d 矩阵（vs GRU 的 d 向量）

**Kimi Linear (KDA)** 进一步改进：scalar gate → channel-wise gate，每个特征维度独立遗忘。
