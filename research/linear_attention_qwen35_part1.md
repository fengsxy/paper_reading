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
