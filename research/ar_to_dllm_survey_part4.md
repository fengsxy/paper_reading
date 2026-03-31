## 五、综合对比表

| 方案 | 转换方式 | Attention模式 | KV Cache | 训练成本 | 最大规模 | 核心优势 | 核心不足 |
|------|----------|---------------|----------|----------|----------|----------|----------|
| **DiffuLLaMA** | 全双向转换 | Full bidirectional | ❌ | ~200B tokens | 7B | 首个系统方案，理论基础好 | 破坏权重分布，无KV cache |
| **Efficient-DLM** | Block-wise转换 | Block间causal + 块内bidir | ✅ | 中等 | 8B | 保留权重分布+KV cache，当前最优 | Block size超参数 |
| **SDAR** | 轻量paradigm转换 | Block间causal + 块内bidir | ✅ | 最低 | 30B MoE | 转换成本最低，推理上超越AR | Block间sequential |
| **Dream 7B** | AR权重初始化 | Full bidirectional | ❌ | Continual PT | 7B | 最直接，Qwen2.5知识迁移 | 与AR仍有差距 |
| **Block Diffusion** | 原生设计 | Block间causal + 块内bidir | ✅ | 从头训练 | 中小 | 架构设计优雅 | 需从头训练 |
| **DiffusionVL** | AR VLM翻译 | Diffusion finetuning | 视实现 | Finetuning | 多模态 | 扩展到多模态 | 复杂度高 |
| **LLaDA** | 从头训练（对照） | Full bidirectional | ❌ | 万亿级tokens | 100B | 充分训练可匹配AR | 计算成本极高 |

---

## 六、关键洞察

### 洞察1：Block-wise 是当前最优的转换范式

DiffuLLaMA 的全 bidirectional 转换有根本性问题：
- 破坏预训练权重分布（上三角突然从 -∞ 变成 0）
- 推理无法用 KV cache → 速度没优势

Efficient-DLM 和 SDAR 的 block-wise 方案完美避开了这两个问题：
- Block 间保持 causal → 权重分布温和变化
- Block 间 KV cache 天然可用
- Block 内 bidirectional → 享受 dLLM 并行解码

**结论：未来 AR→dLLM 转换大概率走 block-wise 路线。**

### 洞察2：转换成本可以非常低

| 方案 | 转换 token 数 | 相对 AR 预训练 |
|------|-------------|--------------|
| DiffuLLaMA | ~200B | ~10% |
| SDAR | 更少 | ~1-5% |
| Dream 7B | 未明确优化 | ~5-10% |

SDAR 证明了：AR 预训练的知识大部分可以保留，conversion 只需要让模型学会"不是 next token prediction，而是 any position prediction"。

### 洞察3：转换后的模型可以超越 AR 原版

SDAR 30B MoE 在 GPQA、ChemBench 上超越 AR → 说明 **diffusion 的 iterative refinement 确实提供了 AR 没有的推理能力**。这不只是"打平"，而是"更好"。

### 洞察4：注意力模式转换的技巧是关键

三种转换策略，效果差距巨大：
1. **暴力切换** causal → bidirectional：效果差，权重崩溃
2. **渐进退火** (DiffuLLaMA)：效果好，但仍然全双向
3. **Block-wise** (Efficient-DLM/SDAR)：效果最好，因为大部分位置仍是 causal

核心原因：AR 预训练时，每个 attention head 都学会了只看"左边"的 pattern。突然让它看"右边"会产生巨大分布外的激活，需要大量训练才能恢复。Block-wise 最大化保留了这些 pattern。

### 洞察5：Position-Dependent Masking 解决了被忽略的 train-test gap

Efficient-DLM 发现的一个巧妙问题：
- 训练时：所有位置 uniform masking（每个 token 等概率被 mask）
- 推理时：block-wise 从左到右生成 → 前面 block 已解码（低 mask rate），后面 block 全 mask
- 解决：训练时给后面位置更高 masking 概率

这类 train-test distribution mismatch 在 dLLM 中普遍存在，是一个值得更深入研究的方向。

---

## 七、与你的工作的关系

如果你要做 "Linear State Memory for dLLM"，AR→dLLM 转换有几个直接关联点：

1. **实验 backbone 的选择**：
   - 可以用 Efficient-DLM 或 SDAR 转换出的 block-wise dLLM 作为 backbone
   - 优势：block 间有 KV cache，block 内的 Information Island 仍然存在 → 你的 linear state 解决 block 内的跨步信息损失

2. **Linear state 与 block-wise 解码的结合**：
   - Block 间：KV cache 保持上下文（已解决）
   - Block 内：linear state 保持跨步信息（你的贡献）
   - 这比在全 bidirectional dLLM 上做 linear state 更实际（因为全双向的推理太慢）

3. **实验效率**：
   - 不需要从头训练 dLLM → 从 AR 转换即可
   - SDAR 的轻量转换 + 你的 linear state augmentation = 低成本高收益

---

## 八、参考文献

1. Gong et al. "Scaling Diffusion Language Models via Adaptation from Autoregressive Models." ICLR 2025. arXiv:2410.17891.
2. Fu et al. "Efficient-DLM: From Autoregressive to Diffusion Language Models, and Beyond in Speed." arXiv:2512.14067, 2025.
3. Cheng et al. "SDAR: A Synergistic Diffusion-AutoRegression Paradigm for Scalable Sequence Generation." arXiv:2510.06303, 2025.
4. Ye et al. "Dream 7B: Diffusion Large Language Models." arXiv:2508.15487, 2025.
5. Arriola et al. "Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models." ICLR 2025 Oral. arXiv:2503.09573.
6. DiffusionVL. "Translating Any Autoregressive Models into Diffusion Vision Language Models." arXiv:2512.15713, 2025.
7. Bie et al. "LLaDA 2.0: Scaling Up Diffusion Language Models to 100B." arXiv:2512.15745, 2025.
8. Nie et al. "LLaDA: Large Language Diffusion Models." arXiv:2502.09992, 2025.
