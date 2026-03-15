
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

## Paper 9: CDLM — Consistency Diffusion Language Models (MLSys under review, 2025.11)
**全文精读完成**

### 关键技术细节：

1. **核心思路：把 continuous diffusion 的 consistency model 搬到 discrete diffusion**：
   - Consistency model 原理：任意中间状态都能直接映射到最终结果，不需要走完所有步
   - 在 dLLM 中：training a block-causal student to jump multiple denoising steps

2. **三个训练目标联合优化**：
   - **Distillation Loss**：从 bidirectional teacher 的 hidden states 蒸馏到 block-causal student
     - 关键：存储 teacher 的 last hidden states（不是 logits），推理时用 lm_head 重建 teacher 分布
     - Forward KL divergence on newly unmasked positions
   - **Consistency Loss**：enforcing student 在 state y 和 block-completion state y* 之间的预测一致性
     - Stop-gradient target（detached from backpropagation）
     - 只在 still-masked positions 上计算
   - **DLM Loss**：标准 masked denoising objective，保持 mask prediction 能力

3. **Trajectory Collection（离线）**：
   - 用 teacher（bidirectional DLM）生成 decoding trajectories
   - 每个 prompt 多个 temperature 采样 → 多条 trajectory
   - 存储每步的 hidden states 用于 white-box distillation
   - 这是离线的——不需要 on-policy 采样

4. **结果**：
   - Dream 7B: 8h training → 3.4-7.9× fewer steps, 3.6-14.5× lower latency
   - LLaDA 8B: 16h training → similar speedup
   - 超越同规模 AR 模型的 tokens/second
   - Accuracy 几乎无损

5. **关键洞察**：
   - Block-causal student 比 bidirectional teacher 推理更快（支持 KV cache）
   - Consistency objective 让 student 能 "跳步"——不需要走完所有 denoising steps
   - 这本质上是 **self-distillation**：同架构同规模，只改 attention pattern

---

## Paper 10: SPG — Sandwiched Policy Gradient (Meta, arXiv 2025.10)
**全文精读完成**

### 关键技术细节：

1. **核心问题：dLLM 的 log-likelihood 不可计算 → 标准 policy gradient 无法直接用**
   - 现有方法用 ELBO 近似 log π_θ(x|c)
   - 问题：ELBO 是 lower bound，对 positive reward OK（maximize lower bound），但对 negative reward 错误（minimize lower bound ≠ minimize true likelihood）

2. **SPG 的解决方案：三明治**
   - Positive advantage（好的 response）：maximize ELBO（lower bound）✓
   - Negative advantage（坏的 response）：minimize EUBO（upper bound）✓
   - "Sandwich" = ELBO ≤ log π ≤ EUBO → 两个方向都是 valid bound

3. **EUBO 推导（Theorem 1）**：
   - 基于 Rényi variational bound
   - 关键区别：log 在 expectation 外面（ELBO 是 log 在里面）
   - β ≥ 1 控制 tightness（β → 1 更紧但方差更大）

4. **Block-wise Masking Strategy**：
   - 不用 random masking，用 block-wise masking 做 Monte Carlo estimation
   - 原因：推理时用 block-wise decoding，random masking 的分布不匹配
   - 跟 Efficient-DLM 的 position-dependent masking 思路一致

5. **结果**：
   - GSM8K +3.6%, MATH500 +2.6%, Countdown +18.4%, Sudoku +27.0%
   - 远超 ELBO-based RL 和 one-step estimation

---

## Paper 11: Seed Diffusion Preview (ByteDance, arXiv 2025.08)
**全文精读完成**

### 关键技术细节：

1. **Two-Stage Curriculum (TSC)**：
   - Stage 1（前 80% steps）：标准 mask-based diffusion training
   - Stage 2（后 20% steps）：加入 edit-based corruption process
     - 用 Levenshtein distance 控制 corruption level
     - 操作集：deletion, insertion, substitution
     - 目的：improve calibration，消除 repetition 等 sampling artifacts

2. **Generation Order Control**：
   - 核心洞察：mask-based diffusion ≡ any-order autoregressive modeling
   - 自然语言是顺序的 → 纯 random order 效率低
   - Seed Diffusion 用 "generation order control" 引导模型偏向 left-to-right
   - 这跟 position-dependent masking（Efficient-DLM）和 CART（Dream）是同一方向

3. **速度**：
   - 2,146 tokens/sec on H20 GPU（比 Mercury 的 1,109 on H100 还快！）
   - 关键：H20 是更便宜的 GPU → 性价比更高

4. **跟 Mercury 的对比**：
   - Mercury: H100, 1,109 tok/s
   - Seed Diffusion: H20, 2,146 tok/s
   - Gemini Diffusion: unknown hardware
   - Seed Diffusion 在 speed-quality Pareto frontier 上当前最优

---

## Paper 12: TiDAR — Think in Diffusion, Talk in Autoregression (NVIDIA, arXiv 2025.11)
**全文精读完成**

### 关键技术细节：

1. **核心架构：单模型内的 AR + Diffusion 混合**
   - 不是两个模型，是一个模型用 structured attention mask 实现两种模式
   - 序列分三部分：prefix（已确定）、proposed（上步的候选，AR 验证）、pre-drafted（本步 diffusion 提出）
   - 一次 forward pass 同时做 AR 验证 + diffusion 起草

2. **与 Speculative Decoding 的关系**：
   - TiDAR 本质上是 self-speculative decoding：drafter = diffusion mode，verifier = AR mode
   - 但 drafter 和 verifier 是**同一个模型的不同 attention pattern**
   - 利用 "free token slots"（memory-bound 区间内，多放几个 token 不增加延迟）

3. **训练**：
   - 用 structured causal-bidirectional hybrid attention mask
   - Diffusion section 全部设为 [MASK]（简化训练，增强 train-test consistency）
   - AR loss + diffusion loss 联合训练

4. **结果**：
   - TiDAR 1.5B: lossless quality vs AR, 4.71× throughput speedup
   - TiDAR 8B: 5.91× throughput speedup, minimal quality loss
   - 超越 speculative decoding 的 throughput
   - 超越 Dream/LLaDA 的 quality + speed

5. **关键洞察**：
   - "diffusion 做初稿，AR 做终稿" — 结合两者优势
   - AR 的 chain factorization 天然适合语言 → 最终 token 用 AR 采样保证质量
   - Diffusion 的并行性 → 多个候选 token 同时计算
   - 这种 hybrid 不需要额外 drafter 模型

## Paper 13: MiniLLM — Knowledge Distillation of Large Language Models (ICLR 2024)
**全文精读完成**

### 关键技术细节：

1. **核心问题：Forward KL vs Reverse KL**
   - Forward KL (标准KD)：student 在 teacher 数据上训练 → mode-covering（试图覆盖所有 mode）→ 在 low-probability 区域过度分配概率
   - Reverse KL (MiniLLM)：student 在自己的数据上训练 → mode-seeking（集中在 teacher 的高概率区域）→ 更精确但可能丢失 mode

2. **On-Policy 训练**：
   - Student 自己生成 trajectory
   - 在自己的 trajectory 上计算 reverse KL
   - 用 policy gradient 优化（类似 RL）
   - 三个稳定技巧：
     - **Single-Step Decomposition**：把序列级目标分解为单步目标，减少方差
     - **Teacher-Mixed Sampling**：α 概率用 teacher 采样，(1-α) 概率用 student 采样
     - **Length Normalization**：防止 student 学会生成短/重复文本（reward hacking）

3. **关键结果**：
   - 120M → 13B 全面超越 SeqKD 和标准 KD
   - Student 在某些任务上**超越 teacher**（exposure bias 更低）
   - Calibration 更好（ECE 更低）
   - Long-text generation 优势最明显

4. **与 RL 的联系（Appendix A.1）**：
   - MiniLLM 等价于 Inverse RL：teacher 的 log probability 作为 reward
   - 这个联系后来被 Reopold 更深入地挖掘

---

## Paper 14: GKD — Generalized Knowledge Distillation (Google DeepMind, ICLR 2024)
**Abstract + Paper 阅读**

### 关键创新：
1. **On-Policy Student-Generated Data**：
   - 训练时用 student 自己的 output 而非 teacher 的 output
   - 解决 distribution mismatch（off-policy 的核心问题）

2. **Generalized Divergence**：
   - 不限于 KL，支持 JSD、TVD 等多种 divergence
   - 不同 divergence 适合不同场景

3. **与 RLHF 兼容**：
   - GKD 可以无缝嵌入 RLHF pipeline
   - 先 GKD 蒸馏，再 RLHF 对齐

4. **结果**：在 summarization 和 translation 上显著优于标准 KD

---

## Paper 15: EOPD — Entropy-Aware On-Policy Distillation (IBM + KAIST, arXiv 2026.03)
**全文精读完成**

### 关键技术细节：

1. **核心发现：Reverse KL 在高 entropy token 上失败**
   - Standard on-policy distillation 用 reverse KL → mode-seeking
   - 问题：teacher 对某些 token 不确定（高 entropy，多种合理选择）
   - Reverse KL 强迫 student 只选一个 mode → 丢失了 teacher 的 uncertainty
   - 量化：蒸馏后 student 只保留 6.8% 的高 entropy tokens（teacher 是 18.5%）

2. **EOPD 的解决方案：entropy-aware 混合目标**
   - L_EOPD = L_OPD(reverse KL) + I[H_t > τ] * L_FKL(forward KL)
   - 低 entropy token：只用 reverse KL（精确匹配 teacher 的确定预测）
   - 高 entropy token：加上 forward KL（保留 teacher 的多样性/不确定性）
   - τ 是 entropy threshold（超参数）

3. **结果**：
   - Qwen3-0.6B: Pass@8 +1.37
   - Qwen3-1.7B: Pass@8 +2.39
   - Qwen3-4B: Pass@8 +5.05
   - 模型越大提升越大
   - 关键：提升主要来自**多样性保持** → Pass@K（需要多样性）提升远大于 Greedy（不需要多样性）

4. **与 dLLM 的关系**：
   - dLLM 的 masked token prediction 本质上就是"高 entropy"场景
   - 多个 masked token 同时预测 → teacher 的 uncertainty 更高
   - EOPD 的 entropy-aware 思路直接适用于 dLLM 蒸馏

---

## Paper 16: Reopold — Relaxed On-Policy Distillation (arXiv 2026.03)
**全文精读完成**

### 关键技术细节：

1. **核心洞察：On-Policy Distillation ≡ Policy Gradient RL**
   - Stop-gradient 后，distillation objective 精确等价于 policy gradient
   - Teacher-student log-likelihood ratio = token-level reward
   - 这意味着 distillation 继承了 RL 的所有优化挑战

2. **三大挑战（RL 视角诊断）**：
   - **Heavy-tailed negative rewards**：student 生成 teacher 不喜欢的 token → 极大负 reward → 梯度爆炸
   - **Near-zero rewards**：大多数 token student 和 teacher 一致 → 接近零的 reward → 浪费计算
   - **Entropy collapse**：student 快速丧失多样性 → 过早收敛

3. **Reopold 三个解决方案**：
   - **Mixture-based reward clipping**：截断极端负 reward → 稳定训练
   - **Entropy-based token-level dynamic sampling**：只在高信息量 token 上学习 → 提升效率
   - **Exploration-to-refinement 两阶段训练**：
     - Stage 1 (exploration)：基于 reward 选择性学习（过滤 near-zero reward tokens）
     - Stage 2 (refinement)：基于 entropy 选择性学习（focus on 高 entropy tokens）

4. **结果**：
   - 比标准 on-policy distillation **6.7-12× 更高 sample efficiency**
   - 7B student 可以匹配 32B teacher（在 visual reasoning 上）
   - 3.32× inference speedup
   - 在 math、visual、tool-use reasoning 上全面超越

5. **关键 insight**：
   - Stop-gradient 是一个 free 的改进——减少梯度方差，不影响期望梯度
   - "temperate and selective" 使用 teacher signal 比"全部使用"更好
   - On-policy distillation 可以比 RL（GRPO 等）更高效（10× less compute）

---

## Paper 17: Progressive Distillation (Salimans & Ho, ICLR 2022)
**经典论文，Abstract + 方法阅读**

### 核心方法：
1. Teacher 用 N 步生成 → 训练 student 用 N/2 步匹配
2. 迭代：student 成为新 teacher → 再训 N/4 步的 student
3. 最终得到 1-4 步的生成模型

### 与 dLLM 的关系：
- 直接类比：dLLM teacher 用 T 步 denoise → 训练 student 用 T/2 步
- CDLM（Paper 9）就是这个思路在 discrete diffusion 上的实现
- 但 discrete diffusion 的 progressive distillation 比 continuous 更难（离散采样不可微）

---

## Paper 18: Consistency Models (Song et al., ICML 2023)
**经典论文，Abstract + 方法阅读**

### 核心方法：
1. 定义 consistency function f(x_t, t) → x_0：任意中间状态直接映射到最终结果
2. Self-consistency property：同一 trajectory 上的所有点映射到同一 x_0
3. 两种训练方式：
   - Consistency Distillation (CD)：从预训练 diffusion model 蒸馏
   - Consistency Training (CT)：直接训练，不需要 teacher

### 与 dLLM 的关系：
- CDLM（Paper 9）直接搬了 CD 到 discrete diffusion
- Consistency 的核心属性（self-consistency）在 discrete space 需要重新定义
- CT 方向在 dLLM 中还未被探索——潜在研究机会

---

## Paper 19: Self-Distilled Reasoner — OPSD (CMU, arXiv 2026.01)
**Abstract + Blog 阅读**

### 核心创新：
1. **Self-Distillation**：不需要外部 teacher
   - Model 自己做 verification（给定 answer，判断 solution 是否正确）
   - 正确 solution 的 log-prob 作为 dense reward signal
   - Student = teacher（同一个模型的不同 mode）

2. **On-Policy Self-Improvement Loop**：
   - Step 1: Student 生成 solution
   - Step 2: 用 privileged info（ground truth answer）筛选正确 solution
   - Step 3: 在正确 solution 上自蒸馏
   - 迭代

3. **结果**：4-5× inference speedup on parallel-structured reasoning tasks

### 与 dLLM 的关系：
- dLLM 天然支持 self-distillation：多步 denoise 的 teacher → 少步的 student
- 不需要外部模型
