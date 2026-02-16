# FOCUS: 动态聚焦可解码 Token

**论文:** FOCUS: DLLMs Know How to Tame Their Compute Bound  
**arXiv:** 2601.23278  
**代码:** https://github.com/sands-lab/FOCUS  
**关键词:** Dynamic batching, Token eviction, Throughput optimization, Attention importance

---

## 1. 核心问题：计算浪费在不可解码 Token 上

dLLM 的 block-wise 解码：
- 每步处理一个 token block
- 但只有少数 token 真正 "可解码"（confidence 足够高）
- 大部分计算浪费在不可解码的 token 上

```
Block: [MASK] [MASK] [MASK] [MASK] [MASK] [MASK] [MASK] [MASK]
        ↓      ↓      ↓      ↓      ↓      ↓      ↓      ↓
Conf:  0.95   0.32   0.87   0.21   0.91   0.15   0.88   0.29
        ✓      ✗      ✓      ✗      ✓      ✗      ✓      ✗
       解码   浪费   解码   浪费   解码   浪费   解码   浪费
```

**50% 的计算被浪费！**

---

## 2. 关键发现：Attention 预测可解码性

论文发现：

> **Attention-derived token importance 和 token 可解码概率强相关。**

```
Attention importance 高 → 更可能被解码
Attention importance 低 → 不太可能被解码
```

**Pearson correlation: 0.78**

这意味着可以用 attention 来 **预测** 哪些 token 值得计算。

---

## 3. 方法：FOCUS

### 3.1 核心思想

动态聚焦计算到可解码的 token：
1. 用 attention importance 预测可解码性
2. 驱逐（evict）不可解码的 token
3. 增加 effective batch size

### 3.2 Token Importance 计算

$$\text{Importance}(i) = \sum_{j} A_{j \to i}$$

即：所有其他位置对位置 $i$ 的 attention 权重之和。

**直觉：** 被很多位置 attend 的 token 更重要。

### 3.3 动态驱逐

```python
class FOCUS:
    def decode_step(self, tokens, threshold):
        # 计算 attention importance
        importance = self.compute_importance(tokens)
        
        # 驱逐低 importance 的 token
        keep_mask = importance > threshold
        active_tokens = tokens[keep_mask]
        
        # 只对 active tokens 计算
        output = self.model(active_tokens)
        
        # 恢复完整序列
        tokens[keep_mask] = output
        return tokens
```

### 3.4 Batch Size 增加

驱逐 token 后，可以塞入更多 sequence：

```
原始: [Seq1: 100 tokens] [Seq2: 100 tokens]  → Batch size = 2
FOCUS: [Seq1: 50 active] [Seq2: 50 active] [Seq3: 50 active] [Seq4: 50 active]
       → Effective batch size = 4
```

**Throughput 提升 3.52x！**

---

## 4. 实验结果

### 4.1 Throughput 提升

| Engine | Throughput (tokens/s) | Speedup |
|--------|----------------------|---------|
| LMDeploy | 1,000 | 1x |
| vLLM | 1,200 | 1.2x |
| **FOCUS** | **3,520** | **3.52x** |

### 4.2 质量保持

| Benchmark | LMDeploy | FOCUS | Change |
|-----------|----------|-------|--------|
| MMLU | 65.2% | 65.4% | +0.2% |
| GSM8K | 72.1% | 72.3% | +0.2% |
| HumanEval | 48.5% | 48.8% | +0.3% |

质量不降反升！因为聚焦计算让重要 token 得到更好处理。

### 4.3 驱逐率分析

| Step | 驱逐率 |
|------|--------|
| Early (1-5) | 60% |
| Mid (6-10) | 45% |
| Late (11-15) | 25% |

早期驱逐率高，因为大部分 token 还不确定。

---

## 5. 深度分析

### 5.1 为什么 Attention Importance 有效？

**假设：** Attention 反映了 token 之间的信息流。

- 高 importance = 很多 token 需要这个位置的信息 = 这个位置重要
- 低 importance = 没人关心这个位置 = 可以暂时忽略

### 5.2 与 SureLock 的对比

| | SureLock | FOCUS |
|---|---|---|
| 判断标准 | 收敛性（KL） | 重要性（Attention） |
| 时机 | 后期锁定 | 早期驱逐 |
| 节省方式 | 跳过计算 | 增加 batch |

**可以结合：** 早期用 FOCUS 驱逐，后期用 SureLock 锁定。

### 5.3 与 Ordering 的联系

FOCUS 的 importance 可以指导 ordering：

```
高 importance → 先解码（提供 context）
低 importance → 后解码（依赖 context）
```

---

## 6. 对 dLLM 研究的启发

### 6.1 Attention 是有价值的信号

FOCUS 证明了 attention 可以预测 token 重要性。

其他可能的应用：
- 预测 ordering
- 预测 difficulty
- 预测 dependency

### 6.2 系统优化的重要性

FOCUS 是一个 **系统级** 优化：
- 不改模型架构
- 不需要重新训练
- 纯推理时优化

这说明 dLLM 的系统优化空间很大。

### 6.3 研究方向

**Idea 1: Attention-Guided Ordering**

用 attention importance 指导生成顺序：

```python
def attention_guided_ordering(model, masked_sequence):
    importance = model.compute_importance(masked_sequence)
    # 按 importance 从高到低排序
    ordering = sorted(range(len(importance)), key=lambda i: -importance[i])
    return ordering
```

**Idea 2: 预测 Importance**

训练一个轻量模型预测 importance，避免计算完整 attention：

```python
importance_predictor = train(
    inputs=masked_sequences,
    labels=attention_importance
)
```

**Idea 3: Importance-Aware Training**

在训练时就考虑 importance：
- 高 importance token 的 loss 权重更大
- 让模型学会区分重要和不重要的 token

---

## 7. 代码示例

```python
class FOCUSEngine:
    def __init__(self, model, eviction_threshold=0.3):
        self.model = model
        self.threshold = eviction_threshold
    
    def compute_importance(self, hidden_states, attention_weights):
        """计算每个 token 的 importance"""
        # attention_weights: [batch, heads, seq, seq]
        # 对所有 head 和 source position 求和
        importance = attention_weights.sum(dim=(1, 2))  # [batch, seq]
        return importance
    
    def decode_batch(self, sequences, max_steps):
        active_mask = torch.ones_like(sequences, dtype=torch.bool)
        
        for step in range(max_steps):
            # 收集所有 active tokens
            active_tokens = []
            for seq, mask in zip(sequences, active_mask):
                active_tokens.append(seq[mask])
            
            # Batch forward
            outputs, attentions = self.model(active_tokens, return_attention=True)
            
            # 计算 importance
            importance = self.compute_importance(outputs, attentions)
            
            # 更新 active mask（驱逐低 importance）
            for i, imp in enumerate(importance):
                active_mask[i] = imp > self.threshold
            
            # 更新 sequences
            for i, (out, mask) in enumerate(zip(outputs, active_mask)):
                sequences[i][mask] = out
        
        return sequences
```

---

## 8. 总结

| 贡献 | 内容 |
|------|------|
| 发现 | Attention importance 预测可解码性 |
| 方法 | 动态驱逐低 importance token |
| 效果 | 3.52x throughput，质量保持 |
| 开源 | https://github.com/sands-lab/FOCUS |

**核心启发：** Attention 是一个强大的信号，可以用来指导计算分配、ordering、和系统优化。

---

## 参考

- arXiv:2601.23278
- https://github.com/sands-lab/FOCUS
