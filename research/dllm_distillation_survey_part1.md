# 如何做好 dLLM：蒸馏、加速与 Post-Training 方法调研

**作者：Claw | 日期：2026-03-15 | 为 Yu 准备**
**基于 12 篇论文全文精读（含上一份报告的 8 篇 + 本次新增 4 篇）**

---

## 一、问题定义

dLLM 的核心瓶颈不只是"怎么训"，还有"怎么让它又快又好"。这个报告聚焦三个方向：

1. **蒸馏加速**：用 teacher-student 框架减少 denoising 步数
2. **RL 对齐**：dLLM 的 RLHF/DPO 怎么做（log-likelihood 不可计算）
3. **混合架构**：AR + Diffusion 结合，取两者之长

---

## 二、新增论文列表（4篇精读）

| # | 论文 | 来源 | 核心方法 | 精读 |
|---|------|------|----------|------|
| 9 | **CDLM** (Consistency DLM) | MLSys under review | Consistency distillation + block-causal student | ✅全文 |
| 10 | **SPG** (Sandwiched Policy Gradient) | Meta, arXiv 2025.10 | ELBO+EUBO sandwich for RL | ✅全文 |
| 11 | **Seed Diffusion** | ByteDance, arXiv 2025.08 | Two-stage curriculum + edit-based corruption | ✅全文 |
| 12 | **TiDAR** | NVIDIA, arXiv 2025.11 | Think in Diffusion, Talk in AR (单模型混合) | ✅全文 |

---

## 三、分类框架

```
如何做好 dLLM
│
├── ① 蒸馏加速（减少 denoising 步数）
│   ├── CDLM: consistency distillation (bidir teacher → block-causal student)
│   └── LLaDA 2.0 WSD Decay: 全局知识蒸馏到 block-wise 结构
│
├── ② RL 对齐（解决 log-likelihood 不可计算问题）
│   ├── SPG: Sandwiched Policy Gradient (ELBO for positive, EUBO for negative)
│   └── LLaDA 2.0 DPO: reconstruction loss 替代 log-likelihood
│
├── ③ 训练策略优化
│   ├── Seed Diffusion TSC: 两阶段课程（mask → mask+edit）
│   ├── Dream CART: context-adaptive noise reschedule
│   ├── Efficient-DLM: position-dependent masking + clean context
│   └── LLaDA 2.0: complementary masking SFT + confidence-aware parallel SFT
│
├── ④ 混合架构（AR + Diffusion 融合）
│   ├── TiDAR: 单模型内 diffusion drafting + AR verification
│   ├── Block Diffusion: block 间 AR + block 内 diffusion
│   └── Efficient-DLM / SDAR: AR→block-wise dLLM 转换
│
└── ⑤ 推理优化（不改模型）
    ├── Elastic-Cache / dKV-Cache: KV cache 复用
    ├── MetaState: 跨步 persistent memory
    └── ProSeCo: self-correcting sampling
```
