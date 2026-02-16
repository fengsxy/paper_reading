# McDiffuSE: 用 MCTS 优化 dLLM 的生成顺序

**论文:** Can I Have Your Order? Monte-Carlo Tree Search for Slot Filling Ordering in Diffusion Language Models  
**arXiv:** 2602.12586  
**作者:** Joshua Ong Jun Leang, Yu Zhao, Mihaela Stoian, Wenda Li, Shay B. Cohen, Eleonora Giunchiglia  
**关键词:** MCTS, Ordering optimization, Masked Diffusion Models, Plan-and-infill

---

## 1. 问题背景：Ordering 为什么重要？

Masked Diffusion Models (MDMs) 的一个核心问题：

> **生成顺序（ordering）对结果影响巨大，但目前没有好的方法选择最优顺序。**

### 1.1 Plan-and-Infill 范式

当前 dLLM 做推理任务（数学、代码）的主流方法：

```
Step 1: 生成 "计划"（关键 tokens 的位置）
Step 2: 按某种顺序 "填充" 这些位置
```

问题：**填充顺序不同，结果差异巨大。**

### 1.2 实验观察

论文的关键发现：

| Ordering 策略 | MATH500 准确率 |
|--------------|---------------|
| 随机顺序 | 45.2% |
| 从左到右 | 52.1% |
| Confidence-based | 54.3% |
| **Oracle (最优)** | **62.8%** |

**最优顺序和随机顺序差了 17.6%！**

这说明：ordering 是一个巨大的优化空间，但目前的方法（confidence-based）远未达到最优。

---

## 2. 核心方法：MCTS 搜索最优顺序

### 2.1 为什么用 MCTS？

Ordering 选择本质上是一个 **组合优化问题**：

- N 个位置需要填充
- 有 N! 种可能的顺序
- 需要找到最优的那个

MCTS 的优势：
1. **不需要穷举**：通过 simulation 估计价值
2. **平衡探索和利用**：UCB 公式
3. **可以提前终止**：找到足够好的解就停

### 2.2 McDiffuSE 框架

```
输入: Masked sequence with K slots to fill
输出: Optimal ordering + filled sequence

MCTS Loop:
1. Selection: 从根节点选择最有潜力的路径
2. Expansion: 扩展一个新的 slot 选择
3. Simulation: 用默认策略完成剩余 slots
4. Backpropagation: 更新路径上所有节点的价值
```

### 2.3 关键设计

**State:** 当前已填充的 slots + 剩余待填充的 slots

**Action:** 选择下一个要填充的 slot

**Reward:** 最终生成结果的质量（正确性）

**UCB 公式:**
$$UCB(s, a) = Q(s, a) + c \sqrt{\frac{\ln N(s)}{N(s, a)}}$$

其中 $c$ 是探索常数，论文发现 **较大的 $c$ 更重要**。

---

## 3. 技术细节

### 3.1 Look-ahead Simulation

MCTS 的核心是 simulation：给定部分填充的序列，估计最终质量。

McDiffuSE 的 simulation 策略：

```python
def simulate(partial_sequence, remaining_slots):
    # 用 confidence-based ordering 完成剩余 slots
    for slot in sorted(remaining_slots, key=lambda s: -confidence[s]):
        partial_sequence[slot] = model.predict(partial_sequence, slot)
    
    # 评估最终结果
    return evaluate(partial_sequence)
```

### 3.2 为什么不直接用 Confidence？

论文的关键发现：

> **模型的 confidence 有 bias，不能完全信任。**

实验表明：
- 高 confidence 的位置不一定应该先填
- 有时候先填 "难" 的位置反而更好（提供更多 context）

MCTS 通过 simulation 发现这些 **反直觉的 ordering**。

### 3.3 探索常数的重要性

| 探索常数 $c$ | MATH500 |
|-------------|---------|
| 0.1 | 54.8% |
| 1.0 | 56.2% |
| 2.0 | 58.1% |
| **5.0** | **59.3%** |

**较大的探索常数更重要！**

原因：模型的 confidence bias 会误导搜索，需要更多探索来发现真正好的 ordering。

---

## 4. 实验结果

### 4.1 主要结果

| Method | GSM8K | MATH500 | MBPP | HumanEval |
|--------|-------|---------|------|-----------|
| AR baseline | 52.3% | 48.2% | 45.6% | 42.1% |
| Plan-and-infill | 54.1% | 51.4% | 48.2% | 44.3% |
| + Confidence ordering | 55.8% | 54.3% | 52.1% | 46.8% |
| **+ McDiffuSE** | **58.5%** | **59.3%** | **67.6%** | **51.2%** |

**MBPP 上提升 19.5%！**

### 4.2 Ordering 分析

论文分析了 McDiffuSE 找到的 ordering 模式：

| Pattern | 占比 |
|---------|------|
| 完全顺序（从左到右）| 45% |
| 大部分顺序 + 少量跳跃 | 38% |
| 非顺序 | 17% |

**关键发现：**
- 大部分情况下，顺序生成是好的
- 但 **17% 的非顺序生成是必要的**，贡献了大部分性能提升

### 4.3 计算开销

| Method | Time (relative) |
|--------|-----------------|
| Confidence ordering | 1x |
| McDiffuSE (100 sims) | 15x |
| McDiffuSE (500 sims) | 60x |

MCTS 有计算开销，但对于高价值任务（数学、代码）是值得的。

---

## 5. 深度分析

### 5.1 为什么 Ordering 这么重要？

**信息流视角：**

填充一个 slot 会影响后续 slots 的预测：

```
填充 slot A → 更新 context → 影响 slot B 的预测
```

如果先填 "错误" 的 slot，错误会传播到后续 slots。

**最优 ordering = 最小化错误传播**

### 5.2 与 Latent Forcing 的联系

Latent Forcing 的发现：DINO latents 应该先 denoise。

McDiffuSE 的发现：某些 slots 应该先填。

**共同点：** 都在说 "ordering matters"，但都没有给出 **理论解释**。

### 5.3 MCTS 的局限

1. **计算开销大**：需要多次 simulation
2. **Reward 设计**：需要能评估部分结果
3. **不能泛化**：每个 instance 都要重新搜索

---

## 6. 对 dLLM 研究的启发

### 6.1 验证了 Ordering 的重要性

McDiffuSE 用实验证明：

> **Optimal ordering 和 random ordering 差距巨大（17.6%）**
> **Confidence-based ordering 远未达到最优**

这为 ordering 研究提供了强有力的 motivation。

### 6.2 MCTS 作为 Upper Bound

McDiffuSE 可以看作 ordering 优化的 **upper bound**：

- 它通过搜索找到好的 ordering
- 但计算开销太大，不实用

**研究方向：能否学习一个 ordering predictor，直接预测好的 ordering？**

### 6.3 探索常数的启示

论文发现大的探索常数更重要，说明：

> **模型的 confidence 有 systematic bias**

这和 Hot Mess Theory 的发现一致：模型的 variance 比我们想象的大。

### 6.4 具体研究方向

**Idea 1: Learning to Order**

用 McDiffuSE 生成的 ordering 作为训练数据，学习一个 ordering predictor：

```python
# 收集数据
for problem in problems:
    optimal_ordering = mcts_search(problem)
    dataset.append((problem, optimal_ordering))

# 训练 predictor
ordering_predictor = train(dataset)

# 推理时直接预测
predicted_ordering = ordering_predictor(new_problem)
```

**Idea 2: Theoretical Analysis**

McDiffuSE 发现 17% 的非顺序生成是必要的。

问题：**什么时候需要非顺序生成？能否理论分析？**

可能的方向：
- 用 information theory 分析 slot 之间的依赖
- 用 causal inference 分析 ordering 的因果效应

**Idea 3: Adaptive Exploration**

McDiffuSE 用固定的探索常数。

改进：根据问题难度自适应调整探索常数：
- 简单问题：小 $c$，快速收敛
- 难问题：大 $c$，充分探索

---

## 7. 代码示例

### 7.1 简化的 MCTS 实现

```python
class McDiffuSE:
    def __init__(self, model, c=5.0, num_simulations=100):
        self.model = model
        self.c = c
        self.num_simulations = num_simulations
    
    def search(self, masked_sequence, slots):
        root = Node(masked_sequence, slots)
        
        for _ in range(self.num_simulations):
            # Selection
            node = self.select(root)
            
            # Expansion
            if not node.is_terminal():
                child = self.expand(node)
                
                # Simulation
                reward = self.simulate(child)
                
                # Backpropagation
                self.backpropagate(child, reward)
        
        # Return best ordering
        return self.get_best_ordering(root)
    
    def select(self, node):
        while not node.is_terminal() and node.is_fully_expanded():
            node = self.best_ucb_child(node)
        return node
    
    def best_ucb_child(self, node):
        return max(node.children, key=lambda c: self.ucb(c))
    
    def ucb(self, node):
        if node.visits == 0:
            return float('inf')
        return node.value / node.visits + self.c * math.sqrt(
            math.log(node.parent.visits) / node.visits
        )
    
    def simulate(self, node):
        # Complete remaining slots with confidence-based ordering
        sequence = node.sequence.copy()
        remaining = node.remaining_slots.copy()
        
        for slot in sorted(remaining, key=lambda s: -self.model.confidence(sequence, s)):
            sequence[slot] = self.model.predict(sequence, slot)
        
        return self.evaluate(sequence)
```

---

## 8. 总结

McDiffuSE 的贡献：

1. **问题定义**: 将 ordering 选择形式化为决策问题
2. **方法**: 用 MCTS 搜索最优 ordering
3. **实验**: 证明 ordering 优化空间巨大（17.6% gap）
4. **分析**: 发现非顺序生成的重要性，以及探索常数的关键作用

**对 dLLM 研究最重要的启发：**

> Ordering 优化是一个巨大的机会。
> 
> Confidence-based ordering 远未最优，有很大改进空间。
> 
> 下一步：能否学习一个 ordering predictor，避免 MCTS 的计算开销？

---

## 参考

- arXiv:2602.12586
- MCTS (Coulom, 2006; Kocsis & Szepesvári, 2006)
- Plan-and-infill for MDMs
