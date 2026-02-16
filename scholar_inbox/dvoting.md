# dVoting: 不需要训练的 dLLM 推理加速

**论文:** dVoting: Fast Voting for dLLMs  
**arXiv:** 2602.12153  
**作者:** Sicheng Feng, Zigeng Chen, Xinyin Ma, Gongfan Fang, Xinchao Wang  
**代码:** https://github.com/fscdc/dVoting  
**关键词:** Voting, Test-time scaling, Training-free, Consistency analysis

---

## 1. 核心观察：Not All Tokens Are Equal

dVoting 的出发点是一个关键观察：

> **多次采样同一个 prompt，大部分 token 预测是一致的，只有少数 token 有变化。**

```
Sample 1: The answer is [42] because [2+2=4] and [...]
Sample 2: The answer is [42] because [2+2=4] and [...]
Sample 3: The answer is [43] because [2+2=4] and [...]
                         ^^
                    这个 token 不一致！
```

**关键洞察：**
- 一致的 token → 模型很确定 → 不需要改
- 不一致的 token → 模型不确定 → 决定最终性能

---

## 2. 方法：Iterative Voting Refinement

### 2.1 算法流程

```
输入: Prompt
输出: Refined response

1. 采样 K 个 responses
2. 分析 token-level consistency
3. 识别 uncertain tokens（跨样本不一致的）
4. 对 uncertain tokens 进行 voting + regeneration
5. 重复直到收敛
```

### 2.2 Consistency Analysis

对于每个位置 $i$，计算跨样本的一致性：

$$\text{Consistency}(i) = \frac{\max_t \text{count}(t, i)}{K}$$

其中 $\text{count}(t, i)$ 是位置 $i$ 预测为 token $t$ 的次数。

- Consistency 高 → 模型确定 → 保留
- Consistency 低 → 模型不确定 → 需要 refine

### 2.3 Voting + Regeneration

对于 uncertain tokens：

1. **Voting:** 选择出现次数最多的 token
2. **Regeneration:** 固定其他 tokens，重新生成 uncertain tokens
3. **迭代:** 重复直到所有 tokens 都 consistent

```python
def dvoting(model, prompt, K=5, threshold=0.8):
    # Step 1: Sample K responses
    samples = [model.generate(prompt) for _ in range(K)]
    
    # Step 2: Analyze consistency
    while True:
        consistency = compute_consistency(samples)
        uncertain_positions = [i for i, c in enumerate(consistency) if c < threshold]
        
        if len(uncertain_positions) == 0:
            break  # Converged
        
        # Step 3: Vote for uncertain tokens
        voted_tokens = vote(samples, uncertain_positions)
        
        # Step 4: Regenerate with voted tokens as context
        for i in range(K):
            samples[i] = model.regenerate(
                samples[i], 
                fixed_positions=certain_positions,
                regenerate_positions=uncertain_positions
            )
    
    return majority_vote(samples)
```

---

## 3. 为什么 dLLM 特别适合这个方法？

### 3.1 AR vs dLLM

| | AR | dLLM |
|---|---|---|
| 重新生成部分 tokens | 需要从头生成 | 可以只生成指定位置 |
| 计算开销 | O(n) per regeneration | O(1) per regeneration |
| 并行性 | 无 | 可以并行生成多个位置 |

**dLLM 的 arbitrary-position generation 是 dVoting 的关键 enabler！**

### 3.2 与 Self-Consistency 的区别

传统 Self-Consistency（AR 模型）：
```
1. 采样 K 个完整 responses
2. 对最终答案 voting
3. 选择出现最多的答案
```

dVoting：
```
1. 采样 K 个 responses
2. 对每个 token 位置 voting
3. 只重新生成 uncertain tokens
4. 迭代 refine
```

**dVoting 更细粒度，更高效。**

---

## 4. 实验结果

### 4.1 主要结果

| Benchmark | Baseline | + dVoting | Improvement |
|-----------|----------|-----------|-------------|
| GSM8K | 68.2% | 75.9% | +7.66% |
| MATH500 | 52.1% | 59.3% | +7.20% |
| ARC-C | 71.3% | 86.1% | +14.84% |
| MMLU | 62.4% | 68.1% | +5.74% |

**ARC-C 上提升 14.84%！**

### 4.2 计算开销

| Method | Relative Time | Improvement |
|--------|---------------|-------------|
| Baseline | 1x | - |
| Self-Consistency (K=5) | 5x | +3.2% |
| **dVoting (K=5)** | **2.3x** | **+7.2%** |

dVoting 比 Self-Consistency 更高效：
- 时间开销更少（2.3x vs 5x）
- 性能提升更大（+7.2% vs +3.2%）

### 4.3 收敛分析

| Iteration | Uncertain Tokens | Accuracy |
|-----------|------------------|----------|
| 0 | 15.2% | 52.1% |
| 1 | 8.3% | 56.4% |
| 2 | 3.1% | 58.7% |
| 3 | 0.8% | 59.3% |

通常 2-3 轮迭代就收敛。

---

## 5. 深度分析

### 5.1 哪些 Tokens 是 Uncertain 的？

论文分析了 uncertain tokens 的分布：

| Token 类型 | Uncertain 比例 |
|-----------|---------------|
| 数字 | 32% |
| 运算符 | 18% |
| 关键词 | 25% |
| 填充词 | 5% |
| 其他 | 20% |

**数字和关键词最容易 uncertain！**

这和直觉一致：
- "The answer is **42**" 中的 42 是关键
- "because **2+2=4**" 中的运算是关键

### 5.2 与 "Not All Tokens Are Equal" 的联系

dVoting 的核心假设和你之前的思考一致：

> **模型一次 forward pass 的信息量 >> 一个 token**

dVoting 利用这个特性：
- 大部分 tokens 一次就能确定
- 只有少数 uncertain tokens 需要额外计算

### 5.3 为什么 Voting 有效？

**假设：** 模型的错误是 **随机的**，不是 **系统性的**。

如果错误是随机的：
- 多次采样，正确答案出现概率更高
- Voting 可以 "平均掉" 随机错误

这和 Hot Mess Theory 的发现一致：模型的 variance 比 bias 更大。

---

## 6. 对 dLLM 研究的启发

### 6.1 Token-Level Analysis 的价值

dVoting 证明了 token-level 分析的价值：

- 不是所有 tokens 都需要同等对待
- Uncertain tokens 决定性能
- 可以针对性地优化 uncertain tokens

### 6.2 与 Ordering 研究的联系

dVoting 的 uncertain tokens ≈ 应该后生成的 tokens？

**假设：**
- Uncertain tokens = 难预测的 tokens = 应该后生成
- Consistent tokens = 容易预测的 tokens = 应该先生成

这和 difficulty-based ordering 的思想一致！

### 6.3 具体研究方向

**Idea 1: Uncertainty-Guided Ordering**

用 dVoting 的 consistency 分析指导 ordering：

```python
def uncertainty_guided_ordering(model, prompt, K=5):
    # 采样分析 uncertainty
    samples = [model.generate(prompt) for _ in range(K)]
    consistency = compute_consistency(samples)
    
    # 按 consistency 从高到低排序
    # 先生成 consistent tokens，后生成 uncertain tokens
    ordering = sorted(range(len(consistency)), key=lambda i: -consistency[i])
    
    return ordering
```

**Idea 2: Adaptive Sampling**

根据 uncertainty 动态调整采样数量：

- 简单问题（uncertainty 低）→ 少采样
- 难问题（uncertainty 高）→ 多采样

**Idea 3: Uncertainty Predictor**

训练一个模型预测哪些 tokens 会 uncertain：

```python
uncertainty_predictor = train_predictor(
    inputs=prompts,
    labels=uncertainty_from_dvoting
)

# 推理时直接预测 uncertainty，不需要多次采样
predicted_uncertainty = uncertainty_predictor(new_prompt)
```

---

## 7. 代码示例

```python
class dVoting:
    def __init__(self, model, K=5, threshold=0.8, max_iters=5):
        self.model = model
        self.K = K
        self.threshold = threshold
        self.max_iters = max_iters
    
    def generate(self, prompt):
        # Initial sampling
        samples = [self.model.generate(prompt) for _ in range(self.K)]
        
        for _ in range(self.max_iters):
            # Compute consistency
            consistency = self.compute_consistency(samples)
            
            # Find uncertain positions
            uncertain = [i for i, c in enumerate(consistency) if c < self.threshold]
            
            if len(uncertain) == 0:
                break
            
            # Vote for uncertain tokens
            voted = self.vote(samples, uncertain)
            
            # Regenerate uncertain tokens
            samples = self.regenerate(samples, uncertain, voted)
        
        return self.final_vote(samples)
    
    def compute_consistency(self, samples):
        """Compute token-level consistency across samples"""
        seq_len = len(samples[0])
        consistency = []
        
        for i in range(seq_len):
            tokens_at_i = [s[i] for s in samples]
            most_common_count = max(Counter(tokens_at_i).values())
            consistency.append(most_common_count / self.K)
        
        return consistency
    
    def vote(self, samples, positions):
        """Vote for tokens at uncertain positions"""
        voted = {}
        for pos in positions:
            tokens = [s[pos] for s in samples]
            voted[pos] = Counter(tokens).most_common(1)[0][0]
        return voted
    
    def regenerate(self, samples, uncertain, voted):
        """Regenerate uncertain tokens with voted context"""
        new_samples = []
        for sample in samples:
            # Fix voted tokens, regenerate others
            new_sample = self.model.regenerate(
                sample,
                mask_positions=uncertain,
                context=voted
            )
            new_samples.append(new_sample)
        return new_samples
```

---

## 8. 总结

dVoting 的贡献：

1. **观察**: 大部分 tokens 跨样本一致，只有少数 uncertain
2. **方法**: 利用 dLLM 的 arbitrary-position generation，只 refine uncertain tokens
3. **结果**: 比 Self-Consistency 更高效（2.3x vs 5x），效果更好（+7.2% vs +3.2%）
4. **开源**: 代码可用

**对 dLLM 研究最重要的启发：**

> Token-level uncertainty 是一个重要信号。
> 
> Uncertain tokens 决定性能，可以针对性优化。
> 
> dLLM 的 arbitrary-position generation 是独特优势，应该充分利用。

---

## 参考

- arXiv:2602.12153
- Self-Consistency (Wang et al., 2022)
- GitHub: https://github.com/fscdc/dVoting
