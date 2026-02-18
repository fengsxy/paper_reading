# Research Ideas v3: 第一性原理深度分析

*基于 Yu 的思考 + 100 篇相关论文调研*
*2026-02-16*

---

## 第一性原理：回到最本质的问题

### 问题 1: 为什么需要加速？

**本质：** 模型一次前向传播的信息量 >> 输出的 token 数

```
AR 模型：
- 一次前向传播 → 1 个 token
- 但 hidden states 包含了对整个序列的 "理解"
- 信息利用率极低

dLLM：
- 一次前向传播 → 多个 token（理论上）
- 但实际受限于 confidence threshold
- 信息利用率仍然不高
```

**你的核心洞察：Not all tokens are equal**
- 简单 token：模型早就 "知道" 了
- 难 token：需要更多计算

### 问题 2: 现有方法的本质是什么？

| 方法 | 本质 | 局限 |
|------|------|------|
| Speculative Decoding | 小模型 draft，大模型 verify | 小模型能力有限，acceptance rate 受限 |
| dLLM 并行解码 | 同时预测多个 token | Hard mask 丢信息，KV Cache 不兼容 |
| MTP | 直接预测多个 next tokens | 联合分布问题，只能 2-3 个 |
| Block Diffusion | 分块生成 | 块大小固定，不 adaptive |

**共同问题：** 都没有真正解决 "哪些 token 该并行，哪些该串行" 的问题

### 问题 3: 理想的解决方案是什么？

```
理想系统：
1. 自动识别 token 难度
2. 简单 token → 并行生成
3. 难 token → 更多计算（或 AR 锚定）
4. 不丢弃中间信息
5. 兼容 KV Cache
```

---

## 从论文中提取的关键 insight

### Insight 1: Confidence 是 difficulty 的 proxy

**来源：** Learning to Parallel, AdaBlock-dLLM, dParallel

```
观察：dLLM 的 confidence 分布天然反映 token 难度
- 高 confidence → 简单 token → 可以早期 commit
- 低 confidence → 难 token → 需要更多 refinement

问题：现有方法用固定 threshold，不 adaptive
```

### Insight 2: Soft mask > Hard mask

**来源：** EvoToken-DLM (Beyond Hard Masks), Residual Context Diffusion

```
EvoToken-DLM:
- 用 evolving soft token distributions 替代 hard binary masks
- 支持 revisable decoding
- "continuous trajectory supervision"

Residual Context Diffusion:
- 回收被丢弃 token 的计算
- "discarded tokens retain contextual information"

核心：不要一次性决定，保留修改的可能
```

### Insight 3: 物理位置 vs 逻辑位置解耦

**来源：** WeDLM

```
WeDLM 的核心创新：
- Topological Reordering: 物理位置和逻辑位置分离
- 保持 causal mask，但允许 bidirectional conditioning
- 兼容 prefix KV Cache

结果：3x speedup on reasoning, 10x on low-entropy generation
```

### Insight 4: 训练-推理对齐

**来源：** d3LLM

```
问题：训练时随机 mask，推理时结构化 unmask → mismatch

d3LLM 的解决方案：
- Pseudo-trajectory distillation
- 教模型 "哪些 token 可以在早期 confident 地解码"
- Entropy-based multi-block decoding

结果：10x speedup over vanilla LLaDA
```

### Insight 5: Adaptive block size

**来源：** AdaBlock-dLLM, Saber

```
问题：固定 block size 不 optimal
- 简单部分：block 可以大
- 难部分：block 应该小

AdaBlock-dLLM:
- Semantic-aware adaptive block size
- 根据内容难度动态调整

Saber:
- Adaptive acceleration + backtracking
- 允许 "后悔"：发现错误时回退
```

---

## 综合分析：Gap 在哪里？

### Gap 1: dLLM 作为 Speculative Decoding 的 Drafter

**现状：** 没有人做过

**为什么有价值：**
- dLLM 天然是 difficulty-aware 的（confidence 分布）
- dLLM 可以并行 draft 多个 token
- 比小模型 drafter 更 "聪明"

**挑战：**
- KV Cache 兼容性 → WeDLM 的位置解耦可以解决
- Acceptance rate → 需要实验验证

### Gap 2: Soft Mask + Remask 的统一框架

**现状：**
- EvoToken-DLM: soft mask
- Saber: backtracking (remask)
- 没有人把两者结合

**为什么有价值：**
- Soft mask 保留信息
- Remask 允许修正错误
- 结合 = 更 robust 的生成

### Gap 3: Difficulty-Aware Parallel Decoding

**现状：**
- 现有方法用固定 threshold 或 learned policy
- 没有人显式建模 "token difficulty"

**为什么有价值：**
- 如果能准确预测 difficulty，可以最优分配计算
- 简单 token 并行，难 token 串行

### Gap 4: Answer-First Generation 的系统研究

**现状：** 没有人做过

**你的想法：**
> "如果把最难的部分（答案）先给出，CoT 生成是否能大幅加速？"

**为什么有价值：**
- 验证 dLLM 是否真的能利用 "锚点" 信息
- 如果成立，可以设计 AR+dLLM 混合系统

---

## 具体 Research Ideas

### Idea 1: dLLM-Guided Speculative Decoding

**核心假设：** dLLM 的 confidence 可以指导 speculative decoding

**方案：**
```
Phase 1: dLLM Draft
- dLLM 并行预测 k 个 token
- 输出 confidence scores

Phase 2: Selective Verification
- 高 confidence token: 直接接受（或轻量验证）
- 低 confidence token: 送给 AR 模型验证

Phase 3: KV Cache 兼容
- 用 WeDLM 的 Topological Reordering
- 保持 causal structure
```

**实验设计：**
```python
# 1. 测量 dLLM confidence 与 AR acceptance 的相关性
for prompt in test_prompts:
    dllm_tokens, dllm_conf = dllm.generate(prompt)
    ar_accepted = ar_model.verify(dllm_tokens)
    correlation.append(corr(dllm_conf, ar_accepted))

# 2. 对比不同 drafter
compare(
    small_model_drafter,  # 传统 speculative decoding
    dllm_drafter,         # 我们的方法
    metrics=['acceptance_rate', 'speedup', 'quality']
)
```

**预期贡献：**
- 新的 speculative decoding 范式
- 利用 dLLM 的 difficulty-awareness
- 可能比小模型 drafter 更高的 acceptance rate

**Novelty: 9/10, Feasibility: 7/10**

---

### Idea 2: Unified Soft-Mask + Remask Framework

**核心假设：** Soft mask 和 remask 是同一个 spectrum 的两端

**理论框架：**
```
传统 dLLM:
- Hard mask: token ∈ {MASK, revealed}
- 一旦 reveal，不能修改

Soft mask (EvoToken-DLM):
- token ∈ [0, 1]^V (distribution over vocabulary)
- 逐渐 "固化"

Remask (Saber):
- 允许把 revealed token 重新 mask
- 但仍然是 binary

统一框架:
- token ∈ [0, 1]^V
- "固化程度" 是连续的
- 低 confidence token 自动保持 "软" 状态
- 高 confidence token 逐渐 "硬化"
- Remask = 降低固化程度
```

**实验设计：**
```python
# 1. 实现 unified soft-remask
class SoftRemaskDLLM:
    def step(self, x_t, t):
        logits = self.model(x_t, t)
        confidence = softmax(logits).max(dim=-1)
        
        # 固化程度 = f(confidence, step)
        hardness = self.compute_hardness(confidence, t)
        
        # 软更新
        x_next = hardness * argmax(logits) + (1 - hardness) * x_t
        
        return x_next

# 2. 对比
compare(
    hard_mask_dllm,
    soft_mask_dllm,  # EvoToken
    remask_dllm,     # Saber
    unified_dllm,    # 我们的方法
)
```

**预期贡献：**
- 统一 soft mask 和 remask
- 更 robust 的生成
- 理论上更优雅

**Novelty: 8/10, Feasibility: 8/10**

---

### Idea 3: Answer-Anchored CoT Generation

**核心假设：** 给定答案后，dLLM 生成 CoT 会大幅加速

**你的原话：**
> "我想测试如果我把一道题里面最难的部分例如答案给定之后 CoT 生成是不是可以很 aggressive 的加速"

**实验设计：**
```python
# Setup
question = "What is 123 * 456?"
answer = "56088"

# Condition 1: Normal generation
prompt_normal = f"Q: {question}\nA: Let's think step by step."
output_normal, steps_normal = dllm.generate(prompt_normal)

# Condition 2: Answer-first (infilling)
prompt_anchored = f"Q: {question}\nA: Let's think step by step. [MASK] The answer is {answer}."
output_anchored, steps_anchored = dllm.infill(prompt_anchored)

# Metrics
compare(steps_normal, steps_anchored)  # 预期: steps_anchored << steps_normal
compare(confidence_normal, confidence_anchored)  # 预期: confidence_anchored 更高
```

**深入分析：**
```python
# 分析 confidence 分布变化
for step in range(num_steps):
    conf_normal = get_confidence(dllm, prompt_normal, step)
    conf_anchored = get_confidence(dllm, prompt_anchored, step)
    
    # 预期：anchored 版本的 confidence 整体更高
    # 特别是靠近答案的 token
    plot_confidence_heatmap(conf_normal, conf_anchored)
```

**如果成立，下一步：**
- 设计 AR+dLLM 混合系统
- AR 生成 "锚点"（难 token）
- dLLM 快速填充中间部分

**预期贡献：**
- 验证 dLLM 的 difficulty-awareness
- 为 AR+dLLM 混合系统提供理论基础
- 可能发现新的 reasoning 加速方法

**Novelty: 8/10, Feasibility: 9/10**

---

### Idea 4: Difficulty Predictor for Optimal Parallelism

**核心假设：** 如果能准确预测 token difficulty，可以最优分配计算

**方案：**
```
Phase 1: 训练 Difficulty Predictor
- 输入: prompt + partial generation
- 输出: 每个 position 的 difficulty score
- 训练数据: 从 dLLM 的 confidence 分布中提取

Phase 2: Difficulty-Guided Decoding
- 高 difficulty positions: 更多 denoising steps
- 低 difficulty positions: 早期 commit

Phase 3: 与 Speculative Decoding 结合
- 高 difficulty: AR 模型生成
- 低 difficulty: dLLM 并行生成
```

**实验设计：**
```python
# 1. 收集 difficulty 数据
difficulty_data = []
for prompt in training_prompts:
    # 跑完整的 dLLM generation
    for step in range(num_steps):
        logits = dllm(x_t, t)
        confidence = softmax(logits).max(dim=-1)
        
        # 记录每个 position 的 "difficulty"
        # difficulty = 需要多少步才能 confident
        difficulty_data.append((prompt, position, steps_to_confident))

# 2. 训练 predictor
predictor = train_difficulty_predictor(difficulty_data)

# 3. 用 predictor 指导 decoding
def guided_decode(prompt):
    difficulty = predictor(prompt)
    
    # 分配计算
    for pos in positions:
        if difficulty[pos] > threshold:
            # 用 AR 或更多 steps
            tokens[pos] = ar_model.generate_one(prompt, pos)
        else:
            # 用 dLLM 并行
            pass
```

**预期贡献：**
- 显式建模 token difficulty
- 最优分配计算资源
- 可能比 learned parallel decoding 更 interpretable

**Novelty: 9/10, Feasibility: 6/10**

---

### Idea 5: WeDLM + Speculative Decoding

**核心假设：** WeDLM 的位置解耦可以让 dLLM 作为 speculative decoding 的 drafter

**WeDLM 的关键创新：**
```
Topological Reordering:
- 物理位置: [1, 2, 3, 4, 5, 6, 7, 8]
- 逻辑位置: [1, 2, 5, 6, 3, 4, 7, 8]

效果:
- 保持 causal mask
- 但允许 bidirectional conditioning
- 兼容 prefix KV Cache
```

**用于 Speculative Decoding：**
```
1. dLLM (with WeDLM) draft k tokens
   - 用 bidirectional attention 获得更好的 draft
   - 但输出是 causally ordered

2. AR verifier 验证
   - 可以直接用 KV Cache
   - 不需要重新计算 prefix

3. 接受/拒绝
   - 接受的 token 加入 KV Cache
   - 拒绝的 token 由 AR 重新生成
```

**实验设计：**
```python
# 1. 实现 WeDLM-based drafter
class WeDLMDrafter:
    def draft(self, prefix, k):
        # 用 WeDLM 的 topological reordering
        # 生成 k 个 token
        return tokens, confidence

# 2. 对比
compare(
    small_model_drafter,
    vanilla_dllm_drafter,  # 不兼容 KV Cache
    wedlm_drafter,         # 兼容 KV Cache
)
```

**预期贡献：**
- 解决 dLLM + speculative decoding 的兼容性问题
- 利用 dLLM 的 bidirectional attention 优势
- 可能比小模型 drafter 更高的 acceptance rate

**Novelty: 8/10, Feasibility: 7/10**

---

## 综合推荐

| Idea | Novelty | Feasibility | 核心贡献 |
|------|---------|-------------|----------|
| 1: dLLM-Guided Spec | 9 | 7 | 新的 speculative decoding 范式 |
| 2: Unified Soft-Remask | 8 | 8 | 统一框架 |
| 3: Answer-Anchored CoT | 8 | 9 | 验证 difficulty-awareness |
| 4: Difficulty Predictor | 9 | 6 | 显式建模 difficulty |
| 5: WeDLM + Spec | 8 | 7 | 解决兼容性问题 |

### 🥇 最推荐：Idea 3 (Answer-Anchored CoT)

**理由：**
1. **Feasibility 最高** — 不需要改架构，只需要改 prompt
2. **验证核心假设** — dLLM 是否真的 difficulty-aware
3. **为其他 idea 铺路** — 如果成立，Idea 1, 4, 5 都有了理论基础
4. **1-2 周出结果**

### 🥈 次选：Idea 1 (dLLM-Guided Speculative Decoding)

**理由：**
- 如果 Idea 3 成立，这个是自然的下一步
- 需要更多工程工作，但 impact 更大

### 🥉 备选：Idea 5 (WeDLM + Speculative Decoding)

**理由：**
- 解决了关键的兼容性问题
- WeDLM 代码已经开源

---

## 实验路线图

```
Week 1-2: Idea 3 (Answer-Anchored CoT)
├── 在 GSM8K 上测试
├── 测量 steps 和 confidence 变化
└── 分析结果

Week 3-4: 根据 Idea 3 结果决定
├── 如果成立 → Idea 1 (dLLM-Guided Spec)
└── 如果不成立 → Idea 2 (Unified Soft-Remask)

Week 5-8: 深入实验 + 写论文
```

---

## 回答你的 Open Questions

### Q: 为什么 MTP 失败，dLLM 成功？

**更深入的分析：**

```
MTP 的问题：
1. 训练：预测固定位置的 next k tokens
2. 假设：P(x_{t+1}, ..., x_{t+k} | x_{<t}) ≈ Π P(x_{t+i} | x_{<t})
3. 问题：这个独立性假设不成立
4. 结果：联合分布 error 随 k 指数增长

dLLM 的优势：
1. 训练：随机 mask，预测任意位置
2. 机制：迭代 refinement，每一步都考虑其他 tokens
3. 效果：隐式处理联合分布
4. 关键：可以 defer 不确定的 token

DeepSeek V3 只能 2-3 个的原因：
- 没有 defer 机制
- 必须一次性决定所有 k 个 tokens
- 联合分布 error 限制了 k
```

### Q: dLLM 的 confidence 真的反映 difficulty 吗？

**需要实验验证：**
```python
# 实验设计
for task in ['gsm8k', 'arc', 'hellaswag']:
    for prompt in task.prompts:
        # 1. 跑 dLLM，记录 confidence
        tokens, confidence = dllm.generate(prompt)
        
        # 2. 用 AR 模型验证每个 token 的 "difficulty"
        # difficulty = AR 模型在该位置的 perplexity
        difficulty = ar_model.get_perplexity(prompt, tokens)
        
        # 3. 计算相关性
        corr = correlation(confidence, 1/difficulty)
        
# 预期：高 confidence ↔ 低 difficulty
```

---

*Generated: 2026-02-16*
*基于 Yu 的思考 + 100 篇论文调研*
