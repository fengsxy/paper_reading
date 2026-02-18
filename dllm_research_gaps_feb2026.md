# Diffusion Language Models: Research Gaps Analysis (Feb 2026)

基于 Scholar Inbox 2026年2月推荐的 66 篇 dLLM 相关论文分析。

---

## 📊 当前研究热点分布

| 方向 | 论文数 | 代表工作 |
|------|--------|----------|
| Inference Acceleration | 53 | FOCUS, DAWN, SureLock, FlashBlock |
| Training/Alignment | 18 | AlignmentFlex, XDLM, VRPO |
| Reasoning/CoT | 8 | Latent Tokens, LLaDOU |
| Code Generation | 4 | DICE, SureLock |
| Architecture | 3 | OeMDM, DiffuSpeech |
| Safety/Watermark | 3 | dgMARK, Fragile Guardrail |

---

## 🔍 Research Gaps 分析

### Gap 1: 理论基础薄弱
**现状：** 大量工作集中在工程优化（加速、缓存），但缺乏对 dLLM 工作机制的深入理论理解。

**具体问题：**
- 为什么 dLLM 在 reasoning 任务上表现好？（只有 2602.03769 初步探索了 latent tokens）
- Attention Floating 机制（NEUIR 的工作）还没有被充分利用
- 缺乏 dLLM vs AR 的信息论分析

**潜在方向：**
- 用信息论框架分析 dLLM 的 bidirectional attention 优势
- 研究 dLLM 的 implicit planning 能力来源
- 建立 dLLM 的 scaling law（目前只有 LLaDA2.0 做到 100B）

---

### Gap 2: Open-ended Generation 仍然落后
**现状：** 2601.22947 (AlignmentFlex) 指出 dLLM 在 open-ended generation 上仍有 substantial gap。

**具体问题：**
- Positional misalignment 问题只是部分解决
- 缺乏对 creative writing、storytelling 的系统研究
- 多样性 vs 质量的 trade-off 没有好的解决方案

**潜在方向：**
- 结合 representation learning 改进 token embedding
- 研究 dLLM 的 controllable generation
- 探索 dLLM + retrieval augmentation

---

### Gap 3: 长文本生成效率
**现状：** Focus-dLLM、FlashBlock 等工作在做，但问题远未解决。

**具体问题：**
- KV Cache 在 dLLM 中的使用不如 AR 模型成熟
- Block diffusion 的 block size 选择仍是启发式的
- 缺乏对 very long context (>32K) 的系统研究

**潜在方向：**
- 自适应 block scheduling（DSB 是初步尝试）
- 结合 sparse attention 的理论分析
- 研究 dLLM 的 context compression

---

### Gap 4: Multimodal dLLM 几乎空白
**现状：** 只有 DiffuSpeech (speech) 和少量 vision 工作，没有统一的 multimodal dLLM。

**具体问题：**
- 如何在 dLLM 框架下统一处理 text + image + audio？
- 缺乏 dLLM 版本的 VLM（LLaDA-V 是后来的工作）
- Cross-modal alignment 在 diffusion 框架下的研究

**潜在方向：**
- 设计 unified multimodal discrete diffusion
- 研究 dLLM 的 cross-modal reasoning
- 探索 dLLM 在 video understanding 中的应用

---

### Gap 5: Safety & Trustworthiness 研究不足
**现状：** 只有 2 篇相关论文（dgMARK watermarking, Fragile Guardrail）。

**具体问题：**
- dLLM 的 jailbreak 攻击研究几乎没有
- 缺乏 dLLM 的 differential privacy 训练方法
- Hallucination detection 在 dLLM 中的特殊性未被研究

**潜在方向：**
- 研究 dLLM 的 adversarial robustness
- 设计 privacy-preserving dLLM training
- 利用 diffusion 的 uncertainty 做 hallucination detection

---

### Gap 6: 与 Yu 研究方向的交叉点

#### 6.1 Representation Learning + dLLM
**Gap:** 没有人研究 dLLM 的 internal representations
- dLLM 学到的 token embedding 有什么特殊性？
- 能否用 contrastive learning 改进 dLLM？
- dLLM 的 layer-wise representation 分析

#### 6.2 Information Theory + dLLM
**Gap:** 缺乏信息论视角的分析
- dLLM 的 mutual information 分析
- 用 information bottleneck 理解 dLLM
- dLLM 的 compression-generation trade-off

#### 6.3 Causal Reasoning + dLLM
**Gap:** 几乎没有相关工作
- dLLM 的 bidirectional attention 是否有助于 causal reasoning？
- 能否设计 causally-aware dLLM？
- dLLM 在 counterfactual generation 中的应用

#### 6.4 Privacy + dLLM
**Gap:** 完全空白
- dLLM 的 membership inference attack
- Differentially private dLLM training
- dLLM 的 unlearning

---

## 🎯 建议的研究方向（按可行性排序）

### 短期（3-6个月）
1. **dLLM Representation Analysis**
   - 分析 LLaDA 的 internal representations
   - 与 AR models 对比
   - 发现 dLLM 的 unique properties

2. **Information-Theoretic Understanding of dLLM**
   - 用 mutual information 分析 bidirectional attention
   - 解释为什么 dLLM 在 reasoning 上好

### 中期（6-12个月）
3. **Privacy-Preserving dLLM**
   - DP-SGD for dLLM training
   - Membership inference attacks on dLLM
   - 与 AR models 的 privacy 对比

4. **Causal dLLM**
   - 设计 causally-aware masking strategy
   - dLLM for counterfactual generation

### 长期（1年+）
5. **Unified Multimodal dLLM**
   - Text + Image + Audio in one framework
   - Cross-modal reasoning

---

## 📚 必读论文 Top 10

1. **Reasoning with Latent Tokens** (2602.03769) - 理解 dLLM reasoning
2. **Relaxing Positional Alignment** (2601.22947) - 核心问题分析
3. **FOCUS** (2601.23278) - 加速方法
4. **DAWN** (2602.06953) - Dependency-aware decoding
5. **XDLM** (2602.01362) - Understanding vs Generation trade-off
6. **OeMDM** (2602.02112) - Generation order 的统一框架
7. **Attention Floating** (2601.07894) - 机制分析
8. **LLaDA 2.1** (2602.08676) - SOTA model
9. **d3LLM** (2601.07568) - Distillation for speed
10. **Fragile Guardrail** (2602.00388) - Safety 初步研究

---

*Generated: 2026-02-15*
