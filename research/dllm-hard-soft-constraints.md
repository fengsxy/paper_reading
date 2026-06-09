# dLLM Hard/Soft 约束分离：架构层面的结构性优势

**I-012 初稿 | 2026-06-09（拖延52+ 天后）**

---

## 0. 核心命题

AR 生成模型在做 planning 时，hard constraints（必须满足）和 soft constraints（最好满足）混在一起处理——靠 prompt 里的"必须"vs"最好"来区分，但这是语言层面的 hack，不是结构性的分离。Diffusion 范式在架构层面天然提供了一种 commitment hierarchy，这是本文的核心观察。

---

## 1. AR 模型的核心限制：顺序承诺（Sequential Commitment）

AR 生成是逐 token 的即时决策。每次输出一个 token，模型就"锁定"了这个决定。

**没有机制区分两种约束的锁定程度。**

举例：模型在 planning 时决定"先做 A 再做 B"。这个序列选择可能来自：
- Hard constraint（如"A 的输出是 B 的输入"——必须串行）
- Soft constraint（如"一般习惯先 A 后 B"——可以交换）

两种情况的 token 序列看起来完全一样。模型只能靠语言暗示来隐式学习，没有任何结构性机制保证 hard constraint 真的被满足。

**信息论根源：** AR 的概率模型 p(x_t | x_{<t}) 是即时条件分布，每个 step 的决策都条件于且仅条件于历史。这是"局部"的概率分布，无法表达"全局约束"——除非把所有约束编码进每个位置的局部条件。

---

## 2. Diffusion 的结构性优势 I：迭代 Refinement 作为承诺层级机制

Diffusion 的去噪过程是迭代的：x_T → x_{T-1} → ... → x_0。

**这天然产生了一种"承诺层级"（Commitment Hierarchy）：**

- **Early steps（T >> 0）**：高度抽象，轨迹空间巨大，模型在探索宏观结构。此时的决策可以被后续步骤大幅覆盖——这是"软"的。
- **Late steps（T → 0）**：高度具体，轨迹空间收缩，模型在精调细节。此时的决策很难被改变——这是"硬"的。

这和人类 planning 的直觉完全一致：**先定大框架（软），后锁细节（硬）。**

**Hard vs Soft constraint 映射：**
- Hard constraints（如安全边界、依赖关系）→ 在 early steps 就收敛到 attractor basin，之后几乎不被扰动
- Soft constraints（如风格、次序偏好）→ 在 late steps 仍有调整空间

这不需要任何语言提示。Diffusion 的 denoising schedule 本身就实现了约束优先级的结构化分离。

---

## 3. 新理论锚点：Entropy-Cut MH 与 FoCore HD Tokens

### 3.1 Entropy-Cut MH（2605.30327）：推理发生在高熵点

**核心发现：**推理发生在**高熵**（不确定性）点，而不是低熵（确定性）点。"Latent space 太确定 = 没有未决决策的空间 = 没有推理。"

这和 H/S 框架的深层联系：
- **Hard constraint 锁定点 = 高熵决策点**：当多条路径在此分叉，选哪条直接影响最终 outcome 的结构。这是推理发生的时刻。
- **Soft constraint 调整点 = 低熵区间**：此时大部分路径已经收敛，调整只影响细节，不影响全局结构。

**关键推论：** AR 模型的问题不仅是"顺序承诺"，而是**在错误的时间尺度（token-level）做推理**。真正需要推理的是在宏观结构分叉点，而不是每个 token 的生成。

### 3.2 FoCore HD Tokens：S-layer 收敛点 = 逻辑锚点

**核心发现：** High-density tokens = S-layer 收敛点，提前稳定，是 reasoning trajectories 中的逻辑锚点。

在 diffusion 去噪过程中：
- **HD tokens** 在 S-layer 提前收敛 → 对应 hard constraint 被满足的结构点
- **LD tokens** 在 L-layer 继续演化 → 对应 soft constraint 的调整空间

**与 VSB 的联系：** VSB 的 divergence threshold 本质上在判断某 token 是否已进入 hard constraint 锁定状态。VSB commit 的 token = entropy 已降至临界点以下 = hard constraint 已满足。

---

## 4. H/S 地形假说（已确认反转）

**原始假设（错误）：** H 先于 S 锁定（S 是 continuous hillside，H 是 abrupt cliff）

**修正假设（确认）：**
- **S-约束 = 丘陵（continuous）**：soft constraints 在整个去噪轨迹中渐进调整
- **H-约束 = 悬崖（abrupt）**：hard constraints 在高熵决策点突然锁定，之后不受噪声影响

**信息论解释：**
- Hard constraints = 对噪声不变量（noise-invariant attractor basin）
- Soft constraints = 噪声敏感（noise-sensitive）
- Diffusion 去噪从高噪声向低噪声演进，恰好使 hard constraint 在早期就收敛到 attractor basin

---

## 5. 与现有工作的关系

- **VSB（2604.23994）**：验证采样，commit decision = entropy 降至临界点。**与 H/S 框架直接相关。**
- **FoCore（2605.01373）**：HD tokens = S-layer 收敛锚点。**提供 token-level 收敛的实证。**
- **DEMASK**：masked diffusion + semantic-level decoding，联合框架。
- **Entropy-Cut MH（2605.30327）**：推理在高熵点发生，**提供信息论基础。**
- **CRH（ICLR 2025 Spotlight）**：chain-of-thought + reasoning emergence，为 H/S 提供认知科学支撑。

**研究空白：** 没有人从"hard/soft constraint 的结构性分离"角度系统分析 diffusion vs AR 的差异，结合 Entropy-Cut MH 的信息论框架和 FoCore 的 token-level 收敛证据。

---

## 6. 可行的研究设计

### 6.1 理论方向
- VSB divergence threshold 可作为 H-constraint 锁定的量化标准
- HD tokens 的 S-layer 收敛位置可作为 commitment boundary 的预测信号
- Entropy-Cut MH 的 mixing time 理论可以解释为什么 diffusion 的多步采样比 AR 的 greedy decoding 更适合复杂推理

### 6.2 实验方向
- 在固定 hard/soft constraint 配置下，对比 AR 和 diffusion model 的 constraint satisfaction rate
- 用 HD tokens 作为 monitor，在去噪过程中预测 hard constraint 是否已被满足
- 用 VSB-style commit decision 判断是否应该"锁定"当前宏观结构

---

## 7. 局限

1. **理论 vs 工程**：Diffusion 的 hard/soft 分离目前只是理论分析，没有实验验证。实际训练中，模型是否真的学到了这种分离还是未知数。
2. **任务类型依赖**：这个优势可能只对"约束丰富的 planning 任务"有意义，对于开放式的创意生成可能不明显。
3. **dLLM 训练挑战**：让 dLLM 在 planning 任务上学到这个分离，可能需要特定的训练目标。

---

## 8. 与 Yu 研究方向的联系

Yu 的 Gated DeltaNet（线性注意力 +门控机制）天然适合实现 hard/soft commitment边界的显式控制：
- **门控 = 选择性记忆/遗忘**：镜像 hard constraint 锁定 vs soft adjustment
- **三层贡献**：信息论框架 + 方法（GRU→GDN）+ 系统（与 KV cache 统一）

---

*初稿完成于 2026-06-09。等待 Yu 的反馈。*