# SOAR: 自适应搜索 vs 加速

**论文:** Search or Accelerate: Confidence-Switched Position Beam Search for Diffusion Language Models  
**arXiv:** 2602.10953  
**关键词:** Adaptive decoding, Beam search, Confidence-switched, Quality-speed tradeoff

---

## 1. 核心洞察：不确定时搜索，确定时加速

当前 dLLM 的 greedy decoding 问题：
- 低 confidence 时：过早 commit，锁定次优路径
- 高 confidence 时：本可以并行，却还在逐步解码

**SOAR 的解决方案：根据 confidence 动态切换策略。**

```
Low confidence  → 搜索（避免过早 commit）
High confidence → 加速（并行解码多个位置）
```

---

## 2. 方法

### 2.1 Confidence-Switched 策略

```python
def soar_decode(model, x, conf_threshold=0.7):
    while has_masked(x):
        confidence = model.get_confidence(x)
        
        if confidence.mean() < conf_threshold:
            # 低 confidence: 搜索模式
            x = beam_search_step(model, x, beam_width=4)
        else:
            # 高 confidence: 加速模式
            x = parallel_decode_step(model, x, num_positions=8)
    
    return x
```

### 2.2 Position Beam Search

在低 confidence 时，对 **unmasking 位置** 做 beam search：

```
当前: [MASK] [MASK] [MASK] [MASK]

Beam 1: unmask 位置 0 → [The] [MASK] [MASK] [MASK]
Beam 2: unmask 位置 2 → [MASK] [MASK] [cat] [MASK]
Beam 3: unmask 位置 0,2 → [The] [MASK] [cat] [MASK]
...

选择最优 beam 继续
```

### 2.3 Parallel Acceleration

在高 confidence 时，一次 unmask 多个位置：

```
当前: [The] [MASK] [MASK] [MASK]
Confidence: [-, 0.92, 0.88, 0.85]

一次 unmask 所有高 confidence 位置:
→ [The] [cat] [sat] [down]
```

---

## 3. 实验结果

| Model | Benchmark | Baseline | SOAR | Speedup |
|-------|-----------|----------|------|---------|
| Dream-7B | GSM8K | 65.2% | 71.8% | 1.2x |
| LLaDA-8B | MBPP | 48.5% | 54.2% | 1.4x |
| Dream-7B | HumanEval | 42.1% | 47.3% | 1.3x |

**质量提升的同时，速度也更快！**

---

## 4. 深度分析

### 4.1 为什么能同时提升质量和速度？

- **质量提升**：低 confidence 时搜索，避免错误 commit
- **速度提升**：高 confidence 时并行，减少 step 数

两者不冲突，因为作用在不同阶段。

### 4.2 与 McDiffuSE 的对比

| | McDiffuSE | SOAR |
|---|---|---|
| 搜索对象 | Ordering | Unmasking 位置 |
| 搜索方法 | MCTS | Beam search |
| 自适应 | 否 | 是（根据 confidence） |

SOAR 更轻量，且自适应。

### 4.3 与 Ordering 的联系

Position beam search 本质上是在搜索 **局部 ordering**：
- 哪些位置应该先 unmask？
- 哪些位置可以一起 unmask？

---

## 5. 对 dLLM 研究的启发

### 5.1 自适应是关键

不同阶段需要不同策略：
- 早期（不确定）：谨慎，多搜索
- 后期（确定）：激进，多并行

### 5.2 研究方向

**Idea: 更细粒度的自适应**

不只是全局 confidence，而是 position-level：

```python
for pos in masked_positions:
    if confidence[pos] < threshold:
        # 这个位置需要搜索
        search_positions.append(pos)
    else:
        # 这个位置可以直接 decode
        parallel_positions.append(pos)
```

---

## 6. 总结

| 贡献 | 内容 |
|------|------|
| 洞察 | 低 confidence 搜索，高 confidence 加速 |
| 方法 | Confidence-switched position beam search |
| 效果 | 质量 +5-6%，速度 +20-40% |

**核心启发：** 自适应策略可以同时提升质量和速度。

---

## 参考

- arXiv:2602.10953
