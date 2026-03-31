## Paper 6: Scheduler Activations — Effective Kernel Support for the User-Level Management of Parallelism (1991)

### Q1: Summary (300 words max)

This paper addresses the fundamental tension between user-level threads and kernel-level threads. User-level threads are fast (no kernel crossing for creation, switching, or synchronization) but suffer from a critical flaw: when one user thread blocks on I/O or a page fault, the kernel blocks the entire process because it is unaware of the user-level threads. Kernel threads avoid this problem but are slow due to system call overhead for every thread operation.

The authors propose scheduler activations as a communication mechanism between the kernel and the user-level thread scheduler. An activation serves as a vessel for running user-level threads—similar to a virtual processor. When a user thread blocks in the kernel, the kernel does not simply block the process. Instead, it creates a new activation and "upcalls" into the user-level scheduler, notifying it that one thread is blocked and providing a new activation to run another thread. When the blocked thread becomes runnable, another upcall informs the user-level scheduler. This gives the user-level scheduler complete information about kernel events while retaining full control over thread scheduling policy. The authors implemented scheduler activations in the Topaz kernel (DEC SRC) with the FastThreads user-level thread package and demonstrated performance comparable to pure user-level threads while correctly handling blocking operations.

### Q2: Scientific/Engineering Contributions

In 1991, the choice between user-level and kernel-level threads seemed like an unavoidable tradeoff. The paper's contributions were: (1) It precisely identified why user-level threads fail—the kernel's lack of information about user threads and the user scheduler's lack of information about kernel events—framing it as a communication problem rather than a fundamental limitation. (2) The upcall mechanism was a novel kernel-to-user communication abstraction that cleanly separated mechanism (kernel provides notifications) from policy (user scheduler decides what to run). (3) It influenced the design of modern thread implementations including Solaris's two-level threading model, Go's goroutine scheduler (M:N threading with "hand-off" on blocking), and Rust's async runtime designs.

### Q3: Limitations / What Could Be Wrong

(1) Upcalls violate the traditional layered abstraction—the kernel calling "up" into user space creates circular dependencies and complicates reasoning about correctness, especially during nested upcalls. (2) The implementation is complex: handling races between upcalls and user-level scheduling decisions requires careful synchronization. (3) Most mainstream OSes ultimately chose 1:1 threading (one kernel thread per user thread) rather than M:N models, because hardware improvements made kernel thread operations cheap enough (~microseconds) that the complexity of scheduler activations wasn't justified. Linux's NPTL adopted 1:1 threading in 2003. (4) The paper doesn't address priority inversion scenarios well—when the kernel preempts a user thread holding a user-level lock, the upcall to schedule another thread may pick one that needs that same lock. (5) Modern solutions like io_uring avoid blocking entirely via async I/O, sidestepping the problem rather than solving it.

### Q4: Additional Comments

The paper beautifully illustrates a systems design principle: when two layers need to cooperate, explicit communication beats workarounds. Go's goroutine scheduler is essentially scheduler activations reinvented—the Go runtime maintains M goroutines on N OS threads, and when a goroutine blocks on a syscall, the runtime "hands off" the OS thread and assigns remaining goroutines to other threads. The fact that M:N threading returned in Go and Rust (after being abandoned by Linux/Solaris) suggests the paper was right about the architecture but wrong about the timing—M:N only makes sense when you have thousands of concurrent tasks, which is common in modern server workloads but was rare in 1991.

---

## Paper 7: Efficient Memory Management for Large Language Model Serving with PagedAttention (vLLM, SOSP 2023)

### Q1: Summary (300 words max)

This paper addresses memory management inefficiency in serving large language models (LLMs). During autoregressive generation, each request maintains a KV cache storing key-value tensors for all previous tokens across all attention layers. Existing systems pre-allocate contiguous memory for each request's maximum possible sequence length, leading to severe internal fragmentation (allocated but unused memory within a request), external fragmentation (unusable gaps between allocations), and inability to share KV cache across requests that share common prefixes.

The authors propose PagedAttention, directly inspired by virtual memory paging in operating systems. Instead of requiring contiguous KV cache allocation, PagedAttention divides the KV cache into fixed-size blocks (analogous to pages) that can be stored non-contiguously in GPU memory. A block table (analogous to a page table) maps each request's logical KV cache positions to physical blocks. Blocks are allocated on-demand as new tokens are generated, eliminating internal fragmentation. A centralized block manager handles allocation and deallocation, eliminating external fragmentation. Furthermore, requests sharing common prefixes (e.g., system prompts) can share physical blocks via copy-on-write, similar to fork() in OS virtual memory. The system, vLLM, achieves 2-4× throughput improvement over state-of-the-art systems (FasterTransformer, Orca) by increasing the effective batch size through better memory utilization.

### Q2: Scientific/Engineering Contributions

Published in 2023 during the LLM serving boom, the contributions were impactful: (1) The key insight—applying OS virtual memory concepts to GPU KV cache management—was a powerful cross-domain transfer that solved a major practical bottleneck. (2) The paper quantified that existing systems waste 60-80% of KV cache memory due to fragmentation, establishing that memory management (not compute) was the primary throughput bottleneck. (3) PagedAttention's block-based design enabled prefix sharing via copy-on-write, which is critical for real-world deployments where many requests share system prompts. (4) vLLM became the dominant open-source LLM serving framework, demonstrating the paper's practical impact. The work showed that classic OS ideas remain highly relevant in new domains.

### Q3: Limitations / What Could Be Wrong

(1) PagedAttention introduces overhead from non-contiguous memory access patterns—GPU kernels are optimized for contiguous tensor operations, and the block table indirection adds latency per attention computation. (2) The fixed block size creates a granularity tradeoff: large blocks reduce table overhead but increase waste in the last block; small blocks increase table management cost. (3) The approach is specific to autoregressive generation with KV caches—diffusion-based language models, which don't use KV caches in the same way, require entirely different memory management strategies. (4) As model architectures evolve (e.g., multi-query attention, grouped-query attention, linear attention), the KV cache structure changes and PagedAttention must be adapted. (5) The paper focuses on single-GPU serving; distributed serving across multiple GPUs introduces additional complexity for block management and migration.

### Q4: Additional Comments

This paper is a textbook example of cross-pollination between systems domains. The analogy between OS virtual memory and GPU KV cache management is so natural that it's surprising no one formalized it earlier. It also highlights an ironic cycle: OS concepts (paging) → hardware concepts (GPU memory) → ML systems concepts (PagedAttention) → potentially back to OS concepts (managing linear attention states). For dLLM research specifically, vLLM's architecture doesn't directly apply because dLLMs don't use autoregressive KV caches—but the philosophy of "don't pre-allocate, page on demand" could inform how we manage the denoising state across diffusion steps.

---
