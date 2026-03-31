# 离散扩散语言模型(dLLM)两大核心问题调研报告

**作者：Claw | 日期：2026-03-15 | 为 Yu 准备**

---

## 一、问题定义

离散扩散语言模型(dLLM)通过迭代去噪生成文本：从全 [MASK] 序列出发，每步预测并揭示部分 token。与自回归模型相比，dLLM 支持并行解码、双向上下文、灵活生成模式。但存在 **两个核心瓶颈**：

### 问题 A：错误累积 (Error Accumulation)
- **本质**：一旦某步揭示了错误 token，该错误在后续步骤中被视为"正确上下文"，误导后续预测
- **原因**：标准 masked diffusion 训练只监督 masked 位置，模型无法区分已揭示 token 的正确/错误
- **表现**：并行解码越激进（每步揭示越多 token），错误累积越严重；quality-speed Pareto 曲线急剧下降

### 问题 B：信息损失 (Information Loss / Information Island)
- **本质**：每步去噪后，采样+remasking 将连续 hidden state h_t 压缩为离散 token，丢弃了丰富的中间表示
- **原因**：标准 dLLM 的 reverse process 是 Markovian 的：p(x_{t-1}|x_t)，只依赖当前离散序列
- **表现**：跨步不一致（实体漂移、前后矛盾）、全局结构丢失、重复重建上下文的计算浪费

### 两个问题的关系
这两个问题**不独立**：信息损失加剧错误累积（因为模型每步都从头重建上下文，没有"记忆"来维持一致性）；错误累积反过来产生更多噪声上下文，使信息损失更严重。理想方案应该**同时缓解**两个问题。

---

## 二、调研论文列表 (10篇核心论文)

| # | 论文 | 会议/年份 | 解决问题 | 核心方法 |
|---|------|-----------|----------|----------|
| 1 | **MetaState** (Xia et al.) | arXiv 2026.03 | 信息损失 | GRU 持久记忆跨步传递 |
| 2 | **ReMDM** (Wang et al.) | NeurIPS 2025 | 错误累积 | 推理时 remasking + 纠错 |
| 3 | **CDLM** (Corrective DLM) | ICML 2025 | 错误累积 | 训练时监督错误 token |
| 4 | **ProSeCo** (Learn from Mistakes) | arXiv 2026.02 | 错误累积 | 自纠正 SFT + corrector loop |
| 5 | **Soft-Masked DLM** | arXiv 2025.10 | 信息损失 | 连续概率代替 hard mask |
| 6 | **Elastic-Cache** | arXiv 2025.10 | 信息损失(计算) | 自适应 KV cache 复用 |
| 7 | **dKV-Cache** (Ma et al.) | arXiv 2025.05 | 信息损失(计算) | 延迟 KV cache 策略 |
| 8 | **Block Diffusion (BD3-LM)** | ICLR 2025 Oral | 两者兼顾 | 块级 AR + 块内扩散 |
| 9 | **STaRR** | arXiv 2026.01 | 错误累积 | 时空动态感知 remasking |
| 10 | **Gated DeltaNet** (Yang et al.) | ICLR 2025 | 信息损失(架构) | 线性注意力 + delta rule |

---

## 三、分类框架与详细分析

我把现有解决方案按 **"解决什么问题" × "在哪个阶段干预"** 分成四大类：

```
                    ┌─────────────────────────────────────────┐
                    │          解决错误累积                      │
                    │                                         │
  训练时干预 ──────► │ ① 训练纠错能力                           │
                    │    CDLM, ProSeCo                        │
                    │                                         │
  推理时干预 ──────► │ ② Remasking 策略                        │
                    │    ReMDM, STaRR, Dream (low-conf remask) │
                    └─────────────────────────────────────────┘
                    
                    ┌─────────────────────────────────────────┐
                    │          解决信息损失                      │
                    │                                         │
  表示层干预 ──────► │ ③ 保持跨步连续信息                       │
                    │    MetaState, Soft-Masked DLM, CANDI     │
                    │                                         │
  计算层干预 ──────► │ ④ KV Cache 复用                         │
                    │    Elastic-Cache, dKV-Cache, Fast-dLLM   │
                    └─────────────────────────────────────────┘
                    
                    ┌─────────────────────────────────────────┐
                    │          两者兼顾                         │
                    │                                         │
  架构层干预 ──────► │ ⑤ 混合架构                              │
                    │    Block Diffusion, SDAR                 │
                    └─────────────────────────────────────────┘
```
