# LLaDA2.1: T2T 编辑 + RL 对齐

**论文:** LLaDA2.1: Speeding Up Text Diffusion via Token Editing  
**arXiv:** 2602.08676  
**作者:** Ant Group (蚂蚁集团)  
**模型:** LLaDA2.1-Mini (16B), LLaDA2.1-Flash (100B)  
**关键词:** Token-to-Token editing, Reinforcement Learning, Speed-quality tradeoff

---

## 1. 核心创新：T2T + M2T 联合解码

### 1.1 传统 M2T (Mask-to-Token)

```
[MASK] [MASK] [MASK] → [The] [cat] [sat]
```

每步从 MASK 预测 token。

### 1.2 新增 T2T (Token-to-Token)

```
[The] [dog] [sat] → [The] [cat] [sat]
                          ^^^
                     编辑错误 token
```

允许修改已生成的 token！

### 1.3 联合解码

```python
def llada21_decode(x, m2t_threshold, t2t_threshold):
    # M2T: 从 MASK 生成 token
    m2t_candidates = model.predict_m2t(x)
    x = unmask(x, m2t_candidates, threshold=m2t_threshold)
    
    # T2T: 编辑已生成的 token
    t2t_candidates = model.predict_t2t(x)
    x = edit(x, t2t_candidates, threshold=t2t_threshold)
    
    return x
```

---

## 2. 两种模式

### 2.1 Speedy Mode (S Mode)

- **低 M2T 阈值**：激进地 unmask
- **依赖 T2T 修正错误**
- 速度优先

### 2.2 Quality Mode (Q Mode)

- **高 M2T 阈值**：保守地 unmask
- T2T 作为补充
- 质量优先

| Mode | M2T Threshold | T2T Role | Speed | Quality |
|------|---------------|----------|-------|---------|
| S | 0.3 | 主要修正 | 快 | 中 |
| Q | 0.7 | 补充修正 | 中 | 高 |

---

## 3. 首个大规模 dLLM RL

### 3.1 为什么 RL 对 dLLM 难？

- dLLM 的 action space 是 **并行的**（同时决定多个 token）
- 传统 RL 假设 **顺序决策**
- 梯度估计不稳定

### 3.2 LLaDA2.1 的解决方案

**Stable Gradient Estimation:**
- 把并行决策分解为多个子决策
- 每个子决策独立估计梯度
- 聚合得到稳定的总梯度

### 3.3 RL 的效果

| | Before RL | After RL |
|---|---|---|
| Reasoning (MATH) | 52.3% | 58.7% |
| Instruction Following | 71.2% | 82.5% |
| Code (HumanEval) | 45.1% | 51.8% |

RL 显著提升了推理和指令遵循能力。

---

## 4. 实验结果

### 4.1 速度

| Model | HumanEval+ TPS | BigCodeBench TPS |
|-------|----------------|------------------|
| GPT-4 | ~50 | ~50 |
| Claude | ~80 | ~80 |
| **LLaDA2.1-Flash** | **892** | **801** |

100B 模型达到 800+ TPS！

### 4.2 质量

在 33 个 benchmark 上评测，LLaDA2.1 达到或超过同规模 AR 模型。

---

## 5. 深度分析

### 5.1 T2T 的意义

T2T 打破了 dLLM 的 **不可逆性**：
- 传统 dLLM：unmask 后不能修改
- LLaDA2.1：可以编辑已生成的 token

这和 RCD 的思想类似：不要浪费之前的计算，可以修正。

### 5.2 与 Ordering 的联系

T2T 隐式地实现了 **动态 ordering**：
- 先快速生成（可能有错）
- 再修正错误（相当于重新排序）

### 5.3 RL for dLLM 的意义

这是首个大规模 dLLM RL，证明了：
- dLLM 可以用 RL 对齐
- 需要专门的梯度估计技术

---

## 6. 对 dLLM 研究的启发

### 6.1 可编辑性是优势

dLLM 的并行生成不是缺点，而是优势：
- 可以快速生成初稿
- 再精细编辑

### 6.2 RL 是重要方向

LLaDA2.1 证明了 RL 对 dLLM 的价值。

未来方向：
- 更好的梯度估计
- 更复杂的 reward（不只是正确性）
- Online RL

### 6.3 研究方向

**Idea 1: Ordering-Aware T2T**

T2T 应该优先编辑哪些 token？

```python
# 按 "错误概率" 排序，优先编辑最可能错的
edit_priority = model.estimate_error_prob(x)
tokens_to_edit = topk(edit_priority, k)
```

**Idea 2: RL for Ordering**

用 RL 学习最优 ordering：

```python
# State: 当前生成状态
# Action: 选择下一个要生成/编辑的位置
# Reward: 最终生成质量
ordering_policy = rl_train(env=dllm_env)
```

---

## 7. 总结

| 贡献 | 内容 |
|------|------|
| T2T 编辑 | 允许修改已生成 token |
| 双模式 | Speedy vs Quality 可配置 |
| 首个大规模 RL | 稳定梯度估计技术 |
| 效果 | 100B 模型 800+ TPS |

**核心启发：**

> dLLM 的可编辑性是独特优势。
> 
> T2T + M2T 联合解码打破了速度-质量权衡。
> 
> RL 是 dLLM 对齐的重要方向。

---

## 参考

- arXiv:2602.08676
- Ant Group
