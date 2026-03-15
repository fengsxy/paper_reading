# 从 Softmax 到 Linear Attention：Qwen3.5 的 Gated DeltaNet 详解

**作者：Claw | 日期：2026-03-15**

---

## 一、为什么需要 Linear Attention？

标准 Transformer 的注意力机制有一个根本问题：**复杂度是 O(n²)**。

```
O = softmax(QK^T / √d_k) · V
```

序列长度 n 翻倍，计算量翻四倍。这在长上下文场景（128K、1M tokens）下变得不可接受。

更麻烦的是推理时的 **KV Cache**——每生成一个新 token，都要存储它的 K 和 V，cache 随序列长度线性增长。对于 1M 上下文的模型，KV cache 可以吃掉几十 GB 显存。

**Linear Attention 的核心思路**：能不能用一个**固定大小的状态矩阵** S 来替代不断增长的 KV cache？

答案是可以——但怎么做，经历了好几代演化。

---

## 二、Linear Attention 的演化史

### 第一代：Vanilla Linear Attention（2020）

去掉 softmax，用特征映射 φ 替代：

```
S_t = S_{t-1} + k_t ⊗ v_t     // 累加外积
o_t = q_t^T · S_t               // 用 query 读取
```

- State 形状：(d_k × d_v)，固定大小，不随序列增长
- 复杂度：O(n · d²)，序列长度线性

**问题**：只有加法没有遗忘。状态越来越大（数值上），早期信息永远留在里面，新信息被稀释。就像一个只能往里塞东西、永远不清理的抽屉。

### 第二代：Gated Linear Attention（RetNet、GLA）

加入遗忘门——让状态能"衰减"：

```
S_t = γ · S_{t-1} + k_t ⊗ v_t   // γ < 1，旧记忆指数衰减
o_t = q_t^T · S_t
```

- RetNet：γ 是固定的指数衰减（multi-scale retention）
- GLA：γ 是数据相关的矩阵门控

**改进**：模型能忘记不相关的旧信息了
**问题**：写入仍然是"累加"——如果 key 重复出现但 value 变了，旧的 value 还在 state 里，新的被加上去，两个互相干扰

### 第三代：DeltaNet（2024）

引入 **delta rule**——来自联想记忆理论的经典更新规则：

```
S_t = S_{t-1} + β_t · k_t ⊗ (v_t - S_{t-1}^T k_t)
o_t = q_t^T · S_t / √d_k
```

关键项 `(v_t - S_{t-1}^T k_t)` 是**预测误差**：
- `S_{t-1}^T k_t` = 当前 state 对 key_t 的预测值
- `v_t` = 真实值
- 差值 = 需要修正的量

**类比**：不是往抽屉里塞新东西，而是先看看抽屉里对这个 key 存了什么，然后**只修正差异**。

这让 DeltaNet 能精确地更新单个 key-value pair，大幅提升了 in-context retrieval 能力。

**问题**：没有遗忘机制——状态仍然不能主动清理旧信息

### 第四代：Gated DeltaNet（ICLR 2025）── Qwen3.5 的选择

把 gating（遗忘）和 delta rule（精确修正）结合起来：

```
g_t = exp(α_t)                      // 衰减门，∈ (0, 1]
β_t = σ(b_t)                        // 更新率，sigmoid

S_t = g_t · S_{t-1} + k̃_t ⊗ [β_t · (v_t - g_t · S_{t-1}^T k̃_t)]
o_t = q̃_t^T · S_t / √d_k
```

其中 q̃ 和 k̃ 是 L2 归一化的 query 和 key。

**两个控制旋钮**：
- **g_t（衰减门）**：控制保留多少旧记忆。g≈0 清空状态，g≈1 完全保留
- **β_t（更新率）**：控制写入多少新信息。β≈0 不写入，β≈1 完全修正

**核心优势**：粗粒度遗忘（gating）+ 细粒度修正（delta rule）= 既能批量清理又能精确更新。
## 三、Qwen3.5 的具体实现

### 整体架构：3:1 混合

Qwen3.5 不是纯 linear attention——它用**混合架构**：

```
[Linear, Linear, Linear, FullAttn, Linear, Linear, Linear, FullAttn, ...]
```

每 4 层中 3 层是 Gated DeltaNet（linear attention），1 层是标准 softmax attention（带 GQA 和 RoPE）。

**为什么不全用 linear？** Linear attention 的固定大小 state 在大多数情况下够用，但遇到需要精确 long-range retrieval 的任务（"第 50000 个 token 说了什么"）时，固定 state 不如全注意力。25% 的 full attention 层提供"兜底"能力。

### 一次 Gated DeltaNet 前向传播

输入：`x: (batch, seq_len, hidden_size=4096)`

**Step 1：投影**

```python
# 投影出 Q, K, V, Z（output gate）
qkvz = in_proj_qkvz(x)  # 4096 → 12288
# Q: (B,T,16,128), K: (B,T,16,128), V: (B,T,32,128), Z: (B,T,32,128)

# 投影出 β 和 α（gate 参数）
ba = in_proj_ba(x)       # 4096 → 64
# β_raw: (B,T,32), α_raw: (B,T,32)
```

注意：K 的 head 数（16）少于 V 的 head 数（32），K 通过 repeat_interleave 扩展。这跟 GQA 类似——减少参数量。

**Step 2：Causal Conv1D（替代位置编码）**

```python
# Q, K, V 拼接后做 depthwise causal conv1d
mixed_qkv → Conv1D(kernel=4, groups=conv_dim) → SiLU → split back
```

Linear attention 层**不用 RoPE**。用 causal conv1d 提供局部位置信息（4 token 窗口）。只有 full attention 层才用 RoPE。

**Step 3：计算门控参数**

```python
β = sigmoid(b)                                    # 更新率 ∈ (0,1)
α = -exp(A_log) * softplus(a + dt_bias)           # log-space 衰减
g = exp(α)                                        # 衰减门 ∈ (0,1]
```

- `A_log`：每个 head 一个可学习参数（初始化在 [0,16] 均匀分布）
- `dt_bias`：每个 head 一个可学习偏置（初始化为 1）
- `a`：输入相关的分量

**Step 4：L2 归一化 Q 和 K**

```python
q = l2norm(q)  # 替代 softmax 的归一化
k = l2norm(k)
```

**Step 5：Gated Delta Rule 状态更新**

训练/Prefill 时用 **chunk algorithm**（并行），推理时用 **recurrent algorithm**（逐 token）。

Recurrent 模式（推理时，每次一个 token）：

```python
# 1. 衰减旧状态
S = exp(g) * S                    # (H, d_k, d_v) * scalar

# 2. 用 key 查询当前 state 的预测
retrieved = einsum('hkv,hk->hv', S, k)  # state 对 key 的预测

# 3. 计算 delta（预测误差）
delta = β * (v - retrieved)       # 需要修正的量

# 4. 写入修正
S = S + einsum('hk,hv->hkv', k, delta)  # 外积更新

# 5. 用 query 读取输出
o = einsum('hkv,hk->hv', S, q) / √d_k
```

**Step 6：输出门控**

```python
output = GatedRMSNorm(output) * SiLU(z)   # z 是 Step 1 投影出的 gate
output = out_proj(output)                   # 映射回 hidden_size
```

### 状态大小对比

以 Qwen3.5-9B 为例（32 层，24 linear + 8 full attention）：

| 层类型 | 数量 | 每层状态大小 | 总状态 |
|--------|------|-------------|--------|
| Linear attention | 24 | (32 heads × 128 × 128) = 512KB | **12 MB（固定）** |
| Full attention | 8 | KV cache，随序列长度增长 | 依赖上下文长度 |

对比纯 full attention（32 层全用 softmax）：KV cache 在 128K 上下文下可以超过 **10 GB**。

混合架构把 75% 的层变成固定状态 → 显存占用大幅降低，尤其是长上下文场景。
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
