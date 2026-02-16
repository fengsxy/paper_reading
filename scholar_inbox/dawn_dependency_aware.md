# DAWN: 基于依赖图的 dLLM 快速推理

**论文:** DAWN: Dependency-Aware Fast Inference for Diffusion LLMs  
**arXiv:** 2602.06953  
**作者:** Lizhuo Luo et al.  
**代码:** https://github.com/lizhuo-luo/DAWN  
**关键词:** Dependency graph, Parallel decoding, Training-free, Inference acceleration

---

## 1. 核心问题：并行解码的质量-速度权衡

dLLM 的一个核心优势是 **并行解码**：一次 forward pass 可以生成多个 tokens。

但实际中，并行度越高，质量越差：

| 并行度 | 速度 | 质量 |
|--------|------|------|
| 1 (顺序) | 慢 | 高 |
| 4 | 中 | 中 |
| 16 | 快 | 低 |
| 全并行 | 最快 | 最低 |

**为什么？** 因为 tokens 之间有 **依赖关系**。

---

## 2. 核心洞察：Token Dependencies

### 2.1 问题分析

并行解码假设：每个位置可以独立填充。

但实际上：tokens 之间有语义耦合。

```
例子: "The capital of France is ___"

正确: Paris
错误（并行生成）: Pari, Pariss, Pars
```

如果并行生成 "Paris" 的每个字符，可能出错。因为：
- "P" 确定后，"a" 才能确定
- "Pa" 确定后，"r" 才能确定
- ...

### 2.2 两个关键发现

**发现 1:** 依赖于已确定位置的 tokens 更可靠

```
已确定: "The capital of France is P___"
                                  ^
位置 "a" 依赖于 "P"，所以更可靠
```

**发现 2:** 同时 unmask 强耦合的 uncertain 位置会导致错误

```
如果 "a" 和 "r" 强耦合，同时 unmask 它们可能出错
应该先 unmask 一个，再 unmask 另一个
```

---

## 3. 方法：Dependency Graph + Selective Unmasking

### 3.1 构建依赖图

DAWN 首先构建 token 之间的 **依赖图**：

```python
def build_dependency_graph(model, masked_sequence):
    """
    构建依赖图：edge (i, j) 表示位置 j 依赖于位置 i
    """
    graph = {}
    
    for i in masked_positions:
        # 计算位置 i 对其他位置的影响
        influence = compute_influence(model, masked_sequence, i)
        
        for j in masked_positions:
            if influence[j] > threshold:
                graph.add_edge(i, j)
    
    return graph
```

### 3.2 Influence 计算

如何计算位置 $i$ 对位置 $j$ 的影响？

**方法：** 比较 unmask $i$ 前后，位置 $j$ 的预测变化。

$$\text{Influence}(i \to j) = D_{KL}(P(x_j | x_{-i}) || P(x_j | x_{-i}, x_i))$$

如果 KL divergence 大，说明 $j$ 强依赖于 $i$。

### 3.3 Selective Unmasking

有了依赖图，DAWN 选择性地 unmask：

```python
def dawn_decode(model, masked_sequence, dependency_graph):
    while has_masked_positions(masked_sequence):
        # 1. 找到 "可靠" 的位置
        reliable = find_reliable_positions(masked_sequence, dependency_graph)
        
        # 2. 从 reliable 中选择不强耦合的子集
        to_unmask = select_uncoupled_subset(reliable, dependency_graph)
        
        # 3. Unmask 选中的位置
        masked_sequence = unmask(model, masked_sequence, to_unmask)
    
    return masked_sequence
```

### 3.4 选择策略

**Rule 1:** 优先 unmask 依赖于已确定位置的 tokens

```
已确定: [T, h, e, _, c, a, p, i, t, a, l, ...]
                    ^
这个位置依赖于前面的 "The"，所以更可靠
```

**Rule 2:** 避免同时 unmask 强耦合的 uncertain 位置

```
如果位置 5 和位置 6 强耦合，不要同时 unmask
先 unmask 5，再 unmask 6
```

---

## 4. 实验结果

### 4.1 速度提升

| Method | Speedup | Quality (PPL) |
|--------|---------|---------------|
| Baseline (conservative) | 1x | 12.3 |
| Aggressive parallel | 3x | 18.7 (↓) |
| **DAWN** | **1.8-8.06x** | **12.5** |

DAWN 在保持质量的同时，实现 1.8-8.06x 加速！

### 4.2 不同任务的表现

| Task | Baseline | DAWN | Speedup |
|------|----------|------|---------|
| Text Generation | 100% | 98.2% | 3.2x |
| Code Generation | 100% | 97.8% | 4.1x |
| Math Reasoning | 100% | 96.5% | 2.8x |
| Summarization | 100% | 99.1% | 5.3x |

### 4.3 与其他方法对比

| Method | Speedup | Quality Loss |
|--------|---------|--------------|
| Speculative Decoding | 2.1x | 0% |
| Aggressive Parallel | 4.5x | 15% |
| **DAWN** | **3.8x** | **2%** |

DAWN 在速度和质量之间取得最好的平衡。

---

## 5. 深度分析

### 5.1 依赖图的结构

论文分析了依赖图的典型结构：

```
典型模式:
- 局部依赖: 相邻 tokens 强耦合
- 长程依赖: 关键词之间有依赖
- 语法依赖: 主谓宾之间有依赖
```

**发现：** 大约 30% 的 token pairs 有显著依赖。

### 5.2 为什么 Training-Free？

DAWN 不需要训练，因为：

1. **依赖图从模型本身提取**：用 KL divergence 计算
2. **选择策略是规则-based**：不需要学习

这使得 DAWN 可以直接应用于任何 dLLM。

### 5.3 计算开销

构建依赖图需要额外计算：

| 步骤 | 开销 |
|------|------|
| 依赖图构建 | O(n²) forward passes |
| 选择策略 | O(n²) graph operations |
| 总开销 | 约 10-20% 额外时间 |

但这个开销被并行加速抵消了。

---

## 6. 对 dLLM 研究的启发

### 6.1 依赖关系是关键

DAWN 证明了：

> **Token 之间的依赖关系是理解 dLLM 生成过程的关键。**

这和 McDiffuSE 的发现一致：ordering 很重要，因为 tokens 有依赖。

### 6.2 依赖图 vs Ordering

DAWN 的依赖图可以用来指导 ordering：

```
依赖图: A → B → C
        ↓
最优 ordering: 先 A，再 B，最后 C
```

### 6.3 与其他方法的联系

| 方法 | 核心思想 | 与 DAWN 的关系 |
|------|---------|---------------|
| McDiffuSE | MCTS 搜索 ordering | DAWN 的依赖图可以指导搜索 |
| dVoting | 识别 uncertain tokens | Uncertain tokens 可能是依赖链的末端 |
| Confidence-based | 按 confidence 排序 | 依赖图比 confidence 更准确 |

### 6.4 具体研究方向

**Idea 1: 学习依赖图**

DAWN 用 KL divergence 计算依赖，开销大。

能否训练一个模型直接预测依赖图？

```python
dependency_predictor = train(
    inputs=masked_sequences,
    labels=dependency_graphs_from_dawn
)
```

**Idea 2: 依赖图 + Ordering**

用依赖图指导 ordering：

```python
def dependency_guided_ordering(dependency_graph):
    # 拓扑排序：先生成被依赖的 tokens
    return topological_sort(dependency_graph)
```

**Idea 3: 动态依赖图**

依赖关系可能随生成过程变化。

能否动态更新依赖图？

```python
for step in generation_steps:
    # 更新依赖图
    dependency_graph = update_graph(dependency_graph, new_tokens)
    
    # 基于更新后的图选择下一步
    next_positions = select_positions(dependency_graph)
```

---

## 7. 代码示例

```python
class DAWN:
    def __init__(self, model, influence_threshold=0.1):
        self.model = model
        self.threshold = influence_threshold
    
    def build_dependency_graph(self, masked_sequence):
        """构建依赖图"""
        masked_positions = get_masked_positions(masked_sequence)
        graph = defaultdict(list)
        
        for i in masked_positions:
            # 计算 unmask i 对其他位置的影响
            base_probs = self.model.predict_probs(masked_sequence)
            
            # Unmask position i
            unmasked = masked_sequence.copy()
            unmasked[i] = self.model.predict(masked_sequence, i)
            new_probs = self.model.predict_probs(unmasked)
            
            # 计算 KL divergence
            for j in masked_positions:
                if j != i:
                    kl = kl_divergence(base_probs[j], new_probs[j])
                    if kl > self.threshold:
                        graph[i].append(j)  # j depends on i
        
        return graph
    
    def select_positions(self, masked_sequence, graph, unmasked_positions):
        """选择下一批要 unmask 的位置"""
        masked_positions = get_masked_positions(masked_sequence)
        
        # Rule 1: 优先选择依赖于已 unmask 位置的
        reliable = []
        for pos in masked_positions:
            dependencies = get_dependencies(graph, pos)
            if all(d in unmasked_positions for d in dependencies):
                reliable.append(pos)
        
        # Rule 2: 从 reliable 中选择不强耦合的子集
        selected = []
        for pos in reliable:
            # 检查是否与已选位置强耦合
            coupled = any(pos in graph[s] or s in graph[pos] for s in selected)
            if not coupled:
                selected.append(pos)
        
        return selected
    
    def generate(self, masked_sequence):
        """DAWN 生成"""
        graph = self.build_dependency_graph(masked_sequence)
        unmasked_positions = set()
        
        while has_masked_positions(masked_sequence):
            # 选择要 unmask 的位置
            to_unmask = self.select_positions(
                masked_sequence, graph, unmasked_positions
            )
            
            # Unmask
            for pos in to_unmask:
                masked_sequence[pos] = self.model.predict(masked_sequence, pos)
                unmasked_positions.add(pos)
        
        return masked_sequence
```

---

## 8. 总结

DAWN 的贡献：

1. **问题分析**: 识别了并行解码失败的原因——token 依赖
2. **方法**: 构建依赖图，选择性 unmask
3. **结果**: 1.8-8.06x 加速，质量损失 <2%
4. **Training-free**: 可直接应用于任何 dLLM

**对 dLLM 研究最重要的启发：**

> Token 依赖关系是理解和优化 dLLM 的关键。
> 
> 依赖图可以指导 ordering、并行策略、和质量-速度权衡。
> 
> 下一步：能否学习依赖图，避免 O(n²) 的计算开销？

---

## 参考

- arXiv:2602.06953
- GitHub: https://github.com/lizhuo-luo/DAWN
