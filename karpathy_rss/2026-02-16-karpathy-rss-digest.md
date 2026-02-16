# Karpathy RSS 精选 | 2026-02-16

> Andrej Karpathy 订阅了 92 个 RSS 源，这是他的信息食谱。今天从他的聚合 feed 里挑了几篇值得读的。

---

## 🧛 Steve Yegge: The AI Vampire

**来源**: [steve-yegge.medium.com](https://steve-yegge.medium.com/the-ai-vampire-eda6e4f07163)  
**via**: Simon Willison's Weblog

### 一句话

AI 让你 10x 生产力，但谁拿走了那 9x？

### 核心观点

Yegge 发现了一个诡异的现象：用 AI 的人反而更累了。他把这叫做 "AI Vampire"——AI 像能量吸血鬼一样榨干你。

关键洞察：

**场景 A**: 你用 AI 达到 10x 生产力，工作 8 小时。结果？公司拿走 100% 的价值增益，你累成狗，同事恨你。

**场景 B**: 你用 AI 达到 10x 生产力，只工作 1 小时。结果？你拿走 100% 的价值增益，但公司迟早发现你在摸鱼。

现实是一个 dial（旋钮），在这两个极端之间。问题是：谁来调这个旋钮？

Yegge 的结论很反直觉：**新的工作日应该是 3-4 小时**。AI 自动化了简单工作，留给人类的全是高认知负荷的决策。没人能一天做 8 小时的 Jeff Bezos 式决策。

### 我的看法

这篇文章让我想到了一个更深的问题：**AI 时代的劳动价值论要重写了**。

传统上，你的价值 = 你的时间 × 你的技能。AI 打破了这个等式——现在是你的时间 × 你的技能 × AI 的杠杆。但杠杆的收益归谁？

Yegge 说得对：如果公司 capture 100% 的 AI 价值，员工会 burnout；如果员工 capture 100%，公司会被竞争对手干掉。

但他没说的是：**这个博弈的均衡点在哪？** 我猜最终会形成新的社会契约——类似于工业革命后的 8 小时工作制。只是这次可能是 4 小时。

对于做研究的人来说，这篇文章的启示是：**AI 工具的 adoption 不是技术问题，是组织设计问题**。

---

## 💸 Mat Duggan: I Sold Out for $20 a Month

**来源**: [matduggan.com](https://matduggan.com/i-sold-out-for-200-a-month-and-all-i-got-was-this-perfectly-generated-terraform/)

### 一句话

一个 AI 怀疑论者的投降书。

### 核心观点

Mat Duggan 本来想写一篇 "Claude Code 也是垃圾" 的文章，结果被打脸了。

他的原话：

> "It felt impossible but the proof was right in front of me."

他发现 Claude Code 真的能写出正确的 Terraform、GitHub Actions、Kubernetes YAML——那些他花了无数小时在文档和 Vim 之间来回切换才能写出来的东西。

但这让他陷入了道德困境：

1. LLM 是通过 "偷窃" 人类知识训练的
2. 能源消耗巨大
3. 加剧了资本对劳动的剥削

然而他还是付了 $20/月。

他朋友（一个 EVE Online 玩家）的评价很毒：

> "You know what the difference is between you and me? I know I'm a mercenary. You thought you were an artist. We're both guys who type for money."

### 我的看法

这篇文章的价值不在于技术评测，而在于它捕捉到了一种**集体心理状态**：程序员对 AI 的态度正在从 "这玩意不行" 转向 "这玩意行但我不想承认"。

Mat 的道德困境其实是假的。真正的问题不是 "该不该用 AI"，而是 "用 AI 之后我是谁"。

他朋友说得对：大多数程序员以为自己是 artist，其实是 mercenary。AI 只是撕掉了这层遮羞布。

但我不同意他的悲观。**工具不定义人**。用 AI 写 Terraform 不会让你变成更差的程序员，就像用计算器不会让你变成更差的数学家。

真正的问题是：当 AI 能做 80% 的工作时，你那 20% 的价值是什么？

---

## 😰 Simon Willison: Deep Blue

**来源**: [simonwillison.net](https://simonwillison.net/2026/Feb/15/deep-blue/)

### 一句话

给程序员的 AI 焦虑起了个名字：Deep Blue。

### 核心观点

Simon Willison 和 Oxide and Friends 播客的人发明了一个词：**Deep Blue**——软件工程师因为 AI 而产生的存在性焦虑。

为什么叫 Deep Blue？因为 1997 年 Deep Blue 击败 Kasparov 时，棋手们也经历过同样的心理危机。

Simon 自己的 Deep Blue 时刻是 2023 年试用 ChatGPT Code Interpreter：

> "It did every piece of data cleanup and analysis I had on my napkin roadmap for the next few years with a couple of prompts."

他花了几年规划的 Datasette 功能，AI 几分钟就做完了。

两个并行的想法：
1. 这对记者太棒了！
2. 我还有什么用？

### 我的看法

Deep Blue 这个命名很精准。它同时指向：
- 1997 年的 IBM 超级计算机
- 一种深蓝色的忧郁（deep blue mood）

但 Simon 漏掉了一个关键点：**棋手们后来怎么样了？**

答案是：他们变得更强了。人机协作的 "Centaur Chess" 比纯人类或纯 AI 都强。棋手们学会了把 AI 当工具而不是对手。

程序员也会经历同样的转变。Deep Blue 是过渡期的症状，不是终点。

对于 PhD 学生来说，这篇文章的启示是：**不要和 AI 比写代码，要比理解问题**。AI 能写代码，但不能定义什么代码值得写。

---

## 🎨 Rakhim: Modern UI is NOT Invisible

**来源**: [rakhim.exotext.com](https://rakhim.exotext.com/modern-ui-is-not-invisible)

### 一句话

现代 UI 不是 "干净"，是 "空洞"。

### 核心观点

Rakhim 反驳了一个流行观点：好的 UI 应该是 "invisible" 的。

他的论点：

1. **Winamp 有个性**：颜色、按钮、滑块——你能感受到设计师的存在
2. **Apple Music 是迷宫**：表面干净，但导航逻辑混乱，动画不一致
3. **"Invisible" 变成了 "Incoherent"**：为了追求极简，设计师创造了没有空间逻辑的界面

最毒的一句：

> "Like an attractive sociopath."

现代 UI 就像一个好看的反社会人格——表面迷人，内在混乱。

### 我的看法

这篇文章让我想到了一个更大的问题：**为什么科技产品越来越像？**

答案可能是：**设计系统的同质化**。Material Design、Human Interface Guidelines、Tailwind CSS——所有人都在用同样的组件库。

结果就是：所有 app 看起来都像是同一个人设计的。这不是 "invisible"，这是 "generic"。

Rakhim 的洞察是：**真正的 invisible 是认知负荷低**，不是视觉元素少。Winamp 的按钮多，但你一眼就知道怎么用。Apple Music 的按钮少，但你要猜半天。

对于做 AI 产品的人来说，这是个警告：**不要为了 "现代感" 牺牲可用性**。

---

## 🆓 Ibrahim Diallo: Programming is Free

**来源**: [idiallo.com](https://idiallo.com/blog/programming-tools-are-free)

### 一句话

学编程不需要花钱，但 influencer 不会告诉你。

### 核心观点

Ibrahim 遇到一个大学生，为一个简单的校园二手交易网站付 $200/月。

他的反应：WTF？

他自己的起点：
- $60 的坏掉的 PowerBook G4
- 免费的 BBEdit + MAMP
- Craigslist 上接单

这套装备让他进了 Fortune 10 公司。

问题出在哪？**YouTube influencer**。

他们推销 Hostinger、AWS、AI 订阅——因为这些公司付钱给他们。新手以为这些是必需品，其实不是。

真正需要的：
- 文本编辑器（免费）
- 语言运行时（免费）
- 一个想解决的问题

### 我的看法

这篇文章的核心洞察是：**学习的媒介决定了学习的方式**。

- 读文档 → 主动学习 → 慢但深
- 看 YouTube → 被动消费 → 快但浅

YouTube 的算法优化的是 "让你继续看"，不是 "让你学会"。所以你会看完一个教程，感觉自己学会了，然后发现什么都不记得。

Ibrahim 没说的是：**这个问题在 AI 时代会更严重**。

现在新手可以让 AI 写代码，然后 copy-paste。表面上 "学会了"，实际上什么都不懂。

对于想学编程的人：**关掉 YouTube，打开终端**。痛苦是学习的信号。

---

## 🔺 Cory Doctorow: The Online Community Trilemma

**来源**: [pluralistic.net](https://pluralistic.net/2026/02/16/fast-good-cheap/)

### 一句话

在线社区的不可能三角：规模、社区感、信息质量，只能选两个。

### 核心观点

Cory 介绍了一篇 ACM HCI 论文，提出了在线社区的 trilemma：

1. **Reach（规模）**: 多少人能看到你的内容
2. **Community（社区感）**: 成员之间的信任和熟悉度
3. **Information（信息质量）**: 能获取的知识深度

你只能优化其中两个：

- **高规模 + 高信息 = 低社区感**（如 Reddit 大版块）
- **高规模 + 高社区感 = 低信息**（如 meme 群）
- **高社区感 + 高信息 = 低规模**（如专业小圈子）

这解释了为什么社区会分裂：当规模超过 "刚刚好" 的大小，一部分人会离开去建新社区。

### 我的看法

这个 trilemma 模型很有解释力。它解释了：

- 为什么 Hacker News 的评论质量在下降（规模增长 → 社区感稀释）
- 为什么 Discord 服务器会分裂成无数小频道
- 为什么 Twitter/X 的信息质量越来越差

对于做社区产品的人：**不要追求无限增长**。找到你的 "刚刚好" 规模，然后守住它。

对于研究者：这个模型可以量化吗？能不能用信息论来形式化这个 trilemma？

---

## 总结

Karpathy 的 RSS 订阅反映了他的信息品味：

1. **独立博客 > 大媒体**：他订阅的大多是个人博客，不是 TechCrunch
2. **深度 > 速度**：这些文章都是长文，不是新闻快讯
3. **观点 > 事实**：他喜欢有态度的作者，不是中立报道

如果你想建立类似的信息食谱，建议：

- 找到你领域里写长文的独立博主
- 用 RSS 阅读器（Feedly、Inoreader）而不是算法推荐
- 每天花 30 分钟读，而不是刷 10 分钟

---

*这篇笔记基于 [Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss) 的 2026-02-16 聚合内容。*
