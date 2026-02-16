# Relaxing Positional Alignment: 用 CTC 解决 dLLM 位置对齐问题

**论文:** Relaxing Positional Alignment in Masked Diffusion Language Models  
**arXiv:** 2601.22947  
**关键词:** Positional alignment, CTC, Slack token, Robustness

---

## 1. 核心问题：位置对齐的脆弱性

MDLM 的一个隐藏问题：

> **一个位置的偏移就能严重破坏语义。**

```
正常:    [The] [capital] [of] [France] [is] [Paris]
偏移1位: [_] [The] [capital] [of] [France] [is]  → 语义崩溃
```

### 1.1 为什么会这样？

MDLM 训练时用 **严格的位置监督**：
- 位置 0 必须预测 token 0
- 位置 1 必须预测 token 1
- ...

但解码时是 **不可逆的**：
- 一旦某个位置 unmask 错了，无法修正
- 错误会传播到后续位置

**训练和解码的 mismatch！**

### 1.2 实验验证

论文做了 controlled intervention：

| 偏移量 | PPL 变化 |
|--------|----------|
| 0 | 12.3 (baseline) |
| 1 | 45.7 (+271%) |
| 2 | 89.2 (+625%) |

一个位置偏移，PPL 涨 3 倍！

---

## 2. 解决方案：CTC + Slack Token

### 2.1 核心思想

不要求严格的位置对齐，允许一定的 "松弛"。

引入特殊 token `<slack>`：
- 模型可以在任意位置输出 `<slack>`
- `<slack>` 在最终输出时被删除
- 相当于给模型 "喘息空间"

### 2.2 CTC 目标

用 Connectionist Temporal Classification (CTC) 替代严格的 cross-entropy：

$$\mathcal{L}_{CTC} = -\log \sum_{\pi \in \mathcal{B}^{-1}(y)} P(\pi | x)$$

其中 $\mathcal{B}^{-1}(y)$ 是所有能 collapse 到目标序列 $y$ 的路径。

**直觉：** 只要最终输出正确，中间的对齐方式不重要。

### 2.3 训练流程

```python
# 原始 MDLM 训练
loss = cross_entropy(model(masked_x), target, position_wise=True)

# CTC 训练
loss = ctc_loss(model(masked_x), target)  # 不要求严格位置对齐
```

---

## 3. 实验结果

### 3.1 生成质量

| Method | MAUVE ↑ | PPL ↓ | Diversity ↑ |
|--------|---------|-------|-------------|
| MDLM | 0.82 | 15.3 | 0.71 |
| + CTC | **0.89** | **13.1** | **0.78** |

### 3.2 位置鲁棒性

| 偏移量 | MDLM PPL | + CTC PPL |
|--------|----------|-----------|
| 0 | 12.3 | 11.8 |
| 1 | 45.7 | 14.2 |
| 2 | 89.2 | 18.5 |

**CTC 让模型对位置偏移更鲁棒！**

### 3.3 Slack Token 使用率

| 任务 | Slack 使用率 |
|------|-------------|
| 短文本 | 2.3% |
| 长文本 | 5.1% |
| 推理任务 | 8.7% |

推理任务用更多 slack，说明需要更多 "喘息空间"。

---

## 4. 深度分析

### 4.1 为什么 CTC 有效？

CTC 的核心：**允许多对一映射**。

```
模型输出: [The] [<slack>] [capital] [of] [France] [is] [Paris]
                  ↓ collapse
目标:      [The] [capital] [of] [France] [is] [Paris]
```

这给了模型灵活性：
- 不确定的位置可以输出 `<slack>`
- 后续位置可以 "补上"

### 4.2 与 WeDLM 的联系

WeDLM 解耦物理位置和逻辑位置。

CTC 方法是另一种解耦方式：
- WeDLM：显式解耦（两套位置编码）
- CTC：隐式解耦（允许 slack）

### 4.3 与 Ordering 研究的联系

位置对齐问题本质上是 **ordering 问题**：

- 严格对齐 = 固定 ordering
- CTC = 灵活 ordering

**启发：** Optimal ordering 可能需要 "松弛" 的位置约束。

---

## 5. 对 dLLM 研究的启发

### 5.1 位置编码需要重新思考

当前 dLLM 继承了 AR 模型的位置编码，但：
- AR 是顺序生成，位置天然对齐
- dLLM 是并行生成，位置可能不对齐

**需要专门为 dLLM 设计的位置编码。**

### 5.2 训练-解码一致性

这篇论文揭示了训练和解码的 mismatch。

类似的 mismatch 可能还有：
- Mask ratio 的 mismatch
- Noise schedule 的 mismatch
- Token dependency 的 mismatch

### 5.3 研究方向

**Idea: Soft Position Encoding**

不用离散的位置，用连续的位置：

$$PE(i) = \text{soft\_position}(i, \text{context})$$

位置可以根据 context 动态调整。

---

## 6. 总结

| 贡献 | 内容 |
|------|------|
| 问题发现 | 位置偏移严重影响 MDLM |
| 解决方案 | CTC + Slack token |
| 效果 | 生成质量提升，鲁棒性增强 |
| 启发 | 位置编码需要为 dLLM 重新设计 |

---

## 参考

- arXiv:2601.22947
- CTC (Graves et al., 2006)
