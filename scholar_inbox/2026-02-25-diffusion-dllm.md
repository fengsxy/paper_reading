---
title: "2026-02-25-diffusion-dllm"
---

# Scholar Inbox 精选 - 2026-02-25

## ⚠️ Scholar Inbox 认证过期

Scholar Inbox CLI 仍返回 302，session 失效。以下论文通过 arxiv API + YDC 手动检索，聚焦本周新提交的 diffusion/dLLM 相关论文。

---

## Diffusion / dLLM 相关论文

### 1. Stop-Think-AutoRegress: Language Modeling with Latent Diffusion Planning ⭐ NEW
**Authors:** Justin Lovelace et al.
**ArXiv:** [2602.20528](https://arxiv.org/abs/2602.20528)
**Submitted:** 2026-02-24 | **Venue:** COLM 2025

**摘要：** STAR-LDM 将 latent diffusion planning 与 autoregressive 生成结合。不同于传统 AR 模型逐 token 决策，STAR-LDM 在生成过程中引入"思考"阶段——暂停生成，通过 diffusion 在连续空间中精炼语义规划，然后再继续。在 LLM-as-judge 评估中，叙事连贯性和常识推理的胜率 >70%。架构还支持通过轻量级分类器进行细粒度属性控制，无需重训练。

**亮点：** 🔥 昨天刚提交。"Stop-Think" 的设计哲学非常优雅——用 diffusion 做全局规划，用 AR 做局部生成，两者各取所长。这是 hybrid diffusion-AR 架构的一个重要探索方向，与 Mercury 2 的商业化路线形成学术-工业互补。

---

### 2. Adaptation to Intrinsic Dependence in Diffusion Language Models ⭐ THEORY
**Authors:** Yunxiao Zhao et al.
**ArXiv:** [2602.20126](https://arxiv.org/abs/2602.20126)
**Submitted:** 2026-02-23 | **Categories:** cs.LG, cs.IT, math.ST, stat.ML

**摘要：** DLM 理论分析的重要突破。提出 distribution-agnostic 的 unmasking schedule，无需先验知识或超参调优即可自适应目标分布的依赖结构。关键创新：随机化每步 unmask 的 token 数量（而非固定）。收敛保证以 KL 散度衡量，scale 为 Õ(TC/K) 和 Õ(DTC/K)，其中 TC/DTC 分别为 total correlation 和 dual total correlation，捕捉数据的内在依赖结构。

**亮点：** 🔥 信息论与 dLLM 的完美交叉。用 total correlation（信息论核心概念）刻画 dLLM 采样效率，为"为什么随机化 unmasking 更好"提供了严格理论基础。对低复杂度分布的加速结果尤其有实践指导意义。跨 cs.IT + cs.LG + math.ST 三个领域。

---

### 3. Scaling Beyond Masked Diffusion Language Models
**Authors:** Subham Sekhar Sahoo et al.
**ArXiv:** [2602.15014](https://arxiv.org/abs/2602.15014)
**Submitted:** 2026-02-16

**摘要：** 首个 uniform-state 和 interpolating 离散扩散方法的 scaling law 研究。发现 Masked diffusion 用简单 cross-entropy 目标训练可提升约 12% FLOPs 效率。关键洞察：perplexity 在同一 diffusion family 内有参考价值，但跨 family 比较时会误导——likelihood scaling 更差的模型可能因更快更实用的采样而在 speed-quality Pareto frontier 上更优。将所有方法 scale 到 1.7B 参数后，uniform-state diffusion 在 GSM8K 上超越 AR 和 Masked diffusion 模型。

**亮点：** 挑战了 "Masked diffusion 是 dLLM 唯一未来" 的主流观点。uniform-state diffusion 在 GSM8K 上的优势暗示不同 noise schedule 可能适合不同任务类型。提供了代码、checkpoint 和视频教程，复现友好。

---

### 4. Sink-Aware Pruning for Diffusion Language Models
**Authors:** Aidar Myrzakhan, Zhiqiang Shen et al.
**ArXiv:** [2602.17664](https://arxiv.org/abs/2602.17664)
**Submitted:** 2026-02-19

**摘要：** 发现 AR LLM 中的 attention sink 假设在 DLM 中不成立：DLM 的 attention-sink 位置在整个生成轨迹上方差显著更高，表明 sink 是暂态的而非结构性必需。基于此观察提出 Sink-Aware Pruning，自动识别并剪枝不稳定的 sink（而非像 AR 模型那样保留 sink）。无需重训练即可实现更好的 quality-efficiency tradeoff。

**亮点：** 揭示了 dLLM 与 AR LLM 在注意力机制上的本质差异。"AR 保留 sink，dLLM 剪枝 sink" 这一反直觉发现对 dLLM 高效推理的工程实践有直接指导意义。与 MAGE (2602.14209) 形成互补。

---

### 5. MAGE: All-[MASK] Block Already Knows Where to Look in Diffusion LLM
**Authors:** Omin Kwon et al.
**ArXiv:** [2602.14209](https://arxiv.org/abs/2602.14209)
**Submitted:** 2026-02-15

**摘要：** 解决 Block Diffusion LLM 长上下文场景下 KV cache 的内存瓶颈。发现 block diffusion 独有的机会：第一个 All-[MASK] 去噪步的注意力可以可靠预测重要的 KV entries 和 budget 需求。MAGE 据此每个 block 只做一次精确注意力计算，后续步骤复用稀疏 KV。在 LongBench 和 Needle-in-a-Haystack 上实现近无损精度，KV budget 大幅减少，端到端加速 3-4x。

**亮点：** 巧妙利用了 block diffusion 的结构特性——All-[MASK] 步天然提供了一个"预览"窗口。轻量级 fine-tuning 策略在单张 H100 上几小时即可完成 1.5B 和 7B 模型的适配，工程实用性极高。

---

### 6. MVLAD-AD: Masked Vision-Language-Action Diffusion for Autonomous Driving
**Authors:** Jiaru Zhang et al.
**ArXiv:** [2602.20577](https://arxiv.org/abs/2602.20577)
**Submitted:** 2026-02-24

**摘要：** 将 masked diffusion 应用于自动驾驶端到端规划。提出离散 action tokenization 策略，从真实驾驶分布构建紧凑的运动学可行 waypoint codebook。引入 geometry-aware embedding learning 使潜空间近似物理几何度量，以及 action-priority decoding 优先生成轨迹。在 nuScenes 上超越 SOTA AR 和 diffusion baseline。

**亮点：** dLLM 技术向自动驾驶领域的迁移。discrete action tokenization + geometry-aware embedding 的设计思路对其他需要物理约束的 dLLM 应用场景有参考价值。

---

## 📌 本周趋势观察

本周 dLLM 领域呈现几个清晰趋势：

1. **理论深化：** 2602.20126 用信息论（total correlation）为 dLLM 采样效率建立了严格理论框架，这是 dLLM 理论研究的重要里程碑。

2. **Hybrid 架构探索：** STAR-LDM (2602.20528) 的 "diffusion planning + AR generation" 模式代表了一种务实的融合路线——不是用 diffusion 替代 AR，而是让两者协作。

3. **高效推理持续升温：** Sink-Aware Pruning、MAGE、Focus-dLLM 等工作从不同角度攻克 dLLM 推理效率瓶颈，且都发现 dLLM 的注意力模式与 AR 模型有本质差异。

4. **Scaling law 重新审视：** Scaling Beyond Masked Diffusion 挑战了 Masked diffusion 的统治地位，提示 uniform-state diffusion 在推理任务上可能更有潜力。

5. **商业化信号：** HN 头条 Mercury 2 (Inception Labs) 是 dLLM 商业化的重要里程碑，学术研究正在快速转化为产品。

---

*今日 digest 共 6 篇论文，聚焦 2026 年 2 月中下旬新提交的工作。Scholar Inbox 认证仍然过期，需要重新登录后才能恢复自动抓取。*
