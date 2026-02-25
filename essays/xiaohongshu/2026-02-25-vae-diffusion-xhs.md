---
layout: post
title: "【小红书】为什么VAE和Diffusion很难端到端训练"
date: 2026-02-25
author: Longxuan Yu
categories: xiaohongshu
---

最近看了几篇论文（UL、REPA-E、Latent Forcing、JiT），发现它们都在解同一个问题：VAE和Diffusion Model怎么一起训？或者说——还需要VAE吗？

📌 问题出在哪？

现在主流的图像生成pipeline是两阶段：先训VAE把图片压成latent，冻住VAE，再训diffusion model。

为什么不直接end-to-end？因为会崩。

REPA-E发现：如果你把diffusion的loss直接反传回VAE，latent space会collapse。diffusion的目标会把latent hack成极其简单的分布——生成是容易了，但重建质量直接崩掉。

本质原因：diffusion想要简单的latent分布（好建模），VAE想要信息丰富的latent（好重建）。两个目标打架。

📌 四种解法

UL的思路：VAE的Gaussian prior本来就不对。换成diffusion prior，用一个参数λ(0)控制latent里编码多少信息。干净，但只管生成，不管理解。

REPA-E的思路：用DINOv2的语义特征做alignment loss去更新VAE，对diffusion loss做stop-gradient。防止collapse，但语义是从外部teacher借来的。

Latent Forcing的思路：重排diffusion trajectory，先生成DINO features（语义），再细化到pixel。把语义信息编码进生成过程的结构里。

JiT的思路：最暴力——直接不要VAE了。在pixel space做flow matching，用x-prediction（直接预测clean image）。Kaiming He的风格，极简设计，证明pixel space diffusion是可行的。

📌 JiT之后的进展

JiT证明了pixel space能work，但FID还是比latent diffusion差。PixelGen在JiT基础上加了perceptual loss，FID从23.67降到7.53，第一次在相同训练设置下pixel diffusion打赢了latent diffusion。

这说明VAE不是必须的，但你需要某种方式把语义信息注入训练过程。

📌 显式解耦已经有人做了

SVG直接用DINO encoder提语义 + residual encoder补高频细节，两路信息显式分开。

📌 但核心问题没人解

所有方案的语义能力都依赖冻住的DINO。SVG、REPA-E、Latent Forcing、PixelGen全是。语义不是模型自己学的，是外部teacher灌进去的。

真正的统一应该是模型在训练过程中自己涌现出语义和细节的分离。下一步不是换一个更好的teacher，而是让模型自己学会把这两种信息分开。
