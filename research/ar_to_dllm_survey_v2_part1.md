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
