---
title: "VAE和Diffusion的联合训练：三篇论文在解同一个问题，但没人碰核心矛盾"
date: 2026-02-25
author: Longxuan Yu
lang: zh
---

# VAE和Diffusion的联合训练：三篇论文在解同一个问题，但没人碰核心矛盾

最近看了三篇论文：Unified Latents (UL)、REPA-E、Latent Forcing。表面上方向不同，但我觉得它们暴露了同一个根本问题：

**latent space 能不能同时服务于生成和理解？**

目前的答案是：不能，至少现有方法都没做到。

### UL：VAE的Gaussian prior本来就是错的

UL（Unified Latents, arXiv:2602.17270）的出发点很直接：传统VAE用Gaussian prior去正则化latent space，但后面接的是diffusion model。Gaussian prior和diffusion model实际学到的latent分布之间有mismatch，这个mismatch导致你没法精确控制latent里到底编码了多少信息。

UL的解法是把Gaussian prior换成diffusion prior。具体做法是把encoder输出的noise level直接和diffusion prior的最小noise level λ(0) 挂钩，这样就得到了一个tight的latent bitrate上界。一个参数λ(0)就能控制reconstruction和generation之间的trade-off。

这个思路是干净的。但UL本质上还是在回答"怎么更好地训练VAE+diffusion"，它没有碰生成和理解的统一问题。latent space被优化来服务生成，理解能力不在它的目标函数里。

### REPA-E：end-to-end训练的坑

REPA-E（arXiv:2504.10483）问了一个更直接的问题：能不能把VAE和diffusion model一起end-to-end训练？

传统做法是先训VAE，冻住，再训diffusion。REPA-E发现如果你直接把diffusion loss反传回VAE，latent space会collapse——diffusion的目标会把latent hack成trivially simple的分布，重建质量崩掉。

它的解法是用REPA loss：把diffusion中间层的feature和冻住的DINOv2做alignment，用这个loss去更新VAE，同时对diffusion loss做stop-gradient。这样DINOv2的语义结构被注入到latent space里，防止collapse。

效果确实好，end-to-end训练收敛更快，FID也更好。但问题是：语义信息来自外部冻住的DINOv2，不是模型自己学出来的。你依赖一个外部teacher来提供理解能力，这不是真正的统一。

### Latent Forcing：方向最对，但还没到

Latent Forcing（arXiv:2602.11401）做的事情和前两篇不太一样。它不是在改VAE-diffusion的训练方式，而是在问：能不能直接在pixel space做diffusion，但保留latent diffusion的效率？

做法是重排diffusion trajectory：先生成DINO features（语义信息），再逐步细化到pixel level。DINO features天然带语义，所以生成过程的早期阶段就已经在处理高层理解信息了。

这个方向我觉得是最接近生成-理解统一的。因为它不是把语义当作外部约束（REPA-E的做法），也不是完全不管语义（UL的做法），而是把语义信息直接编码进生成过程的结构里。

但Latent Forcing目前还是在做图像生成，没有显式地验证它的latent space在理解任务上的表现。

### 核心矛盾是什么

三篇论文放在一起看，核心矛盾很清楚：

**最优的生成空间不是最优的理解空间。**

这个我之前在essay里写过。理解只需要抽象的轮廓信息，linear probing能分类就行。但生成需要所有细节——高频纹理、精确像素值。一个latent space如果要同时编码这两种信息，它们会互相干扰。

UL的做法是只管生成，不管理解。REPA-E的做法是从外部注入理解能力（DINOv2），但这是借来的，不是自己的。Latent Forcing的做法最有意思——它试图让生成过程本身就按语义层次组织，这样理解能力是生成过程的副产品。

但没有一篇真正回答：**能不能设计一个latent space，让生成和理解的信息自然解耦？**

我的直觉是需要一个解耦的表征结构。比如latent的前N个维度编码语义（用于理解），后M个维度编码细节（用于生成），两者在训练中被显式分开。REPA的思路其实已经在往这个方向走了——它用alignment loss把diffusion的中间层往语义方向拉，相当于在网络内部做了一种隐式的解耦。但这种解耦是soft的，没有理论保证。

更根本的问题可能是：生成和理解需要的信息量差了几个数量级。理解可能只需要几百bit的语义信息，但生成需要几万bit的像素信息。在同一个bottleneck里同时传输这两种信息，信息论上就是有矛盾的。UL的bitrate bound框架其实提供了一个很好的工具来分析这个问题——你可以问：在给定bitrate下，生成和理解各自的最优latent是什么？它们的gap有多大？

### 一句话

UL和REPA-E都在解VAE-diffusion联合训练的问题，但都没碰生成-理解统一。Latent Forcing方向最对，但还没到。下一步应该是：用信息论搞清楚生成和理解在latent space里到底需要什么，然后设计显式的解耦机制。

---

*相关论文：*
- *Unified Latents (UL): How to train your latents (arXiv:2602.17270)*
- *REPA-E: Unlocking VAE for End-to-End Tuning with Latent Diffusion Transformers (arXiv:2504.10483)*
- *Latent Forcing: Reordering the Diffusion Trajectory for Pixel-Space Image Generation (arXiv:2602.11401)*
