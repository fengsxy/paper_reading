# Karpathy RSS Digest - 2026-03-23

> 来源：[Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)
> 时间范围：2026-03-22 15:00 UTC - 2026-03-23 15:00 UTC
> 文章数：13 篇（排除 1 篇付费墙、1 篇低质量订阅推广）

---

## 🔥 深度推荐

### Simon Willison：用 Claude Skills 让 LLM 学会 Starlette 1.0

**[Simon Willison](https://simonwillison.net/2026/Mar/22/starlette/#atom-everything)** - 2026-03-22 23:57

Starlette 1.0 刚发布，API 有 breaking changes（比如 lifespan 替代 on_startup/on_shutdown）。问题来了：LLM 训练数据里只有旧版 Starlette，怎么让它生成 1.0 兼容的代码？Simon 的方案是用 Claude Skills——先让 Claude 克隆仓库、通读文档，自动生成一份完整的 Skill 文档，然后点一个按钮就把它注入到日常 Claude 对话里。验证效果：直接让 Claude 用 Starlette 1.0 搓了个 Kanban 任务管理 app（SQLite + Jinja2），Claude 自己写测试、自己跑测试。他特别指出："Claude 本身就已经是 coding agent 了，不需要 Claude Code 也能写+测代码。"

**点评**：Skills 作为"按需知识注入"的范式越来越成熟。对做框架升级迁移的人来说，这比翻 changelog 高效得多。

### Cory Doctorow：人手不足本身就是 Enshittification

**[Pluralistic](https://pluralistic.net/2026/03/22/nobodys-home/)** - 2026-03-23 05:54

Doctorow 的新长文把"understaffing"（人手不足）定义为一种价值转移机制：CVS 药房只留一个药剂师，你排队等半小时→你的时间换了他们的人力成本；自助结账出故障→你的劳动替代了他们的员工；顾客怒气→转嫁给仅存的前线员工。私募基金"roll-up"整个行业后集体削减人力，因为竞争对手都是自己人，消费者和工人无处可去。他把 AI 客服也归入同一逻辑："AI 取代客服"不是因为 AI 更好，而是因为企业本来就不在乎问题能不能解决——至少 chatbot 不需要薪水，也不会被你的怒火伤害。

**点评**：把 AI 替代论从技术叙事拉回政治经济学视角，论证"we did this with AI = we don't care if this is done well"。值得反复读。

### Jim Nielsen：你看不见的设计准则正在塑造你的产品

**[Jim Nielsen's Blog](https://blog.jim-nielsen.com/2026/opacity-of-generative-tools/)** - Feed 今日推送（文章标注 2026-04-17）

通过 Simon Willison 的文章，Jim 发现 OpenAI Codex 的前端生成模板里写死了一组设计准则：要用表现力强的字体、避免默认字体栈；用有意义的动画而非泛滥的微交互；背景要有层次不能纯色平铺。问题是——如果你的团队开会讨论这些准则，肯定会吵半天达不成一致。但因为它们被"不透明地"塞进了 LLM 的 system prompt，你根本看不见，也就默认接受了。"当你外包思考时，你可能正在内化别人的、你永远不会同意的准则。"

**点评**：对 AI-assisted design/coding 的元批判。用 AI 生成代码 ≠ 你做了设计决策，可能只是继承了别人的偏见。

---

## 📱 科技观察

### Markdown 是怎么吞掉整个世界的

**[matduggan.com](https://matduggan.com/markdown-ate-the-world/)** - 2026-03-23 12:14

从 .doc 格式的"文件系统套文件系统"的疯狂架构讲起，一路讲到 Markdown 如何因为简单、可读、版本控制友好而逐步替代传统文字处理器，成为开发者文档、博客、笔记的事实标准。对 .doc 二进制格式的技术剖析（Compound File Binary Format = 简化版 FAT 文件系统）写得很清楚。

### Simon Willison 的 beats 和研究笔记（4 篇）

Simon 今天产出密集：
- **[JavaScript Sandboxing Research](https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/)** — 用 Claude Code 横评 isolated-vm / vm2 / quickjs-emscripten / QuickJS-NG / ShadowRealm / Deno Workers 六种 JS 沙箱方案
- **[PCGamer Performance Audit](https://simonwillison.net/2026/Mar/22/pcgamer-audit/)** — PC Gamer 推荐 RSS 阅读器的文章本身 37MB，自动播放广告加起来几百 MB。Simon 用 Rodney（Claude Code for web）做了性能审计
- **[DNS Lookup Tool](https://simonwillison.net/2026/Mar/22/dns/)** — 发现 Cloudflare 1.1.1.1 有 CORS-enabled JSON API，顺手搓了个 DNS 查询 UI
- **[Beats now have notes](https://simonwillison.net/2026/Mar/23/beats-now-have-notes/)** — 博客功能更新：beats 条目现在可以加注释了

### Tedium：社交媒体的"煎饼式"讨论

**[Tedium](https://feed.tedium.co/link/15204/17304313/social-media-flat-discussion)** - 2026-03-23 13:17

Ernie Smith 用"煎饼"隐喻社交媒体上的讨论：每个热评（hot take）就像一张煎饼——做起来快、看起来都一样、吃完让人昏沉。极化观点占据话语权，深思熟虑的分析被淹没在层层叠叠的平庸之中。

---

## 💤 跳过

- **Abort Retry Fail: Hitachi Ltd, Part I** — 付费文章，无法阅读
- **The Silicon Underground: What came after 486?** — CPU 命名史趣闻（486→Pentium），轻量怀旧向
- **Joan Westenberg: "Collaboration" is bullshit** — 内容主体是订阅推广，实质内容极少

---

*数据来源: [Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)*
*生成时间: 2026-03-23 15:00 UTC*
