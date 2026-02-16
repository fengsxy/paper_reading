# RCD: 回收被丢弃 Token 的计算

**论文:** Residual Context Diffusion Language Models  
**arXiv:** 2601.22954  
**作者:** Berkeley, Sewon Min, Kurt Keutzer, Amir Gholami 等  
**关键词:** Residual context, Computation recycling, Remasking, AIME

---

## 1. 核心问题：Remasking 浪费计算

当前 dLLM 的 remasking 机制：
1. 每步预测所有 masked 位置
2. 只保留最 confident 的 token
3. **丢弃其他 token 的计算**

```
Step 1: 预测 [A] [B] [C] [D] [E]
        Conf: 0.9 0.3 0.8 0.2 0.7
        保留: [A]     [C]     [E]
        丢弃:     [B]     [D]      ← 计算浪费！

Step 2: 重新预测 [B] [D]
        但之前的计算完全没用上
```

**问题：** 被丢弃的 token 虽然不够 confident，但包含有用的 **contextual information**。

---

## 2. 核心洞察：被丢弃的 Token 有价值

论文的关键发现：

> **被丢弃的 token representations 包含对后续解码有用的上下文信息。**

实验验证：
- 把被丢弃的 representation 注入下一步
- 准确率提升 5-10%

**这些 "失败" 的预测不是垃圾，而是有价值的 context！**

---

## 3. 方法：Residual Context Diffusion (RCD)

### 3.1 核心思想

不丢弃被 remask 的 token，而是把它们的 representation 作为 **residual context** 注入下一步。

```
Step 1: 预测 [A] [B] [C] [D] [E]
        保留: [A]     [C]     [E]
        Residual: repr([B]), repr([D])  ← 保存！

Step 2: 预测 [B] [D]
        输入: masked + residual([B], [D])  ← 注入！
```

### 3.2 Residual Injection

```python
class RCD(nn.Module):
    def __init__(self, base_model):
        self.base_model = base_model
        self.residual_proj = nn.Linear(d_model, d_model)
    
    def forward(self, x, residual_context):
        # 基础模型的 hidden states
        h = self.base_model.encode(x)
        
        # 注入 residual context
        if residual_context is not None:
            residual = self.residual_proj(residual_context)
            h = h + residual  # 残差连接
        
        # 解码
        return self.base_model.decode(h)
```

### 3.3 两阶段训练

直接端到端训练 RCD 会有 **内存瓶颈**（需要存储所有中间 representation）。

论文提出 **decoupled two-stage training**：

**Stage 1:** 训练 base model（标准 dLLM 训练）

**Stage 2:** 冻结 base model，只训练 residual projection
- 用 Stage 1 的 checkpoint
- 只需要 ~1B tokens
- 内存友好

---

## 4. 实验结果

### 4.1 主要结果

| Model | Benchmark | Base | + RCD | Improvement |
|-------|-----------|------|-------|-------------|
| SDAR | AIME | 12.3% | 23.1% | **+10.8%** |
| SDAR | MATH500 | 45.2% | 52.8% | +7.6% |
| LLaDA | GSM8K | 68.5% | 74.2% | +5.7% |
| LLaDA | HumanEval | 42.1% | 47.8% | +5.7% |

**AIME 上准确率几乎翻倍！**

### 4.2 Step 效率

| Accuracy Target | Base Steps | RCD Steps | Reduction |
|-----------------|------------|-----------|-----------|
| 40% | 20 | 8 | 4x |
| 50% | 30 | 12 | 2.5x |
| 60% | 50 | 20 | 2.5x |

RCD 用更少的 step 达到相同准确率。

### 4.3 训练效率

| | Base Training | RCD Stage 2 |
|---|---|---|
| Tokens | 100B+ | ~1B |
| Time | Days | Hours |
| Memory | High | Low |

RCD 的额外训练成本很低。

---

## 5. 深度分析

### 5.1 为什么 Residual Context 有效？

**假设：** 被丢弃的 token 虽然预测错误，但 representation 编码了：
- 对正确答案的 "猜测"
- 周围 context 的理解
- 不确定性信息

这些信息对下一步预测有帮助。

### 5.2 与 Soft Remask 的联系

RCD 是一种 **soft remasking**：
- Hard remask: 完全丢弃被 remask 的 token
- Soft remask (RCD): 保留 representation 作为 residual

这和之前讨论的 "Beyond Hard Mask" 思想一致！

### 5.3 与 dVoting 的联系

dVoting 发现：uncertain token 决定性能。

RCD 发现：uncertain token 的 representation 有价值。

**结合：** 对 uncertain token 既做 voting，又保留 residual。

### 5.4 与 Ordering 的联系

RCD 隐式地实现了一种 ordering：
- 先确定 confident token
- 用它们的 context 帮助 uncertain token

这和 difficulty-based ordering 的思想一致。

---

## 6. 对 dLLM 研究的启发

### 6.1 不要浪费计算

当前 dLLM 的 remasking 浪费了大量计算。

RCD 证明了：**被丢弃的计算可以回收利用。**

### 6.2 Representation 比 Token 更有价值

Token 是离散的，要么对要么错。

Representation 是连续的，即使预测错误也包含有用信息。

**启发：** 应该更多地利用 representation，而不只是 token。

### 6.3 研究方向

**Idea 1: Multi-Step Residual**

不只保留上一步的 residual，保留多步：

```python
residual = alpha_1 * residual_t1 + alpha_2 * residual_t2 + ...
```

**Idea 2: Selective Residual**

不是所有被丢弃的 token 都有价值，选择性保留：

```python
# 只保留 "差一点就对" 的 token
keep_residual = (confidence > 0.3) & (confidence < 0.7)
```

**Idea 3: Residual-Guided Ordering**

用 residual 的质量指导 ordering：
- Residual 质量高 → 这个位置快要收敛了
- Residual 质量低 → 需要更多 context

---

## 7. 代码示例

```python
class ResidualContextDiffusion:
    def __init__(self, base_model, residual_dim):
        self.base_model = base_model
        self.residual_proj = nn.Linear(residual_dim, residual_dim)
        self.residual_gate = nn.Linear(residual_dim, 1)
    
    def decode(self, masked_sequence, num_steps):
        residual_context = None
        
        for step in range(num_steps):
            # Forward with residual injection
            hidden, logits = self.base_model(
                masked_sequence, 
                residual=residual_context
            )
            
            # 选择要 unmask 的位置
            confidence = logits.softmax(-1).max(-1).values
            unmask_mask = confidence > threshold
            
            # 保存被 remask 位置的 representation 作为 residual
            remask_mask = ~unmask_mask & (masked_sequence == MASK)
            if remask_mask.any():
                new_residual = self.residual_proj(hidden[remask_mask])
                
                # Gated combination with previous residual
                if residual_context is not None:
                    gate = self.residual_gate(new_residual).sigmoid()
                    residual_context[remask_mask] = (
                        gate * new_residual + 
                        (1 - gate) * residual_context[remask_mask]
                    )
                else:
                    residual_context = torch.zeros_like(hidden)
                    residual_context[remask_mask] = new_residual
            
            # Unmask
            masked_sequence[unmask_mask] = logits[unmask_mask].argmax(-1)
        
        return masked_sequence
```

---

## 8. 总结

| 贡献 | 内容 |
|------|------|
| 问题 | Remasking 浪费被丢弃 token 的计算 |
| 洞察 | 被丢弃的 representation 包含有用 context |
| 方法 | Residual injection + 两阶段训练 |
| 效果 | AIME 准确率翻倍，step 减少 2.5-4x |

**核心启发：** 

> 不要只看 token，要看 representation。
> 
> 被丢弃的计算不是垃圾，而是有价值的 context。
> 
> Soft remasking > Hard remasking。

---

## 参考

- arXiv:2601.22954
- Berkeley AI Research
