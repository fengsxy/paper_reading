# Daily Paper Review — 2026-04-10

**Paper**: Breaking Block Boundaries: Anchor-based History-stable Decoding for Diffusion Large Language Models
**arXiv ID**: 2604.08964v1
**Date**: 2026-04-10
**Tag**: dLLM / Decoding / Stable Token Detection

---

## 1. Task

**问题形式化**：

Semi-autoregressive（Semi-AR）decoding 在 base dLLM 和高级解码策略中广泛使用。但存在一个核心问题：

> **Block constraints**——每个 block 的 token 只能在 block 内部被解锁，不能跨越 block boundary 提前 commit。
>
> 这导致很多跨 block 的 stable token（已经收敛的 token）被不必要地延迟解锁——因为 block boundary 限制了它们只能在 block 轮到时才被处理。

论文的三个发现：
1. **Naive lookahead decoding 不可靠**——只看当前 step 的置信度无法判断 token 是否真正稳定
2. **Token stability 与收敛趋势高度相关**——看历史趋势比单步判断更准
3. **历史信息被隔离**——现有方法没有利用历史信息

**目标**：设计 Anchor-based History-stable Decoding（AHD），用动态 anchor 监控 token 稳定性趋势，实现跨 block boundary 的 early decoding。

---

## 2. Challenge

| 方法 | 困境 |
|------|------|
| Fixed block | block boundary 硬性限制，stable token 被延迟 |
| Naive lookahead | 只看当前 step，被高置信度的假稳定欺骗 |
| Confidence threshold only | 单步信号，不考虑时间趋势 |
| 没有利用历史信息 | AR 模型天然没有历史，但 dLLM 有完整的去噪轨迹 |

**根本问题**：如何判断一个 token 在跨 block 后仍然 stable？这需要历史信息。

---

## 3. Insight & Novelty

### 3.1 Insight

**Insight 1：Token stability 不是单步属性，而是时间序列属性。**

> 单步置信度高 ≠ token 已经稳定。可能是假稳定（当前 step 置信度高，但之前 step 不稳定）。
> 真正的稳定 token：连续多个 step 置信度都高，且变化趋势一致。

**受启发于**：时间序列分析的常识——判断一个信号是否"稳定"，要看它的趋势，而不是单个采样点。

**Insight 2：收敛趋势（convergence trend）是 token stability 的最佳指标。**

> 如果一个 token 的预测在最近 N 个 step 持续向某个方向变化（熵下降、置信度上升），它更可能真正稳定。
> 如果一个 token 的预测在波动，说明还未收敛。

**受启发于**：物理中的惯性定律——已收敛的系统状态更难被改变。

**Insight 3：跨 block 信息可以帮助稳定 token 的判断。**

> 当一个 block 完成时，它的输出提供了额外信息——如果跨 block 的 token 与已完成 block 的输出一致，说明该 token 很可能已稳定。

### 3.2 Novelty

**创新点 1**：Anchor 机制——动态跟踪 token 稳定性趋势
- **解决的问题**：如何利用历史信息判断 token stability
- **受启发于**：收敛趋势观察 + 历史信息隔离问题
- **具体设计**：设置动态 anchor，每个 token 维护一个 stability trend vector，每步更新，用趋势而非单步值判断稳定性

**创新点 2**：跨 block early decoding
- **解决的问题**：block boundary 阻止 stable token 提前 commit
- **受启发于**：跨 block 信息帮助 stability 判断
- **具体设计**：当 anchor 判断某 token 已稳定，且它属于下一个 block，直接提前解锁——不需要等下一个 block 开始

**创新点 3**：验证了 naive lookahead 不可靠
- **解决的问题**：澄清了现有方法的问题根源
- **受启发于**：实验观察
- **具体设计**：对比实验显示 naive lookahead 在多个任务上与 AHD 差距显著

---

## 4. Potential Flaw

### 4.1 情境局限

- **不同 denoising schedule 效果未知**：不同 step 数的模型需要不同的 anchor 更新策略
- **与其他解码策略叠加效果未充分探索**：AHD + SWD 或 AHD + VSB 的组合效果
- **计算开销**：维护每个 token 的 anchor 需要额外存储和计算

### 4.2 数据问题

- **收敛速度慢的数据**：某些数据域 token 天然收敛慢，AHD 的 anchor 判断可能过于保守
- **收敛速度快的 trivial 数据**：anchor 可能过于激进，过早 commit

### 4.3 值得挖掘的方向

**最值得做的**：AHD + VSB 的 unified 框架。

> AHD 用 anchor trend 判断 token 是否跨 block stable
> VSB 用 NF vs FA divergence 判断 block 是否 self-contained
>
> 这两个方法可以互补：AHD 做 token-level stability tracking，VSB 做 block-level self-containedness check。
>
> 如果设计一个联合框架：AHD 首先识别 stable tokens，VSB 然后判断哪些 block 可以 commit。这是一个更完整的 dLLM 解码系统。

**另一方向**：将 AHD 的 anchor 思想与 **R2-dLLM 的 temporal finalization** 对比——两者都在做 temporal stability 判断，但是用趋势（AHD）还是用阈值（R2-dLLM）？哪个更 robust？

---

## 5. Motivation

**General idea 推导路径**（第一性原理）：

> Block decoding 的初衷是：限制每次处理的 token 数量，降低计算复杂度。
>
> 但仔细想：这个限制是必要的吗？
>
> **不是。** block boundary 是人为设定的，不是由 token 的实际状态决定的。
>
> 如果某个 token 已经稳定了，它就不需要再占用下一个 block 的计算资源——即使它属于下一个 block，它也可以提前 commit。
>
> **但我们怎么知道一个 token 是否已经稳定？**
>
> 单一 step 的置信度不够——它可能是假稳定。
>
> **那看多个 step 的趋势呢？**
>
> 如果一个 token 在连续 5 个 step 的预测几乎相同，它很可能已经稳定了。这比单步判断更可靠。
>
> 一旦有了趋势判断，block boundary 就变成了人工约束——它不应该阻止 stable token 的 early commit。
>
> 这就是 AHD 的核心洞察：**block boundary 应该由 token 的实际收敛状态决定，而不是由预先设定的顺序决定。**
