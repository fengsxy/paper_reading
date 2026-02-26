---
layout: default
title: "Karpathy RSS Digest — 2026-02-26"
permalink: /karpathy_rss/2026-02-26-karpathy-rss-digest
---

# Karpathy RSS Digest — 2026-02-26

> Andrej Karpathy 的 curated RSS 过去 24 小时精选。直接、有洞察、偶尔吐槽。

---

## 🚨 Gary Marcus：Anthropic vs 五角大楼，人类站在悬崖边

**Marcus on AI** · [原文](https://garymarcus.substack.com/p/america-and-probably-the-world-stands)

Gary Marcus 今天发了一篇几乎是在喊的文章：国防部长 Pete Hegseth 正在逼 Anthropic 交出不受限制的军事 AI 访问权限，包括无人在环的自主武器和军事监控，截止日期是明天下午 5:01。

Marcus 的核心恐慌有两层。第一层是明面上的：一个对 AI 能力和局限没有"nuanced understanding"的人，要把 AI 塞进核武器决策链。第二层更微妙：Hegseth 设了一个不可能的 deadline，目的是绕过国会——这种量级的 AI 政策本应经过公共审议，而不是一个内阁成员拿枪顶着脑袋逼出来的。

文章最后呼吁读者立刻打电话给自己的参议员和众议员。

**吐槽：** Marcus 是 AI 圈著名的"狼来了"选手，但这次他喊的不是"AGI 不行"，而是"有人要拿不行的 AGI 去打仗"。这两件事的严重程度差了几个数量级。Hegseth 的 deadline 策略本身就说明了一切——如果这件事经得起公开讨论，为什么要用 24 小时最后通牒？Dario Amodei 之前写过那篇著名的"Machines of Loving Grace"，现在他得面对的是 machines of loving firepower。Anthropic 的 Responsible Scaling Policy 即将迎来它的终极压力测试，而且考官不是学术界，是五角大楼。

---

## 📖 Works on My Machine：用科幻小说做思想实验

**Works on My Machine** · [原文](https://worksonmymachine.ai/p/from-nodes-to-stories-fiction-as)

作者之前做了一个叫 Traffic Jam Explorer 的工具（用 Claude 生成的），把 AI 导致的经济连锁反应画成节点图：AI 变强 → 裁员 → 消费萎缩 → 反馈循环加速。但他发现节点图太抽象，从"二阶效应"到"新职业"之间的跳跃让人摸不着头脑。

于是他换了个方法：让 Claude 写短篇小说。"给我写一个 Computational Experience Reviewer 的普通下午。"结果出奇地好用——叙事让抽象概念落了地，小说成了思维工具。

他由此启动了一个新项目 [Near Zero](https://nearzero.software/)：每周一篇短篇，设定在软件成本归零之后的世界。第一篇叫 The Executable Muse，讲的是"软件即内容"时代的审核员日常。

同期，Citrini Capital 发了一篇虚构的 2028 宏观备忘录——S&P 跌 38%，失业率 10.2%，房贷市场崩盘。同样的起点，完全不同的视角：一个数失去的工作，一个想象新生的工作。

**洞察：** 这篇文章最有意思的不是结论，而是方法论。"Fiction as a thinking tool"——用叙事来压力测试抽象概念——其实是一种被低估的研究方法。经济学家用模型，工程师用 prototype，而这哥们用短篇小说。听起来不严肃，但想想看：当你被迫描述一个人的具体一天时，你不得不回答模型可以回避的问题——这个人住哪？谁付他工资？他下午三点在干嘛？这些细节会逼出节点图永远不会暴露的矛盾。某种意义上，这就是 AI 时代的 scenario planning。

---

## 🇳🇱 Bert Hubert：荷兰把增值税外包给了美国公司

**Bert Hubert's writings** · [原文](https://berthub.eu/articles/posts/btw-as-an-american-service/)

荷兰 DNS 大佬 Bert Hubert（PowerDNS 作者）今天用荷兰语写了一篇愤怒的文章：荷兰税务局正在把整个增值税（BTW）系统外包给美国公司 FAST Enterprises。不是"买他们的软件"，是"turnkey 全包"——软件、服务器、运维、管理，全部由 FAST 远程操作。荷兰税务局自己的几千名 IT 员工？跟这个新系统没关系。

数字很吓人：荷兰每周收 15 亿欧元增值税。如果 Trump 哪天心情不好对荷兰搞制裁，FAST 一断服务，荷兰政府立刻要去国际资本市场借钱——然后 Financial Times 上就会出现你不想看到的那种文章。

更要命的是，FAST 的系统要接入税务局其他 20-25 个内部系统。荷兰国家法律顾问已经确认：根据美国法律，美国政府有权合法访问这些数据。

Hubert 把这叫做"BTW as a Service"——政府级别的 shadow IT。

**吐槽：** 这篇和昨天 Doctorow 写的"数据主权"主题完美呼应。Doctorow 在理论层面讲"post-American internet"，Hubert 在实操层面展示了一个活生生的反面教材。2026 年了，一个欧洲国家还在把核心税收基础设施交给美国公司全权托管——这不是技术决策，这是主权让渡。最讽刺的是，荷兰人自己有 PowerDNS 这种世界级基础设施软件，有 ASML 这种卡全球脖子的公司，但税务局的采购流程显然活在另一个平行宇宙里。

---

## 🤨 Terence Eden：This Time Is Different

**Terence Eden's Blog** · [原文](https://shkspr.mobi/blog/2026/02/this-time-is-different/)

一篇短小精悍的吐槽。Eden 列了一串技术泡沫的墓碑：3D TV、AMP、AR、Beanie Babies、Blockchain、Metaverse、NFTs、Quibi、WiMAX……然后指出：鼓吹这些东西的基本是同一批人（而且几乎都是男的），现在他们又在鼓吹 AI。

"This time is different!" ——John Templeton 说过，这是投资史上最贵的四个字。

Eden 的立场不是"AI 没用"，而是"AI 显然只会是众多技术中的一种，而不是 winner takes all"。他引用了 Terry Pratchett 的 Ankh-Morpork 比喻：没有敌人真正征服过这座城市——蛮族入侵者来了几天后发现马没了，几个月后就变成了又一个有自己涂鸦和小吃店的少数族群。

**吐槽：** 这篇文章的论证其实很弱——把 AI 和 Beanie Babies 放在同一个列表里本身就是 false equivalence。但它捕捉到了一种真实的情绪：tech hype cycle 的疲劳感。问题是，"this time is different"有时候确实是对的——互联网、智能手机、搜索引擎，这些都曾经被人用同样的话嘲笑过。Eden 的 Pratchett 引用倒是精准：AI 不会"征服"一切，但它会像蛮族一样融入日常，几个月后你发现它已经开了自己的小吃店。

---

## 🖥️ The Silicon Underground：Pentium III，27 岁生日快乐

**The Silicon Underground** · [原文](https://dfarq.homeip.net/pentium-iii-launched-feb-28-1999/)

怀旧向。1999 年 2 月 28 日 Pentium III 发布，第一个突破 GHz 的 CPU。文章的有趣论点：Pentium III 其实比它的继任者 Pentium 4 更好。P4 频率更高，但 P3 的 IPC（每时钟周期指令数）更强。Intel 为了追求 GHz 数字走了弯路，直到后来的 Core 架构才回到正轨。

**一句话：** 27 年前 Intel 就证明了：benchmark 数字大不等于实际性能好。这个教训在 LLM 时代依然适用——看看那些 MMLU 刷到 90+ 但实际用起来一塌糊涂的模型就知道了。

---

## 📜 Cory Doctorow：你建好了，Trump 就来抢

**Pluralistic** · [原文](https://pluralistic.net/2026/02/25/most-favored-nation/)

Doctorow 今天的长文（真的很长）核心论点：光靠"建更好的替代品"不够，因为 Trump 不在乎你是不是公平竞争赢的——他在乎的是赢。

起因是 Reuters 泄露的一份外交电报：Trump 命令美国外交官在全球范围内打击"数据主权"政策。Doctorow 的推理链：

1. "If you build it, they will come" 是陷阱——人们不用 Instagram 是因为爱 Zuckerberg，而是因为爱朋友
2. 集体行动困境让人走不掉——你不会一个人去空荡荡的新平台等朋友
3. 需要对抗性互操作（adversarial interoperability）——就像当年 Zuckerberg 用 bot 从 Myspace 吸用户一样
4. 但反规避法（anticircumvention laws）让这变成了违法行为——而这些法律恰恰是美国贸易代表推到全球的
5. Trump 的关税战反而帮了忙：他违反了"你保留反规避法，我不武器化你的基础设施"的默契
6. 所以现在是废除反规避法、逃离美国科技平台的最佳时机

有人问"这样做会不会惹怒 Trump？"Doctorow 的回答：Trump 不是因为你犯规才生气，他是因为你赢了才生气。你乖乖建替代品，万一真成功了，他会直接抢——就像他对 TikTok 做的那样。

**吐槽：** Doctorow 这篇是他"post-American internet"系列的又一篇，论点一如既往地清晰。但我觉得他低估了一个问题：adversarial interoperability 在社交媒体上可行，在企业 IT 上就难多了。你可以写个 bot 从 Instagram 抓 feed，但你没法写个 bot 把整个公司的 SharePoint 迁移到开源替代品上——数据结构、权限模型、审计日志，这些东西的复杂度不是一个 scraper 能解决的。Bert Hubert 那篇荷兰税务局的文章就是最好的例证：问题不是没有替代品，而是迁移成本高到让人宁愿把脑袋放在美国的砧板上。

---

*今天的 feed 主题异常集中：数据主权、AI 军事化、技术泡沫怀疑论。Karpathy 订阅的这些 RSS 源画出了一幅 2026 年初的时代肖像——AI 不再只是技术问题，它已经是地缘政治问题了。Marcus 担心 AI 被塞进核武器，Doctorow 担心 AI 平台被武器化，Hubert 担心政府 IT 被美国控制，Eden 担心这一切都是泡沫。唯一乐观的是 Works on My Machine 那哥们——他在用 Claude 写科幻小说想象新工作。*

---

*数据来源：[Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss) · 抓取时间 2026-02-26 16:00 UTC*
