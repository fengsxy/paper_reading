# Karpathy RSS Digest - 2026-03-13

> 来源：[Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)
> 时间范围：2026-03-12 15:00 UTC - 2026-03-13 15:00 UTC
> 文章数：8 篇

---

## 🔥 Shopify CEO 用 autoresearch 把 Liquid 模板引擎提速 53%

**[Simon Willison's Weblog](https://simonwillison.net/2026/Mar/13/liquid/#atom-everything)** - 2026-03-13 03:44

Shopify CEO Tobias Lütke 使用 Karpathy 的 autoresearch 范式，让 coding agent 跑了约 120 次自动实验，在 Liquid（20 年历史的 Ruby 模板引擎）上找到了数十个微优化点。93 个 commit，解析+渲染提速 53%，内存分配减少 61%。关键发现包括：用 `byteindex` 替代正则扫描（-12% 解析时间）、缓存小整数 `to_s`（避免 267 次分配）等。

**点评**：这才是 AI coding agent 的最佳用法——不是写新代码，而是在有完善测试套件的老项目上暴力搜索优化空间。974 个单测是前提，没有测试的项目连试都别试。另外，CEO 又能写代码了，这是 agent 时代最讽刺也最真实的副产品。

---

## 🔥 Cory Doctorow: 三种 AI 精神病

**[Pluralistic](https://pluralistic.net/)** - 2026-03-13

Doctorow 把 "AI psychosis" 概念扩展为三个层面：投资者妄想（单位经济学全线亏损却靠 Byzantine premium 骗钱）、老板妄想（用不能干活的 chatbot 替代能干活的人）、批评者妄想（criti-hype，把 AI 公司的夸大宣传当真然后反向放大）。核心论点：AI 是一项普通技术，不普通的是泡沫。

**点评**：三个框架都够毒辣，但第三个最有启发性——批评者无意中帮 AI 公司维持了"例外论"叙事。Doctorow 的结论简单粗暴：AI 不特殊，泡沫才特殊。治泡沫用反垄断，不用反技术。

---

## 💻 Forge: 统一 Git 平台 CLI

**[Andrew Nesbitt](https://nesbitt.io/2026/03/13/forge.html)** - 2026-03-13 10:00

一个统一的 CLI 工具，支持 GitHub、GitLab、Gitea、Forgejo 和 Bitbucket。同一套命令操作不同平台。

**点评**：终于有人做了。多平台 Git 用户的刚需工具，不过能不能打还得看 API 覆盖率和维护力度。

---

## 🔥 "是工作教会了我思考"

**[Ibrahim Diallo](https://idiallo.com/blog/work-taught-me-how-to-think?src=feed)** - 2026-03-13 12:00

从大学退学到家具仓库，用 VBScript + OCR 自动化收据管理，再到后来用 Telnet 调试陌生硬件。作者的核心观点：学校教你解已知问题的形状，工作教你面对未知问题的态度。关键转变不是学会了某项技术，而是不再害怕不懂的东西。

**点评**：每个自学成才的程序员都有类似的原点故事——某个"受够了"的时刻。文章写得克制真诚，没有变成"退学创业"的爽文。

---

## 🌍 荷兰税务局要把增值税系统外包给美国公司

**[Bert Hubert](https://berthub.eu/articles/posts/software-turnkey-as-a-service/)** - 2026-03-13 11:43

荷兰税务局（Belastingdienst）计划将增值税系统整体交给美国公司运营——不只是用美国软件，而是连服务器和运维全部由美国人管理。3月19日议会将讨论此事。

**点评**：数字主权不是口号问题。一个国家的核心税务数据放在另一个国家的公司手里，这在任何时代都是疯狂的。

---

## 🍎 Firefox 和 Safari 的字体渲染 Bug

**[Terence Eden's Blog](https://shkspr.mobi/blog/2026/03/an-odd-font-rendering-bug-in-firefox-and-safari/)** - 2026-03-13 12:34

Unicode 组合字符在 Chrome 上正常渲染，但 Firefox 和 Safari 搞砸了。起因是尼日利亚演员名字中的约鲁巴语变音符号。

**点评**：又一个 Unicode 的坑。浏览器 2026 年了还搞不定组合字符，说明国际化永远是最后被修的 bug。

---

## 💰 Microsoft IPO 四十周年

**[The Silicon Underground](https://dfarq.homeip.net/microsofts-1986-ipo/)** - 2026-03-13 11:00

1986 年 3 月 13 日，Microsoft 上市。四十年后我们仍在感受那场 IPO 的余震——它开启了"寻找下一个 Microsoft"的投资狂潮。

**点评**：恰好今天是四十周年纪念日。从 DOS 到 Azure 到 Copilot，Microsoft 的生存能力堪比蟑螂——这是最高赞美。

---

## 🎲 Everything's Casino

**[Joan Westenberg](https://www.joanwestenberg.com/everythings-casino/)** - 2026-03-13 02:38

从美伊冲突到金融市场，一切都是赌场。

**点评**：标题即论点，不多说。

---

## 📊 统计

- **AI/编程**：3 篇（autoresearch 优化、AI 泡沫批判、工作与学习）
- **工具/开源**：2 篇（Forge CLI、字体渲染 bug）
- **数字主权/政策**：1 篇（荷兰税务外包）
- **科技历史**：1 篇（Microsoft IPO）
- **时评**：1 篇（地缘政治）

**今日亮点**：Shopify CEO 亲自下场用 Karpathy 的 autoresearch 做性能优化，这可能是目前 coding agent 最有说服力的实际案例。不是 demo，不是 benchmark，是在生产级代码库上跑出了 53% 的真实提升。

---

*数据来源: [Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)*
*生成时间: 2026-03-13 15:00 UTC*
