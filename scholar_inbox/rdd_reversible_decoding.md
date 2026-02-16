# RDD: 可逆 Diffusion 解码

**论文:** Reversible Diffusion Decoding for Diffusion Language Models  
**arXiv:** 2602.00150  
**关键词:** Reversibility, Backtracking, Stagnation detection, Error recovery

---

## 1. 核心问题：不可逆 Commit 导致 Stagnation

dLLM 的 block-wise 解码是 **不可逆** 的：
- 一旦 unmask，无法撤回
- 错误的早期 commit 会导致 **stagnation**（卡住）

```
Step 1: [The] [MASK] [MASK] [MASK]
Step 2: [The] [wrong] [MASK] [MASK]  ← 错误 commit
Step 3: [The] [wrong] [token] [MASK]  ← 被迫继续
Step 4: [The] [wrong] [token] [here]  ← 质量差
```

**Stagnation:** 模型知道错了，但无法回头。

---

## 2. 方法：Reversible Diffusion Decoding (RDD)

### 2.1 核心思想

引入 **可逆性**：检测 stagnation，回退到之前的状态，重新生成。

### 2.2 Stagnation Detection

监控 reverse process 的进展：

$$\text{Stagnation} = \frac{\Delta \text{confidence}}{\Delta \text{step}} < \epsilon$$

如果 confidence 不再提升，说明卡住了。

### 2.3 Backtracking

检测到 stagnation 后，回退到之前的 block：

```python
def rdd_decode(model, x, cache):
    while has_masked(x):
        # 保存当前状态
        cache.save(x, step)
        
        # 正常解码
        x_new = diffusion_step(model, x)
        
        # 检测 stagnation
        if is_stagnation(x, x_new):
            # 回退
            x, step = cache.backtrack(num_blocks=1)
            # 重新 mask 不确定的 token
            x = confidence_guided_remask(x)
        else:
            x = x_new
    
    return x
```

### 2.4 Confidence-Guided Re-masking

回退后，选择性地重新 mask：
- 高 confidence token：保留
- 低 confidence token：重新 mask

```python
def confidence_guided_remask(x, threshold=0.5):
    confidence = model.get_confidence(x)
    remask_positions = confidence < threshold
    x[remask_positions] = MASK
    return x
```

---

## 3. 实验结果

| Benchmark | Baseline | + RDD | Improvement |
|-----------|----------|-------|-------------|
| Text Generation | 12.3 PPL | 11.5 PPL | -6.5% |
| Code | 45.2% | 49.8% | +4.6% |
| Math | 52.1% | 56.3% | +4.2% |

### Stagnation 频率

| Task | Stagnation Rate |
|------|-----------------|
| Simple text | 5% |
| Code | 15% |
| Math reasoning | 22% |

推理任务更容易 stagnate。

---

## 4. 深度分析

### 4.1 为什么 Stagnation 发生？

**假设：** 早期 commit 的错误会 "污染" 后续 context。

```
错误 token → 错误 context → 后续预测更难 → stagnation
```

### 4.2 与 LLaDA2.1 T2T 的对比

| | LLaDA2.1 T2T | RDD |
|---|---|---|
| 修正方式 | 编辑已生成 token | 回退 + 重新生成 |
| 粒度 | Token-level | Block-level |
| 需要训练 | 是 | 否 |

RDD 是 training-free 的替代方案。

### 4.3 与 Ordering 的联系

Stagnation 可能和 ordering 有关：
- 错误的 ordering → 早期 commit 错误 token → stagnation
- 好的 ordering → 减少 stagnation

**研究方向：** 用 stagnation 频率评估 ordering 质量。

---

## 5. 对 dLLM 研究的启发

### 5.1 可逆性是重要特性

当前 dLLM 的不可逆性是一个限制。

RDD 证明了可逆性的价值：
- 允许错误恢复
- 提升鲁棒性

### 5.2 研究方向

**Idea 1: 预测 Stagnation**

训练一个模型预测哪些 commit 会导致 stagnation：

```python
stagnation_predictor = train(
    inputs=partial_sequences,
    labels=will_stagnate
)

# 推理时避免高风险 commit
if stagnation_predictor(x, candidate) > threshold:
    skip_this_commit()
```

**Idea 2: Ordering 避免 Stagnation**

设计 ordering 策略，最小化 stagnation 风险：

```python
def stagnation_aware_ordering(model, x):
    # 估计每个位置的 stagnation 风险
    risk = estimate_stagnation_risk(model, x)
    
    # 先生成低风险位置
    ordering = sorted(positions, key=lambda p: risk[p])
    return ordering
```

---

## 6. 总结

| 贡献 | 内容 |
|------|------|
| 问题 | 不可逆 commit 导致 stagnation |
| 方法 | 检测 stagnation + 回退 + 重新生成 |
| 效果 | PPL -6.5%，推理 +4% |
| 优势 | Training-free |

**核心启发：** 可逆性让 dLLM 能从错误中恢复，是提升鲁棒性的关键。

---

## 参考

- arXiv:2602.00150
