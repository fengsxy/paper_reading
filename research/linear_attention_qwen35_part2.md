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
