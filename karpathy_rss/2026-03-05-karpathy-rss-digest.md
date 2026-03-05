# Karpathy RSS Digest - 2026-03-05

> 来源：[Andrej Karpathy Curated RSS](https://youmind.com/rss/pack/andrej-karpathy-curated-rss)  
> 时间范围：2026-03-04 16:00 UTC - 2026-03-05 16:00 UTC  
> 文章数：7 篇

---

## 🔥 AI 编程的新礼仪：别把未审查的代码扔给队友

**[Anti-patterns: things to avoid](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/)** - Simon Willison

Simon Willison 写了一篇关于 agentic engineering 反模式的文章，核心观点一针见血：**别把 AI 生成的几百上千行代码直接开 PR，然后指望别人帮你审查。**

这个反模式现在太常见了。你用 AI 生成了一堆代码，自己都没仔细看过，就扔到 PR 里让同事审查。问题是：他们也可以自己 prompt AI 啊，你这样做到底提供了什么价值？

一个好的 agentic engineering PR 应该：
- 代码能跑，你自己测试过
- 改动足够小，不给审查者增加认知负担
- 包含上下文说明，解释为什么这么改
- PR 描述也要自己审查，别直接用 AI 生成的

**点评**：这是 AI 辅助编程时代的新职业道德。AI 可以帮你写代码，但不能替你负责。你的工作是交付能用的代码，不是交付"看起来像代码的东西"。

---

## 💻 MacBook Neo：苹果的消费级新尝试

**[Thoughts and Observations on the MacBook Neo](https://daringfireball.net/2026/03/599_not_a_piece_of_junk_macbook_neo)** - John Gruber

John Gruber 评论了苹果新发布的 MacBook Neo，称其为"Apple Silicon 时代第一款面向消费市场的重要新 Mac"。目标是在 PC 市场占据更大份额。

同时，苹果还更新了 Studio Display 产品线，但有个有趣的限制：**新的 Studio Display 和 Studio Display XDR 都不支持 Intel Mac**。而且 M1/M2/M3 基础款只能跑 60Hz，要 120Hz 需要 Pro 或更高版本，或者 M4/M5。

**点评**：苹果这是在用硬件兼容性逼用户升级。Intel Mac 用户：你们的时代结束了。

---

## 📦 包管理器的魔法文件

**[Package Manager Magic Files](https://nesbitt.io/2026/03/05/package-manager-magic-files.html)** - Andrew Nesbitt

一篇关于各种包管理器"魔法文件"的总结：`.npmrc`、`MANIFEST.in`、`Directory.Packages.props`、`.pnpmfile.cjs` 等等。

这些文件通常藏在项目根目录，控制着依赖管理的各种行为，但很多人并不知道它们的存在。

**点评**：每个生态系统都有自己的隐藏配置文件。了解它们能让你从"会用"升级到"精通"。

---

## 📚 文学角：下地狱救导师才能毕业

**[Book Review: Katabasis by R. F. Kuang](https://shkspr.mobi/blog/2026/03/book-review-katabasis-by-r-f-kuang/)** - Terence Eden's Blog

R.F. Kuang 的新书《Katabasis》：如果你的导师死了，唯一能毕业的方法是下地狱把他带回来。

评论者说这是 Kuang 第一本让他笑出声的书。作者在大学的悲惨经历成就了《Babel》和现在的《Katabasis》。

**点评**：PhD 学生的终极噩梦变成了文学作品。某种程度上，这比真实的 PhD 经历还温和一些。

---

## 🦠 历史回顾：米开朗基罗病毒

**[Remembering the Michelangelo virus](https://dfarq.homeip.net/remembering-michelangelo/)** - The Silicon Underground

1992 年 3 月 6 日，米开朗基罗病毒被设计为覆盖硬盘的前 100 个扇区。虽然不如格式化那么彻底，但对普通用户来说效果差不多。

**点评**：那个年代的病毒还有"纪念日"，现在的恶意软件只想要你的钱。时代变了。

---

## 📊 统计

- **技术文章**：5 篇（AI 编程、硬件、包管理、病毒历史）
- **文化内容**：1 篇（书评）
- **苹果相关**：3 篇（MacBook Neo + Studio Display）

**今日主题**：AI 辅助编程的职业道德 + 苹果硬件更新

---

*Digest 生成时间：2026-03-05*
