# SureLock: 跳过已收敛 Token 的计算

**论文:** Stopping Computation for Converged Tokens in Masked Diffusion-LM Decoding  
**arXiv:** 2602.06412  
**会议:** ICLR 2026  
**代码:** https://daioba.github.io/surelock  
**关键词:** Early stopping, Token locking, FLOPs reduction, KV cache

---

## 1. 核心观察：大量计算被浪费

MDLM 每一步都对 **所有位置** 计算 attention 和 FFN，即使很多位置已经 "收敛"（不再变化）。

```
Step 1: [MASK] [MASK] [MASK] [MASK] [MASK]  → 全部计算
Step 2: [The]  [MASK] [MASK] [MASK] [MASK]  → 全部计算（但 "The" 已确定）
Step 3: [The]  [cat]  [MASK] [MASK] [MASK]  → 全部计算（但 "The", "cat" 已确定）
...
```

**问题：** 已确定的 token 还在重复计算，浪费 30-50% 的 FLOPs。

---

## 2. 方法：SureLock

### 2.1 核心思想

当一个位置的预测 "稳定" 后，**锁定** 它：
- 跳过该位置的 query 和 FFN 计算
- 但保留 KV cache，让其他位置能 attend 到它

### 2.2 "Sure" 条件

如何判断一个位置已经稳定？

**监控 local KL divergence：**

$$\text{Sure}(i, t) = D_{KL}(P_t(x_i) || P_{t-1}(x_i)) < \epsilon$$

如果连续几步的预测分布变化很小，就认为已收敛。

### 2.3 锁定机制

```python
class SureLock:
    def forward(self, x, locked_positions):
        # 只对未锁定位置计算 query
        unlocked = [i for i in range(len(x)) if i not in locked_positions]
        
        Q = self.W_q(x[unlocked])  # 只计算未锁定位置的 query
        K = self.W_k(x)            # 所有位置的 key（包括锁定的，用 cache）
        V = self.W_v(x)            # 所有位置的 value
        
        # Attention: unlocked positions attend to all positions
        attn = softmax(Q @ K.T / sqrt(d))
        out = attn @ V
        
        # FFN: 只对未锁定位置
        out[unlocked] = self.ffn(out[unlocked])
        
        return out
```

### 2.4 复杂度分析

| | 原始 | SureLock |
|---|---|---|
| Attention | $O(N^2 d)$ | $O(MN d)$ |
| FFN | $O(N d^2)$ | $O(M d^2)$ |

其中 $M$ 是未锁定位置数，随迭代减少。

---

## 3. 理论保证

论文提供了理论分析：

> **监控 local KL 足以 bound 最终 token 概率的偏差。**

**定理：** 如果在 step $t$ 锁定位置 $i$，且 $D_{KL}(P_t || P_{t-1}) < \epsilon$，则最终输出的 KL 偏差 bounded by $O(\epsilon \cdot T)$。

这说明 SureLock 的质量损失是可控的。

---

## 4. 实验结果

### 4.1 FLOPs 节省

| Model | FLOPs Reduction | Quality (PPL) |
|-------|-----------------|---------------|
| LLaDA-8B | 30-50% | 保持 |
| MDLM-1B | 25-40% | 保持 |

### 4.2 不同任务

| Task | FLOPs Saved | Quality Change |
|------|-------------|----------------|
| Text Generation | 35% | -0.2 PPL |
| Code Generation | 42% | -0.1% accuracy |
| Math Reasoning | 28% | -0.3% accuracy |

Math reasoning 节省较少，因为更多位置需要 "思考"。

### 4.3 锁定时机分析

| Step | 锁定比例 |
|------|---------|
| 1-5 | 15% |
| 6-10 | 45% |
| 11-15 | 72% |
| 16-20 | 88% |

大部分位置在中后期被锁定。

---

## 5. 深度分析

### 5.1 与 dVoting 的联系

dVoting 发现：大部分 token 跨样本一致。

SureLock 发现：大部分 token 跨 step 一致。

**共同点：** 只有少数 token 是 "难" 的，需要更多计算。

### 5.2 与 DAWN 的联系

DAWN 用依赖图决定并行策略。

SureLock 用收敛性决定计算分配。

**可以结合：** 用依赖图预测哪些位置会早收敛。

### 5.3 与 Adaptive Computation 的联系

SureLock 是一种 **token-level adaptive computation**：
- 简单 token → 少计算
- 难 token → 多计算

类似于 Universal Transformer 的 ACT，但更细粒度。

---

## 6. 对 dLLM 研究的启发

### 6.1 计算应该 Token-Aware

当前 dLLM 对所有 token 平等对待，但：
- 有些 token 很容易（"the", "a", "is"）
- 有些 token 很难（数字、专有名词）

**应该把计算分配给难的 token。**

### 6.2 Early Stopping 的价值

SureLock 证明了 early stopping 的价值：
- 不需要等所有 step 完成
- 可以 token-by-token 地 early stop

### 6.3 研究方向

**Idea 1: 预测收敛时间**

训练一个模型预测每个位置需要多少 step 才能收敛：

```python
convergence_predictor = train(
    inputs=masked_sequences,
    labels=convergence_steps_from_surelock
)
```

**Idea 2: 动态计算分配**

根据预测的难度，动态分配计算：
- 难位置：更多 attention heads，更大 FFN
- 简单位置：更少计算

**Idea 3: 与 Ordering 结合**

先生成容易收敛的位置，后生成难的位置：
- 容易位置早锁定 → 节省计算
- 难位置有更多 context → 更准确

---

## 7. 代码示例

```python
class SureLockDecoder:
    def __init__(self, model, epsilon=0.01, patience=2):
        self.model = model
        self.epsilon = epsilon
        self.patience = patience
    
    def decode(self, masked_sequence, num_steps):
        locked = set()
        kv_cache = {}
        prev_probs = {}
        stable_count = defaultdict(int)
        
        for step in range(num_steps):
            # 只对未锁定位置计算
            unlocked = [i for i in range(len(masked_sequence)) if i not in locked]
            
            # Forward pass with selective computation
            probs, new_kv = self.model.forward(
                masked_sequence, 
                compute_positions=unlocked,
                kv_cache=kv_cache
            )
            kv_cache.update(new_kv)
            
            # Check convergence for each position
            for i in unlocked:
                if i in prev_probs:
                    kl = kl_divergence(probs[i], prev_probs[i])
                    if kl < self.epsilon:
                        stable_count[i] += 1
                        if stable_count[i] >= self.patience:
                            locked.add(i)
                    else:
                        stable_count[i] = 0
                prev_probs[i] = probs[i]
            
            # Unmask based on probs
            masked_sequence = self.unmask_step(masked_sequence, probs, locked)
        
        return masked_sequence
```

---

## 8. 总结

| 贡献 | 内容 |
|------|------|
| 问题 | dLLM 对已收敛 token 重复计算 |
| 方法 | 监控 KL，锁定稳定位置 |
| 效果 | 30-50% FLOPs 节省，质量保持 |
| 理论 | 证明 local KL 监控足以 bound 误差 |

**核心启发：** 不是所有 token 都需要同等计算，应该把资源给难的 token。

---

## 参考

- arXiv:2602.06412
- ICLR 2026
- https://daioba.github.io/surelock
