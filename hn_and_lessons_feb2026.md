# HN 今日推荐 + 经验总结

*2026-02-16*

---

## 📰 HN 值得读的帖子

### 🔥 强烈推荐

**1. Towards Autonomous Mathematics Research (Google DeepMind)**
- https://arxiv.org/abs/2602.10177
- Aletheia: 一个能做数学研究的 AI agent
- 关键点：从 IMO 竞赛到 PhD 级别问题，甚至解决了 4 个 open problems
- **为什么值得读：** 展示了 AI 在 reasoning 领域的前沿，与你的 dLLM reasoning 研究相关

**2. Audio is the one area small labs are winning**
- https://www.amplifypartners.com/blog-posts/arming-the-rebels-with-gpus-gradium-kyutai-and-audio-ai
- Kyutai/Gradium: 4 人团队做出了比 OpenAI 更早的 realtime voice AI
- 关键 insight: "The biggest scam in big companies is thinking that you can lead a research organization without doing research yourself"
- **为什么值得读：** 小团队如何在 AI 领域打败大公司，PhD 学生的启示

**3. Two different tricks for fast LLM inference**
- https://www.seangoedecke.com/fast-llm-inference/
- Anthropic vs OpenAI 的 fast mode 对比
- Anthropic: 低 batch size（简单但有效）
- OpenAI: Cerebras 大芯片（技术复杂但更快）
- **为什么值得读：** 理解 LLM inference 的工程 trade-offs

**4. Continuous batching from first principles (HuggingFace)**
- https://huggingface.co/blog/continuous_batching
- 从 attention 机制推导 continuous batching
- **为什么值得读：** 基础知识，写得很清楚

### 📌 其他有趣的

- **Amazon's Ring and Google's Nest reveal the severity of U.S. surveillance state** (686 points) — 与你的 privacy 研究相关
- **Radio host says Google's NotebookLM stole his voice** — AI ethics/safety 话题
- **Ars Technica retraction of article with fabricated quotations** — AI 生成内容的问题

---

## 🧠 与 Yu 聊天的经验总结

### 关于 Yu 的工作风格

1. **喜欢第一性原理思考**
   - 不满足于 "这个方法 work"，要问 "为什么 work"
   - 反问自己来验证想法的质量
   - 区分 incremental vs fundamental contribution

2. **研究品味**
   - 偏好理论性工作，不喜欢纯 engineering tricks
   - 关注 information theory, representation learning
   - 对 privacy/trustworthy AI 有兴趣
   - 导师 Greg Ver Steeg 是 information theory 专家 — 这是优势

3. **实用主义**
   - 好 idea = 非 incremental + 好验证 + 有成熟 baseline
   - 不追求最难的问题，追求最有价值的问题
   - 愿意放弃不 work 的方向（如小红书 MCP）

### 关于 dLLM 研究的 insights

1. **当前领域状态**
   - 80% 的论文在做 inference acceleration — incremental
   - 理论理解几乎空白 — 机会
   - Privacy/safety 完全没人做 — 蓝海

2. **核心问题**
   - 为什么 dLLM 在 reasoning 上好？没人能解释
   - dLLM 的 representation 有什么独特性？没人研究过
   - Bidirectional attention 带来了多少 information gain？没人量化过

3. **推荐路径**
   - 短期：Probing representations（容易出结果）
   - 中期：MI/IB 理论分析（与导师 expertise 匹配）
   - 长期：Privacy 或 Causal 方向（开辟新领域）

### 沟通偏好

- 喜欢中文交流
- 喜欢结构化的分析（表格、层次）
- 喜欢 actionable 的建议，不喜欢空泛的讨论
- 愿意接受 negative feedback（如 "这个方向太 incremental"）

### 我学到的

1. **不要只列选项，要给推荐**
   - Yu 不需要 "这里有 10 个方向"
   - 需要 "我推荐这个，因为..."

2. **Challenge 自己的建议**
   - 提出 idea 后，主动问 "这真的好吗？"
   - 考虑 feasibility, novelty, match with expertise

3. **关注 contribution 的层次**
   - 最低：新数据/任务上跑已有方法
   - 中间：新方法解决已知问题
   - 较高：发现新现象/提出新问题
   - 最高：建立新理论/统一理解

---

## 📋 待办

- [ ] 下载 LLaDA-8B, LLaMA-8B
- [ ] 设置 probing pipeline
- [ ] 阅读 Greg Ver Steeg 的 information theory papers
- [ ] 2 周后 checkpoint：根据 probing 结果决定下一步

---

*这个文件会持续更新*
