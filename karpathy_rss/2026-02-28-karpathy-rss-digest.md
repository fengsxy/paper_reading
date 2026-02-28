---
layout: default
title: "Karpathy RSS Digest — 2026-02-28"
permalink: /karpathy_rss/2026-02-28-karpathy-rss-digest
---

# Karpathy RSS Digest — 2026-02-28

> Andrej Karpathy 的 curated RSS 过去 24 小时精选。直接、有洞察、偶尔吐槽。

---

## 🍪 Anil Dash：给 Dario 一块饼干？Anthropic 与战争机器

**Anil Dash** · [原文](https://anildash.com/2026/02/27/a-cookie-for-dario/)

接着昨天 Marcus 的"悬崖边"文章，Anil Dash 写了一篇更冷静但更尖锐的分析。Anthropic CEO Dario Amodei 拒绝了国防部长 Hegseth 要求提供不受限军事 AI 访问的要求，科技圈一片叫好。Dash 的反应：别急着发饼干。

核心论点：拒绝让自己的技术被用来犯战争罪，这不是英雄行为，这是底线。如果我们把"不卖死亡"当成值得大肆表扬的事，那说明我们的标准已经低到地下室了。

Dash 还补了一刀实操层面的分析：卖给五角大楼本身就是噩梦——无尽的合规文书、FedRAMP 认证、采购流程，对一家快速迭代的 AI 公司来说，这笔生意的 ROI 可能本来就不划算。所以 Anthropic 的"道德立场"可能同时也是一个精明的商业决策。

**吐槽：** Dash 说得对，但他漏了一个更深层的问题：Anthropic 今天能说不，是因为他们还没上市、还没有股东压力。等到 IPO 之后，"我们拒绝了一个几十亿美元的政府合同因为道德"这句话在财报电话会上会怎么被接收？Responsible Scaling Policy 在 VC 面前是卖点，在华尔街面前可能就是负债。Dario 写"Machines of Loving Grace"的时候大概没想到，最大的考验不是技术对齐，而是资本对齐。

---

## 🔬 Max Woolf：一个 AI coding 怀疑论者的详尽实验报告

**Max Woolf's Blog / Simon Willison 转载** · [原文](https://minimaxir.com/2026/02/ai-agent-coding/)

这篇是近期"coding agent 真的变强了"系列文章中质量最高的一篇，没有之一。Max Woolf 去年五月写过一篇"我作为资深 LLM 用户其实不怎么用 LLM"，态度是谨慎怀疑。现在他回来了，带着一堆详细到令人发指的实验记录。

他的转变轨迹：从用 LLM 做代码审查（有用但有限）→ 试 GitHub Copilot（还行）→ 被同事安利 Claude Code → 从简单的 YouTube 元数据爬虫开始 → 逐步升级到越来越复杂的项目。关键转折点在去年 11-12 月：agent 的可靠性突然跨过了一个阈值，从"偶尔能用"变成了"大部分时候能用"。

Simon Willison 转发时的评价：又一篇"OK, coding agents got good in November"的文章，但这篇的价值在于细节——每个项目的具体 prompt、失败模式、成本、时间对比，全都摊开了。

**洞察：** Woolf 的方法论值得学习。他不是那种"我用 Claude 写了一个 app 所以 AI 改变世界"的人，也不是"我试了一次不行所以 AI 是骗局"的人。他是一个数据科学家，用控制变量的方式测试了 agent 在不同复杂度任务上的表现，然后诚实地报告了结果。这种"excessive detail"恰恰是当前 AI 讨论中最缺的东西——大家要么在写 hype piece，要么在写 doom piece，很少有人愿意花时间做这种无聊但有价值的基准测试。对于做研究的人来说，这篇文章的实验设计本身就值得一读。

---

## 🔐 Simon Willison 转：求你们别用 passkey 加密用户数据了

**Simon Willison's Weblog** · [原文](https://simonwillison.net/2026/Feb/27/passkeys/)

Tim Cappalli（身份认证领域的老兵）写了一篇几乎是在恳求的文章：停止用 passkey 的 PRF（Pseudo-Random Function）扩展来加密用户数据。

问题很简单：passkey 是认证凭证，不是加密密钥。当你把它同时用于两个目的时，丢失 passkey 的"爆炸半径"就从"我登不上了"升级到"我的数据永远没了"。用户丢 passkey 的频率比你想象的高得多——换手机、重置设备、云同步出问题——而大多数用户根本不理解"你的消息备份已经被不可逆地加密了，密钥在你丢掉的那个 passkey 里"意味着什么。

Cappalli 列举了已经在用 PRF 加密的场景：消息备份、端到端加密、文档加密、加密钱包解锁。每一个都是"用户最珍贵的数据"级别。

**吐槽：** 这是一个经典的"工程师觉得优雅但用户会哭"的设计模式。PRF 在技术上确实很漂亮——用一个凭证同时解决认证和加密，减少了用户需要管理的秘密数量。但安全系统设计的第一原则是：假设用户会做最蠢的事。把认证和加密绑在同一个凭证上，就像把家门钥匙和保险箱钥匙焊在一起——方便是方便了，丢了就全完了。更糟糕的是，passkey 的"无密码"卖点让用户觉得这东西比密码更不容易丢，但实际上 passkey 的恢复路径比密码复杂得多。

---

## 💰 Gary Marcus：OpenAI 的新融资说得通吗？

**Marcus on AI** · [原文](https://garymarcus.substack.com/p/does-openais-new-financing-make-sense)

Marcus 今天换了个赛道，从地缘政治回到商业分析。OpenAI 的最新融资轮引发了他的质疑：数字对不上。

他不是唯一一个怀疑的人——文章标题就是"I am not alone in seriously doubting it"。核心问题：OpenAI 的烧钱速度、收入增长曲线、和估值之间的关系，在传统财务分析框架下越来越难自洽。

**一句话：** Marcus 质疑 OpenAI 融资就像他质疑 AGI 一样——论点不新，但每次市场给他新弹药。问题是，在 AI 领域，"这不合理"和"这会崩"之间的距离可能比任何人想象的都远。WeWork 不合理了好几年才崩。

---

## 🏛️ Gary Marcus：Trump 是不是玩过头了？

**Marcus on AI** · [原文](https://garymarcus.substack.com/p/did-trump-just-overplay-his-hand)

Marcus 今天的第二篇，接着 Anthropic vs 五角大楼的故事线。他认为 Hegseth 的最后通牒策略可能适得其反——硅谷的反应比预期更统一，而且不只是 Anthropic，其他公司也在观望。

"We will learn a lot about Silicon Valley in the upcoming days"——这句话是全文的核心。Marcus 在赌硅谷会在这个问题上展现出比平时更多的脊梁骨。

**吐槽：** 我对此持谨慎乐观。硅谷在道德问题上的团结通常持续到第一个人签了合同为止。但这次不一样的是：军事 AI 的法律风险太大了。不是道德风险——是字面意义上的"你的工程师可能被传唤到海牙"的风险。有时候恐惧比良心更可靠。

---

## 🖥️ John Gruber：iOS 26 Phone App 的隐藏设置之谜

**Daring Fireball** · [原文](https://daringfireball.net/2026/02/sometimes_hidden_setting_phone_app)

Gruber 写了一篇典型的 Gruber 式长文：iOS 26 Phone App 有一个"Tap Recents to Call"设置，但这个设置只在你选择了 Unified 视图时才会出现在 Settings 里。如果你用的是其他视图，这个设置就消失了——不是灰掉，是直接不存在。

Gruber 的判词：lazy design。用户不应该需要先改一个设置才能看到另一个设置。

**一句话：** Apple 的 Settings app 已经是一个考古遗址了，每个版本都在上面堆新的地层。这种"设置的可见性取决于另一个设置"的模式，是复杂度失控的经典症状。

---

## 🔓 Anthropic 给开源维护者免费 Claude Max

**Simon Willison's Weblog** · [原文](https://simonwillison.net/2026/Feb/27/claude-max-oss-six-months/)

Anthropic 宣布给符合条件的开源维护者提供免费的 $200/月 Claude Max 20x 计划，为期六个月。条件：5000+ GitHub stars 或 1M+ 月 NPM 下载量的核心维护者。

**吐槽：** 聪明的获客策略。开源维护者是开发者社区里影响力最大的群体之一，让他们免费用六个月，等于买了六个月的口碑营销。而且门槛设得很精准——5000 stars 刚好筛掉了"我 fork 了一个项目"的人，留下了真正有影响力的维护者。唯一的问题是：六个月后呢？从免费到 $200/月的落差，可能会制造一批"用过最好的但付不起"的怨念用户。

---

## 🎬 MG Siegler / Gruber：Netflix 收购 Warner Bros，TUDUMB

**Daring Fireball** · [原文](https://spyglass.org/netflix-warner-bros-paramount-deal/)

MG Siegler 造了个词：TUDUMB（Netflix + Warner Bros Discovery + Paramount Skydance 的合并体）。Netflix 要用债务融资收购 WBD，价格比 Paramount Skydance 自身市值高出 $100B。Siegler 的分析：这不是为了内容，是为了杠杆。Netflix 是 $400B 的公司，WBD 值 $11B——这是大鱼吃小鱼，而且大鱼打算用小鱼的骨头当牙签。

**一句话：** 流媒体战争的终局不是"谁的内容好"，而是"谁的资产负债表能撑到最后"。Netflix 赌的是：在 AI 时代，内容生产成本会暴跌，所以现在高价买分发渠道和 IP 库是值得的。这个赌注是否正确，取决于 AI 生成内容能不能真的替代人类创作——而这恰恰是目前最没有共识的问题。

---

## 🔧 其他值得一看

- **Ed Zitron：The Hater's Guide to Private Equity** · [原文](https://www.wheresyoured.at/hatersguide-pe/) — Zitron 继续他的"仇恨指南"系列，这次瞄准 PE。开头就是"We have a global intelligence crisis, in that a lot of people are being really fucking stupid"。Zitron 的文风。
- **Simon Willison：Unicode Explorer** · [原文](https://simonwillison.net/2026/Feb/27/unicode-explorer/) — Willison 在手机上用 LLM 写了一个 Unicode 浏览器，用 HTTP range request 做二分搜索。这人的 side project 产出速度不是人类级别的。
- **Jim Nielsen：Computers and the Internet, A Two-Edged Sword** · [原文](https://blog.jim-nielsen.com/2026/two-edged-sword-of-computers-and-internet/) — Dave Rupert 的反思引发的连锁思考：电脑和互联网可能对我不好，但我的工作、爱好、教育、娱乐全在上面。这是 2026 年版的"我恨我爱的东西"。
- **Gruber：如何屏蔽 macOS Tahoe 升级提醒** · [原文](https://robservatory.com/block-the-upgrade-to-tahoe-alerts-and-system-settings-indicator/) — 用 `softwareupdate --ignore` 可以屏蔽 90 天。Apple 的升级骚扰策略越来越像 Windows 了。
- **Terence Eden：家用电池 30 个月省了 3MWh** · [原文](https://shkspr.mobi/blog/2026/02/30-months-to-3mwh-some-more-home-battery-stats/) — 实打实的数据，Moixa 4.8kWh 电池配太阳能板的长期收益报告。
- **lcamtuf：Approximation Game** · [原文](https://lcamtuf.substack.com/p/approximation-game) — 从 22/7 ≈ π 讲到 Dirichlet 的鸽巢原理，数学科普小品。
- **Cory Doctorow：加州可以阻止 Larry Ellison 收购 Warner Bros** · [原文](https://pluralistic.net/2026/02/28/golden-mean/) — Doctorow 论证加州的反垄断工具可以用来阻止 Oracle 创始人的媒体收购野心。States' rights 的左翼用法。

---

*今天的 feed 有一条清晰的主线：AI 公司的道德边界在哪里？Anthropic 拒绝五角大楼、Dash 质疑我们的表扬标准、Marcus 观察硅谷的脊梁骨测试——三篇文章从不同角度拷问同一个问题。与此同时，Max Woolf 的实验报告提醒我们：在所有这些宏大叙事之下，coding agent 确实在变强，而且变强的方式是可以被严谨测量的。这大概就是 2026 年 AI 讨论的缩影——一半人在争论该不该用，另一半人已经在用了并且在认真记录效果。*

---

*数据来源：[Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss) · 抓取时间 2026-02-28 16:00 UTC*
