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
