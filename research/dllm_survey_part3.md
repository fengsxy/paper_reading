### 类别②：Remasking 策略（解决错误累积，推理时干预）

#### ReMDM — Remasking Discrete Diffusion Models (NeurIPS 2025)

**核心洞察**：标准 masked diffusion 一旦揭示 token 就不能改了。ReMDM 引入"反悔机制"——允许已揭示的 token 被重新 mask 掉，再重新预测。

**方法**：
- 定义一个自定义 backward process，其中包含 remasking 概率
- 推理时每步可以把低 confidence 的已揭示 token 重新 mask
- 从连续时间 discrete diffusion 框架严格推导，不是 ad-hoc heuristic
- 增加采样步数 → 质量提升（inference-time compute scaling）

**好在哪**：
- Training-free，直接应用到预训练 MDLM 上
- 理论上有保证（从 CTMC 框架推导）
- 在分子设计等科学领域效果显著
- 支持 inference-time scaling：更多步 → 接近 AR 质量

**不足**：
- 在 LLM 任务上提升有限（HumanEval 上不降不升：40.24→40.24）
- 每步需要额外的 remasking 决策，增加了推理复杂度
- 没有利用历史信息，每步重新判断

---

#### STaRR — Spatial-Temporal Token-Dynamics-Aware Responsive Remasking (arXiv 2026.01)

**核心洞察**：现有 remasking 策略用静态 confidence 阈值，忽略了 token confidence 的**时空动态**——同一位置在不同步骤的 confidence 变化趋势才是关键信号。

**方法**：
- **时间维度**：追踪每个 token position 的 confidence 随 denoising step 的变化趋势（上升=稳定，下降=不可靠）
- **空间维度**：考虑相邻 token 的 confidence 相关性（一个错误 token 周围的 token 也可能不可靠）
- 动态调整 remasking 概率，避免不必要的 remask（静态阈值会 remask 太多正确 token）

**好在哪**：
- Training-free
- 比 ReMDM 更精准——减少了对正确 token 的误 remask
- 利用了跨步的 confidence 动态信息（某种程度上缓解了信息损失）

**不足**：
- 需要维护每个 position 的 confidence 历史（额外内存）
- 仍然在 token level 操作，没有 hidden state level 的信息保持
