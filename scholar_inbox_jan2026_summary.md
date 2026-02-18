# Scholar Inbox - January 2026 Summary

## 01-06-2026 (1/264 papers)


16
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
VINO: A Unified Visual Generator with Interleaved OmniModal Context

Junyi Chen, Tong He, Zhoujie Fu, Pengfei Wan, Kun Gai, Weicai Ye

ArXiv 2026 (Submitted on January 5)
thumb_up_alt
19
visibility
77
format_quote
0
photo_camera
Computer Vision and Graphics
We present VINO, a unified visual generator that performs image and video generation and editing within a single framework. Instead of relying on task-specific models or independent modules for each modality, VINO uses a shared diffusion backbone that conditions on text, images and videos, enabling a broad range of visual creation and editing tasks under one model. Specifically, VINO couples a vision-language model (VLM) with a Multimodal Diffusion Transformer (MMDiT), where multimodal inputs are encoded as interleaved conditioning tokens, and then used to guide the diffusion process. This design supports multi-reference grounding, long-form instruction following, and coherent identity preservation across static and dynamic content, while avoiding modality-specific architectural components. To train such a unified system, we introduce a multi-stage training pipeline that progressively expands a video generation base model into a unified, multi-task generator capable of both image and video input and output. Across diverse generation and editing benchmarks, VINO demonstrates strong visual quality, faithful instruction following, improved reference and attribute preservation, and more controllable multi-identity edits. Our results highlight a practical path toward scalable unified visual generation, and the promise of interleaved, in-context computation as a foundation for general-purpose visual creation.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers

You have reached the end 🍰

---

## 01-07-2026 (27/1039 papers)


97
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
DIP: Dynamic In-Context Planner For Diffusion Language Models

Yang Li, Han Meng, Chenan Wang, Haipeng Chen

ArXiv 2026 (Submitted on January 6)
thumb_up_alt
7
visibility
24
format_quote
0
g_translate
Language
Diffusion language models (DLMs) have shown strong potential for general natural language tasks with in-context examples. However, due to the bidirectional attention mechanism, DLMs incur substantial computational cost as context length increases. This work addresses this issue with a key discovery: unlike the sequential generation in autoregressive language models (ARLMs), the diffusion generation paradigm in DLMs allows efficient dynamic adjustment of the context during generation. Building on this insight, we propose Dynamic In-Context Planner (DIP), a context-optimization method that dynamically selects and inserts in-context examples during generation, rather than providing all examples in the prompt upfront. Results show DIP maintains generation quality while achieving up to 12.9× inference speedup over standard inference and 1.17× over KV cache-enhanced inference.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
77
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Critic-Guided Reinforcement Unlearning in Text-to-Image Diffusion

Mykola Vysotskyi, Zahar Kohut, Mariia Shpir, Taras Rumezhak, Volodymyr Karpiv

ArXiv 2026 (Submitted on January 6)
thumb_up_alt
1
visibility
19
format_quote
0
hub
Machine Learning
Machine unlearning in text-to-image diffusion models aims to remove targeted concepts while preserving overall utility. Prior diffusion unlearning methods typically rely on supervised weight edits or global penalties; reinforcement-learning (RL) approaches, while flexible, often optimize sparse end-of-trajectory rewards, yielding high-variance updates and weak credit assignment. We present a general RL framework for diffusion unlearning that treats denoising as a sequential decision process and introduces a timestep-aware critic with noisy-step rewards. Concretely, we train a CLIP-based reward predictor on noisy latents and use its per-step signal to compute advantage estimates for policy-gradient updates of the reverse diffusion kernel. Our algorithm is simple to implement, supports off-policy reuse, and plugs into standard text-to-image backbones. Across multiple concepts, the method achieves better or comparable forgetting to strong baselines while maintaining image quality and benign prompt fidelity; ablations show that (i) per-step critics and (ii) noisy-conditioned rewards are key to stability and effectiveness. We release code and evaluation scripts to facilitate reproducibility and future research on RL-based diffusion unlearning.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary

---

## 01-08-2026 (24/1200 papers)


94
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Bridging the Discrete-Continuous Gap: Unified Multimodal Generation via Coupled Manifold Discrete Absorbing Diffusion

Yuanfeng Xu, Yuhao Chen, Liang Lin, Guangrun Wang

ArXiv 2026 (Submitted on January 7)
thumb_up_alt
6
visibility
18
format_quote
0
g_translate
Language
The bifurcation of generative modeling into autoregressive approaches for discrete data (text) and diffusion approaches for continuous data (images) hinders the development of truly unified multimodal systems. While Masked Language Models (MLMs) offer efficient bidirectional context, they traditionally lack the generative fidelity of autoregressive models and the semantic continuity of diffusion models. Furthermore, extending masked generation to multimodal settings introduces severe alignment challenges and training instability. In this work, we propose CoM-DAD (Coupled Manifold Discrete Absorbing Diffusion), a novel probabilistic framework that reformulates multimodal generation as a hierarchical dual-process. CoM-DAD decouples high-level semantic planning from low-level token synthesis. First, we model the semantic manifold via a continuous latent diffusion process; second, we treat token generation as a discrete absorbing diffusion process, regulated by a Variable-Rate Noise Schedule, conditioned on these evolving semantic priors. Crucially, we introduce a Stochastic Mixed-Modal Transport strategy that aligns disparate modalities without requiring heavy contrastive dual-encoders. Our method demonstrates superior stability over standard masked modeling, establishing a new paradigm for scalable, unified text-image generation.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
62
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning

Yifan Wang, Yanyu Li, Sergey Tulyakov, Yun Fu, Anil Kag

ArXiv 2026 (Submitted on January 7)
thumb_up_alt
3
visibility
21
format_quote
0
photo_camera
Computer Vision and Graphics
Direct Preference Optimization (DPO) has recently improved Text-to-Video (T2V) generation by enhancing visual fidelity and text alignment. However, current methods rely on non-differentiable preference signals from human annotations or learned reward models. This reliance makes training label-intensive, bias-prone, and easy-to-game, which often triggers reward hacking and unstable training. We propose Diffusion-DRF, a differentiable reward flow for fine-tuning video diffusion models using a frozen, off-the-shelf Vision-Language Model (VLM) as a training-free critic. Diffusion-DRF directly backpropagates VLM feedback through the diffusion denoising chain, converting logit-level responses into token-aware gradients for optimization. We propose an automated, aspect-structured prompting pipeline to obtain reliable multi-

---

## 01-09-2026 (23/1258 papers)


95
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
STDD:Spatio-Temporal Dynamics-Driven Token Refinement in Diffusion Language Models

Xinhao Sun, Maoliang Li, Zihao Zheng, Jiayu Chen, Hezhao Xu, ... Xiang Chen

ArXiv 2025 (Submitted on December 7)
thumb_up_alt
0
visibility
8
format_quote
0
g_translate
Language
Unlike autoregressive language models, diffusion language models (DLMs) generate text by iteratively denoising all token positions in parallel. At each timestep, the remasking strategy of a DLM selects low-priority tokens to defer their decoding, thereby improving both efficiency and output quality. However, mainstream remasking strategies rely on a single global confidence threshold, overlooking the temporal and spatial dynamics of individual tokens. Motivated by the redundant iterations and constrained parallelism introduced by fixed-threshold remasking, we propose a novel remasking approach that dynamically detects Temporal Variance and Spatial Deviance of each token, which reflect its convergence status and inter-token correlations. Using these signals, our method adaptively adjusts the confidence threshold for every token at every step. Empirical results show that our approach significantly improves the operational efficiency of DLMs across mainstream datasets, achieving speedups of up to 8.9 times while faithfully preserving generation quality.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
92
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Token Maturation: Autoregressive Language Generation via Continuous Token Dynamics

Oshri Naparstek

ArXiv 2026 (Submitted on January 8)
thumb_up_alt
1
visibility
16
format_quote
0
g_translate
Language
Autoregressive language models are conventionally defined over discrete token sequences, committing to a specific token at every generation step. This early discretization forces uncertainty to be resolved through token-level sampling, often leading to instability, repetition, and sensitivity to decoding heuristics. In this work, we introduce a continuous autoregressive formulation of language generation in which tokens are represented as continuous vectors that mature over multiple update steps before being discretized. Rather than sampling tokens, the model evolves continuous token representations through a deterministic dynamical process, committing to a discrete token only when the representation has sufficiently converged. Discrete text is recovered via hard decoding, while uncertainty is maintained and resolved in the continuous space. We show that this maturation process alone is sufficient to produce coherent and diverse text using deterministic decoding (argmax), without reliance on token-level sampling, diffusion-style denoising, or auxiliary stabilization mechanisms. Additional perturbations, such as stochastic dynamics or history smoothing, c

---

## 01-10-2026 (14/1230 papers)


79
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Boosting Latent Diffusion Models via Disentangled Representation Alignment

John Page, Xuesong Niu, Kai Wu, Kun Gai

ArXiv 2026 (Submitted on January 9)
thumb_up_alt
15
visibility
103
format_quote
0
photo_camera
Computer Vision and Graphics
Latent Diffusion Models (LDMs) generate high-quality images by operating in a compressed latent space, typically obtained through image tokenizers such as Variational Autoencoders (VAEs). In pursuit of a generation-friendly VAE, recent studies have explored leveraging Vision Foundation Models (VFMs) as representation alignment targets for VAEs, mirroring the approach commonly adopted for LDMs. Although this yields certain performance gains, using the same alignment target for both VAEs and LDMs overlooks their fundamentally different representational requirements. We advocate that while LDMs benefit from latents retaining high-level semantic concepts, VAEs should excel in semantic disentanglement, enabling encoding of attribute-level information in a structured way. To address this, we propose the Semantic disentangled VAE (Send-VAE), explicitly optimized for disentangled representation learning through aligning its latent space with the semantic hierarchy of pre-trained VFMs. Our approach employs a non-linear mapper network to transform VAE latents, aligning them with VFMs to bridge the gap between attribute-level disentanglement and high-level semantics, facilitating effective guidance for VAE learning. We evaluate semantic disentanglement via linear probing on attribute prediction tasks, showing strong correlation with improved generation performance. Finally, using Send-VAE, we train flow-based transformers SiTs; experiments show Send-VAE significantly speeds up training and achieves a state-of-the-art FID of 1.21 and 1.75 with and without classifier-free guidance on ImageNet 256x256.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
68
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Visualising Information Flow in Word Embeddings with Diffusion Tensor Imaging

Thomas Fabian

ArXiv 2026 (Submitted on January 9)
thumb_up_alt
2
visibility
5
format_quote
0
g_translate
Language
Understanding how large language models (LLMs) represent natural language is a central challenge in natural language processing (NLP) research. Many existing methods extract word embeddings from an LLM, visualise the embedding space via point-plots, and compare the relative positions of certain words. However, this approach only considers single words and not whole natural language expressions, thus disregards the context in which a word is used. Here we present a novel tool for analysing and visualising information flow in natural language expressions by applying diffusion tensor imaging (DTI) to word embeddings. We find that DTI reveals how i

---

## 01-11-2026 (14/1230 papers)


79
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Boosting Latent Diffusion Models via Disentangled Representation Alignment

John Page, Xuesong Niu, Kai Wu, Kun Gai

ArXiv 2026 (Submitted on January 9)
thumb_up_alt
15
visibility
103
format_quote
0
photo_camera
Computer Vision and Graphics
Latent Diffusion Models (LDMs) generate high-quality images by operating in a compressed latent space, typically obtained through image tokenizers such as Variational Autoencoders (VAEs). In pursuit of a generation-friendly VAE, recent studies have explored leveraging Vision Foundation Models (VFMs) as representation alignment targets for VAEs, mirroring the approach commonly adopted for LDMs. Although this yields certain performance gains, using the same alignment target for both VAEs and LDMs overlooks their fundamentally different representational requirements. We advocate that while LDMs benefit from latents retaining high-level semantic concepts, VAEs should excel in semantic disentanglement, enabling encoding of attribute-level information in a structured way. To address this, we propose the Semantic disentangled VAE (Send-VAE), explicitly optimized for disentangled representation learning through aligning its latent space with the semantic hierarchy of pre-trained VFMs. Our approach employs a non-linear mapper network to transform VAE latents, aligning them with VFMs to bridge the gap between attribute-level disentanglement and high-level semantics, facilitating effective guidance for VAE learning. We evaluate semantic disentanglement via linear probing on attribute prediction tasks, showing strong correlation with improved generation performance. Finally, using Send-VAE, we train flow-based transformers SiTs; experiments show Send-VAE significantly speeds up training and achieves a state-of-the-art FID of 1.21 and 1.75 with and without classifier-free guidance on ImageNet 256x256.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
68
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Visualising Information Flow in Word Embeddings with Diffusion Tensor Imaging

Thomas Fabian

ArXiv 2026 (Submitted on January 9)
thumb_up_alt
2
visibility
5
format_quote
0
g_translate
Language
Understanding how large language models (LLMs) represent natural language is a central challenge in natural language processing (NLP) research. Many existing methods extract word embeddings from an LLM, visualise the embedding space via point-plots, and compare the relative positions of certain words. However, this approach only considers single words and not whole natural language expressions, thus disregards the context in which a word is used. Here we present a novel tool for analysing and visualising information flow in natural language expressions by applying diffusion tensor imaging (DTI) to word embeddings. We find that DTI reveals how i

---

## 01-12-2026 (14/1230 papers)


79
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Boosting Latent Diffusion Models via Disentangled Representation Alignment

John Page, Xuesong Niu, Kai Wu, Kun Gai

ArXiv 2026 (Submitted on January 9)
thumb_up_alt
15
visibility
103
format_quote
0
photo_camera
Computer Vision and Graphics
Latent Diffusion Models (LDMs) generate high-quality images by operating in a compressed latent space, typically obtained through image tokenizers such as Variational Autoencoders (VAEs). In pursuit of a generation-friendly VAE, recent studies have explored leveraging Vision Foundation Models (VFMs) as representation alignment targets for VAEs, mirroring the approach commonly adopted for LDMs. Although this yields certain performance gains, using the same alignment target for both VAEs and LDMs overlooks their fundamentally different representational requirements. We advocate that while LDMs benefit from latents retaining high-level semantic concepts, VAEs should excel in semantic disentanglement, enabling encoding of attribute-level information in a structured way. To address this, we propose the Semantic disentangled VAE (Send-VAE), explicitly optimized for disentangled representation learning through aligning its latent space with the semantic hierarchy of pre-trained VFMs. Our approach employs a non-linear mapper network to transform VAE latents, aligning them with VFMs to bridge the gap between attribute-level disentanglement and high-level semantics, facilitating effective guidance for VAE learning. We evaluate semantic disentanglement via linear probing on attribute prediction tasks, showing strong correlation with improved generation performance. Finally, using Send-VAE, we train flow-based transformers SiTs; experiments show Send-VAE significantly speeds up training and achieves a state-of-the-art FID of 1.21 and 1.75 with and without classifier-free guidance on ImageNet 256x256.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
68
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Visualising Information Flow in Word Embeddings with Diffusion Tensor Imaging

Thomas Fabian

ArXiv 2026 (Submitted on January 9)
thumb_up_alt
2
visibility
5
format_quote
0
g_translate
Language
Understanding how large language models (LLMs) represent natural language is a central challenge in natural language processing (NLP) research. Many existing methods extract word embeddings from an LLM, visualise the embedding space via point-plots, and compare the relative positions of certain words. However, this approach only considers single words and not whole natural language expressions, thus disregards the context in which a word is used. Here we present a novel tool for analysing and visualising information flow in natural language expressions by applying diffusion tensor imaging (DTI) to word embeddings. We find that DTI reveals how i

---

## 01-13-2026 (42/1997 papers)


97
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Mosaic: Unlocking Long-Context Inference for Diffusion LLMs via Global Memory Planning and Dynamic Peak Taming

Liang Zheng, Bowen Shi, Yitao Hu, Jiawei Zhang, Ruofan Li, ... Keqiu Li

ArXiv 2026 (Submitted on January 10)
thumb_up_alt
3
visibility
14
format_quote
0
hub
Machine Learning
category
Computer Science
Artificial Intelligence
Large Language Models
Memory Management
Diffusion Models
Long-Context Inference
Mosaic
Diffusion-based large language models (dLLMs) have emerged as a promising paradigm, utilizing simultaneous denoising to enable global planning and iterative refinement. While these capabilities are particularly advantageous for long-context generation, deploying such models faces a prohibitive memory capacity barrier stemming from severe system inefficiencies. We identify that existing inference systems are ill-suited for this paradigm: unlike autoregressive models constrained by the cumulative KV-cache, dLLMs are bottlenecked by transient activations recomputed at every step. Furthermore, general-purpose memory reuse mechanisms lack the global visibility to adapt to dLLMs' dynamic memory peaks, which toggle between logits and FFNs. To address these mismatches, we propose Mosaic, a memory-efficient inference system that shifts from local, static management to a global, dynamic paradigm. Mosaic integrates a mask-only logits kernel to eliminate redundancy, a lazy chunking optimizer driven by an online heuristic search to adaptively mitigate dynamic peaks, and a global memory manager to resolve fragmentation via virtual addressing. Extensive evaluations demonstrate that Mosaic achieves an average 2.71× reduction in the memory peak-to-average ratio and increases the maximum inference sequence length supportable on identical hardware by 15.89-32.98×. This scalability is achieved without compromising accuracy and speed, and in fact reducing latency by 4.12%-23.26%.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
94
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
d3LLM: Ultra-Fast Diffusion LLM using Pseudo-Trajectory Distillation

Yu-Yang Qian, Junda Su, Lanxiang Hu, Peiyuan Zhang, Zhijie Deng, ... Hao Zhang

ArXiv 2026 (Submitted on January 12)
thumb_up_alt
4
visibility
24
format_quote
0
hub
Machine Learning
category
Computer Science
Machine Learning
Diffusion Models
Diffusion Large Language Models
Pseudo-Trajectory Distillation
Multi-Block Decoding
Accuracy Under Parallelism
AUP
Diffusion large language models (dLLMs) offer capabilities beyond those of autoregressive (AR) LLMs, such as parallel decoding and random-order generation. However, realizing these benefits in practice is non-trivial, as dLLMs inherently face an accuracy-parallelism trade-off. Despite increasing interest, existing methods typically focus on only one-side of the coin

---

## 01-14-2026 (16/1328 papers)


73
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Where Does Vision Meet Language? Understanding and Refining Visual Fusion in MLLMs via Contrastive Attention

Shezheng Song, Shasha Li, Jie Yu

ArXiv 2026 (Submitted on January 13)
thumb_up_alt
7
visibility
41
format_quote
0
photo_camera
Computer Vision and Graphics
category
Computer Science
Artificial Intelligence
Multimodal Learning
Multimodal Language Models
Contrastive Attention
Visual Fusion
Layer-wise Analysis
Review Mechanism
Multimodal Large Language Models (MLLMs) have achieved remarkable progress in vision-language understanding, yet how they internally integrate visual and textual information remains poorly understood. To bridge this gap, we perform a systematic layer-wise masking analysis across multiple architectures, revealing how visual-text fusion evolves within MLLMs. The results show that fusion emerges at several specific layers rather than being uniformly distributed across the network, and certain models exhibit a late-stage "review" phenomenon where visual signals are reactivated before output generation. Besides, we further analyze layer-wise attention evolution and observe persistent high-attention noise on irrelevant regions, along with gradually increasing attention on text-aligned areas. Guided by these insights, we introduce a training-free contrastive attention framework that models the transformation between early fusion and final layers to highlight meaningful attention shifts. Extensive experiments across various MLLMs and benchmarks validate our analysis and demonstrate that the proposed approach improves multimodal reasoning performance. Code will be released.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
69
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Revealing the Attention Floating Mechanism in Masked Diffusion Models

Xin Dai, Pengcheng Huang, Zhenghao Liu, Shuo Wang, Yukun Yan, ... Maosong Sun

ArXiv 2026 (Submitted on January 12)
thumb_up_alt
1
visibility
4
format_quote
0
hub
Machine Learning
category
Computer Science
Natural Language Processing
Attention Mechanisms
Attention Floating
Bidirectional Attention
Layer-wise Normalization
Contextual Retrieval
Denoising Process
Masked diffusion models (MDMs), which leverage bidirectional attention and a denoising process, are narrowing the performance gap with autoregressive models (ARMs). However, their internal attention mechanisms remain under-explored. This paper investigates the attention behaviors in MDMs, revealing the phenomenon of Attention Floating. Unlike ARMs, where attention converges to a fixed sink, MDMs exhibit dynamic, dispersed attention anchors that shift across denoising steps and layers. Further analysis reveals its Shallow Structure-Aware, Deep Content-Focused attention mechanism: shallow layers utilize floating tokens to build a global struct

---

## 01-15-2026 (16/1166 papers)


52
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Hot-Start from Pixels: Low-Resolution Visual Tokens for Chinese Language Modeling

Shuyang Xiang, Hao Guan

ArXiv 2026 (Submitted on January 14)
thumb_up_alt
1
visibility
12
format_quote
0
photo_camera
Computer Vision and Graphics
category
Computer Science
Natural Language Processing
Chinese Language Modeling
Chinese Language Modeling
Vision Tokens
Hot-Start Effect
THUCNews Dataset
Vision Encoder
Large language models typically represent Chinese characters as discrete index-based tokens, largely ignoring their visual form. For logographic scripts, visual structure carries semantic and phonetic information, which may aid prediction. We investigate whether low-resolution visual inputs can serve as an alternative for character-level modeling. Instead of token IDs, our decoder receives grayscale images of individual characters, with resolutions as low as 8×8 pixels. Remarkably, these inputs achieve 39.2% accuracy, comparable to the index-based baseline of 39.1%. Such low-resource settings also exhibit a pronounced hot-start effect: by 0.4% of total training, accuracy reaches above 12%, while index-based models lag at below 6%. Overall, our results demonstrate that minimal visual structure can provide a robust and efficient signal for Chinese language modeling, offering an alternative perspective on character representation that complements traditional index-based approaches.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
46
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
LLMs Meet Isolation Kernel: Lightweight, Learning-free Binary Embeddings for Fast Retrieval

Zhibo Zhang, Yang Xu, Kai Ming Ting, Cam-Tu Nguyen

ArXiv 2026 (Submitted on January 14)
thumb_up_alt
2
visibility
6
format_quote
0
computer
Computer Science
category
Computer Science
Machine Learning
Natural Language Processing
Binary Embeddings
Isolation Kernel
Learning-free Compression
Approximate Nearest Neighbor
Text Retrieval
Large language models (LLMs) have recently enabled remarkable progress in text representation. However, their embeddings are typically high-dimensional, leading to substantial storage and retrieval overhead. Although recent approaches such as Matryoshka Representation Learning (MRL) and Contrastive Sparse Representation (CSR) alleviate these issues to some extent, they still suffer from retrieval accuracy degradation. This paper proposes Isolation Kernel Embedding or IKE, a learning-free method that transforms an LLM embedding into a binary embedding using Isolation Kernel (IK). IKE is an ensemble of diverse (random) partitions, enabling robust estimation of ideal kernel in the LLM embedding space, thus reducing retrieval accuracy loss as the ensemble grows. Lightweight and based on binary encoding, it offers low memory footprint and fast bitwise computation, lowering r

---

## 01-16-2026 (16/1294 papers)


90
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Think-Then-Generate: Reasoning-Aware Text-to-Image Diffusion with LLM Encoders

Siqi Kou, Jiachun Jin, Zetong Zhou, Ye Ma, Yugang Wang, ... Zhijie Deng

ArXiv 2026 (Submitted on January 15)
thumb_up_alt
25
visibility
112
format_quote
0
photo_camera
Computer Vision and Graphics
category
Computer Science
Artificial Intelligence
Text-to-Image Generation
Text-to-Image Generation (T2I)
CoT Reasoning
Dual-GRPO
Group Relative Policy Optimization
WISE Benchmark
Recent progress in text-to-image (T2I) diffusion models (DMs) has enabled high-quality visual synthesis from diverse textual prompts. Yet, most existing T2I DMs, even those equipped with large language model (LLM)-based text encoders, remain text-pixel mappers -- they employ LLMs merely as text encoders, without leveraging their inherent reasoning capabilities to infer what should be visually depicted given the textual prompt. To move beyond such literal generation, we propose the think-then-generate (T2G) paradigm, where the LLM-based text encoder is encouraged to reason about and rewrite raw user prompts; the states of the rewritten prompts then serve as diffusion conditioning. To achieve this, we first activate the think-then-rewrite pattern of the LLM encoder with a lightweight supervised fine-tuning process. Subsequently, the LLM encoder and diffusion backbone are co-optimized to ensure faithful reasoning about the context and accurate rendering of the semantics via Dual-GRPO. In particular, the text encoder is reinforced using image-grounded rewards to infer and recall world knowledge, while the diffusion backbone is pushed to produce semantically consistent and visually coherent images. Experiments show substantial improvements in factual consistency, semantic alignment, and visual realism across reasoning-based image generation and editing benchmarks, achieving 0.79 on WISE score, nearly on par with GPT-4. Our results constitute a promising step toward next-generation unified models with reasoning, expression, and demonstration capacities.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
65
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Forgetting as a Feature: Cognitive Alignment of Large Language Models

Hien Tran, Quinten Steenhuis, Alexandros Christoforos, Chadbourne Davis

ArXiv 2025 (Submitted on December 28)
thumb_up_alt
1
visibility
20
format_quote
0
g_translate
Language
category
Computer Science
Artificial Intelligence
Cognitive Computing
Memory Dynamics
Bayesian Inference
Probabilistic Models
Forgetting Mechanisms
Cognitive Alignment
Large Language Models (LLMs) are often evaluated against ideals of perfect Bayesian inference, yet growing evidence suggests that their in-context reasoning exhibits systematic forgetting of past information. Rather than viewing this behavior as a limitati

---

## 01-20-2026 (16/1532 papers)


94
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Unlocking the Potentials of Retrieval-Augmented Generation for Diffusion Language Models

Chuanyue Yu, Jiahui Wang, Yuhan Li, Heng Chang, Ge Lan, ... Ziwei Zhang

ArXiv 2026 (Submitted on January 16)
thumb_up_alt
0
visibility
2
format_quote
0
category
category
Computer Science
Natural Language Processing
Retrieval-Augmented Generation
Retrieval-Augmented Generation (RAG)
Diffusion Language Models (DLMs)
Semantic Drift
Response Semantic Drift (RSD)
Semantic-Preserving REtrieval-Augmented Diffusion (SPREAD)
Diffusion Language Models (DLMs) have recently demonstrated remarkable capabilities in natural language processing tasks. However, the potential of Retrieval-Augmented Generation (RAG), which shows great successes for enhancing large language models (LLMs), has not been well explored, due to the fundamental difference between LLM and DLM decoding. To fill this critical gap, we systematically test the performance of DLMs within the RAG framework. Our findings reveal that DLMs coupled with RAG show promising potentials with stronger dependency on contextual information, but suffer from limited generation precision. We identify a key underlying issue: Response Semantic Drift (RSD), where the generated answer progressively deviates from the query's original semantics, leading to low precision content. We trace this problem to the denoising strategies in DLMs, which fail to maintain semantic alignment with the query throughout the iterative denoising process. To address this, we propose Semantic-Preserving REtrieval-Augmented Diffusion (SPREAD), a novel framework that introduces a query-relevance-guided denoising strategy. By actively guiding the denoising trajectory, SPREAD ensures the generation remains anchored to the query's semantics and effectively suppresses drift. Experimental results demonstrate that SPREAD significantly enhances the precision and effectively mitigates RSD of generated answers within the RAG framework.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
59
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
T
⋆
: Progressive Block Scaling for MDM Through Trajectory Aware RL

Hanchen Xia, Baoyou Chen, Yutang Ge, Guojiang Zhao, Siyu Zhu

ArXiv 2026 (Submitted on January 16)
thumb_up_alt
1
visibility
6
format_quote
0
category
category
Computer Science
Machine Learning
Natural Language Processing
Masked Diffusion Models
Trajectory-aware Reinforcement Learning
Block Size Scaling
Progressive Training
MATH500
We present T
⋆
, a simple TraceRL-based training curriculum for progressive block-size scaling in masked diffusion language models (MDMs). Starting from an AR-initialized small-block MDM, T
⋆
~transitions smoothly to larger blocks, enabling higher-parallelism decoding with minimal performance degradation on math reasoning benchmarks. Moreov

---

## 01-21-2026 (39/2123 papers)


93
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Plan, Verify and Fill: A Structured Parallel Decoding Approach for Diffusion Language Models

Miao Li, Hanyang Jiang, Sikai Chen, Hengyu Fu, Yuhang Cai, ... Pascal Van Hentenryck

ArXiv 2026 (Submitted on January 18)
thumb_up_alt
0
visibility
11
format_quote
0
category
category
Computer Science
Artificial Intelligence
Natural Language Processing
Diffusion Models
Parallel Decoding
Planning Tokens
Structural Saturation
NFE Reduction
Diffusion Language Models (DLMs) present a promising non-sequential paradigm for text generation, distinct from standard autoregressive (AR) approaches. However, current decoding strategies often adopt a reactive stance, underutilizing the global bidirectional context to dictate global trajectories. To address this, we propose Plan-Verify-Fill (PVF), a training-free paradigm that grounds planning via quantitative validation. PVF actively constructs a hierarchical skeleton by prioritizing high-leverage semantic anchors and employs a verification protocol to operationalize pragmatic structural stopping where further deliberation yields diminishing returns. Extensive evaluations on LLaDA-8B-Instruct and Dream-7B-Instruct demonstrate that PVF reduces the Number of Function Evaluations (NFE) by up to 65% compared to confidence-based parallel decoding across benchmark datasets, unlocking superior efficiency without compromising accuracy.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
89
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Autoregressive Models Rival Diffusion Models at ANY-ORDER Generation

Tianqi Du, Lizhe Fang, Weijie Yang, Chenheng Zhang, Zeming Wei, ... Yisen Wang

ArXiv 2026 (Submitted on January 19)
thumb_up_alt
3
visibility
18
format_quote
0
category
category
Computer Science
Natural Language Processing
Language Modeling
Autoregressive Models
Diffusion Models
Any-order Generation
Groupwise Prediction
Progressive Training
Dynamic Resampling
A3
Diffusion language models enable any-order generation and bidirectional conditioning, offering appealing flexibility for tasks such as infilling, rewriting, and self-correction. However, their formulation-predicting one part of a sequence from another within a single-step dependency-limits modeling depth and often yields lower sample quality and stability than autoregressive (AR) models. To address this, we revisit autoregressive modeling as a foundation and reformulate diffusion-style training into a structured multi-group prediction process. We propose Any-order Any-subset Autoregressive modeling (A3), a generalized framework that extends the standard AR factorization to arbitrary token groups and generation orders. A3 preserves the probabilistic rigor and multi-layer dependency modeling of AR while inheriting diffusion models' flexibility for parallel and bidirectional g

---

## 01-22-2026 (33/1991 papers)


96
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Diffusion In Diffusion: Reclaiming Global Coherence in Semi-Autoregressive Diffusion

Linrui Ma, Yufei Cui, Kai Han, Yunhe Wang

ArXiv 2026 (Submitted on January 21)
thumb_up_alt
1
visibility
13
format_quote
0
category
category
Computer Science
Machine Learning
Natural Language Processing
Diffusion Models
Block Diffusion
Structural Block Diffusion
Autoregressive Models
OpenWebText Dataset
One of the most compelling features of global discrete diffusion language models is their global bidirectional contextual capability. However, existing block-based diffusion studies tend to introduce autoregressive priors, which, while offering benefits, can cause models to lose this global coherence at the macro level. To regain global contextual understanding while preserving the advantages of the semi-autoregressive paradigm, we propose Diffusion in Diffusion, a 'draft-then-refine' framework designed to overcome the irreversibility and myopia problems inherent in block diffusion models. Our approach first employs block diffusion to generate rapid drafts using small blocks, then refines these drafts through global bidirectional diffusion with a larger bidirectional receptive field. We utilize snapshot confidence remasking to identify the most critical tokens that require modification, and apply mix-scale training to expand the block diffusion model's global capabilities. Empirical results demonstrate that our approach sets a new benchmark for discrete diffusion models on the OpenWebText dataset. Using only 26% of the fine-tuning budget of baseline models, we reduce generative perplexity from 25.7 to 21.9, significantly narrowing the performance gap with autoregressive models.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
96
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Top 10 Open Challenges Steering the Future of Diffusion Language Model and Its Variants

Yunhe Wang, Kai Han, Huiling Zhen, Yuchuan Tian, Hanting Chen, ... Dacheng Tao

ArXiv 2026 (Submitted on January 20)
thumb_up_alt
11
visibility
28
format_quote
0
category
category
Computer Science
Artificial Intelligence
Natural Language Processing
Diffusion Models
Transformers
Auto-Regressive Models
Multimodal Intelligence
Deep Research Agents
The paradigm of Large Language Models (LLMs) is currently defined by auto-regressive (AR) architectures, which generate text through a sequential ``brick-by-brick'' process. Despite their success, AR models are inherently constrained by a causal bottleneck that limits global structural foresight and iterative refinement. Diffusion Language Models (DLMs) offer a transformative alternative, conceptualizing text generation as a holistic, bidirectional denoising process akin to a sculptor refining a masterpiece. However, the potential of DLMs remains largely untapped as the

---

## 01-23-2026 (18/1200 papers)


95
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Parallelism and Generation Order in Masked Diffusion Language Models: Limits Today, Potential Tomorrow

Yangyang Zhong, Yanmei Gu, Zhengqing Zang, Xiaomeng Li, Yuqi Ding, ... Junbo Zhao

ArXiv 2026 (Submitted on January 22)
thumb_up_alt
1
visibility
13
format_quote
0
category
category
Computer Science
Machine Learning
Graph Neural Networks
Graph Neural Networks (GNN)
Layer-wise Normalization
Dynamic Aggregation
Scalability
OGB Benchmarks
Masked Diffusion Language Models (MDLMs) promise parallel token generation and arbitrary-order decoding, yet it remains unclear to what extent current models truly realize these capabilities. We characterize MDLM behavior along two dimensions -- parallelism strength and generation order -- using Average Finalization Parallelism (AFP) and Kendall's tau. We evaluate eight mainstream MDLMs (up to 100B parameters) on 58 benchmarks spanning knowledge, reasoning, and programming. The results show that MDLMs still lag behind comparably sized autoregressive models, mainly because parallel probabilistic modeling weakens inter-token dependencies. Meanwhile, MDLMs exhibit adaptive decoding behavior: their parallelism and generation order vary significantly with the task domain, the stage of reasoning, and whether the output is correct. On tasks that require "backward information" (e.g., Sudoku), MDLMs adopt a solution order that tends to fill easier Sudoku blanks first, highlighting their advantages. Finally, we provide theoretical motivation and design insights supporting a Generate-then-Edit paradigm, which mitigates dependency loss while retaining the efficiency of parallel decoding.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
93
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Scaling Text-to-Image Diffusion Transformers with Representation Autoencoders

Shengbang Tong, Boyang Zheng, Ziteng Wang, Bingda Tang, Nanye Ma, ... Saining Xie

ArXiv 2026 (Submitted on January 22)
thumb_up_alt
45
visibility
159
format_quote
0
category
category
Computer Science
Machine Learning
Computer Vision
Text-to-Image Generation
Context-Aware Attention
Cross-Entropy Loss
ImageNet
COCO
Representation Autoencoders (RAEs)
Context-Aware Attention
Transformer
Representation Autoencoders (RAEs) have shown distinct advantages in diffusion modeling on ImageNet by training in high-dimensional semantic latent spaces. In this work, we investigate whether this framework can scale to large-scale, freeform text-to-image (T2I) generation. We first scale RAE decoders on the frozen representation encoder (SigLIP-2) beyond ImageNet by training on web, synthetic, and text-rendering data, finding that while scale improves general fidelity, targeted data composition is essential for specific domains like text. We then rigorously stress-test the RAE design choices 

---

## 01-24-2026 (11/1291 papers)


97
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Towards Latent Diffusion Suitable For Text

Nesta Midavaine, Christian A. Naesseth, Grigory Bartosh

ArXiv 2026 (Submitted on January 7)
thumb_up_alt
6
visibility
67
format_quote
0
category
category
Computer Science
Machine Learning
Language Modeling
Diffusion Models
Neural Flow Diffusion Models
Unconditional Generation
ROCstories Dataset
NFDM
Language diffusion models aim to improve sampling speed and coherence over autoregressive LLMs. We introduce Neural Flow Diffusion Models for language generation, an extension of NFDM that enables the straightforward application of continuous diffusion models to discrete state spaces. NFDM learns a multivariate forward process from the data, ensuring that the forward process and generative trajectory are a good fit for language modeling. Our model substantially reduces the likelihood gap with autoregressive models of the same size, while achieving sample quality comparable to that of previous latent diffusion models.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
93
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Auto-Regressive Masked Diffusion Models

Mahdi Karami, Ali Ghodsi

ArXiv 2026 (Submitted on January 23)
thumb_up_alt
8
visibility
47
format_quote
0
category
category
Computer Science
Machine Learning
Natural Language Processing
Language Modeling
Autoregressive Models
Diffusion Models
Parallel Generation
Causal Attention
Strided Parallel Generation
Masked diffusion models (MDMs) have emerged as a promising approach for language modeling, yet they face a performance gap compared to autoregressive models (ARMs) and require more training iterations. In this work, we present the Auto-Regressive Masked Diffusion (ARMD) model, an architecture designed to close this gap by unifying the training efficiency of autoregressive models with the parallel generation capabilities of diffusion-based models. Our key insight is to reframe the masked diffusion process as a block-wise causal model. This perspective allows us to design a strictly causal, permutation-equivariant architecture that computes all conditional probabilities across multiple denoising steps in a single, parallel forward pass. The resulting architecture supports efficient, autoregressive-style decoding and a progressive permutation training scheme, allowing the model to learn both canonical left-to-right and random token orderings. Leveraging this flexibility, we introduce a novel strided parallel generation strategy that accelerates inference by generating tokens in parallel streams while maintaining global coherence. Empirical results demonstrate that ARMD achieves state-of-the-art performance on standard language modeling benchmarks, outperforming established diffusion baselines while requiring significantly fewer training steps. Furthermore, it est

---

## 01-25-2026 (11/1291 papers)


97
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Towards Latent Diffusion Suitable For Text

Nesta Midavaine, Christian A. Naesseth, Grigory Bartosh

ArXiv 2026 (Submitted on January 7)
thumb_up_alt
6
visibility
67
format_quote
0
category
category
Computer Science
Machine Learning
Language Modeling
Diffusion Models
Neural Flow Diffusion Models
Unconditional Generation
ROCstories Dataset
NFDM
Language diffusion models aim to improve sampling speed and coherence over autoregressive LLMs. We introduce Neural Flow Diffusion Models for language generation, an extension of NFDM that enables the straightforward application of continuous diffusion models to discrete state spaces. NFDM learns a multivariate forward process from the data, ensuring that the forward process and generative trajectory are a good fit for language modeling. Our model substantially reduces the likelihood gap with autoregressive models of the same size, while achieving sample quality comparable to that of previous latent diffusion models.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
93
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Auto-Regressive Masked Diffusion Models

Mahdi Karami, Ali Ghodsi

ArXiv 2026 (Submitted on January 23)
thumb_up_alt
8
visibility
47
format_quote
0
category
category
Computer Science
Machine Learning
Natural Language Processing
Language Modeling
Autoregressive Models
Diffusion Models
Parallel Generation
Causal Attention
Strided Parallel Generation
Masked diffusion models (MDMs) have emerged as a promising approach for language modeling, yet they face a performance gap compared to autoregressive models (ARMs) and require more training iterations. In this work, we present the Auto-Regressive Masked Diffusion (ARMD) model, an architecture designed to close this gap by unifying the training efficiency of autoregressive models with the parallel generation capabilities of diffusion-based models. Our key insight is to reframe the masked diffusion process as a block-wise causal model. This perspective allows us to design a strictly causal, permutation-equivariant architecture that computes all conditional probabilities across multiple denoising steps in a single, parallel forward pass. The resulting architecture supports efficient, autoregressive-style decoding and a progressive permutation training scheme, allowing the model to learn both canonical left-to-right and random token orderings. Leveraging this flexibility, we introduce a novel strided parallel generation strategy that accelerates inference by generating tokens in parallel streams while maintaining global coherence. Empirical results demonstrate that ARMD achieves state-of-the-art performance on standard language modeling benchmarks, outperforming established diffusion baselines while requiring significantly fewer training steps. Furthermore, it est

---

## 01-26-2026 (11/1291 papers)


97
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Towards Latent Diffusion Suitable For Text

Nesta Midavaine, Christian A. Naesseth, Grigory Bartosh

ArXiv 2026 (Submitted on January 7)
thumb_up_alt
6
visibility
67
format_quote
0
category
category
Computer Science
Machine Learning
Language Modeling
Diffusion Models
Neural Flow Diffusion Models
Unconditional Generation
ROCstories Dataset
NFDM
Language diffusion models aim to improve sampling speed and coherence over autoregressive LLMs. We introduce Neural Flow Diffusion Models for language generation, an extension of NFDM that enables the straightforward application of continuous diffusion models to discrete state spaces. NFDM learns a multivariate forward process from the data, ensuring that the forward process and generative trajectory are a good fit for language modeling. Our model substantially reduces the likelihood gap with autoregressive models of the same size, while achieving sample quality comparable to that of previous latent diffusion models.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
93
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Auto-Regressive Masked Diffusion Models

Mahdi Karami, Ali Ghodsi

ArXiv 2026 (Submitted on January 23)
thumb_up_alt
8
visibility
47
format_quote
0
category
category
Computer Science
Machine Learning
Natural Language Processing
Language Modeling
Autoregressive Models
Diffusion Models
Parallel Generation
Causal Attention
Strided Parallel Generation
Masked diffusion models (MDMs) have emerged as a promising approach for language modeling, yet they face a performance gap compared to autoregressive models (ARMs) and require more training iterations. In this work, we present the Auto-Regressive Masked Diffusion (ARMD) model, an architecture designed to close this gap by unifying the training efficiency of autoregressive models with the parallel generation capabilities of diffusion-based models. Our key insight is to reframe the masked diffusion process as a block-wise causal model. This perspective allows us to design a strictly causal, permutation-equivariant architecture that computes all conditional probabilities across multiple denoising steps in a single, parallel forward pass. The resulting architecture supports efficient, autoregressive-style decoding and a progressive permutation training scheme, allowing the model to learn both canonical left-to-right and random token orderings. Leveraging this flexibility, we introduce a novel strided parallel generation strategy that accelerates inference by generating tokens in parallel streams while maintaining global coherence. Empirical results demonstrate that ARMD achieves state-of-the-art performance on standard language modeling benchmarks, outperforming established diffusion baselines while requiring significantly fewer training steps. Furthermore, it est

---

## 01-27-2026 (38/1974 papers)


99
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
treaming-dLLM: Accelerating Diffusion LLMs via Suffix Pruning and Dynamic Decoding

Zhongyu Xiao, Zhiwei Hao, Jianyuan Guo, Yong Luo, Jia Liu, ... Han Hu

ArXiv 2026 (Submitted on January 25)
thumb_up_alt
1
visibility
11
format_quote
0
category
category
Computer Science
Artificial Intelligence
Natural Language Processing
Diffusion Models
Parallel Decoding
Suffix Pruning
Dynamic Decoding
Confidence Thresholds
Block-wise Diffusion
Streaming-dLLM
Diffusion Large Language Models (dLLMs) offer a compelling paradigm for natural language generation, leveraging parallel decoding and bidirectional attention to achieve superior global coherence compared to autoregressive models. While recent works have accelerated inference via KV cache reuse or heuristic decoding, they overlook the intrinsic inefficiencies within the block-wise diffusion process. Specifically, they suffer from spatial redundancy by modeling informative-sparse suffix regions uniformly and temporal inefficiency by applying fixed denoising schedules across all the decoding process. To address this, we propose Streaming-dLLM, a training-free framework that streamlines inference across both spatial and temporal dimensions. Spatially, we introduce attenuation guided suffix modeling to approximate the full context by pruning redundant mask tokens. Temporally, we employ a dynamic confidence aware strategy with an early exit mechanism, allowing the model to skip unnecessary iterations for converged tokens. Extensive experiments show that Streaming-dLLM achieves up to 68.2X speedup while maintaining generation quality, highlighting its effectiveness in diffusion decoding. The code is available at https://github.com/xiaoshideta/Streaming-dLLM.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
Project Page
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
97
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
VidLaDA: Bidirectional Diffusion Large Language Models for Efficient Video Understanding

Zhihao He, Tieyuan Chen, Kangyu Wang, Ziran Qin, Yang Shao, ... Weiyao Lin

ArXiv 2026 (Submitted on January 25)
thumb_up_alt
1
visibility
40
format_quote
0
category
category
Computer Science
Artificial Intelligence
Video Understanding
Video Large Language Models
Diffusion Language Models
Bidirectional Attention
MARS-Cache
Spatiotemporal Reasoning
Standard Autoregressive Video LLMs inevitably suffer from causal masking biases that hinder global spatiotemporal modeling, leading to suboptimal understanding efficiency. We propose VidLaDA, a Video LLM based on Diffusion Language Model utilizing bidirectional attention to capture bidirectional dependencies. To further tackle the inference bottleneck of diffusion decoding on massive video tokens, we introduce MARS-Cache. This framework accelerates inference by combining asynchronous visual cache refreshing with frame-wise c

---

## 01-28-2026 (18/1390 papers)


97
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
One Token Is Enough: Improving Diffusion Language Models with a Sink Token

Zihou Zhang, Zheyong Xie, Li Zhong, Haifeng Liu, Shaosheng Cao

ArXiv 2026 (Submitted on January 27)
thumb_up_alt
7
visibility
35
format_quote
0
g_translate
Language
category
Computer Science
Natural Language Processing
Diffusion Models
Diffusion Language Models (DLMs)
Attention Mechanism
Sink Token
Stability
Position-Stable Token
Diffusion Language Models (DLMs) have emerged as a compelling alternative to autoregressive approaches, enabling parallel text generation with competitive performance. Despite these advantages, there is a critical instability in DLMs: the moving sink phenomenon. Our analysis indicates that sink tokens exhibit low-norm representations in the Transformer's value space, and that the moving sink phenomenon serves as a protective mechanism in DLMs to prevent excessive information mixing. However, their unpredictable positions across diffusion steps undermine inference robustness. To resolve this, we propose a simple but effective extra sink token implemented via a modified attention mask. Specifically, we introduce a special token constrained to attend solely to itself, while remaining globally visible to all other tokens. Experimental results demonstrate that introducing a single extra token stabilizes attention sinks, substantially improving model performance. Crucially, further analysis confirms that the effectiveness of this token is independent of its position and characterized by negligible semantic content, validating its role as a robust and dedicated structural sink.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
94
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference

Fuliang Liu, Xue Li, Ketai Zhao, Yinxi Gao, Ziyan Zhou, ... Chen Tian

ArXiv 2026 (Submitted on January 27)
thumb_up_alt
5
visibility
18
format_quote
0
g_translate
Language
category
Computer Science
Artificial Intelligence
Speculative Decoding
Speculative Decoding
Diffusion Models
Parallel Generation
Tree Pruning
N-gram
Autoregressive Models
DART
Speculative decoding is an effective and lossless approach for accelerating LLM inference. However, existing widely adopted model-based draft designs, such as EAGLE3, improve accuracy at the cost of multi-step autoregressive inference, resulting in high drafting latency and ultimately rendering the drafting stage itself a performance bottleneck. Inspired by diffusion-based large language models (dLLMs), we propose DART, which leverages parallel generation to reduce drafting latency. DART predicts logits for multiple future masked positions in parallel within a single forward pass based on hidden states of the target model, thereby eliminating autoregressive rollouts in the dra

---

## 01-29-2026 (33/1109 papers)


99
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Improving Diffusion Language Model Decoding through Joint Search in Generation Order and Token Space

Yangyi Shen, Tianjian Feng, Jiaqi Han, Wen Wang, Tianlang Chen, ... Stefano Ermon

ArXiv 2026 (Submitted on January 28)
thumb_up_alt
3
visibility
28
format_quote
0
g_translate
Language
category
Computer Science
Artificial Intelligence
Diffusion Models
Diffusion Language Models
Order-Token Search
Likelihood Estimation
Joint Search
Reasoning Accuracy
Diffusion Language Models (DLMs) offer order-agnostic generation that can explore many possible decoding trajectories. However, current decoding methods commit to a single trajectory, limiting exploration in trajectory space. We introduce Order-Token Search to explore this space through jointly searching over generation order and token values. Its core is a likelihood estimator that scores denoising actions, enabling stable pruning and efficient exploration of diverse trajectories. Across mathematical reasoning and coding benchmarks, Order-Token Search consistently outperforms baselines on GSM8K, MATH500, Countdown, and HumanEval (3.1%, 3.8%, 7.9%, and 6.8% absolute over backbone), matching or surpassing diffu-GRPO post-trained d1-LLaDA. Our work establishes joint search as a key component for advancing decoding in DLMs.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
99
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Window-Diffusion: Accelerating Diffusion Language Model Inference with Windowed Token Pruning and Caching

Fengrui Zuo, Zhiwei Ke, Yiming Liu, Wenqi Lou, Chao Wang, Xvehai Zhou

ArXiv 2026 (Submitted on January 28)
thumb_up_alt
1
visibility
13
format_quote
0
hub
Machine Learning
category
Computer Science
Machine Learning
Diffusion Models
Diffusion Language Models
Token Pruning
Caching
Windowed Inference
Dual-Window Mechanism
KV Cache
Adaptive-Length Inference
Diffusion language models (DLMs) generate text through iterative denoising, but inference requires full-sequence attention at every iteration, resulting in substantial redundant computation on masked tokens. Block-wise diffusion can reduce this cost, yet it typically relies on retraining and constrained update orders, limiting its direct applicability to pretrained DLMs. Our token-level analysis reveals pronounced structural locality in DLM inference. Decoding is driven by a small set of prefix-localized active tokens; the influence of distant undecoded context diminishes rapidly, and decoded tokens exhibit stage-wise temporal stability, enabling reuse of intermediate representations except for a brief post-decode transient. Motivated by these observations, we propose \placeholder\footnote{The source code is available at <a href='https://github.com/vhicrgit/Window-Diffusion' target='_blank'>https://github.com/vhicrgit/Window-Diffusion.}, a

---

## 01-30-2026 (62/1491 papers)


98
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Causal Autoregressive Diffusion Language Model

Junhao Ruan, Bei Li, Yongjing Yin, Pengcheng Huang, Xin Chen, ... JingBo Zhu

ArXiv 2026 (Submitted on January 29)
thumb_up_alt
2
visibility
15
format_quote
0
g_translate
Language
category
Computer Science
Natural Language Processing
Language Modeling
Language Modeling
Causal Diffusion
Parallel Generation
Autoregressive Models
Discrete Diffusion
CARD
In this work, we propose Causal Autoregressive Diffusion (CARD), a novel framework that unifies the training efficiency of ARMs with the high-throughput inference of diffusion models. CARD reformulates the diffusion process within a strictly causal attention mask, enabling dense, per-token supervision in a single forward pass. To address the optimization instability of causal diffusion, we introduce a soft-tailed masking schema to preserve local context and a context-aware reweighting mechanism derived from signal-to-noise principles. This design enables dynamic parallel decoding, where the model leverages KV-caching to adaptively generate variable-length token sequences based on confidence. Empirically, CARD outperforms existing discrete diffusion baselines while reducing training latency by 3 × compared to block diffusion methods. Our results demonstrate that CARD achieves ARM-level data efficiency while unlocking the latency benefits of parallel generation, establishing a robust paradigm for next-generation efficient LLMs.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
93
Relevance
thumb_up_alt
thumb_down_off_alt
Like/Dislike
Thinking Out of Order: When Output Order Stops Reflecting Reasoning Order in Diffusion Language Models

Longxuan Yu, Yu Fu, Shaorong Zhang, Hui Liu, Mukund Varma T, ... Yue Dong

ArXiv 2026 (Submitted on January 29)
thumb_up_alt
6
visibility
9
format_quote
0
g_translate
Language
category
Computer Science
Artificial Intelligence
Natural Language Processing
Diffusion Models
Order Robustness
Confidence-Based Remasking
Autoregressive Models
Reasoning Order
Autoregressive (AR) language models enforce a fixed left-to-right generation order, creating a fundamental limitation when the required output structure conflicts with natural reasoning (e.g., producing answers before explanations due to presentation or schema constraints). In such cases, AR models must commit to answers before generating intermediate reasoning, and this rigid constraint forces premature commitment. Masked diffusion language models (MDLMs), which iteratively refine all tokens in parallel, offer a way to decouple computation order from output structure. We validate this capability on GSM8K, Math500, and ReasonOrderQA, a benchmark we introduce with controlled difficulty and order-level evaluation. When prompts request answers before reasoning, AR models exhibit large accuracy gaps 

---

## 01-31-2026 (49/1602 papers)


99
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
Relaxing Positional Alignment in Masked Diffusion Language Models

Mengyu Ye, Ryosuke Takahashi, Keito Kudo, Jun Suzuki

ArXiv 2026 (Submitted on January 30)
thumb_up_alt
2
visibility
13
format_quote
0
g_translate
Language
category
Computer Science
Natural Language Processing
Masked Diffusion Language Models
Masked Diffusion Language Models (MDLM)
Alignment Flexibility
Positional Misalignment
CTC
Open-Ended Generation
Masked diffusion language models (MDLMs) have emerged as a promising alternative to dominant autoregressive approaches. Although they achieve competitive performance on several tasks, a substantial gap remains in open-ended text generation. We hypothesize that one cause of this gap is that strict positional prediction makes MDLM decoding highly sensitive to token misalignment, and we show through controlled interventions that a one-position shift can severely disrupt semantics. This observation suggests that enforcing strict positional supervision during training is misaligned with the irreversible denoising dynamics of MDLM decoding. Motivated by this mismatch, we adopt an alignment-flexible supervision strategy during fine-tuning. Specifically, we introduce a special token <slack> via the connectionist temporal classification objective. We apply this approach to the widely used MDLM model and conduct experiments on five open-ended text generation benchmarks. Our method consistently outperforms the original model and improves robustness to positional shifts, indicating that relaxing strict positional supervision is an important factor in improving generation quality in MDLMs.
Details
bookmark_add
Bookmark
Collections
arXiv
picture_as_pdf
PDF
html
HTML
Share
lightbulb
AI Summary
backup_table
Figures & Tables
Scholar Maps
ads_click
Similar Papers
98
Relevance
thumb_up_off_alt
thumb_down_off_alt
Like/Dislike
FOCUS: DLLMs Know How to Tame Their Compute Bound

Kaihua Liang, Xin Tan, An Zhong, Hong Xu, Marco Canini

ArXiv 2026 (Submitted on January 30)
thumb_up_alt
2
visibility
17
format_quote
0
hub
Machine Learning
category
Computer Science
Artificial Intelligence
Natural Language Processing
Diffusion Models
Token Eviction
Block-Diffusion
FOCUS
Attention Importance
Inference Efficiency
Diffusion Large Language Models (DLLMs) offer a compelling alternative to Auto-Regressive models, but their deployment is constrained by high decoding cost. In this work, we identify a key inefficiency in DLLM decoding: while computation is parallelized over token blocks, only a small subset of tokens is decodable at each diffusion step, causing most compute to be wasted on non-decodable tokens. We further observe a strong correlation between attention-derived token importance and token-wise decoding probability. Based on this insight, we propose FOCUS -- an inference system designed for DLLMs. By dynamically focusing computation on decodable tokens and evicting non-decodable ones on-the-fly, 

---

