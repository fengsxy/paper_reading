# Daily Papers — 2026-03-22

> 周末产出低，新论文有限。以下为 Friday 3/20 arxiv 新上线中与研究方向相关的亮点，均未在前两日日报中收录。

## Architecture & Representation

### 1. InfoMamba: Attention-Free Hybrid Mamba-Transformer
- **Authors:** Youjin Wang et al.
- **Link:** https://arxiv.org/abs/2603.18031
- **Key:** 提出 information-maximizing fusion (IMF)，用互信息目标驱动 SSM 与全局 bottleneck 的融合。用 concept bottleneck 线性滤波层替代 self-attention，实现近线性复杂度下的全局建模。跨分类、密集预测、非视觉任务均优于 Transformer/SSM 基线。
- **相关性:** 互信息驱动的表示融合 + 高效架构，与 info-theoretic representation learning 直接相关。

### 2. R2-Dreamer: Redundancy-Reduced World Models (ICLR 2026)
- **Authors:** Naoki Morihira et al.
- **Link:** https://arxiv.org/abs/2603.18202
- **Key:** 受 Barlow Twins 启发的冗余缩减目标用于 decoder-free MBRL。自监督内部正则化防止表示坍塌，无需数据增强。比 DreamerV3 训练快 1.59×。
- **相关性:** Barlow Twins 式信息论正则化在 RL 中的实践。

### 3. Path-Constrained Mixture-of-Experts
- **Authors:** Zijin Gu et al.
- **Link:** https://arxiv.org/abs/2603.18297
- **Key:** 跨层共享 router 参数约束 expert path 空间，0.9B/16B 模型上一致优于独立路由。Token 按语言功能自然聚类到相同路径，无需辅助负载均衡。
- **相关性:** 路径视角理解 MoE 表示结构。

## Alignment & Safety

### 4. Detection Is Cheap, Routing Is Learned: Why Refusal-Based Alignment Fails
- **Authors:** Gregory Frank et al.
- **Link:** https://arxiv.org/abs/2603.18280
- **Key:** 研究中国大模型政治审查作为 alignment 自然实验。发现"检测-路由-生成"三阶段框架：模型保留知识但改变表达方式。同一模型家族内，硬拒绝降至零而叙事引导升至最大值，使审查对 refusal-only benchmark 不可见。跨模型 transfer 失败，routing 几何是 model-specific 的。
- **相关性:** Trustworthy AI / alignment 评估方法论。

## Transformer Foundations

### 5. Frayed RoPE and Long Inputs: A Geometric Perspective (ICLR 2026)
- **Authors:** Aozhong Zhang et al.
- **Link:** https://arxiv.org/abs/2603.18017
- **Key:** 从几何角度统一理解 RoPE 下的注意力行为。发现长输入破坏 key/query 聚类分离导致 sink token 失效。提出 RoPE-ID，对通道子集施加高频 RoPE 即可 zero-shot 推广到长输入。
