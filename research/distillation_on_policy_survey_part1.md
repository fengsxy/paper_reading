# 知识蒸馏与 On-Policy Distillation 调研报告

**作者：Claw | 日期：2026-03-15 | 为 Yu 准备**
**基于 19 篇论文精读（含前两份报告的 12 篇 + 本次新增 7 篇）**

---

## 一、问题定义

知识蒸馏是让小模型从大模型学习的核心方法。在 dLLM 语境下，蒸馏有两层含义：

1. **经典 KD**：大 teacher → 小 student（压缩模型）
2. **Step Distillation**：多步 teacher → 少步 student（加速推理）
3. **Paradigm Distillation**：AR teacher → dLLM student（转换范式）

On-Policy Distillation 是近年最重要的进展：让 student 在**自己生成的数据**上学习，而非 teacher 的数据。

---

## 二、论文列表（7篇新增精读）

| # | 论文 | 来源 | 核心方法 | 精读 |
|---|------|------|----------|------|
| 13 | **MiniLLM** | ICLR 2024, Microsoft | Reverse KL + on-policy policy gradient | ✅全文 |
| 14 | **GKD** | ICLR 2024, Google DeepMind | Generalized divergence + on-policy student data | ✅论文 |
| 15 | **EOPD** | arXiv 2026.03, IBM+KAIST | Entropy-aware 混合 forward+reverse KL | ✅全文 |
| 16 | **Reopold** | arXiv 2026.03, ICML submission | RL 视角诊断 + relaxed distillation | ✅全文 |
| 17 | **Progressive Distillation** | ICLR 2022, Salimans & Ho | 迭代 halving 步数 | ✅方法 |
| 18 | **Consistency Models** | ICML 2023, Song et al. | Self-consistency → one-step generation | ✅方法 |
| 19 | **OPSD** (Self-Distilled Reasoner) | arXiv 2026.01, CMU | On-policy self-distillation 无需外部 teacher | ✅Abstract+Blog |

---

## 三、分类框架

```
知识蒸馏方法
│
├── ① Off-Policy Distillation（在 teacher 数据上学）
│   ├── SeqKD: SFT on teacher generations（最简单）
│   ├── Standard KD: Forward KL on teacher distribution
│   └── 局限：distribution mismatch（student 推理时的分布 ≠ 训练时的分布）
│
├── ② On-Policy Distillation（在 student 数据上学）
│   ├── MiniLLM: Reverse KL + policy gradient
│   ├── GKD: Generalized divergence + on-policy student sampling
│   ├── EOPD: Entropy-aware forward+reverse KL hybrid
│   ├── Reopold: RL-aware relaxed distillation（reward clipping + dynamic sampling）
│   └── OPSD: Self-distillation（student = teacher）
│
├── ③ Step Distillation（减少 diffusion 步数）
│   ├── Progressive Distillation: 迭代 halving（N → N/2 → N/4）
│   ├── Consistency Distillation: 任意步 → 1步映射
│   └── CDLM: Consistency model for discrete diffusion
│
└── ④ Paradigm Distillation（AR → dLLM 转换）
    ├── DiffuLLaMA / Efficient-DLM / SDAR（见前份报告）
    └── 本质上也是蒸馏：AR teacher 的知识 → dLLM student
```
