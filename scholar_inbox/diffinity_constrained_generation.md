# Diffinity: 让 dLLM 遵守正则表达式约束

**论文:** Continuous Diffusion Models Can Obey Formal Syntax  
**arXiv:** 2602.12468  
**关键词:** Constrained generation, Regular expressions, Training-free guidance, JSON

---

## 1. 核心问题：dLLM 难以满足硬约束

dLLM 的连续 latent dynamics 使得离散约束难以施加：

```
约束: 输出必须是合法 JSON
dLLM: 在连续空间 denoise，不保证离散约束
```

AR 模型可以用 constrained decoding（每步只选合法 token），但 dLLM 是并行生成，不能直接套用。

---

## 2. 方法：Analytic Score Guidance

### 2.1 核心思想

构造一个 **analytic score**，估计当前 latent state 解码为合法字符串的概率，用其梯度引导采样。

$$\nabla_x \log P(\text{valid} | x)$$

### 2.2 正则表达式约束

用正则表达式表达约束（JSON schema 可以转换为正则）：

```
JSON: {"name": string, "age": number}
Regex: \{"name":\s*"[^"]*",\s*"age":\s*\d+\}
```

### 2.3 Score 计算

对于正则表达式 $R$，构造 DFA，计算：

$$P(\text{valid} | x) = \sum_{\text{path in DFA}} P(\text{path} | x)$$

这是可微的，可以计算梯度。

---

## 3. 实验结果

| Benchmark | Constraint Satisfaction | PPL Cost |
|-----------|------------------------|----------|
| JSON (simple) | 96% | +0.3 |
| JSON (complex) | 82% | +0.8 |
| Natural language | 68% | +1.2 |

### 对比 AR Constrained Decoding

| | AR | Diffinity |
|---|---|---|
| Constraint Satisfaction | 72% | 82% |
| Output Quality (PPL) | 15.2 | 14.8 |

Diffinity 在约束满足和输出质量上都更好！

---

## 4. 深度分析

### 4.1 为什么 dLLM 更适合约束生成？

AR 的 constrained decoding 是 **greedy** 的：
- 每步只看当前 token
- 可能走进死胡同

dLLM 是 **global** 的：
- 同时考虑所有位置
- 可以全局优化约束满足

### 4.2 与 Ordering 的联系

约束生成可以指导 ordering：
- 约束相关的 token 应该先生成（确保满足约束）
- 自由的 token 后生成（填充细节）

### 4.3 研究方向

**Idea: 约束感知的 Ordering**

```python
def constraint_aware_ordering(constraint, positions):
    # 分析哪些位置受约束影响
    constrained_positions = analyze_constraint(constraint, positions)
    
    # 先生成受约束的位置
    ordering = constrained_positions + free_positions
    return ordering
```

---

## 5. 总结

| 贡献 | 内容 |
|------|------|
| 问题 | dLLM 难以满足离散约束 |
| 方法 | Analytic score guidance |
| 效果 | 68-96% 约束满足，质量保持 |

**核心启发：** dLLM 的 global generation 是约束生成的优势，应该充分利用。

---

## 参考

- arXiv:2602.12468
- PLAID diffusion model
