# Self-Rewarding SMC: 用 SMC 提升 dLLM 采样质量

**论文:** Self-Rewarding Sequential Monte Carlo for Masked Diffusion Language Models  
**arXiv:** 2602.01849  
**代码:** https://github.com/Algolzw/self-rewarding-smc  
**关键词:** Sequential Monte Carlo, Particle filtering, Trajectory-level confidence, Diversity

---

## 1. 核心问题：Greedy Decoding 导致多样性崩塌

当前 dLLM 的 confidence-based 采样是 **greedy** 的：
- 每步只保留最 confident 的 token
- 一旦选错，无法回头
- 生成路径多样性崩塌

```
Step 1: 选择 "The" (conf=0.95)
Step 2: 选择 "cat" (conf=0.88)  ← 可能不是最优
Step 3: 被迫沿着 "The cat..." 继续
...
多样性丧失，可能错过更好的路径
```

---

## 2. 方法：Self-Rewarding SMC

### 2.1 核心思想

用 **Sequential Monte Carlo (SMC)** 维护多个并行的生成路径（particles），通过 resampling 聚焦到高质量路径。

### 2.2 Particle = 一条生成轨迹

```
Particle 1: [The] [cat] [sat] ...
Particle 2: [A]   [dog] [ran] ...
Particle 3: [The] [bird] [flew] ...
...
```

每个 particle 是一条独立的生成路径。

### 2.3 Self-Rewarding: 轨迹级 Confidence

**关键创新：** 用 **trajectory-level confidence** 作为 importance weight。

$$w_i = \prod_{t=1}^{T} \text{conf}(x_i^t)$$

整条轨迹的 confidence 乘积，而不是单步 confidence。

### 2.4 Resampling

根据 importance weight 重采样：
- 高 weight 的 particle 被复制
- 低 weight 的 particle 被淘汰

```python
def smc_step(particles, weights):
    # Resample based on weights
    indices = multinomial_resample(weights)
    particles = particles[indices]
    
    # Continue generation
    for i, p in enumerate(particles):
        particles[i] = diffusion_step(p)
        weights[i] = compute_trajectory_confidence(particles[i])
    
    return particles, weights
```

---

## 3. 实验结果

### 3.1 质量提升

| Model | Benchmark | Baseline | + SMC | Improvement |
|-------|-----------|----------|-------|-------------|
| LLaDA-8B | GSM8K | 68.2% | 74.5% | +6.3% |
| Dream-7B | MATH500 | 45.3% | 52.1% | +6.8% |
| MDLM | HumanEval | 42.1% | 48.7% | +6.6% |

### 3.2 多样性提升

| | Baseline | + SMC |
|---|---|---|
| Distinct-1 | 0.42 | 0.61 |
| Distinct-2 | 0.58 | 0.73 |
| Self-BLEU ↓ | 0.72 | 0.51 |

SMC 显著提升了生成多样性。

### 3.3 计算开销

| Particles | Speedup vs Sequential | Quality |
|-----------|----------------------|---------|
| 4 | 3.2x | +4.2% |
| 8 | 5.8x | +6.3% |
| 16 | 8.1x | +6.8% |

更多 particles = 更好质量，且可以并行。

---

## 4. 深度分析

### 4.1 为什么 SMC 适合 dLLM？

dLLM 的并行生成天然适合 SMC：
- 多个 particles 可以并行计算
- 不像 AR 需要顺序生成

### 4.2 与 McDiffuSE 的对比

| | McDiffuSE | SMC |
|---|---|---|
| 搜索空间 | Ordering | 生成路径 |
| 方法 | MCTS | Particle filtering |
| 开销 | 高（sequential） | 低（parallel） |

SMC 更适合并行加速。

### 4.3 与 dVoting 的联系

dVoting 用多次采样 + voting。

SMC 用多个 particles + resampling。

**区别：** SMC 是 **在线** 的（边生成边筛选），dVoting 是 **离线** 的（生成完再 vote）。

---

## 5. 对 dLLM 研究的启发

### 5.1 Trajectory-Level 思考

不要只看单步 confidence，要看整条轨迹。

这和 ordering 研究相关：好的 ordering 应该让整条轨迹的 confidence 更高。

### 5.2 并行 = 质量

SMC 证明了：**并行计算可以转化为质量提升**。

这是 dLLM 相对于 AR 的独特优势。

### 5.3 研究方向

**Idea: SMC + Ordering**

用 SMC 探索不同的 ordering：

```python
# 每个 particle 用不同的 ordering
particles = [
    generate_with_ordering(ordering_1),
    generate_with_ordering(ordering_2),
    ...
]
# Resample based on trajectory confidence
```

---

## 6. 总结

| 贡献 | 内容 |
|------|------|
| 问题 | Greedy decoding 导致多样性崩塌 |
| 方法 | SMC + trajectory-level confidence |
| 效果 | +6% 质量，+30% 多样性 |
| 优势 | 可并行，无需训练 |

**核心启发：** dLLM 的并行能力可以转化为质量提升，SMC 是一个有效的方法。

---

## 参考

- arXiv:2602.01849
- https://github.com/Algolzw/self-rewarding-smc
