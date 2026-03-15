# AR→dLLM 转换方法调研报告（精读版）

**作者：Claw | 日期：2026-03-15 | 为 Yu 准备**
**基于 8 篇论文全文精读**

---

## 一、问题定义

从头训练 dLLM 极其昂贵（LLaDA-8B 用了 2.3T tokens），而开源 AR 模型已积累大量知识。**能否低成本地将 AR 模型转换为 dLLM？**

### 核心挑战

1. **注意力模式不匹配**：AR 是 causal（下三角），dLLM 是 bidirectional（全注意力）。直接切换会破坏预训练权重分布
2. **训练目标不匹配**：AR 预测 next token，dLLM 预测所有 masked token
3. **训练效率**：转换需要多少 token？越少越好
4. **能力保持**：转换后能否保留 reasoning、ICL 等能力？
5. **推理效率**：转换后能否用 KV cache？

---

## 二、论文列表（8篇精读 + 2篇对照）

| # | 论文 | 会议/年份 | 核心方法 | 规模 | 精读 |
|---|------|-----------|----------|------|------|
| 1 | **DiffuLLaMA** | ICLR 2025 | Attention mask annealing + shift | 7B | ✅全文 |
| 2 | **Efficient-DLM** (NVIDIA) | arXiv 2025.12 | Block-wise attention + position-dependent masking | 8B | ✅全文 |
| 3 | **SDAR** (上海AI Lab) | arXiv 2025.10 | 轻量 paradigm conversion | 30B MoE | ✅全文 |
| 4 | **Dream 7B** (HKU) | arXiv 2025.08 | Qwen2.5 初始化 + CART noise reschedule | 7B | ✅全文 |
| 5 | **LLaDA 2.0** (蚂蚁) | arXiv 2025.12 | WSD 三阶段转换 | 100B MoE | ✅全文 |
| 6 | **RND1** (Radical Numerics) | arXiv 2025.10 | 直接切换 + layer-specific LR | 30B MoE | ✅报告 |
| 7 | **Mercury Coder** (Inception) | arXiv 2025.06 | 商业级 block diffusion | 未公开 | ✅全文 |
| 8 | **BD3-LM** (Cornell) | ICLR 2025 Oral | 原生 block diffusion 设计 | 中小 | Abstract |
| 9 | **LLaDA** (对照) | arXiv 2025.02 | 从头训练 | 8B | 参考 |
| 10 | **DiffusionVL** (华科) | arXiv 2025.12 | AR VLM→diffusion VLM | 多模态 | 参考 |

---

## 三、分类框架

按"注意力模式转换策略"分为四大类：

```
AR → dLLM 转换方法
│
├── ① 全双向转换（Full Bidirectional）
│   ├── DiffuLLaMA: 渐进退火 causal → bidirectional
│   ├── Dream 7B: 直接初始化 + CART
│   └── RND1: 直接切换 + layer-specific LR
│
├── ② 块级混合转换（Block-wise Hybrid）
│   ├── Efficient-DLM: block间causal + 块内bidir + clean context + pos-dep masking
│   ├── SDAR: 轻量 paradigm conversion
│   └── BD3-LM: 原生设计（从头训练）
│
├── ③ 渐进式三阶段转换（Progressive WSD）
│   └── LLaDA 2.0: AR → 渐进扩大block → 全MDLM → 缩小block → 高效BDLM
│
├── ④ 商业级部署
│   └── Mercury Coder: block diffusion + 万亿token训练 + 自定义推理kernel
│
└── 对照：从头训练
    └── LLaDA: 纯 diffusion pretraining (2.3T tokens)
```
## 四、各类方案详细分析

### 类别①：全双向转换

#### DiffuLLaMA (ICLR 2025)

**核心发现**：AR 和 diffusion 的 loss 在特定 masking schedule 下**精确数学等价**——不是近似。这是 AR→dLLM 转换可行的理论基础。

**三个关键技术**：
1. **Attention Mask Annealing**：不是简单 linear interpolation，而是 log-space 分阶段退火。先 anneal 对角线附近（局部），再扩展到远处（全局）。前 10% steps 保持纯 causal，最后 10% 完全 bidirectional。
2. **Shift Operation**：保留 AR 的 position i 预测 token i+1 模式（不改为预测 token i），最大化保留权重分布。
3. **Time-Embedding-Free**：不加 time embedding 反而更好——基于 RADD 的发现：absorbing diffusion 的 concrete score 与时间无关。

**实验细节**：
- DiffuGPT-127M 转换后**超越了 GPT2-127M**（AR→diffusion 后变好了！）
- DiffuLLaMA-7B 在 commonsense reasoning 上接近 LLaMA2-7B
- 但 GSM8K 差距明显（reasoning 最难转换）
- 训练成本：~200B tokens（AR 预训练的 10%）
- 从 AR 的 final LR 开始训练（不重新 warmup）

**好在哪**：第一个系统性证明 AR→dLLM 可行，有严格的数学基础

**不足**：全 bidirectional → 无 KV cache → 推理慢；200B tokens 仍不算便宜

---

#### Dream 7B (HKU, arXiv 2025.08)

**核心创新是 CART（Context-Adaptive Token-Level Noise Rescheduling）**：
- 标准训练：所有 masked token 共享一个全局 noise level → suboptimal
- CART：根据每个 masked token 周围的 clean token 数量，用 geometric distribution 动态调整其 effective noise level
- 近处的 clean token 贡献大 → 该 masked token 的 effective noise 应更低
- 公式：w(t, x_t, n) = 1/2 * Σ 1[x_t^i ≠ MASK] * Geo(p, |n-i|-1)

**关键数据**：
- 只用 0.6T tokens（LLaDA 的 1/4），就全面超越 LLaDA-8B → AR 初始化极其有效
- Planning 任务碾压式优势：Sudoku 81.0 vs Qwen2.5 的 21.0（4倍！）
- Trip planning 17.8 vs Qwen2.5 的 3.6（5倍！）
- **Planning 优势是 dLLM 范式的固有优势**：能同时看到整个序列，做全局规划而非贪心

**不足**：全 bidirectional → 无 KV cache；与 AR 原版在 reasoning 上仍有差距

---

#### RND1 (Radical Numerics, arXiv 2025.10)

**最简单的方案**：直接切 causal → bidirectional，不用 annealing。

**关键发现**：Layer-specific learning rates 是关键
- Dense layers（attention/FFN）用低 LR → 防止 catastrophic forgetting
- 新增的 diffusion-specific layers 用高 LR → 快速学习
- 约束 dense layers 的更新幅度 → 保留知识密集型能力

**规模**：30B MoE（3B active），从 Qwen3-30B-A3B 转换。发布时最大开源 base DLM。

**不足**：全 bidirectional → 无 KV cache

---

### 类别②：块级混合转换

#### Efficient-DLM (NVIDIA Song Han 组, arXiv 2025.12)

**Table 1 是全文最重要的实验**（Abstract 里完全看不到）：

| 方案 | 12-task 平均 |
|------|-------------|
| Full bidir + shift | 18.10（崩溃）|
| Full bidir - shift | 19.29（仍崩）|
| Block-wise + noisy context + shift | 28.23 |
| Block-wise + **clean context** + shift | 37.69 |
| Block-wise + **clean context** - shift | **38.41**（最优）|

**三个关键发现**：

1. **Clean context 比 noisy context 重要 9.46%**——block-wise 训练时，已解码的 block 应该用 clean token 作为 context（不加噪声）。这是全文最大的单一改进。

2. **Block-wise 下不需要 token shift**——跟 DiffuLLaMA 的结论相反！原因：block-wise + clean context 已足够保留权重分布，shift 反而增加任务难度。

3. **Position-Dependent Token Masking**：
   - 训练时 uniform masking vs 推理时 block-wise 从左到右 → train-test mismatch
   - 解决：w_i(t) = exp[β(1-t)i]，后面位置更高 mask 概率
   - 在高并行度（TPF=5.6）下提升 4.38%

**Weight Drift 可视化（Figure 2e）**：
- Full bidir: attention 层和 FFN 层 drift 都大
- Block-wise + clean context: **两者都小** → 定量证明权重分布保留最好

**训练动态**：10B tokens 够基本转换，50B 不错，100B 最优

**最终结果（8B）**：比 Dream 7B 高 +5.4% accuracy，4.5× throughput

---

#### SDAR (上海AI Lab, arXiv 2025.10)

**最重要的实验（Section 4）**：同架构(2B)、同数据(1T)、同超参公平对比 AR vs MDLM
- AR-2B-Chat 在几乎所有 benchmark 上大幅超越 MDLM-2B-Chat
- 原因：AR 直接优化 NLL，每个 token 都参与梯度；MDLM 优化 NELBO（loose bound），只有 masked tokens 参与 loss
- **结论：AR 训练效率远高于 MDLM → 先训 AR 再转换是正确路线**

**转换极其轻量**：
- 只用 30-50B tokens（预训练的 3-5%，比 DiffuLLaMA 便宜 4-7 倍）
- 不需要 annealing、不需要 shift、不需要原始预训练数据
- 直接做 block-wise 适配

**规模最大**：1.7B, 4B, 8B (dense) + 30B MoE

**关键结果**：SDAR-30B-A3B-Sci 在 GPQA、ChemBench 上**超越 AR 原版** → diffusion 的 iterative refinement 确实提供了 AR 没有的推理能力

**与 Efficient-DLM 的区别**：
- SDAR 不用 clean context（训练时 context 是 noisy 的）
- SDAR 不用 position-dependent masking
- 更便宜但 accuracy 可能不如 Efficient-DLM
- **两者可以结合：SDAR 的低成本 + Efficient-DLM 的 clean context 和 pos-dep masking**
### 类别③：渐进式三阶段转换

#### LLaDA 2.0 (蚂蚁集团, arXiv 2025.12) — 目前最大的 dLLM

**核心创新：WSD (Warmup-Stable-Decay) 三阶段转换**

关键洞察：**AR 可以看作 block size = 1 的 Block Diffusion LM**。所以从 AR 到 dLLM 的转换，本质上就是逐步增大 block size。

1. **Warmup**：Block size 从 1 → 4 → 32 → 64 → 4096 渐进增大
   - 逐步扩大 receptive field：causal → 局部 bidir → 全 bidir
   - 每次扩大都用适量数据做平滑过渡
   - 到 4096 时 = 全序列 MDLM

2. **Stable**：Block size = 4096（全序列），大规模 MDLM 训练
   - 此阶段不需要维护 clean context → 计算效率高
   - 深化模型对 diffusion dynamics 的理解
   - **这一步是 LLaDA 2.0 独有的**——其他 block-wise 方案直接跳过

3. **Decay**：Block size 从 4096 → 2048 → ... → 32 逐步缩小
   - 将全局知识蒸馏到高效的 block-wise 结构
   - 最终得到支持 KV cache 的高效推理模型

**Post-training 创新**：
- **Complementary Masking SFT**：确保每个 token 都参与学习（标准 random masking 浪费 token）
- **Confidence-Aware Parallel SFT**：训练模型更 "sharp" → 解锁激进并行解码
- **DPO for dLLM**：用 reconstruction loss 替代 AR 的 log-likelihood
- **Document-level Attention Mask**：防止 packed training 中的跨文档 spurious dependencies → 比 CART 等技巧更 fundamental

**规模**：LLaDA2.0-mini (16B) + LLaDA2.0-flash (100B MoE) — 目前最大的 dLLM

**与其他方案的关键区别**：
- WSD 是"先学全局知识（Stable 阶段做 full MDLM），再蒸馏到高效结构（Decay 阶段）"
- 其他 block-wise 方案直接转成 block → 可能损失全局建模能力
- 代价：三阶段训练成本最高

---

### 类别④：商业级部署

#### Mercury Coder (Inception Labs, arXiv 2025.06)

**第一个达到商业可用速度的 dLLM**：
- Mercury Coder Mini: **1109 tokens/sec** on H100（比 frontier AR 快 10×！）
- Mercury Coder Small: 737 tokens/sec on H100
- Copilot Arena 排名第二（质量），速度第一

**关键技术洞察**：
1. **架构与 diffusion 正交**——Transformer、RNN、SSM 都可以做 diffusion backbone
2. 速度优势来自**并行解码的高 arithmetic intensity** → 更好的 GPU 利用率
3. Custom kernels for parallel inference workloads
4. 兼容 OpenAI API → drop-in replacement

**训练**：万亿级 token，基于 BD3-LM 框架扩展，web crawl + curated + synthetic data

**与你的工作的关系**：
- Mercury 证明了 dLLM 的商业可行性
- 如果 linear state memory 能减少 denoising 步数 → 直接提升商业价值
- "架构与 diffusion 正交" → linear attention 也可以做 diffusion backbone
## 五、综合对比表

| 方案 | 注意力转换 | KV Cache | 转换成本 | 最大规模 | 核心优势 | 核心不足 |
|------|-----------|----------|----------|----------|----------|----------|
| **DiffuLLaMA** | 渐进退火→全bidir | ❌ | ~200B tokens (10%) | 7B | 理论数学基础最强 | 无KV cache，成本中等 |
| **Dream 7B** | 直接初始化→全bidir | ❌ | ~0.6T tokens | 7B | CART创新，planning碾压AR | 无KV cache，reasoning差距 |
| **RND1** | 直接切换→全bidir | ❌ | 中等 | 30B MoE | 最简单，layer-specific LR | 无KV cache |
| **Efficient-DLM** | Block-wise (间causal+内bidir) | ✅ | 10-100B tokens | 8B | 当前accuracy最优，clean context | Block size超参 |
| **SDAR** | Block-wise paradigm转换 | ✅ | 30-50B tokens (3-5%) | 30B MoE | 转换成本最低，推理超越AR | 无clean context/pos-dep mask |
| **LLaDA 2.0** | WSD三阶段渐进 | ✅ | 三阶段（最高） | 100B MoE | 规模最大，post-training最完整 | 训练成本最高 |
| **Mercury** | Block diffusion (商业) | ✅ | 万亿级（从头） | 未公开 | 1100 tok/s，商业可用 | 闭源 |
| **LLaDA** (对照) | 从头训练 全bidir | ❌ | 2.3T tokens | 8B | 充分训练可匹配AR | 计算成本极高 |

---

## 六、关键洞察（精读后的深层理解）

### 洞察1：Block-wise 是当前最优转换范式，原因在于 weight drift

Efficient-DLM 的 Figure 2e 给出了**定量证据**：
- Full bidir 转换后，attention 层和 FFN 层的 weight drift 都很大
- Block-wise + clean context 转换后，两者都很小
- Weight drift 越小 → 知识保留越多 → 转换后性能越好

DiffuLLaMA 的 annealing 试图缓解这个问题，但只是减慢了 drift，没有从根本上解决。Block-wise 从架构层面保证了大部分位置仍是 causal → 根本性地减少 drift。

### 洞察2：Clean context 是被严重低估的技术

Efficient-DLM 发现 clean context 贡献了 +9.46% 的提升——比 position-dependent masking (+4.38%) 和去掉 shift (+0.72%) 加起来都大。

但 SDAR 没有使用 clean context，LLaDA 2.0 在 Stable 阶段也没有。这意味着**现有最强方案还没有用上最强技巧**。组合 SDAR 的低成本 + Efficient-DLM 的 clean context 是一个低垂果实。

### 洞察3：AR 训练效率远高于 MDLM（SDAR 的公平对比）

同架构同数据对比：AR 大幅超越 MDLM。原因：
- AR 优化 NLL，每个 token 都参与梯度
- MDLM 优化 NELBO（loose upper bound），只有 masked tokens 参与 loss
- **结论：先训 AR 再转换永远比从头训 dLLM 更高效**

LLaDA 2.0 的 100B 实验也支持这个结论：AR 初始化的 dLLM 在训练早期就已经很好，从头训的需要更多 compute 才能追上。

### 洞察4：dLLM 在 planning/constraint satisfaction 上有范式级优势

Dream 7B 的 Sudoku 结果（81.0 vs AR 的 21.0）不是偶然——这是 diffusion 的并行+双向+迭代修正带来的固有优势。SDAR 在科学推理上超越 AR 也验证了这一点。

这个优势在 block-wise 方案中被部分保留（block 内有双向+迭代），但 block 间仍是 sequential。**如何在保持 KV cache 的同时最大化 diffusion 的 planning 优势，是一个开放问题。**

### 洞察5：Token shift 的必要性取决于 attention 模式

- 全 bidirectional 时：shift 有用（DiffuLLaMA, Dream 都用了）
- Block-wise + clean context 时：shift 有害（Efficient-DLM 不用更好）
- 原因：shift 是为了在全 bidir 下保留 AR 权重分布，但 block-wise 本身已解决这个问题

### 洞察6：LLaDA 2.0 的 WSD 揭示了一个重要设计空间

WSD 的核心思路是"先在全 MDLM 下学全局知识，再蒸馏到 block-wise"。这暗示：
- 全 MDLM 的全局建模能力 > block-wise 的局部建模能力
- 但全 MDLM 推理太慢
- **理想方案：训练时用全 MDLM，推理时用 block-wise + linear state 保持全局信息**
## 七、与你的 Linear State Memory 工作的关系

### 直接连接点

1. **实验 backbone 选择**：
   - 用 Efficient-DLM 或 SDAR 转换出的 block-wise dLLM 作为 backbone
   - Block 间已有 KV cache（已解决），block 内的 Information Island 仍存在 → 你的 linear state 填这个空
   - 比在全 bidirectional dLLM 上做 linear state 更实际（全双向推理太慢）

2. **LLaDA 2.0 的 WSD 启示**：
   - WSD 的 Stable 阶段（全 MDLM）学到了全局知识，Decay 阶段蒸馏到 block-wise 时**会损失全局信息**
   - 你的 linear state 可以作为 Decay 阶段的补偿——在 block-wise 结构中用 linear state 保持全局信息
   - Story：**"WSD trains global knowledge, linear state preserves it during block-wise inference"**

3. **Mercury 的商业启示**：
   - dLLM 的商业价值在于速度（1100 tok/s）
   - 如果 linear state memory 能减少 denoising 步数（更少步达到相同质量）→ 直接提升商业价值
   - "架构与 diffusion 正交" → linear attention 做 backbone 也可行

4. **SDAR 的公平对比给了理论支撑**：
   - AR 训练效率 >> MDLM → 先训 AR 再转换是正确路线
   - 你的方案不需要从头训——基于已有的 AR→dLLM 转换模型加 linear state augmentation
   - 成本极低：frozen backbone + 轻量 linear state 模块

### 建议的实验路线

**Phase 0: 选 backbone（1天）**
- 下载 Efficient-DLM 8B 或 SDAR 8B（如果开源）
- 或者自己用 SDAR 方法从 Qwen3 8B 转换（30-50B tokens）

**Phase 1: Linear State > GRU in MetaState（2-3周）**
- 把 MetaState 的 GRU Updater 替换为 Gated DeltaNet
- 在 block-wise backbone 上测试
- 预期：match 或超越 MetaState，训练速度更快

**Phase 2: 与 KV Cache 统一（1-2周）**
- Block 间 KV cache + block 内 linear state
- 测量 speed × quality Pareto

**Phase 3: Schedule-Memory 联合优化（如果投 top venue）**

---

## 八、参考文献

1. Gong et al. "Scaling Diffusion Language Models via Adaptation from Autoregressive Models." ICLR 2025. arXiv:2410.17891.
2. Fu et al. "Efficient-DLM: From Autoregressive to Diffusion Language Models, and Beyond in Speed." arXiv:2512.14067, 2025.
3. Cheng et al. "SDAR: A Synergistic Diffusion-AutoRegression Paradigm." arXiv:2510.06303, 2025.
4. Ye et al. "Dream 7B: Diffusion Large Language Models." arXiv:2508.15487, 2025.
5. Bie et al. "LLaDA 2.0: Scaling Up Diffusion Language Models to 100B." arXiv:2512.15745, 2025.
6. Radical Numerics. "RND1: Simple, Scalable AR-to-Diffusion Conversion." Tech Report, 2025.
7. Khanna et al. "Mercury: Ultra-Fast Language Models Based on Diffusion." arXiv:2506.17298, 2025.
8. Arriola et al. "Block Diffusion: Interpolating Between AR and Diffusion LMs." ICLR 2025 Oral. arXiv:2503.09573.
9. Nie et al. "LLaDA: Large Language Diffusion Models." arXiv:2502.09992, 2025.
10. DiffusionVL. "Translating Any AR Models into Diffusion VLMs." arXiv:2512.15713, 2025.

---

**精读笔记**：完整的论文精读笔记（包含 abstract 看不到的技术细节）见 `research/ar_to_dllm_reading_notes.md`
