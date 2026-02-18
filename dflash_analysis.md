# DFlash 代码分析 + Difficulty-Aware 改进方案

## DFlash 核心流程

```python
# spec_generate 的核心逻辑：

# 1. Prefill: target model 处理 input
output = target(input_ids, ...)
target_hidden = extract_context_feature(output.hidden_states, self.target_layer_ids)

# 2. Decode loop:
while start < max_length:
    # 2.1 Draft: 用 block diffusion 生成 block_size 个 token
    block_output_ids = output_ids[:, start : start + block_size].clone()
    noise_embedding = target.model.embed_tokens(block_output_ids)
    
    # 关键：draft model 用 target_hidden 作为 conditioning
    draft_logits = target.lm_head(self(
        target_hidden=target_hidden,
        noise_embedding=noise_embedding,
        ...
    ))
    
    # 2.2 Sample draft tokens
    block_output_ids[:, 1:] = sample(draft_logits)  # 直接 argmax/sample
    
    # 2.3 Verify: target model 验证
    output = target(block_output_ids, ...)
    posterior = sample(output.logits, temperature)
    
    # 2.4 计算 acceptance length
    acceptance_length = (block_output_ids[:, 1:] == posterior[:, :-1]).cumprod(dim=1).sum()
    
    # 2.5 更新
    start += acceptance_length + 1
```

## 关键观察

### 1. Draft 是 "盲目" 的
```python
block_output_ids[:, 1:] = sample(draft_logits)  # 没有 confidence 信息
```
- 直接 sample，不管 confidence 高低
- 所有位置同等对待

### 2. Verification 是 "被动" 的
```python
acceptance_length = (block_output_ids[:, 1:] == posterior[:, :-1]).cumprod(dim=1).sum()
```
- 只能接受/拒绝
- 一旦遇到第一个不匹配，后面全部拒绝（cumprod）

### 3. 没有利用 draft_logits 的 confidence
```python
draft_logits = target.lm_head(self(...))
# draft_logits 包含 confidence 信息，但没有用！
```

---

## Difficulty-Aware 改进方案

### 方案 A: Confidence-Guided Sampling

```python
# 原始：直接 sample
block_output_ids[:, 1:] = sample(draft_logits)

# 改进：根据 confidence 调整 sampling
probs = F.softmax(draft_logits, dim=-1)
confidence = probs.max(dim=-1).values  # [batch, block_size-1]

# 高 confidence: 用 argmax (greedy)
# 低 confidence: 用 temperature sampling (探索)
for i in range(block_size - 1):
    if confidence[0, i] > high_threshold:
        block_output_ids[0, i+1] = draft_logits[0, i].argmax()
    else:
        # 低 confidence 位置，多采样几次，选最好的
        candidates = [sample(draft_logits[0, i:i+1], temp=1.0) for _ in range(k)]
        # 用某种方式选最好的（比如 target model 打分）
        block_output_ids[0, i+1] = select_best(candidates)
```

**问题：** 这样会增加计算量，可能抵消加速效果

### 方案 B: Adaptive Block Size

```python
# 原始：固定 block_size
block_output_ids = output_ids[:, start : start + block_size]

# 改进：根据 confidence 动态调整 block size
# 先用少量 steps 预测 confidence
probs = F.softmax(draft_logits, dim=-1)
confidence = probs.max(dim=-1).values

# 找到第一个低 confidence 位置
first_hard = (confidence < threshold).nonzero()
if first_hard.numel() > 0:
    adaptive_block_size = min(first_hard[0].item() + 1, block_size)
else:
    adaptive_block_size = block_size

# 只 draft 到第一个难的位置
block_output_ids = output_ids[:, start : start + adaptive_block_size]
```

**优点：** 不增加计算量，只是更聪明地选择 block size
**问题：** 可能导致 block size 太小，反而变慢

### 方案 C: Confidence-Weighted Verification (最有潜力)

```python
# 原始：严格匹配
acceptance_length = (block_output_ids[:, 1:] == posterior[:, :-1]).cumprod(dim=1).sum()

# 问题：一旦不匹配就全部拒绝，太严格了

# 改进思路：
# 如果 draft 的 confidence 很高，但 target 给了不同的 token，
# 可能是因为两者都是合理的选择（比如同义词）
# 这种情况下，可以考虑 "软接受"

probs = F.softmax(draft_logits, dim=-1)
draft_confidence = probs.max(dim=-1).values

target_probs = F.softmax(output.logits, dim=-1)
# 检查 draft token 在 target 分布中的概率
draft_token_prob_in_target = target_probs.gather(-1, block_output_ids[:, 1:].unsqueeze(-1)).squeeze(-1)

# 如果 draft token 在 target 分布中概率也不低，可以接受
soft_accept = draft_token_prob_in_target > soft_threshold

# 结合 hard match 和 soft accept
match = (block_output_ids[:, 1:] == posterior[:, :-1]) | soft_accept
acceptance_length = match.cumprod(dim=1).sum()
```

**这个方向更有意思！** 因为：
1. 不增加 draft 的计算量
2. 利用了 target model 的信息
3. 可能提高 acceptance rate

---

## 最推荐的改进方向

### 核心 Idea: Soft Acceptance with Difficulty Awareness

**观察：** 
- DFlash 的 acceptance 是 hard match：draft == target
- 但有时候 draft 和 target 都是合理的（比如 "the" vs "a"）
- 这种情况下强制拒绝是浪费

**改进：**
```python
def soft_verify(draft_tokens, draft_logits, target_logits, threshold=0.1):
    """
    Soft verification: 
    - Hard match: draft == target.argmax() → accept
    - Soft match: draft 在 target 分布中概率 > threshold → accept
    """
    target_probs = F.softmax(target_logits, dim=-1)
    
    # draft token 在 target 分布中的概率
    draft_prob_in_target = target_probs.gather(-1, draft_tokens.unsqueeze(-1)).squeeze(-1)
    
    # Hard match
    hard_match = draft_tokens == target_logits.argmax(dim=-1)
    
    # Soft match: draft 虽然不是 argmax，但概率也不低
    soft_match = draft_prob_in_target > threshold
    
    # 接受条件：hard match OR soft match
    accept = hard_match | soft_match
    
    return accept.cumprod(dim=1).sum()
```

**为什么这个方向好：**
1. **不改变 draft 过程** — 只改 verification
2. **理论上合理** — 如果 draft token 在 target 分布中概率高，说明 target 也认为这是合理的
3. **可能显著提高 acceptance rate** — 尤其是对于 "等价" 的 token
4. **实验简单** — 只需要改几行代码

---

## 实验计划

### Week 1: 验证假设
```python
# 分析 DFlash 的 rejection 原因
for prompt in test_prompts:
    draft_tokens, draft_logits = dflash.draft(prompt)
    target_logits = target.forward(draft_tokens)
    
    # 统计：被拒绝的 token 中，有多少在 target 分布中概率 > 0.1？
    rejected_mask = draft_tokens != target_logits.argmax(dim=-1)
    rejected_prob = target_probs[rejected_mask].gather(-1, draft_tokens[rejected_mask])
    
    print(f"Rejected tokens with prob > 0.1: {(rejected_prob > 0.1).sum()}")
```

如果这个数字很大，说明 soft acceptance 有潜力。

### Week 2: 实现 + 对比
```python
# 对比
compare(
    dflash_original,
    dflash_soft_accept_0.1,
    dflash_soft_accept_0.05,
    dflash_soft_accept_0.2,
)
```

### Week 3: 分析 + 写作
- 分析什么情况下 soft acceptance 帮助最大
- 分析 threshold 的选择
- 写 ablation study

---

## 总结

**最推荐的改进：Soft Acceptance**

| 方面 | 原始 DFlash | Soft Acceptance |
|------|-------------|-----------------|
| Draft | 不变 | 不变 |
| Verify | Hard match | Hard OR Soft match |
| 计算量 | 不变 | 几乎不变（只多一个 gather） |
| Acceptance rate | baseline | 可能更高 |

**这个方向的优点：**
1. 改动最小（几行代码）
2. 不增加计算量
3. 理论上合理
4. 容易验证

**你觉得这个方向可行吗？**
