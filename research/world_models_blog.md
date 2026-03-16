# 世界模型（World Models）：AI 的下一个战场

> 当 LLM 还在争论谁的 benchmark 更高时，一场关于"AI 是否真正理解世界"的战争已经打响。

## 一、什么是世界模型？

想象你打台球。还没出杆，你就能在脑中预测球的轨迹——角度、力度、反弹。那个"脑内模拟器"，就是世界模型。

**学术定义**：世界模型是一个压缩的、可模拟的内部表征，能捕捉因果结构并产生预测。

在 AI 语境下：**agent 学到的内部模拟器，能预测"如果我做了动作 A，环境会变成什么样"，从而支持规划和决策，而不是靠试错。**

认知科学家 Stanislas Dehaene 说得更直接：**学习的本质就是形成世界模型的过程。**

## 二、核心争论：LLM 是世界模型吗？

这是目前 AI 领域最大的分歧之一，三个阵营各执一词。

### 阵营一："LLM 就是世界模型"

代表人物：Ilya Sutskever（OpenAI 联合创始人）

> "当我们训练神经网络预测下一个词时……它在学习一个世界模型。文本是世界的投影。"

MIT 研究发现 LLM 确实学到了空间和时间的线性表征，且对不同 prompt 变化具有鲁棒性。

### 阵营二："LLM 绝对不是世界模型"

代表人物：Yann LeCun + Richard Sutton

LeCun 2025 年从 Meta 离职创办 AMI Labs，2026 年 3 月融了 **10.3 亿美元**（欧洲最大种子轮），all in 世界模型。

Richard Sutton（RL 之父）更尖锐：**"LLM 学的不是世界的法则，而是人类对话的模式。它模拟的是'一个人会说什么'，而不是'世界会发生什么'。"**

### 阵营三：中间派

代表人物：Melanie Mitchell

**LLM 拥有零碎且不完整的世界模型。** 语言本身就是对世界的稀疏描述，LLM 自然继承了这种局限性。它学到了一些因果关系，但远不是完整的物理世界模型。

## 三、两大技术流派

### 表征派（Representation）
在潜在空间中学习抽象表征，不生成像素，丢弃不重要的细节。
- 代表：LeCun 的 **JEPA**（Joint Embedding Predictive Architecture）
- 核心思想：预测发生在抽象空间，而非像素空间

### 生成派（Generation）
直接生成未来的视频/图像帧。
- 代表：DeepMind **Genie 3**、OpenAI **Sora**
- 核心思想：能生成逼真的未来 = 理解了世界

## 四、五大技术路线（2025-2026）

| 路线 | 领军人物 | 方法 | 状态 |
|------|---------|------|------|
| **JEPA** | LeCun / AMI Labs | 潜在空间联合嵌入预测 | $10.3B 融资，尚未发布产品 |
| **Dreamer** | Danijar Hafner (Google) | Model-based RL，想象力规划 | DreamerV3 登 Nature 2025 |
| **Genie 3** | Google DeepMind | 实时可交互 3D 世界生成 | 已发布，transformer 架构 |
| **Marble** | 李飞飞 / World Labs | 空间智能，3D 场景理解 | 强调空间推理能力 |
| **AXIOM** | Karl Friston / Verses.ai | 主动推理 + 物体槽位建模 | 最小化自由能框架 |

## 五、李飞飞的三个能力标准

李飞飞定义了世界模型必须具备的三种能力：

1. **空间理解**：距离、方向、物体关系
2. **物理预测**：物体会怎么运动
3. **可交互性**：动作改变世界状态

她的判断：当前 AI 在空间能力上与人类差距巨大——无法估计距离、不能在脑中旋转物体、无法预测基本物理规律。

## 六、一个硬核的数学结论

Richens 等人（2025）证明了一个定理：

> **任何能在多步目标导向任务上保持低后悔的智能体，都必然学会了环境的预测模型。**

换句话说，世界模型不是可选项，而是通用智能的**数学必然**。

## 七、四大核心科学问题

### 1. 长时域误差累积
自回归生成的暴露偏差导致误差随步数指数增长，>50步后物理规则崩溃。当前解法包括残差学习（ReDRAW）、因果滑动窗口（PAN）、记忆回查等。

### 2. 空间与物理一致性
生成式模型画面好看但不遵守物理——物体穿模、质量守恒失效。3D原生架构（Genie 3）和 3D Gaussian Splatting 是前沿方向。

### 3. 交互可控制性
视频生成模型是 prompt-to-video，不能响应 agent 动作输入。Dreamer 的 latent policy 直接在隐空间规划是一种解法。

### 4. 评估指标缺失
多数论文还在用 PSNR/LPIPS 评像素保真度，但物理任务需要**物理一致性**指标。新趋势是 Task Completion Rate 和 Physics Plausibility Score。

## 八、四大应用领域

- **自动驾驶**：Drive-WM, GAIA-1（多视角联合建模）
- **机器人操作**：LUMOS（语言条件模仿学习）、DreamerV3
- **游戏与仿真**：Genie 3（任意游戏世界建模）
- **导航**：X-MOBILITY（NVIDIA，端到端可泛化导航）

## 九、未来共识

多数人同意的方向是 **"LLM + 世界模型 + 执行层"三层协同架构**：
- LLM 负责语言和推理
- 世界模型负责物理世界的预测和模拟
- 执行层负责具身动作

## 十、关键资源

- 综述论文：[Understanding World or Predicting Future?](https://arxiv.org/abs/2411.14499)（清华，ACM CSUR 2025）
- 综述论文：[World Models for Embodied AI](https://arxiv.org/abs/2510.16732)（南开）
- 论文列表：[AwesomeWorldModels](https://github.com/Li-Zn-H/AwesomeWorldModels)（50+ 分类论文）
- 技术路线对比：[Five Competing Approaches](https://themesis.com/2026/01/07/world-models-five-competing-approaches/)

---

*世界模型的探索，不是要打造一个替代 LLM 的"博学智者"，而是让 AI 真正理解它所处的物理世界。这场竞赛才刚刚开始。*
