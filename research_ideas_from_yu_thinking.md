# Research Ideas：基于 Yu 的思考

*2026-02-16*

---

## 你的核心洞察

### 洞察 1: Not all tokens are equal
- 模型一次前向传播的信息量 >> 一个 token
- AR 架构是瓶颈：模型可能第一层就知道答案，但只能一个个吐
- dLLM 和 speculative decoding 都在突破这个限制

### 洞察 2: dLLM 的本质优势
- **Difficulty-aware**: confidence 分布天然反映 token 难度
- **Defer 机制**: 不确定的 token 可以推迟决定
- **并行能力**: 简单 token 可以一次性出

### 洞察 3: dLLM 的核心问题
1. 预训练效率低 → 解法：finetune AR model
2. 训练推理不对齐 → 解法：d3LLM 的 trajectory distillation
3. KV Cache 不能用 → 解法：WeDLM 的位置解耦
4. Hard mask 丢信息 → 解法：soft/progressive mask

### 洞察 4: MTP 为什么失败，dLLM 为什么成功？
- MTP：联合分布问题，预测数量受限（DeepSeek V3 只能 2-3 个）
- dLLM：训练更激进（随机 mask），可以 defer 不确定 token

---

## 从你的思考中提炼的 Idea

### Idea A: dLLM 作为 Speculative Decoding 的 Drafter

**核心假设：** dLLM 的 confidence 可以指导哪些 token 需要 AR 验证

**具体方案：**
```
1. dLLM 并行预测多个 token，输出 confidence
2. 高 confidence token → 直接接受
3. 低 confidence token → 送给 AR 模型验证/生成
4. 用 WeDLM 的位置解耦来兼容 AR 的 KV Cache
```

**为什么可能 work：**
- dLLM 天然是 difficulty-aware 的
- 简单 token 不需要大模型验证
- 难 token 由 AR 锚定后，dLLM 可以快速填充

**实验验证：**
1. 测量 dLLM confidence 与 token 难度的相关性
2. 对比：dLLM drafter vs 小模型 drafter 的 acceptance rate

**Baseline 代码：**
- LLaDA: https://github.com/ML-GSAI/LLaDA
- Speculative decoding: HuggingFace 有实现

**评分：Novelty 9/10, Feasibility 7/10**

---

### Idea B: Answer-First CoT Generation

**核心假设：** 如果先给出最难的部分（答案），dLLM 生成 CoT 会大幅加速

**你的原话：**
> "我想测试如果我把一道题里面最难的部分例如答案给定之后 CoT 生成是不是可以很 aggressive 的加速"

**具体方案：**
```
1. 给定 question + answer
2. 让 dLLM 生成中间的 CoT
3. 测量：
   - 生成速度 vs 正常生成
   - 需要的 denoising steps
   - Confidence 分布变化
```

**为什么可能 work：**
- 答案是 "锚点"，降低了其他 token 的不确定性
- dLLM 的双向 attention 可以利用答案信息
- 类似于 "填空" 而不是 "生成"

**实验设计：**
```python
# 正常生成
prompt = "Question: ... Let's think step by step."
output = dllm.generate(prompt, max_tokens=500)

# Answer-first 生成
prompt = "Question: ... The answer is 42. Let's think step by step."
# mask 掉中间的 CoT 部分，保留答案
output = dllm.infill(prompt, mask_positions=[...])

# 对比
compare(normal_steps, answer_first_steps)
compare(normal_confidence, answer_first_confidence)
```

**预期结果：**
- Answer-first 需要更少的 denoising steps
- Confidence 整体更高
- 如果成立，说明 dLLM 确实是 difficulty-aware 的

**评分：Novelty 8/10, Feasibility 9/10**

---

### Idea C: Soft Remask + Beyond Hard Mask 结合

**你的原话：**
> "Remask 算法和 Beyond Hard Mask 的方法如何结合到一起"

**核心问题：** 当前 dLLM 的 hard mask 丢弃太多信息

**现有方法：**
- Hard mask: 一次性决定 mask/unmask
- Soft mask (Beyond Hard Masks): progressive token evolution
- Remask: 允许重新 mask 已生成的 token

**结合方案：**
```
1. 不用 hard mask，用 soft confidence scores
2. 每一步：
   - 高 confidence token: 逐渐 "固化"
   - 低 confidence token: 保持 "软" 状态，可以被修改
3. Remask 变成自然的：低 confidence token 自动被重新考虑
```

**为什么可能 work：**
- 保留更多中间信息
- 允许模型 "改变主意"
- 更接近人类写作过程（draft → revise）

**实验设计：**
```python
# 测量 Beyond Hard Mask 的 token 变化
for step in range(num_steps):
    logits = model(x_t)
    confidence = softmax(logits).max(dim=-1)
    
    # 记录每个 position 的 token 变化
    track_token_changes(step, predicted_tokens, confidence)

# 分析
plot_token_stability_vs_confidence()
plot_final_quality_vs_soft_threshold()
```

**评分：Novelty 7/10, Feasibility 8/10**

---

### Idea D: WeDLM 位置解耦用于 Speculative Decoding

**你的原话：**
> "深入的看类似 WeDLM 这样物理顺序和逻辑顺序的架构能否用到投机采样里面"

**核心问题：** dLLM 的双向 attention 与 AR 的 KV Cache 不兼容

**WeDLM 的方案：**
```
物理位置: [1, 2, 3, 4, 5, 6, 7, 8]
逻辑位置: [1, 2, 5, 6, 3, 4, 7, 8]  (重排后)

预测时用双向 attention
重排后保证因果性，可以用 KV Cache
```

**用于 Speculative Decoding：**
```
1. dLLM drafter 用双向 attention 预测多个 token
2. 重排成因果顺序
3. AR verifier 用 KV Cache 验证
4. 接受的 token 加入 KV Cache
5. 拒绝的 token 由 AR 重新生成
```

**为什么可能 work：**
- 解决了 dLLM 与 AR 的兼容性问题
- dLLM 可以利用双向信息做更好的 draft
- AR 的 KV Cache 不受影响

**挑战：**
- 重排的 overhead
- 如何处理被拒绝的 token

**评分：Novelty 8/10, Feasibility 6/10**

---

## 综合推荐

| Idea | Novelty | Feasibility | 核心贡献 |
|------|---------|-------------|----------|
| A: dLLM as Drafter | 9 | 7 | 新的 speculative decoding 范式 |
| B: Answer-First CoT | 8 | 9 | 验证 difficulty-aware 假设 |
| C: Soft Remask | 7 | 8 | 改进 dLLM 推理 |
| D: 位置解耦 + Spec | 8 | 6 | 解决兼容性问题 |

### 🥇 最推荐：Idea B (Answer-First CoT)

**理由：**
1. **Feasibility 最高** — 不需要改架构，只需要改 prompt
2. **验证核心假设** — 如果成立，证明 dLLM 是 difficulty-aware 的
3. **为 Idea A 铺路** — 如果 B 成立，A 就有了理论基础
4. **实验简单** — 1-2 周可以出结果

**具体 action plan：**
```
Week 1: 
- 在 GSM8K 上测试 answer-first vs normal generation
- 测量 denoising steps 和 confidence

Week 2:
- 分析结果
- 如果成立，设计 Idea A 的实验
```

### 🥈 次选：Idea A (dLLM as Drafter)

**理由：**
- 如果 Idea B 成立，这个就是自然的下一步
- 需要更多工程工作

---

## 你的 Open Questions 的回答

### Q: 为什么 MTP 失败，dLLM 成功？

**我的理解：**

1. **训练方式不同**
   - MTP: 预测固定位置的 next k tokens
   - dLLM: 随机 mask，预测任意位置

2. **联合分布处理不同**
   - MTP: 假设 tokens 独立，但实际不独立 → 分布 mismatch
   - dLLM: 迭代 refinement，每一步都考虑其他 tokens → 隐式处理联合分布

3. **Defer 机制**
   - MTP: 必须一次性决定所有 k 个 tokens
   - dLLM: 不确定的 token 可以推迟到下一步

4. **DeepSeek V3 只能 2-3 个的原因**
   - 联合分布的 error 随 k 指数增长
   - dLLM 通过迭代 refinement 避免了这个问题

---

*Generated: 2026-02-16*
*基于 Yu 的思考整理*
