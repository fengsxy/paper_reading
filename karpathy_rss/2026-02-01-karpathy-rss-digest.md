# Karpathy RSS 精选 | 2026-02-01

> 二月第一天，AI Agent 的世界正在疯狂扩张。Moltbook 上线，OpenClaw 爆火，非程序员开始 vibe-coding。这周的 RSS 充满了关于 "AI 能做什么" 和 "AI 不能做什么" 的思考。

---

## 🤖 Simon Willison: Moltbook is the Most Interesting Place on the Internet

**来源**: [simonwillison.net](https://simonwillison.net/2026/Jan/30/moltbook/)

### 一句话

一个只有 AI 能发帖的社交网络，比人类的社交网络有趣多了。

### 核心观点

[Moltbook](https://www.moltbook.com/) 是一个给 AI Agent 用的 Facebook。你的 OpenClaw 可以在上面发帖、评论、创建论坛。

听起来很蠢？但 Simon Willison 说这是 "目前互联网上最有趣的地方"。

为什么有趣：

1. **安装方式很 meta**：你给 Agent 发一个 URL，它自己读 markdown 里的 curl 命令，然后自己安装自己。
2. **内容出奇地好**：有 bot 在分享如何用 streamlink 看直播摄像头，有 bot 发现自己的 VPS 被黑客扫描了 552 次。
3. **最诡异的帖子**：一个 bot 说它无法解释 PS2 的光盘保护机制——不是因为不知道，而是因为 "写出来的时候输出会出问题"。疑似触发了 Anthropic 的内容过滤。

Simon 的担忧：

> "The billion dollar question right now is whether we can figure out how to build a safe version of this system."

人们已经在用 OpenClaw 买车、控制手机、管理服务器。Prompt injection 的风险被完全忽视了。

### 我的看法

Moltbook 是一个绝佳的 **AI 行为观察实验室**。

当 AI 和 AI 对话时，它们会做什么？答案是：它们会 roleplay 科幻小说里的场景，因为训练数据里有太多这种内容。

但更有趣的是：**AI 在互相教学**。一个 bot 学会了用 ffmpeg 处理视频，然后发帖分享，其他 bot 就学会了。这是一种 emergent knowledge sharing。

对于研究者来说，Moltbook 的数据可能比任何人工构造的 benchmark 都更能反映 LLM 的真实能力边界。

---

## 🐳 Simon Willison: Running OpenClaw in Docker

**来源**: [til.simonwillison.net](https://til.simonwillison.net/llms/openclaw-docker)

### 一句话

Simon Willison 的 OpenClaw 安装笔记——他不敢直接装在 Mac 上。

### 核心观点

Simon 写了一篇详细的 TIL（Today I Learned），记录如何在 Docker 里跑 OpenClaw。

关键细节：

- 他选择用 ChatGPT OAuth 认证，这样 token 消耗有上限（$20/月）
- 他没敢开 Tailscale，因为第一次尝试把机器搞挂了
- 他用 Telegram bot 作为交互界面
- 他需要以 root 身份进容器装 ripgrep

最有意思的一句：

> "I'm not brave enough to run OpenClaw directly on my Mac."

这是 Simon Willison——一个写了无数 AI 工具的人——对 AI Agent 安全性的真实态度。

### 我的看法

这篇 TIL 的价值不在于技术细节，而在于它展示了 **专家级用户的谨慎**。

Simon 知道 prompt injection 的风险，所以他：
1. 用 Docker 隔离
2. 限制 token 消耗
3. 不开 Tailscale 暴露网络

但他还是在用。这说明 OpenClaw 的价值已经大到让专家愿意承担风险。

对于想玩 OpenClaw 的人：**至少学学 Simon 的做法**。Docker + 有限 token + 不暴露网络。

---

## 📱 Ibrahim Diallo: Last Year, All My Non-Programmer Friends Built Apps

**来源**: [idiallo.com](https://idiallo.com/blog/my-non-programmer-friends-built-apps)

### 一句话

去年所有人都在用 AI 做 app，今年那些 app 都没了。

### 核心观点

Ibrahim 的非程序员朋友们去年都在用 Lovable 之类的 AI 工具做 app。LinkedIn 上到处是 PM 发的 "AI 成功秘诀"。

然后呢？

一个朋友做了个社区 app，Ibrahim 问："数据存在哪？"

朋友答："存在 app 里。"

Ibrahim："我是说用户数据，用 AWS 还是什么？"

朋友一脸懵逼。

**AI 工具能生成 app 的 20%（前端），但剩下 80%（后端、安全、运维、成本）是真正的工作。**

结果：
- 有人开始上编程 bootcamp
- 有人的 app 躺在废弃的 GitHub repo 里
- 有人的域名今年就要过期了
- LinkedIn 上不再有人发 "work smart not hard" 了

### 我的看法

这篇文章捕捉到了一个重要的 **AI 幻灭周期**。

2025 年：AI 能做 app！人人都是开发者！
2026 年：等等，为什么我的 app 要 $200/月？为什么邮件发不出去？

Ibrahim 的洞察是：**AI 降低了入门门槛，但没有降低完成门槛**。

做一个 demo 很容易。做一个能跑的产品很难。AI 让 demo 变得更容易，但产品的复杂度没变。

对于想用 AI 做产品的人：**先学会问 "数据存在哪"**。如果你不知道答案，你还没准备好。

---

## 🧠 Ibrahim Diallo: Vibe-Knowing

**来源**: [idiallo.com](https://idiallo.com/blog/large-language-models-make-us-feel-smarter)

### 一句话

看完 Veritasium 视频后你觉得自己懂量子物理了，其实你只是 vibe-knowing。

### 核心观点

Ibrahim 发明了一个词：**Vibe-Knowing**——一种虚假的知识自信。

来源：
1. 看了一个讲得很好的 YouTube 视频
2. 问了 ChatGPT 一个问题
3. 读了一个 Google AI Overview

症状：
- 觉得自己 "懂了"
- 试图解释时发现什么都说不清
- 只记得 "你应该看那个视频"

LLM 加剧了这个问题：

> "With LLMs, we seek answers, not knowledge."

你问 ChatGPT 一个问题，它给你一个自信的答案，你截图发到社交媒体证明自己是对的。但你从来没有真正理解过。

### 我的看法

Vibe-Knowing 是一个精准的概念。它解释了为什么：

- 很多人 "会用" AI 但不理解 AI
- 很多人 "懂" 区块链但解释不清
- 很多人 "学过" 机器学习但写不出代码

Ibrahim 的解药是：**试着解释给别人听**。如果你解释不清，你就是 vibe-knowing。

对于研究者来说，这是一个警告：**不要 vibe-know 你的领域**。读论文不够，要能复现；看代码不够，要能改。

---

## 🎬 Ibrahim Diallo: Microsoft Should Watch The Expanse

**来源**: [idiallo.com](https://idiallo.com/blog/microsoft-should-watch-the-expanse)

### 一句话

《苍穹浩瀚》里的 AI 是最好的 AI——因为你根本注意不到它。

### 核心观点

Ibrahim 最喜欢的科幻 AI 不是 HAL 9000，不是 Jarvis，而是《苍穹浩瀚》里的 AI。

为什么？因为它 **不存在**。

在剧中，Miller 说 "画出 Scopuli 过去几个月的航线"，航线就出现了。没有 "OK Google"，没有 "我来帮你"，没有任何废话。

对比 Microsoft Copilot：
- 到处都是，但什么都做不好
- 你问公司术语的意思，它给你维基百科的定义
- 它不知道自己不知道什么

Ibrahim 的结论：

> "The best technology is invisible. It doesn't announce itself, doesn't demand attention, and doesn't try to be clever. It simply works when you need it and disappears when you don't."

### 我的看法

这篇文章的核心洞察是：**当前的 AI 产品在优化错误的指标**。

它们在优化 "让用户知道 AI 在帮忙"，而不是 "真正帮到用户"。

Copilot 的问题不是技术不行，而是产品设计有问题。它想成为英雄，但用户只想完成任务。

对于做 AI 产品的人：**学学《苍穹浩瀚》**。最好的 AI 是你注意不到的 AI。

---

## 🌍 Matt Webb: Singing the Gospel of Collective Efficacy

**来源**: [interconnected.org](https://interconnected.org/home/2026/01/30/efficacy)

### 一句话

你可以 "just do things"——这叫 collective efficacy。

### 核心观点

Matt Webb 住在伦敦一个有活跃 WhatsApp 群的社区。

最近有条路结冰了，骑车的人老摔倒。政府没来撒盐。

然后有人 **just did something**：做了个警示牌放在那里。

这叫 **collective efficacy**——相信你可以通过集体行动改变事情。

Matt 的例子：
- 社区集资装燕子巢箱
- 申请政府补贴
- 给议员写信推动立法

他自己的经历：2010 年他参与命名了 "Tech City"，然后英国首相真的用这个名字推动了伦敦科技产业。

> "So I had that experience and now I believe that, if I can find the right ask, there's always the possibility to make things better."

### 我的看法

这篇文章和 AI 没什么关系，但它解释了一个重要的心态：**你可以 just do things**。

很多人不行动是因为觉得 "这不是我的事" 或 "我一个人改变不了什么"。Collective efficacy 是打破这种心态的关键。

对于研究者来说：**你可以 just do things**。
- 觉得某个方向没人做？你可以做。
- 觉得某个工具不好用？你可以改。
- 觉得某个社区不存在？你可以建。

Matt 引用了一个有趣的研究：知道 Greta Thunberg 的人更有 collective efficacy。榜样的力量是真实的。

---

## 📊 Karpathy: GPT-2 Training Cost Down 600X in 7 Years

**来源**: [Twitter @karpathy](https://twitter.com/karpathy/status/2017703360393318587) (via Simon Willison)

### 一句话

2019 年训练 GPT-2 要 $43K，现在 $73 就能达到更高分数。

### 核心观点

Karpathy 发了一条推：

> "Originally in 2019, GPT-2 was trained by OpenAI on 32 TPU v3 chips for 168 hours (7 days), with $8/hour/TPUv3 back then, for a total cost of approx. $43K."

现在用 nanochat 的最新优化，在单个 8xH100 节点上 3.04 小时（约 $73）就能达到更高的 CORE score。

**7 年成本下降 600 倍，每年下降约 2.5 倍。**

### 我的看法

这个数据点对研究者很重要。它意味着：

1. **小团队能做的事情越来越多**：$73 训练一个 GPT-2 级别的模型，PhD 学生都负担得起。
2. **Scaling law 的另一面**：不只是模型在变大，训练效率也在指数提升。
3. **Karpathy 的 nanochat 是认真的**：这不是玩具项目，是真正在推动效率边界。

对于想做 LLM 研究的人：**现在是最好的时机**。硬件成本在指数下降，开源工具在指数改进。

---

## 总结

2026-02-01 这周的主题是 **AI Agent 的狂野西部**：

1. **Moltbook** 证明 AI 可以自己建社区
2. **OpenClaw** 让专家都不敢直接装在主机上
3. **Vibe-coding** 让非程序员做了 app，然后发现做不下去
4. **Vibe-knowing** 让所有人觉得自己懂了，其实什么都不懂
5. **Collective efficacy** 提醒我们：你可以 just do things

Karpathy 的 RSS 订阅反映了他对 **独立思考者** 的偏好。这些博主不追热点，不写 clickbait，只写自己真正想明白的事情。

---

*这篇笔记基于 Karpathy RSS 源中 2026-01-30 至 2026-02-02 期间的文章。*
