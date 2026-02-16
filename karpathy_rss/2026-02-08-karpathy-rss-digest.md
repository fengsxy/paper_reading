# Karpathy RSS 精选 | 2026-02-02 ~ 02-08

> 这周的主题：AI Agent 正在重塑软件开发的每一个环节。从 Codex App 发布到 Dark Factory 模式，从 Mitchell Hashimoto 的 AI 采用之旅到 David Crawshaw 的 "95% 时间在读代码"。

---

## 🏭 Simon Willison: StrongDM's Dark Factory

**来源**: [simonwillison.net](https://simonwillison.net/2026/Feb/7/software-factory/)

### 一句话

有团队已经在用 AI 写代码，而且人类根本不看代码。

### 核心观点

Dan Shapiro 提出了 AI 采用的五个层级，最高级叫 "Dark Factory"——AI 写代码，人类不看代码，直接部署。

听起来疯狂？StrongDM 的团队已经在这么做了。

他们发布了 [Software Factories and the Agentic Moment](https://factory.strongdm.ai)，描述了他们的工作方式：

- AI 写代码
- AI 写测试
- AI 跑测试
- 人类只看结果

Simon 的评价：这是真正的 "Level 5" AI 采用。

### 我的看法

Dark Factory 模式的前提是：**测试覆盖率足够高，你可以信任测试结果而不是代码本身**。

这其实是 TDD 的终极形态——你定义行为，AI 实现行为，测试验证行为。代码变成了中间产物，不是最终产物。

对于研究者来说，这意味着：**未来的软件工程研究可能要从 "如何写好代码" 转向 "如何定义好行为"**。

---

## 🎮 Mitchell Hashimoto: My AI Adoption Journey

**来源**: [mitchellh.com](https://mitchellh.com/writing/my-ai-adoption-journey)

### 一句话

Terraform 和 Vagrant 的创造者分享了他的 AI 采用之旅。

### 核心观点

Mitchell Hashimoto 是 HashiCorp 的创始人，写过 Terraform、Vagrant、Packer 等著名工具。他的 AI 采用建议非常实用：

**Step 1: 放弃 Chatbot**
> "Chatbots have real value... but their utility in coding is highly limited."

**Step 2: 复现你自己的工作**
> "I literally did the work twice. I'd do the work manually, and then I'd fight an agent to produce identical results."

**Step 3: End-of-Day Agents**
> "Block out the last 30 minutes of every day to kick off one or more agents."

**Step 4: Outsource the Slam Dunks**
> 你知道 agent 能搞定的任务，让它做，你去做更有趣的事。

**Step 5: Engineer the Harness**
> 每次 agent 做错事，就更新 AGENTS.md 防止再犯。

**Step 6: Always Have an Agent Running**
> 目标是随时都有 agent 在跑。目前他做到了 10-20%。

### 我的看法

Mitchell 的方法论最有价值的是 **Step 2: 复现你自己的工作**。

大多数人学 AI 工具的方式是：让 AI 做新任务，然后评估结果。问题是你不知道 "好" 的标准是什么。

Mitchell 的方法是：先自己做，再让 AI 做同样的事。这样你有一个 ground truth 来评估 AI 的输出。

对于 PhD 学生：**用这个方法学 AI 工具**。先手写一个实验，再让 AI 复现，你会学到 AI 的能力边界在哪。

---

## 🎉 David Crawshaw: Eight More Months of Agents

**来源**: [crawshaw.io](https://crawshaw.io/blog/eight-more-months-of-agents)

### 一句话

一年前 AI 写 25% 的代码，现在写 90%。

### 核心观点

David Crawshaw（前 Tailscale CTO）更新了他的 AI 编程体验：

**一年前 vs 现在：**
- 2025 年 2 月：Claude Code 能写 25% 的代码
- 2026 年 2 月：最新 Opus 能写 90% 的代码

**时间分配变化：**
- 大公司：80% 读代码，20% 写代码
- 创业公司（以前）：50-50
- 创业公司（现在）：95% 读代码，5% 写代码

**IDE 正在衰落：**
> "The history of IDEs is so strange... Since those glorious moments in 1999, I have spent more of my programming life outside of IDEs than in them."

**最重要的一句：**
> "I am having more fun programming than I ever have, because so many more of the programs I wish I could find the time to write actually exist."

### 我的看法

Crawshaw 的数据点很重要：**90% 的代码由 AI 写**。

但更重要的是他的心态：他不是在抱怨 AI 抢了他的工作，而是在庆祝他能做更多想做的事。

他的哲学：
> "The best software for an agent is whatever is best for a programmer."

这意味着：**为程序员设计的工具，自动就是为 AI 设计的工具**。因为每个用户都会有 agent 帮他们写代码。

---

## 🔒 Mitchell Hashimoto: Vouch

**来源**: [github.com/mitchellh/vouch](https://github.com/mitchellh/vouch)

### 一句话

开源项目被 AI 生成的垃圾 PR 淹没了，Mitchell 做了个工具来解决。

### 核心观点

问题：AI 让提交 PR 的门槛降到了零，开源项目被垃圾 PR 淹没。

解决方案：**Vouch** —— 一个信任系统。

- 未被 vouch 的用户不能贡献
- 被 denounce 的用户被永久封禁
- 贡献者通过 GitHub issue/discussion 评论来 vouch 或 denounce

Mitchell 的态度：
> "Who and how someone is vouched or denounced is up to the project. I'm not the value police for the world."

### 我的看法

Vouch 是对 **AI 时代开源治理** 的一个有趣尝试。

传统开源的假设是：提交 PR 有成本（时间、精力），所以大多数 PR 是善意的。AI 打破了这个假设。

Vouch 的解决方案是：**重新引入社会成本**。你需要被社区认可才能贡献。

这可能是未来开源项目的标配。

---

## 🎨 Brandon Sanderson on AI and Art

**来源**: [YouTube](https://www.youtube.com/watch?v=mb3uK-_QkOo&t=832s) (via Guido van Rossum)

### 一句话

AI 能创作，但它不能被创作改变。

### 核心观点

Brandon Sanderson（《风暴之光》作者）谈 AI 和艺术：

> "The book, the painting, the film script is not the only art. It's important, but in a way it's a receipt. It's a diploma."

> "The most important change made by an artistic endeavor is the change it makes in you."

> "I don't care if the AI can create something that is better than what we can create, because it cannot be changed by that creation."

他把 AI 和《星际迷航》里的 Data 对比：Data 创作艺术是因为他想成长、想理解。AI 不是。

### 我的看法

Sanderson 的观点很深刻：**艺术的价值不在于产出，而在于过程对创作者的改变**。

这对研究者也适用：写论文的价值不只是论文本身，而是写论文过程中你学到的东西。

如果你让 AI 写论文，你得到了论文，但失去了学习。

---

## 🔐 Deno Sandbox

**来源**: [deno.com](https://deno.com/blog/introducing-deno-sandbox)

### 一句话

Deno 发布了一个沙箱产品，最酷的功能是 API 密钥不会泄露给沙箱内的代码。

### 核心观点

Deno 发布了 Deno Sandbox，一个托管的代码执行环境。

最有趣的功能是 **密钥代理**：

```python
with sdk.sandboxes.create(
    allowNet=["api.openai.com"],
    secrets={
        "OPENAI_API_KEY": {
            "hosts": ["api.openai.com"],
            "value": os.environ.get("OPENAI_API_KEY"),
        }
    },
) as sandbox:
    # $OPENAI_API_KEY 在容器内是一个占位符
    # 出站请求经过代理，代理替换占位符为真实密钥
```

这意味着：**沙箱内的恶意代码无法窃取你的 API 密钥**。

### 我的看法

这是 **AI Agent 安全** 的一个重要进展。

Agent 需要访问 API，但你不想让 agent 能窃取密钥。Deno 的方案是：agent 只能用密钥，不能看密钥。

对于做 AI 安全研究的人：这是一个值得研究的方向。

---

## 📊 Claude Opus 4.6 Fast Mode

**来源**: [code.claude.com](https://code.claude.com/docs/en/fast-mode)

### 一句话

Anthropic 发布了 Opus 4.6 的快速模式，速度快 2.5x，价格贵 6x。

### 核心观点

新功能：在 Claude Code 里输入 `/fast` 可以用快速版 Opus 4.6。

价格：
- 普通 Opus：$5/M input, $25/M output
- Fast Opus：$30/M input, $150/M output（6x）
- 2 月 16 日前 50% 折扣（3x）

速度：快 2.5x。

### 我的看法

这个定价策略很有意思：**用价格来分配稀缺资源**。

快速推理需要更多硬件，Anthropic 用高价来限制使用量。愿意付钱的人（比如赶 deadline 的开发者）可以用，不急的人用普通版。

对于研究者：**速度和成本的 tradeoff 是一个研究方向**。什么时候值得花 6x 的钱换 2.5x 的速度？

---

## 🧠 Tom Dale on Mental Health Crisis

**来源**: [Twitter @tomdale](https://twitter.com/tomdale/status/2019828626972131441)

### 一句话

这周几乎每个软件工程师都在经历某种程度的心理健康危机。

### 核心观点

Tom Dale（Ember.js 创始人）观察到：

> "I don't know why this week became the tipping point, but nearly every software engineer I've talked to is experiencing some degree of mental health crisis."

不只是失业焦虑：
- 看到软件从稀缺变成丰富引发的近乎躁狂的状态
- 对 agent 使用的强迫行为
- 面对变化速度的认知过载
- 活在拐点时刻的解离感

### 我的看法

这和 Simon Willison 的 "Deep Blue" 概念呼应：**AI 正在引发软件工程师的集体心理危机**。

不是因为 AI 不好用，恰恰是因为 AI 太好用了。当你花了十年学的技能突然变得不那么重要，心理冲击是真实的。

对于 PhD 学生：**照顾好自己的心理健康**。这个领域变化太快，焦虑是正常的。

---

## 总结

2026-02-02 到 02-08 这周的关键词是 **Agent 成熟**：

1. **Dark Factory** 已经有人在用了
2. **90% 的代码** 可以由 AI 写
3. **IDE 正在衰落**，terminal + agent 是新范式
4. **开源治理** 需要新工具（Vouch）
5. **心理健康危机** 是真实的

Mitchell Hashimoto 的建议最实用：先自己做，再让 AI 复现，这样你才知道 AI 的能力边界。

---

*这篇笔记基于 Karpathy RSS 源中 2026-02-02 至 2026-02-08 期间的文章。*
词：

1. **Dark Factory** 已经有人在实践了
2. **Mitchell Hashimoto** 的 AI 采用方法论值得学习
3. **90% 代码由 AI 写** 是新常态
4. **开源治理** 需要新工具（Vouch）
5. **心理健康危机** 是真实的

Karpathy 订阅的这些博主有一个共同点：他们都在 **认真思考 AI 带来的变化**，而不是简单地拥抱或拒绝。

---

*这篇笔记基于 Karpathy RSS 源中 2026-02-02 至 2026-02-08 期间的文章。*
