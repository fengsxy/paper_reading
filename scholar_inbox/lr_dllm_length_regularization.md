# LR-DLLM: 解决变长生成的长度偏差问题

**论文:** Improving Variable-Length Generation in Diffusion Language Models via Length Regularization  
**arXiv:** 2602.07546  
**关键词:** Variable-length, Length bias, Confidence calibration, Infilling

---

## 1. 核心问题：dLLM 不擅长变长生成

dLLM 的推理在 **固定长度 canvas** 上进行，隐式假设目标长度已知。

但现实任务（completion, infilling）长度未知：

```
Prompt: "def fibonacci(n):"
Canvas: [MASK] × 50  ← 假设 50 tokens

问题：
- 如果真实答案只需要 30 tokens？→ 生成冗余内容
- 如果真实答案需要 80 tokens？→ 生成不完整
```

### 1.1 长度偏差

论文发现：**不同长度的 confidence 不可比！**

```
Length 30: confidence = 0.85
Length 50: confidence = 0.72
Length 80: confidence = 0.65

直觉上选 30？错！
长度越短，confidence 天然越高（更少的 token 要预测）
```

这导致 dLLM 系统性地 **under-generate**。

---

## 2. 方法：Length Regularization

### 2.1 核心思想

把生成长度作为 **显式变量**，校正长度引起的 confidence 偏差。

$$\text{Score}(x, L) = \text{Confidence}(x, L) - \lambda \cdot \text{LengthBias}(L)$$

### 2.2 Length Bias 估计

通过统计分析估计不同长度的 baseline confidence：

$$\text{LengthBias}(L) = \mathbb{E}[\text{Confidence} | \text{Length} = L]$$

### 2.3 动态长度调整

```python
class LRDLLM:
    def generate(self, prompt, max_length):
        best_score = -inf
        best_output = None
        
        for L in range(1, max_length):
            # 在长度 L 的 canvas 上生成
            output, confidence = self.dllm.generate(prompt, length=L)
            
            # 校正 confidence
            score = confidence - self.length_bias[L]
            
            if score > best_score:
                best_score = score
                best_output = output
        
        return best_output
```

---

## 3. 实验结果

### 3.1 Code Infilling

| Method | HumanEval-Infill | McEval (4 langs) |
|--------|------------------|------------------|
| DreamOn | 37.9% | 37.2% |
| **LR-DLLM** | **51.3%** | **51.5%** |
| Improvement | +13.4% | +14.3% |

### 3.2 长度预测准确性

| Method | Length MAE |
|--------|------------|
| Fixed length | 15.3 |
| Confidence-based | 8.7 |
| **LR-DLLM** | **3.2** |

LR-DLLM 的长度预测更准确。

---

## 4. 深度分析

### 4.1 为什么存在长度偏差？

**数学解释：**

$$\text{Confidence}(L) = \prod_{i=1}^{L} P(x_i | x_{<i})$$

长度越长，乘积越小 → confidence 越低。

这是 **intrinsic bias**，不是模型问题。

### 4.2 与 Ordering 的联系

长度选择本质上是一种 **宏观 ordering**：
- 先决定生成多少 token
- 再决定每个 token 是什么

LR-DLLM 解决了第一个问题。

### 4.3 研究方向

**Idea: 联合优化长度和内容**

不是先选长度再生成，而是联合优化：

$$\max_{L, x} P(x | L) \cdot P(L)$$

---

## 5. 总结

| 贡献 | 内容 |
|------|------|
| 问题 | dLLM 的 confidence 有长度偏差 |
| 方法 | 显式建模长度，校正偏差 |
| 效果 | Infilling +13-14% |

**核心启发：** dLLM 的 confidence 不能直接比较，需要校正各种 bias。

---

## 参考

- arXiv:2602.07546
