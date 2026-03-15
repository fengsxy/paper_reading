
## Paper 2: Efficient-DLM (NVIDIA, arXiv 2025.12)
**全文精读完成**

### 关键技术细节（abstract 里看不到的）：

1. **Block-wise Attention 的三种变体对比（Table 1 极其重要）**：
   - (b) Full bidirectional + token shift: avg 18.10（崩溃）
   - (c) Full bidirectional - token shift: avg 19.29（仍然崩）
   - (d) Block-wise + noisy context + token shift: avg 28.23（好很多）
   - (f) Block-wise + **clean context** + token shift: avg 37.69（接近AR）
   - (g) Block-wise + clean context - token shift: avg **38.41**（最优，超过原AR的41.79的91%）
   
   **核心发现**：clean context 比 noisy context 重要 9.46%！不 shift 比 shift 好！

2. **与 DiffuLLaMA 的关键分歧**：
   - DiffuLLaMA 说 token shift 很重要 → Efficient-DLM 说**不需要 shift**
   - 原因：DiffuLLaMA 用全 bidirectional，shift 帮助保留 AR 的权重分布
   - Efficient-DLM 用 block-wise + clean context，已经足够保留权重分布，shift 反而增加任务难度
   - **结论：shift 只在全 bidirectional 情况下有用，block-wise 不需要**

3. **Weight Drift 可视化（Figure 2e）**：
   - Full bidirectional: attention 层 drift 大，FFN 层 drift 也大
   - Block-wise w/o clean context: attention 小，FFN 仍然大
   - Block-wise w/ clean context: **两者都小**
   - 定量证明了 block-wise + clean context 最大化保留 AR 权重

4. **Block Size 分析（Figure 3，非常详细）**：
   - Qwen2.5 1.5B: sweet spot = 16
   - Qwen3 4B: sweet spot = 64
   - 规律：**模型越大，最优 block size 越大**（larger models 更 tolerant of corruption）
   - 一个 block size 训练可以 generalize 到其他 eval block sizes

5. **Position-Dependent Token Masking 细节（Eq.2）**：
   - w_i(t) = exp[β(1-t)i]
   - β=0: uniform（标准）
   - β>0: 后面位置更高 mask 概率
   - 关键：当 t→0（接近完成）时 positional bias 最强；t→1（早期）时接近 uniform
   - 最优 β 使得 λ=exp(-βL') ≈ 0.1
   - 效果：在高并行度（TPF=5.6）下提升 4.38%！低并行度下也有提升

6. **训练动态分析（Figure 8）**：
   - 10B tokens：已经能做基本的 AR→dLM 转换
   - 50B tokens：accuracy-NFE Pareto 曲线显著改善
   - 100B tokens：继续改善，但边际递减
   - **结论：10B 够用（基本），50B 不错，100B 最优**

7. **最终结果（8B 规模）**：
   - 从 Qwen3 8B 转换
   - 100B tokens 训练
   - Block size 64 训练，128 eval
   - 12 task 平均：comparable to Qwen3 8B（slightly better）
   - 比 Dream 7B: +5.4% accuracy, 4.5× throughput
   - 比 Qwen3 4B: +2.7% accuracy, 2.7× throughput

### 与其他工作的关系：
- 直接对标 DiffuLLaMA 和 Dream：证明 block-wise 全面优于 full bidirectional
- 与 BD3-LM 的关系：用了 BD3-LM 的 block-wise + clean context 设计，但从 AR 初始化而非从头训练
- 与 SDAR 的关系：类似思路，但 Efficient-DLM 更深入分析了 attention pattern 和 masking

## Paper 3: SDAR (Shanghai AI Lab, arXiv 2025.10)
**全文精读完成**

### 关键技术细节：

1. **AR vs MDLM 公平对比（Section 4，最重要的实验）**：
   - 同架构(2B)、同数据(1T tokens)、同超参训练 AR 和 MDLM
   - AR-2B-Chat 在几乎所有 benchmark 上大幅超越 MDLM-2B-Chat
   - 原因：AR 直接优化 NLL，每个 token 都参与梯度更新；MDLM 优化 NELBO（loose upper bound），只有 masked tokens 参与 loss
   - **结论：AR 训练效率远高于 MDLM → 先训 AR 再转换是正确路线**

2. **四个对比模型设计**：
   - AR-2B → 直接用（baseline）
   - AR-2B → SDAR-2B（AR 转 block diffusion，本文方法）
   - MDLM-2B → 直接用（diffusion baseline）
   - MDLM-2B → MDLM-BD-2B（MDLM 转 block diffusion）
   - 结果：SDAR ≈ AR >> MDLM-BD >> MDLM
   - **AR backbone 转出来的 BD 模型远优于 MDLM backbone 转出来的**

3. **转换极其轻量**：
   - 只用 30-50B tokens（相比 1T 预训练的 3-5%）
   - 不需要 attention mask annealing（直接切换！）
   - 不需要 token shift
   - 不需要原始预训练数据（用任意开源数据即可）
   - **比 DiffuLLaMA 的 200B tokens 便宜 4-7 倍**

4. **规模化验证（最大 30B MoE）**：
   - 1.7B, 4B, 8B (dense) + 30B MoE
   - 越大模型：对 block size 越鲁棒，可以用更大 block → 更高并行度
   - SDAR-30B-A3B-Sci（MoE）在 GPQA、ChemBench 上**超越 AR 原版**
   - 第一个支持 long chain-of-thought 的 diffusion 模型

5. **两种 remasking 策略**：
   - Static：每步解码固定 ⌈B/T⌉ 个 token（最高 confidence 的）
   - Dynamic：confidence > threshold τ 的全部解码
   - Dynamic 更快但质量略低

6. **与 Efficient-DLM 的关键区别**：
   - SDAR 不用 clean context（SDAR 训练时 context 是 noisy 的）
   - SDAR 不用 position-dependent masking
   - SDAR 转换成本更低（30-50B vs 50-100B）
   - 但 Efficient-DLM 在 accuracy 上可能更优（clean context 的加持）
   - **两者可以结合：SDAR 的低成本 + Efficient-DLM 的 clean context 和 position-dependent masking**

7. **推理超越 AR 的解释**：
   - 局部 bidirectional attention 允许模型看到 block 内所有 token → 减少 causal constraints
   - 对科学推理（化学式、DNA序列等需要双向理解的）特别有帮助
   - Iterative refinement 允许模型"修改"已预测的 token
   - test-time scaling（majority voting, pass@k）下提升更大 → "strong potential for RL optimization"

## Paper 4: Dream 7B (HKU, arXiv 2025.08)
**全文精读完成**

### 关键技术细节：

1. **AR 初始化 + Shift Operation（跟 DiffuLLaMA 一致）**：
   - 直接用 Qwen2.5-7B 权重初始化
   - 保留 AR 的 shift：position i 的 hidden state 预测 position i+1 的 token
   - 全 bidirectional attention（不是 block-wise）
   - **跟 Efficient-DLM 的发现矛盾**：Efficient-DLM 说 block-wise 下不需要 shift

2. **CART：Context-Adaptive Token-Level Noise Rescheduling（Dream 的核心创新）**：
   - 标准训练：所有 masked token 共享一个全局 noise level t → suboptimal
   - CART：根据每个 masked token 周围的 clean token 数量，动态调整其 effective noise level
   - 用 geometric distribution 衡量 clean token 对 masked token 的信息贡献
   - 距离近的 clean token 贡献大 → 该 masked token 的 effective noise 应该更低（更接近 clean）
   - 公式：w(t, x_t, n) = 1/2 * Σ 1[x_t^i ≠ MASK] * Geo(p, |n-i|-1)
   - p 控制 sharpness：小 p → clean tokens 贡献均匀，大 p → 局部影响更强

3. **训练数据量（关键差异）**：
   - Dream 7B：只用 580B tokens（0.6T）
   - LLaDA 8B：2.3T tokens
   - Qwen2.5 7B（AR baseline）：18T tokens
   - **Dream 用 1/4 LLaDA 的数据，就全面超越 LLaDA** → AR 初始化极其有效

4. **Planning 任务上的碾压式优势**：
   - Countdown: Dream 16.0 vs Qwen2.5 6.2
   - Sudoku: Dream **81.0** vs Qwen2.5 21.0 (4倍!)
   - Trip planning: Dream 17.8 vs Qwen2.5 3.6 (5倍!)
   - LLaDA 也比 Qwen2.5 好 → 这是 diffusion 范式的固有优势，不是 Dream 特有的
   - **原因：diffusion 能同时看到整个序列，做全局规划而非贪心左到右**

5. **与其他方法的关键对比**：
   - Dream 用全 bidirectional + shift → 跟 DiffuLLaMA 路线一致
   - Efficient-DLM 用 block-wise + clean context - shift → 不同路线
   - Efficient-DLM 8B 比 Dream 7B：+5.4% accuracy, 4.5× throughput
   - **结论：Dream 的 CART 是好创新，但 full bidirectional 限制了它的推理效率**

6. **SFT 阶段**：
   - 只对 response 加噪，prompt 保持 clean
   - 1.8M instruction-response pairs
   - 这跟 block-wise 方案的 "clean context" 思路一致

### 重要启示：
- CART 可以跟 block-wise 方案结合（Efficient-DLM 的 position-dependent masking 是 CART 的简化版）
- Planning 优势是 dLLM 最大的卖点之一，值得在 story 中强调
- 0.6T tokens 就能从 Qwen2.5 转出强大的 dLLM → 转换效率很高

## Paper 5: Block Diffusion / BD3-LM (Cornell/Kuleshov, ICLR 2025 Oral)
**Abstract + project page 阅读（无 HTML 全文）**

### 关键细节：
1. **原生 block-wise 设计**：不是从 AR 转换，而是从头训练
2. **核心贡献**：
   - 高效训练算法
   - 梯度方差估计器
   - Data-driven noise schedule（最小化方差）
3. **KV cache + 任意长度生成支持**
4. **ICLR 2025 Oral** — 说明 block diffusion 被社区高度认可
5. **局限**：从头训练，规模较小
6. **代码开源**：github.com/kuleshov-group/bd3lms

---

## Paper 6: LLaDA 2.0 (Ant Group + RUC, arXiv 2025.12)
**全文精读完成 — 这是最重要的一篇**

### 关键技术细节：

1. **WSD (Warmup-Stable-Decay) 三阶段转换策略**：
   - **Warmup**: Block size 从 1 → 4 → 32 → 64 → 4096 渐进增大
     - AR 可以看作 block size = 1 的 BDLM！
     - 逐步扩大 receptive field，从 causal → 局部 bidir → 全 bidir
   - **Stable**: Block size = 4096（= 全序列），做大规模 MDLM 训练
     - 此阶段不需要维护 clean context → 计算效率高
     - 深化模型对 diffusion dynamics 的理解
   - **Decay**: Block size 从 4096 → 2048 → ... → 32 逐步缩小
     - 将全局知识蒸馏到高效的 block-wise 结构
     - 最终得到支持 KV cache 的高效推理模型

   **核心洞察：AR = block size 1 的 BDLM → 渐进增大 block size 是最自然的转换路径**

2. **规模：100B 参数（MoE）**：
   - LLaDA2.0-mini: 16B
   - LLaDA2.0-flash: 100B（MoE）
   - 目前最大的 dLLM！
   - 基于 Ling-mini-2.0 和 Ling-flash-2.0（Ant Group 的 AR 模型）

3. **Document-level Attention Mask**：
   - 问题：packed training 时跨文档的 spurious dependencies
   - 解决：严格限制 attention 在文档边界内
   - 比 CART 和 random-length 等技巧更fundamental
   - 在 CPT 训练中效果最好

4. **Post-training 创新**：
   - **Complementary Masking SFT**：确保每个 token 都参与学习（传统 random masking 浪费 token）
   - **Confidence-Aware Parallel SFT**：训练模型更 "sharp"，解锁激进的并行解码
   - **DPO for dLLM**：将 DPO 从 AR 适配到 dLLM（用 reconstruction loss 替代 log-likelihood）
   - **Auxiliary confidence prediction loss**：提升解码时的置信度 → 更高并行度

5. **与其他转换方法的关键区别**：
   - DiffuLLaMA/Dream: 直接切到 full bidirectional（激进）
   - SDAR/Efficient-DLM: 直接用 block-wise（中等）
   - LLaDA 2.0: WSD 三阶段（最渐进）：先扩到全 bidirectional 做充分训练，再缩回 block-wise 做高效推理
   - **WSD 是"先学全局知识，再蒸馏到高效结构"的思路** → 比直接 block-wise 转换可能更好

6. **开源**：huggingface.co/collections/inclusionAI/llada-20

### 与前面论文的对比总结：
- 规模最大（100B）
- 转换策略最精细（WSD 三阶段）
- Post-training 最完整（SFT + confidence + DPO）
- 但转换成本也最高（三阶段 + 大规模 MDLM 训练）

## Paper 7: RND1 (Radical Numerics, arXiv 2025.10)
**Blog + Tech Report 阅读**

### 关键技术细节：
1. **最直接的转换方案**：
   - 从 Qwen3-30B-A3B（MoE）直接转换
   - 直接切换 causal → bidirectional（不用 annealing！）
   - 关键发现：Layer-specific learning rates 很重要
     - Dense layers（attention/FFN）用低 LR → 防止 catastrophic forgetting
     - 新增的 diffusion-specific layers 用高 LR → 快速学习
   
2. **规模**：30B MoE（3B active）— 发布时最大的开源 base DLM

3. **Knowledge preservation 策略**：
   - 约束 dense layers 的更新幅度
   - 保留 AR 预训练的知识密集型能力（world knowledge, factual recall）
   - 这跟 Efficient-DLM 用 weight drift 分析得出的结论一致

4. **与其他方法的对比**：
   - 比 DiffuLLaMA 更简单（不需要 annealing）
   - 比 SDAR 更直接（不需要 block-wise 过渡）
   - 但效果可能不如 block-wise 方案（全 bidirectional → 无 KV cache）

---

## Paper 8: Mercury Coder (Inception Labs, arXiv 2025.06)
**全文精读**

### 关键技术细节：
1. **商业级 dLLM**：
   - Mercury Coder Mini: 1109 tokens/sec on H100（比 frontier AR 快 10×！）
   - Mercury Coder Small: 737 tokens/sec on H100
   - 第一个达到商业可用速度的 dLLM

2. **训练**：
   - 基于 BD3-LM 的 block diffusion 框架扩展
   - 万亿级 token 训练（web crawl + curated + synthetic）
   - Transformer 架构（不是新架构，是新训练方法）
   - 关键：架构选择与 diffusion 正交——diffusion 是训练/推理算法，不约束模型架构

3. **推理优化**：
   - 并行生成多个 token（coarse-to-fine）
   - Custom kernels for parallel inference workloads
   - 更高的 arithmetic intensity → 更好的 GPU 利用率
   - 兼容 OpenAI API（drop-in replacement）

4. **代码任务**：
   - Copilot Arena 排名第二（质量），速度第一
   - 在 HumanEval、MBPP、BigCodeBench 等上表现 competitive
   - Infilling 是天然优势

5. **关键洞察**：
   - "diffusion 不约束架构"——Transformer、RNN、SSM 都可以做 diffusion
   - 速度优势来自**并行解码**，不是架构差异
   - 这意味着 linear attention（如 Gated DeltaNet）也可以做 diffusion 的 backbone

### 与你的工作的关系：
- Mercury 证明了 dLLM 的商业可行性（速度是杀手级优势）
- 如果 linear state memory 能进一步加速推理（减少 denoising 步数），商业价值巨大
