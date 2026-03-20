# Karpathy RSS Digest - 2026-03-20

> 来源：[Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)
> 时间范围：2026-03-19 15:00 UTC - 2026-03-20 15:00 UTC
> 文章数：14 篇（排除 0 篇赞助广告）

---

## 🔥 深度推荐

### OpenAI 收购 Astral（uv/ruff/ty）— Simon Willison 深度分析

**[Simon Willison's Weblog](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/#atom-everything)** - 2026-03-19 16:45

OpenAI 宣布收购 Astral，Python 生态中 uv、ruff、ty 三大工具的母公司。Astral 团队将并入 Codex 团队。Simon 从多角度分析了这笔交易：人才收购 vs 产品收购的张力、uv 作为 Python 基础设施的战略地位、与 Anthropic 收购 Bun 的镜像关系、以及 fork 作为安全网的可信度。值得注意的细节：Astral 悄悄完成了 Series A 和 B 融资，之前从未公开。

**点评**：对做 Python 开发的人来说这是大事件。uv 月下载量超 1.26 亿，现在归 OpenAI 所有。开源治理的经典案例——许可证宽松意味着最坏情况是 fork，但 fork 真的可行吗？

### AI 公司的泡沫策略：语言管控、末日叙事与军工合同

**[Ibrahim Diallo](https://idiallo.com/blog/everyone-is-supposed-to-die-when-machines-can-think?src=feed)** - 2026-03-20 12:00

犀利的行业批评：AI 公司在三条战线上"霸凌"——Microsoft 在 Discord 封禁 "Microslop" 用户，Nvidia 要求人们停用 "AI slop" 这个词；末日叙事让实际问题显得微不足道；Anthropic 和 OpenAI 的国防合同之争掩盖了根本问题——它们都在亏钱。

**点评**：写得尖锐但不偏激。"AGI 是一个能在不知道答案时说'我不知道'的 AI" 这句话很有意思。

---

## 📱 科技观察

### Google Android 侧载新限制：24 小时等待期

**[Gruber → Android Authority](https://www.androidauthority.com/google-android-sideloading-unverified-apps-new-rules-3650343/)** - 2026-03-19 19:03

Google 正式公布 Android 侧载新流程：未经验证的开发者应用需要 24 小时冷静期才能安装。Gruber 讽刺引用了 "Open always wins"，并指出 Tim Sweeney 已经拿了 Google 的钱，签了协议到 2032 年。

### Gruber 对 JavaScript 的激进观点：浏览器不该支持脚本语言

**[Daring Fireball → HN](https://news.ycombinator.com/item?id=47390945)** - 2026-03-19 17:31

Gruber 重申他最具争议的观点：浏览器支持 JavaScript 是一个历史性错误。没有 JS 就没有 49MB 的网页，也没有监控追踪产业。

### StopTheMadness / StopTheScript 浏览器扩展

**[Gruber → Jeff Johnson](https://mastodon.social/@lapcatsoftware/116252960395480568)** - 2026-03-19 21:09

Safari 的 StopTheMadness Pro 和 StopTheScript 扩展推荐，以及 Chrome 端的 Quick JavaScript Switcher。另外还有一个叫 OnlyAds 的反讽扩展——只显示广告，隐藏其他内容。

### 通信即监控 — Ibrahim Diallo

**[Ibrahim Diallo](https://idiallo.com/blog/communication-is-surveillance-by-design?src=feed)** - 2026-03-18 12:00 *(昨日边界附近)*

从 Bourne 系列电影中的"追踪电话"场景出发，解释现代通信的监控本质：CDR 记录、HTTPS 的局限、E2EE 的意义。结论：我们无法让通信隐形，只能让它不可读。

---

## 🔧 硬核项目

### Life TV：用 AVR 微控制器向复古 CRT 电视发射视频信号

**[Maurycy's Blog](https://maurycyz.com/projects/lifetv/)** - 2026-03-19

用 AVR128DA23 微控制器的 6MHz 方波谐波，向 Sony FD-30A 袖珍 CRT 电视无线发射 Conway's Game of Life 的画面。两个电阻 + 两个引脚实现 4 级 RF 幅度。

**点评**：极致的硬件 hack。用数字电路的"噪声"作为特征而非 bug，优雅地实现了模拟电视信号发射。

---

## 📚 轻量内容

- **[Package Manager Mirroring](https://nesbitt.io/2026/03/20/package-manager-mirroring.html)** - Andrew Nesbitt — 每个包管理器的镜像工具和协议汇总
- **[EnshittifAIcation](https://it-notes.dragas.net/2026/03/20/enshittifaication/)** - IT Notes — AI bot 推荐 VPN、给 nginx 写 Apache 配置、建议用云 VPS 替换 128GB 内存的三个真实案例
- **[The first 3Dfx card: Orchid Righteous 3D](https://dfarq.homeip.net/the-first-3dfx-card-orchid-righteous-3d/)** - Silicon Underground — 1996 年首款 3Dfx 消费级显卡回顾
- **[How do we define our own flourishing?](https://www.joanwestenberg.com/members-only-how-do-we-define-our-own-flourishing/)** - Westenberg — 从 Kardashev 文明尺度谈人类繁荣的定义（付费墙）
- **[SQLAlchemy 2 In Practice - Chapter 1](https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-1---database-setup)** - Miguel Grinberg — SQLAlchemy 2 实战书第一章免费阅读
- **[AppleScript: Save MarsEdit Document to Text File](https://daringfireball.net/2026/03/applescript_save_marsedit_document_to_text_file)** - Gruber — 工作流优化小脚本
- **[Mark Simonson 发现字体设计那天](https://www.marksimonson.com/notebook/view/the-day-i-discovered-type-design/)** - Gruber 推荐 — 字体设计师的起源故事

---

*数据来源: [Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)*
*生成时间: 2026-03-20 15:00 UTC*
