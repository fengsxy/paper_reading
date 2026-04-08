# dLLM 的 Hard vs Soft 约束分离：架构层面的结构性优势

## 问题的本质

Yu 在 2026-04-07 晚间提出了一个深层问题：现在 LLMs 做 planning 时，hard constraints（必须满足）和 soft constraints（最好满足）混在一起处理——prompt 里用"必须"vs"最好"的语言区分，但这本质上是语言层面的 hack，不是结构性的分离。这可能是架构问题而非模型问题。

这个观察非常深刻。我来深入分析 diffusion 范式是否在这方面有结构性优势。

## AR 模型的核心限制：顺序承诺（Sequential Commitment）

AR 生成是逐 token 的即时决策。每次输出一个 token，模型就"锁定"了这个决定，无法反悔。

**关键问题：没有机制区分两种约束的"锁定程度"。**

举例：模型在 planning 时决定"先做 A 再做 B"。这个序列选择可能来自：
- Hard constraint（如"A 的输出是 B 的输入"——必须串行）
- Soft constraint（如"一般习惯先 A 后 B"——可以交换）

两种情况的 token 序列看起来完全一样。模型只能靠 prompt 里的语言暗示（"必须"vs"建议"）来隐式学习，但没有任何结构性机制来保证 hard constraint 真的被满足。

**理论根源：** AR 的概率模型 p(x_t | x_{<t}) 是即时条件分布，每个 step 的决策都条件于且仅条件于历史。这是"局部"的概率分布，无法表达"全局约束"——除非把所有约束编码进每个位置的局部条件。

## Diffusion 的结构性优势 I：迭代 Refinement 作为承诺层级机制

Diffusion 的去噪过程是迭代的：x_T → x_{T-1} → ... → x_0。每一步都基于当前的 noisy 状态和条件信息来预测更清晰的版本。

**这天然产生了一种"承诺层级"（Commitment Hierarchy）：**

- **Early steps（T >> 0）**：高度抽象，轨迹空间巨大，模型在探索宏观结构。此时的决策可以被后续步骤大幅覆盖——这是"软"的。
- **Late steps（T → 0）**：高度具体，轨迹空间收缩，模型在精调细节。此时的决策很难被改变——这是"硬"的。

这和人类 planning 的直觉完全一致：**先定大框架（软），后锁细节（硬）。**

**Hard vs Soft constraint 映射：**
- Hard constraints（如安全边界、依赖关系）→ 在 early steps 就收敛到 attractor basin，之后几乎不被扰动
- Soft constraints（如风格、次序偏好）→ 在 late steps 仍有调整空间

这不需要任何语言提示。Diffusion 的去噪 schedule 本身就实现了约束优先级的结构化分离。

## Diffusion 的结构性优势 II：双向条件（Bidirectional Conditioning）

AR 模型是严格单向的：每个 token 只条件于左侧上下文。规划时，这意味着"后面的计划"无法影响"前面的决策"。

Diffusion 模型在每个 denoising step，预测 p(x_t | x_{t+1}, ..., x_T, c)，即**同时条件于所有未来的 token**。

**这带来一个关键能力：全局约束的端到端满足。**

举例：假设有个 hard constraint "任务必须在第 5 步完成"。在 AR 模型中，这需要靠 prompt 提示"不要超过 5 步"——模型没有结构性的理由在第 5 步停止。在 diffusion 模型中，c 包含"结束时间"的完整信息，去噪过程可以从最终状态反向影响每一步的生成，确保全局一致性。

**这和 Gated DeltaNet（Yu 的研究）的类比：** Gated DeltaNet 通过门控机制选择性保留/遗忘信息，实现精确的上下文编辑。Diffusion 的 bidirectional conditioning 本质上也是一种"全局视图"——不是选择性遗忘，而是选择性关注。

## Diffusion 的结构性优势 III：denoising trajectory 作为 plan refinement 的隐喻

Diffusion 的去噪轨迹 x_T → x_0 可以看作一个**从抽象计划到具体计划的 refinement 过程**：

1. x_T：完全噪声，等价于"任意可能的 plan"
2. x_{T-1}：稍微清晰，相当于"plan 的高层结构"
3. ...
4. x_0：完整 plan，具体到每个 action

这和 **HTN（Hierarchical Task Network）planning** 的 plan refinement 有惊人相似的结构：
- HTN：高层任务 → 子任务分解 → 原子 action
- Diffusion：噪声 plan → 宏观结构 → 细节 plan

区别在于：HTN 需要手工设计 task hierarchy，而 diffusion 的 hierarchy 是从数据中学习的。

## 与现有工作的关系

- **Projected Diffusion（NeurIPS 2024）**：用 guidance 处理 hard constraints，在特定 denoising steps 施加外部信号。但没有区分 hard/soft 的层次结构。
- **Constraints-Guided Diffusion Reasoner（2025）**：根据 constraint 类型调整 denoising过程的权重。但仍是工程性处理，不是结构性分离。
- **JM2D（CoRL 2025）**：将 diffusion 用于机器人 planning 的层级轨迹生成。

**研究空白：** 没有人从"hard/soft constraint 的结构性分离"角度系统分析 diffusion vs AR 的差异。这可能是一个有价值的小众研究点。

## 关键洞察：承诺层级（Commitment Hierarchy）的信息论解释

Hard constraints 应该是**信息论意义下对噪声不变量**——无论怎么加噪声，hard constraint 的满足状态不变。

Soft constraints 是**噪声敏感的**——加噪后可能从"满足"变为"不满足"。

Diffusion 的去噪过程恰好从噪声空间映射到数据流形。如果 hard constraint 是流形上的结构化子空间，那么去噪过程会在早期就收敛到这个子空间（因为它对噪声不变量），而 soft constraints 则会在后期继续调整。

**这意味着：diffusion 的 denoising schedule 本身就在做 constraint prioritization，不需要额外的机制。**

## 这个洞察的局限

1. **理论 vs 工程**：Diffusion 的 hard/soft 分离目前只是理论分析，没有实验验证。实际训练中，模型是否真的学到了这种分离还是未知数。
2. **任务类型依赖**：这个优势可能只对"约束丰富的 planning 任务"有意义，对于开放式的创意生成可能不明显。
3. **dLLM 训练挑战**：让 dLLM 在 planning 任务上学到这个分离，可能需要特定的训练目标（如 contrastive denoising或分层 reward）。

## 下一步

1. 调研 Projected Diffusion 的具体方法，看是否能提取出可实验的假设
2. 设计一个简单的 toy experiment：在固定的 hard/soft constraint 配置下，对比 AR 和 diffusion model 的 constraint satisfaction rate
3. 联系 Gated DeltaNet 的研究：门控机制是否可以用于显式控制 hard/soft commitment 的边界？

---

*这是 2026-04-08 的自主研究笔记，基于与 Yu 的晚间讨论。*
