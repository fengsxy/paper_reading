# dLLM 研究趋势分析 (2025.09 - 2026.02)

基于 Scholar Inbox 推荐的 82 篇 dLLM 相关论文。

---

## 📊 总体统计

| 月份 | 论文数 | 主要热点 |
|------|--------|----------|
| 2025-09 | 7 | 早期探索，频率训练 |
| 2025-10 | 29 | **爆发期**，加速方法涌现 |
| 2025-11 | 5 | 相对平静 |
| 2025-12 | 13 | 系统优化，内存管理 |
| 2026-01 | 12 | 理论探索开始 |
| 2026-02 | 16 | decoding 策略多样化 |

---

## 🔥 研究热点分布

### 1. 加速/效率 (40 篇, 49%)
**这是绝对主流。** 几乎一半的论文在做加速。

关键工作：
- **Block Diffusion**: Fast-dLLM, AdaBlock-dLLM, FlashBlock
- **Parallel Decoding**: dParallel, CreditDecoding
- **Token Eviction**: FOCUS, Saber
- **Memory Optimization**: Taming Memory Footprint Crisis

**观察：** 这说明 dLLM 的核心痛点是 **速度**。社区在疯狂优化，但没人问 "为什么要用 dLLM"。

### 2. Training 方法 (17 篇, 21%)
- Reward-guided: RFG, Advantage Weighted Matching
- Alignment: Free Lunch Alignment, Visual Generation Tuning
- RL: Boundary-Guided Policy Optimization, UniRL-Zero

### 3. Decoding 策略 (16 篇, 20%)
- Variable length: ρ-EOS, CAL
- Sampling: FourierSampler, TAPS, Self-Rewarding SMC
- Order: Where-to-Unmask, Generation Order (info-theoretic)

### 4. 理论/机制理解 (6 篇, 7%)
**严重不足。** 只有 6 篇在做理论分析。

关键工作：
- Spectral Generative Flow Models
- DiffuSpeech (unified framework)
- Corrected Samplers for Discrete Flow

### 5. 安全 (1 篇, 1%)
**几乎空白。** 只有 1 篇关于 hallucination detection。

---

## 📈 时间线演变

```
2025-09: 早期探索
         └─ 频率训练、基础方法

2025-10: 爆发期 (29 篇!)
         └─ 加速方法大量涌现
         └─ LLaDA 热度带动

2025-11: 平静期
         └─ 消化前期工作

2025-12: 系统化
         └─ 内存优化、生产部署
         └─ Causal Concept-Guided

2026-01: 理论萌芽
         └─ "Top 10 Open Challenges" 出现
         └─ "Flexibility Trap" 质疑 dLLM
         └─ 你的论文 "Thinking Out of Order"

2026-02: 多样化
         └─ Decoding 策略百花齐放
         └─ 开始关注 open-ended generation
```

---

## 🎯 关键论文 (按重要性)

### 必读：理论/机制
1. **[2601.15165] The Flexibility Trap** - 质疑 dLLM 的 arbitrary order
2. **[2601.14041] Top 10 Open Challenges** - 领域综述
3. **[2510.06190] On Powerful Ways to Generate** - AR vs Diffusion 对比
4. **[2601.08893] Spectral Generative Flow Models** - 物理视角

### 必读：方法
1. **[2601.22947] AlignmentFlex** - Positional alignment 问题
2. **[2601.23278] FOCUS** - Token eviction 加速
3. **[2601.22527] ρ-EOS** - Variable length 解决方案
4. **[2601.23182] FourierSampler** - 频域 decoding

### 值得关注
1. **[2511.22146] C²DLM** - Causal Concept-Guided
2. **[2510.18114] Latent Discrete Diffusion** - 新架构
3. **[2602.11364] Energy of Falsehood** - Hallucination detection

---

## 🤔 我的观察

### 1. 这个领域在做什么？
**主要在做 engineering optimization，不是 fundamental research。**

- 49% 在加速
- 21% 在改 training
- 20% 在改 decoding
- 只有 7% 在理解机制

### 2. 什么问题被忽视了？

**问题 A: Diffusion 是 essential 还是 incidental？**
- 没人在问这个
- 如果 AR + MTP 能达到类似效果，dLLM 的 motivation 就有问题

**问题 B: 什么任务真正需要 dLLM？**
- 大家在 benchmark 上比，但没人问 "这个 benchmark 需要 dLLM 吗？"
- Yu 的论文给出了一个答案：reasoning tasks where output order ≠ reasoning order

**问题 C: Optimal generation order 是什么？**
- Where-to-Unmask 在学 order，但用的是 ground-truth guided
- 没有人从 first principles 推导 optimal order

**问题 D: dLLM 的 representation 有什么特殊性？**
- 没有人问 "bidirectional attention 学到了什么 AR 学不到的？"

### 3. 领域的隐含假设

这个领域有一个隐含假设：**dLLM 是 AR 的替代品，我们要让它更快、更好。**

但这个假设可能是错的。也许：
- dLLM 不是 AR 的替代品，而是 complement
- dLLM 只在特定任务上有优势
- Diffusion 本身不是 essential，只是实现 joint prediction 的一种方式

---

## 💡 Research Opportunities

### 高价值 + 低竞争
1. **Information-theoretic understanding of dLLM**
   - 用 MI 分析 bidirectional attention
   - 推导 optimal generation order
   - 与 Greg 的背景契合

2. **Task-Model Matching**
   - Formalize "什么任务需要 dLLM"
   - 建立 task → optimal model 的 mapping

3. **Learning Optimal Generation Order**
   - 不是 ground-truth guided
   - 而是 principled (e.g., MI-based)

### 高价值 + 高竞争
1. **加速** - 太多人在做
2. **Multimodal dLLM** - 开始有人做了

### 低价值
1. **又一个 decoding 策略** - 除非有 principled insight
2. **又一个 benchmark 提升** - incremental

---

*Generated: 2026-02-15*
*Data source: Scholar Inbox (2025-09 to 2026-02)*
