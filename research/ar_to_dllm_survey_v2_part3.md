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
