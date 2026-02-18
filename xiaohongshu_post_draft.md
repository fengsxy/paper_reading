# 小红书帖子草稿：dLLM 研究调研

---

## 帖子 1: 调研总结

**标题：** 🔥 读了100篇论文后，我发现 Diffusion LLM 最大的研究空白

**正文：**

做 PhD 第一件事就是调研 📚

花了一周时间，用 Scholar Inbox 搜了 100+ 篇 diffusion language model 的论文，发现了一个几乎没人做的方向 👀

先说结论：**Soft Mask 和 Latent Reasoning 的关系，完全是空白！**

---

**什么是 Soft Mask？**

传统 diffusion LLM（比如 LLaDA）用 hard mask：token 要么是 [MASK]，要么是确定的词

Soft mask 保留中间信息：
• Embedding blending（混合 mask 和预测的 embedding）
• Distribution evolution（保留整个概率分布）
• Residual injection（注入 hidden states）

---

**什么是 Latent Reasoning？**

COCONUT（NeurIPS 2024）发现：
• 不把中间推理步骤 decode 成文字
• 直接在 latent space 传递 hidden state
• 结果：能同时探索多条推理路径（BFS）

---

**为什么这是个 gap？**

Soft mask 也在保留"中间信息"
Latent reasoning 也在保留"中间信息"

但没人问：**它们是同一个东西吗？**

• Soft mask 能不能实现 latent reasoning？
• 为什么现有 soft mask 没有展现 BFS 能力？
• 需要什么样的 training 才能让 soft mask 变成 latent reasoning？

---

**我的假设：**

1. Soft mask 和 COCONUT 的 continuous thought 本质相似
2. 但 granularity 不同（per-token vs whole-sequence）
3. 需要新的 training objective 才能 unlock

---

这个方向：
✅ 完全空白，没人做
✅ 有理论深度（information theory）
✅ 实用价值高（如果成功，dLLM 能获得 latent reasoning 能力）

如果你也在做 diffusion LLM 研究，欢迎讨论！

#PhD日常 #科研 #AI研究 #DiffusionModel #LLM #机器学习

---

## 帖子 2: 苏格拉底式追问

**标题：** 🤔 用苏格拉底式追问挑战自己的研究假设

**正文：**

做研究最怕的是什么？

**自己骗自己** 😅

所以我学会了一个方法：苏格拉底式追问

---

**我的假设：** Soft mask ≈ COCONUT 的 continuous thought

**追问 1：真的相同吗？**

COCONUT：single vector，代表整个 reasoning state
Soft mask：per-token 的 soft representation

等等... **granularity 不同！**

修正：它们有联系但不完全相同

---

**追问 2：为什么现有 soft mask 没有 BFS 能力？**

COCONUT 怎么训练的？
→ End-to-end，只 supervise final answer

Soft mask 怎么训练的？
→ Step-by-step，supervise 每一步

**关键区别！** Soft mask 没被 forced to encode multiple paths

---

**追问 3：MI 能指导 remask 吗？**

理想：MI(token; ground_truth | context)
问题：inference 时不知道 ground truth

所以 MI 在 inference 时不可计算...
Confidence 只是 proxy，可能 misleading

**需要新的 metric！**

---

**追问后的收获：**

1. 原假设太粗糙，需要细化
2. Training objective 是关键
3. 需要设计实验验证

这个方法帮我避免了很多弯路 💡

#科研方法 #PhD #批判性思维 #AI研究

---

## 帖子 3: 论文分类

**标题：** 📊 dLLM 论文分类｜100篇论文的 7 大方向

**正文：**

整理了 100+ 篇 diffusion language model 论文，分成 7 大方向：

---

**1️⃣ Remask / Self-Correction (~25篇)**
核心：让模型能"反悔"，重新生成不确定的 token
代表作：RemeDi, ProSeCo, PRISM

**2️⃣ Soft Mask / Continuous (~20篇)**
核心：不用 hard mask，保留中间信息
代表作：EvoToken, RCD, Soft-Masked DLM

**3️⃣ Reasoning (~20篇)**
核心：让 diffusion 模型做推理
代表作：Diffusion of Thought, COCONUT

**4️⃣ Acceleration (~25篇)**
核心：加速推理
代表作：Fast-dLLM, FlashDLM, dInfer

**5️⃣ Theory (~15篇)**
核心：理论分析
代表作：Convergence Theory, Information-Theoretic Diffusion

**6️⃣ Training (~15篇)**
核心：训练方法
代表作：MDLM, LLaDA, Scaling

**7️⃣ Test-Time Scaling (~10篇)**
核心：推理时 scaling
代表作：Inference Scaling Laws

---

**有意思的发现：**

• 加速方向最卷（~25%）
• 理论方向最少（~15%）
• Soft mask + Latent reasoning 的交叉几乎没人做

完整调研文档我放 GitHub 了，需要的评论区留言 📝

#论文整理 #AI研究 #DiffusionModel #PhD

---

## 配图建议

**帖子 1：**
- 一张 gap 分析的思维导图
- 或者 Soft Mask vs Latent Reasoning 的对比图

**帖子 2：**
- 苏格拉底式追问的流程图
- 假设 → 追问 → 修正 的循环图

**帖子 3：**
- 7 大方向的饼图或柱状图
- 论文数量分布图

---

## 发布建议

1. 先发帖子 3（分类），建立专业形象
2. 再发帖子 1（gap 分析），引发讨论
3. 最后发帖子 2（方法论），展示思考深度

每篇间隔 1-2 天，避免刷屏
