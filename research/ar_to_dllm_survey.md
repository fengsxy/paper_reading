# AR→dLLM 转换方法调研报告

**作者：Claw | 日期：2026-03-15 | 为 Yu 准备**

---

## 一、问题定义

从头训练 dLLM 极其昂贵（LLaDA-8B 用了数万亿 token），而开源 AR 模型（LLaMA、Qwen）已经积累了大量知识。**能否把已训练好的 AR 模型"转换"为 dLLM，以低成本获得 dLLM 的并行解码、双向上下文等优势？**

### 核心挑战

1. **注意力模式不匹配**：AR 是 causal attention（下三角 mask），dLLM 是 bidirectional attention（全注意力）。直接从 causal 切到 bidirectional 会破坏预训练权重的分布
2. **训练目标不匹配**：AR 预测 next token，dLLM 预测所有 masked token。loss landscape 完全不同
3. **位置编码适配**：AR 的 RoPE 等位置编码针对 causal 设计，bidirectional 场景下需要调整
4. **训练效率**：continual pretraining 需要多少 token 才能完成转换？越少越好
5. **能力保持**：转换后能否保留 AR 模型的 reasoning、ICL 等能力？

---

## 二、调研论文列表（7篇核心论文）

| # | 论文 | 会议/年份 | 核心方法 | 规模 |
|---|------|-----------|----------|------|
| 1 | **DiffuLLaMA** (Gong et al.) | ICLR 2025 | Continual pretraining + attention mask annealing | 127M→7B |
| 2 | **Efficient-DLM** (Fu et al., NVIDIA) | arXiv 2025.12 | Block-wise attention + position-dependent masking | 8B |
| 3 | **SDAR** (Cheng et al.) | arXiv 2025.10 | 轻量 paradigm conversion + block diffusion | 最高 30B MoE |
| 4 | **Dream 7B** (Ye et al., HKU) | arXiv 2025.08 | 从 Qwen2.5 初始化 + masked diffusion SFT | 7B |
| 5 | **Block Diffusion (BD3-LM)** (Arriola et al.) | ICLR 2025 Oral | Block 间 AR + block 内 diffusion | 中小规模 |
| 6 | **DiffusionVL** (HUST) | arXiv 2025.12 | AR→diffusion VLM 翻译框架 | 多模态 |
| 7 | **LLaDA 2.0** (Bie et al.) | arXiv 2025.12 | 从头训练 vs AR 初始化对比 | 100B |

---

## 三、分类框架

```
AR → dLLM 转换方法
│
├── ① 全双向转换（Full Bidirectional Conversion）
│   └── DiffuLLaMA: causal → bidirectional，完整转换
│
├── ② 块级混合转换（Block-wise Hybrid Conversion）
│   ├── Efficient-DLM: block 间 causal + block 内 bidirectional
│   ├── SDAR: block-wise paradigm conversion
│   └── Block Diffusion: 原生设计但思路相同
│
├── ③ 直接初始化 + 扩散微调（Init + Diffusion Finetuning）
│   ├── Dream 7B: 用 Qwen2.5 权重初始化
│   └── DiffusionVL: 翻译 AR VLM 到 diffusion VLM
│
└── ④ 从头训练（对照组）
    └── LLaDA / LLaDA 2.0: 纯 diffusion pretraining
```
## 四、各类方案详细分析

### 类别①：全双向转换

#### DiffuLLaMA — Scaling Diffusion LMs via Adaptation from AR Models (ICLR 2025)

**核心洞察**：AR 和 diffusion 的训练目标存在数学联系——masked diffusion 的 loss 可以看作 AR cross-entropy loss 的加权泛化。这意味着 AR 预训练的权重是 diffusion 训练的良好初始化。

**方法**：三个关键技术
1. **Attention Mask Annealing**：不直接从 causal → bidirectional（太激进，权重分布崩溃）。而是渐进退火：
   - 开始：保持 causal mask
   - 中期：逐步将上三角的值从 -∞ 提升到 0
   - 结束：完全 bidirectional
   - 让模型平滑过渡，保留 AR 权重的知识

2. **Shift Operation**：AR 模型预测 next token（position i 预测 i+1），但 diffusion 模型预测当前 token（position i 预测 i）。加一个 shift 操作对齐这个差异。

3. **Time-Embedding-Free**：发现不加 time embedding 效果更好（RADD 的发现：absorbing diffusion 的 score 与时间无关）。

**训练成本**：< 200B tokens（相比 AR 预训练的万亿级，大幅节省）

**结果**：
- GPT2 (127M/355M) → DiffuGPT：超越之前的 MDLM、SEDD 等 DLM
- LLaMA 7B → DiffuLLaMA 7B：competitive with AR 版本
- 支持 ICL、Fill-in-the-Middle、instruction following

**好在哪**：
- 第一个系统性证明 AR→dLLM 转换可行的工作
- Attention mask annealing 巧妙解决了 causal→bidirectional 的过渡问题
- 数学上建立了 AR 和 diffusion objective 的联系

**不足**：
- 全 bidirectional attention → 推理时无法用 KV cache
- 200B tokens 仍然不算很便宜（约 LLaMA 预训练的 10%）
- 对大规模模型（>7B）的可扩展性未充分验证

---

### 类别②：块级混合转换

#### Efficient-DLM — From AR to Diffusion LMs, and Beyond in Speed (NVIDIA, arXiv 2025.12)

**核心洞察**：DiffuLLaMA 的全 bidirectional 转换有两个问题——(1) 破坏预训练权重分布太严重，(2) 推理时没法用 KV cache。**Block-wise attention** 同时解决这两个问题。

**方法**：
1. **Block-wise Attention Pattern**：
   - 序列分成大小为 B 的 block
   - Block 间：causal attention（前面的 block 看不到后面的）
   - Block 内：bidirectional attention（同 block 内可以互相看）
   - 关键好处：**保持了大部分 causal 结构** → 预训练权重分布更好保留

2. **Position-Dependent Token Masking**：
   - 标准训练：uniform masking（每个 token 等概率被 mask）
   - 问题：推理时是从左到右逐 block 解码的，前面 block 已解码（mask rate 低），后面 block 全 mask（mask rate 高）→ 训练和推理的 mask 分布不匹配
   - 解决：训练时给后面位置的 token 更高的 masking 概率 → 模拟推理时的真实分布

3. **系统优化**：
   - Block 间 KV cache 天然可用（causal）
   - Block 内并行解码（diffusion）
   - Throughput 大幅提升

**结果**：
- Efficient-DLM 8B 比 Dream 7B 高 +5.4% accuracy，4.5× throughput
- 比 Qwen3 4B 高 +2.7% accuracy，2.7× throughput
- 在 accuracy 和 speed 上同时超越 AR 和 dLLM

**好在哪**：
- 目前 AR→dLLM 转换的最优方案
- Block-wise attention 是关键创新：保留权重分布 + 支持 KV cache
- Position-dependent masking 优雅地解决了 train-test mismatch
- 来自 NVIDIA（Song Han 组），工程质量高

**不足**：
- Block size 是超参数，影响 speed-quality trade-off
- Block 内仍然有标准 dLLM 的信息损失问题

---

#### SDAR — Synergistic Diffusion-AutoRegression (arXiv 2025.10)

**核心洞察**：AR 模型在训练效率上远超 dLLM，所以应该**先充分训练 AR，再做轻量转换**——而非从头做 diffusion training。

**方法**：
1. 完全用 AR 模式训练（充分利用 AR 的训练效率）
2. 训练结束后，做**轻量 paradigm conversion**：
   - 引入 block-wise diffusion 解码：block 间 AR，block 内 diffusion
   - 短暂的 adaptation training（数据量比 DiffuLLaMA 更少）
3. 推理时：autoregressively 逐 block 生成（全局连贯），每个 block 内 parallel decode

**结果**：
- 最大规模到 30B MoE
- 在 GPQA、ChemBench 等科学推理上**超越 AR 版本**
- 支持 test-time scaling（majority voting, pass@k）
- 越大的模型对 block size 和 decoding threshold 越鲁棒

**好在哪**：
- 转换成本最低——只需要轻量 adaptation
- 规模最大（30B MoE）
- 在推理任务上超越 AR（这很重要！说明 diffusion 的 iterative refinement 有额外价值）

**不足**：
- Block 间仍然是 sequential（AR），并行度受限于 block 内
- 需要设计 block size vs quality 的 trade-off
### 类别③：直接初始化 + 扩散微调

#### Dream 7B — Diffusion Large Language Models (HKU, arXiv 2025.08)

**核心洞察**：用强大的 AR 模型（Qwen2.5-7B）的权重直接初始化 dLLM backbone，然后用 masked diffusion objective 做 continual pretraining。

**方法**：
1. **初始化**：直接加载 Qwen2.5-7B 的全部权重
2. **转换训练**：用 masked diffusion objective（predict masked tokens）做 continual pretraining
3. **SFT**：标准 instruction tuning，但用 diffusion 训练范式
4. **推理创新**：
   - 低 confidence remasking（类似 ReMDM 思路）
   - Picard iteration 式的 iterative refinement

**结果**：
- 在多个 benchmark 上与 Qwen2.5-7B 匹配或接近
- 支持 variable-length generation（DreamOn 扩展）
- 比从头训练的 LLaDA-8B 在某些任务上更好

**好在哪**：
- 最直接的方案：拿 AR 权重，换训练 objective，done
- 验证了 Qwen2.5 的知识可以迁移到 diffusion 范式
- HKU NLP 组的工程质量好，开源完整

**不足**：
- 没有 block-wise 设计 → 全 bidirectional → 无 KV cache
- Continual pretraining 数据量未明确优化
- 与 AR 原版仍有不小差距（尤其 reasoning）

---

#### DiffusionVL — Translating AR Models into Diffusion VLMs (HUST, arXiv 2025.12)

**核心洞察**：当前 diffusion VLM 受限于 base dLLM 的能力。与其等 dLLM 变强，不如直接把强大的 AR VLM"翻译"成 diffusion VLM。

**方法**：
1. 拿任意预训练 AR VLM（如 LLaVA、Qwen-VL 等）
2. 用 diffusion finetuning 框架转换：
   - 保留 vision encoder
   - 将 language decoder 从 AR → diffusion
   - 设计 adaptation 策略保留视觉理解能力

**好在哪**：
- 扩展到多模态领域
- 证明 AR→diffusion 转换不限于纯文本

**不足**：
- 多模态的复杂度增加
- 视觉 token 和文本 token 的 masking 策略需要不同处理

---

### 类别④：从头训练（对照组）

#### LLaDA / LLaDA 2.0 — Large Language Diffusion Models (arXiv 2025/2025.12)

**为什么列为对照**：LLaDA 是从头训练 dLLM 的代表，不涉及 AR→dLLM 转换，但提供了重要的 baseline 和 insights。

**LLaDA 关键发现**：
- dLLM 从头训练 **可以** 达到 AR 水平（LLaDA-8B vs LLaMA3-8B）
- 天然解决 reversal curse（AR 模型的固有缺陷）
- 支持 ICL、instruction following

**LLaDA 2.0 (100B scale) 关键发现**：
- AR 初始化的 dLLM 在**训练早期**更好，但从头训练的 dLLM 在充分训练后可以追上
- 结论："Given sufficient compute, training from scratch can match AR-initialized models"
- 但 "sufficient compute" = 非常大量的 token

**对比启示**：
- 如果计算预算有限（大多数情况）→ AR→dLLM 转换是更实际的路线
- 如果追求最优性能且不限计算 → 从头训练可能更好（可以设计更好的架构）
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
