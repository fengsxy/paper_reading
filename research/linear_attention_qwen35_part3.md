## 四、Chunk Algorithm：如何并行训练 Linear Attention

Recurrent 模式每次只处理一个 token（O(n) 步，串行），训练时太慢。Chunk algorithm 把序列切成大小为 C（默认 64）的块，块内并行计算。

**核心思路**：每个 chunk 内部用矩阵运算并行处理，chunk 之间传递状态。

每个 chunk 的计算分两部分：
1. **Intra-chunk**（块内）：chunk 内部的 token 之间的注意力，用带衰减 mask 的矩阵乘法
2. **Inter-chunk**（块间）：从上一个 chunk 传来的状态 S 对当前 chunk 的贡献

```python
# 块内衰减 mask（下三角）
L[j,k] = exp(G[j] - G[k])  for j ≥ k, else 0

# WY 分解处理 delta rule 的累积效应
A = -(k_β @ k^T * L)  # masked upper triangle
v_corrected = (I + A) @ (v * β)  # forward substitution

# 块间状态更新
S_i = decay * S_{i-1} + k^T @ v_corrected

# 输出 = 块间贡献 + 块内贡献
o_inter = q * exp(G) @ S_{i-1}    # 从历史状态读取
o_intra = (q @ k^T * L) @ v_new   # 块内注意力
o = o_inter + o_intra
```

复杂度：O(n · C · d²)，序列长度线性。C=64 时，和 recurrent 模式相比并行度提升 64 倍。

---

## 五、各种 Linear Attention 变体对比

| 模型 | 状态更新规则 | 遗忘 | 精确修正 | 用在哪 |
|------|-------------|------|----------|--------|
| **Vanilla Linear** | S += k⊗v | ❌ | ❌ | 早期研究 |
| **RetNet** | S = γ·S + k⊗v | ✅ 固定衰减 | ❌ | 微软 RetNet |
| **GLA** | S = diag(G)·S + k⊗v | ✅ 数据相关 | ❌ | GLA 系列 |
| **Mamba (S6)** | h = Āh + B̄x | ✅ 选择性 | ❌ | Jamba, Falcon |
| **Mamba2 (SSD)** | h = Āh + B̄x | ✅ 结构化 | ❌ | Mamba-2 |
| **DeltaNet** | S += k⊗β(v − S^Tk) | ❌ | ✅ | DeltaNet |
| **Gated DeltaNet** | S = g·S + k⊗β(v − gS^Tk) | ✅ 数据相关 | ✅ | **Qwen3.5** |
| **RWKV-6** | h = diag(w)·h + k⊗v | ✅ 通道级 | ❌ | RWKV |

**Gated DeltaNet 是目前唯一同时具备遗忘和精确修正能力的线性注意力机制。** 这就是为什么 Qwen3.5 选择了它。

---

## 六、为什么 Gated DeltaNet 适合 dLLM？

回到你正在做的 dLLM 研究，Gated DeltaNet 作为 MetaState 的 Updater 替代方案有几个天然优势：

### 1. 精确修正 ≈ Denoising 的自然语义

dLLM 的 denoising 过程本质上就是"修正错误预测"：
- 早期步骤：大量 masked token，需要大量写入（高 β）
- 晚期步骤：大部分已揭示，只需要小幅修正（低 β，精确 delta）
- Delta rule 的"先查询旧预测，再修正差异"与 denoising 的语义完美对应

### 2. 遗忘门 ≈ 信息更新的自然机制

每步 denoising 后，一些 token 从 [MASK] 变成具体 token——之前关于这些位置的"猜测"应该被遗忘，替换为确定信息。Gated DeltaNet 的 g_t 控制遗忘，β_t 控制写入——天然适合这个过程。

### 3. 固定大小状态 ≈ 高效跨步记忆

MetaState 的 GRU 状态是 d 维向量。Gated DeltaNet 的状态是 d_k × d_v 矩阵——信息容量大得多（128×128 = 16384 维 vs GRU 的几百维）。

### 4. 可并行训练

MetaState 用 GRU 做 K-step unrolling 训练时，GRU 是严格串行的。Gated DeltaNet 有 chunk algorithm——K 步可以并行展开，训练速度大幅提升。

---

## 七、参考文献

1. Yang et al. "Gated Delta Networks: Improving Mamba2 with Delta Rule." ICLR 2025. arXiv:2412.06464.
2. Katharopoulos et al. "Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention." ICML 2020.
3. Sun et al. "Retentive Network: A Successor to Transformer for Large Language Models." arXiv:2307.08621, 2023.
4. Yang et al. "Gated Linear Attention Transformers with Hardware-Efficient Training." ICML 2024.
5. Yang et al. "Parallelizing Linear Transformers with the Delta Rule over Sequence Length." NeurIPS 2024. arXiv:2406.06484.
6. Gu & Dao. "Mamba: Linear-Time Sequence Modeling with Selective State Spaces." ICLR 2024.
7. Dao & Gu. "Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality." ICML 2024.
8. Qwen Team. "Qwen3.5: Scaling Hybrid Attention to 397B Parameters." 2026.
9. Zhang et al. "Kimi Linear: An Expressive, Efficient Attention Architecture (KDA)." arXiv:2510.26692, 2025.
10. justinchuby. "Qwen3.5 Gated DeltaNet Analysis for ONNX." GitHub Gist, 2026.
