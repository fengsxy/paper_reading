---
layout: default
title: "MCS Locks"
description: "可扩展自旋锁"
parent: CS 202 论文解读
nav_order: 11
---

# MCS Locks：让每个线程在自家门口等，别都挤在一把锁上

> 论文: *Algorithms for Scalable Synchronization on Shared-Memory Multiprocessors* (Mellor-Crummey & Scott, ACM TOCS 1991)

## 1. 背景与动机

在多处理器系统中，互斥锁（mutual exclusion lock）是最基本的同步原语。当多个线程需要访问共享资源时，锁保证同一时刻只有一个线程能进入临界区。然而，锁的实现方式对多处理器系统的性能有着巨大影响。

1991 年，主流的自旋锁（spinlock）实现主要有两种：

**Test-and-Set (TAS) Lock**：线程反复执行原子的 test-and-set 指令尝试获取锁。如果锁被占用，线程在一个紧密循环中不断重试。问题在于：每次 test-and-set 都是一个原子的读-修改-写操作，会在总线上产生一次独占访问。当 N 个线程同时自旋时，总线上每秒会产生 O(N) 次原子操作，总线带宽被自旋流量淹没，连持有锁的线程的正常内存访问都会被拖慢。

**Test-and-Test-and-Set (TTAS) Lock**：改进版本——线程先用普通的 load 指令检查锁的状态（test），只有当锁看起来空闲时才执行 test-and-set（test-and-set）。这减少了总线上的原子操作次数，因为普通 load 可以命中本地缓存。但问题是：当锁被释放时，所有等待线程的缓存行同时被 invalidate，它们几乎同时发起 test-and-set，产生一次"惊群效应"（thundering herd），瞬间的总线风暴仍然很严重。

这两种锁的根本问题在于：**所有线程都在同一个共享变量上自旋**。无论是 TAS 还是 TTAS，锁变量只有一个，所有线程的自旋操作都指向同一个内存地址。这导致了两个后果：

1. **缓存一致性流量（Cache Coherence Traffic）**：锁变量的每次修改都会触发所有持有该缓存行副本的处理器的 invalidation，产生 O(N) 的一致性消息。
2. **无公平性保证**：锁释放后，哪个线程能抢到锁完全取决于硬件仲裁，可能导致某些线程长期饥饿。

Mellor-Crummey 和 Scott 的核心洞察是：**如果每个线程在自己的本地变量上自旋，而不是在共享的锁变量上自旋，就可以同时解决性能和公平性问题**。

## 2. 核心设计与关键创新

### 2.1 MCS Lock 的基本思想

MCS lock 使用一个显式的链表队列来组织等待线程。每个线程拥有一个本地的队列节点（qnode），包含一个 `locked` 标志位和一个 `next` 指针。锁本身只是一个指向队列尾部的指针（tail）。

**获取锁（Lock）**：
1. 线程分配一个本地 qnode，设置 `locked = true`（表示"我在等待"）。
2. 使用原子的 `fetch-and-store`（或 `swap`）操作将自己的 qnode 挂到队列尾部，同时获取前驱节点的指针。
3. 如果前驱为 NULL，说明队列为空，直接获得锁。
4. 否则，将前驱的 `next` 指针指向自己，然后在自己的 `locked` 标志上自旋等待。

**释放锁（Unlock）**：
1. 检查自己的 `next` 指针。如果有后继节点，将后继的 `locked` 设为 false，唤醒它。
2. 如果没有后继节点，使用 `compare-and-swap` 尝试将 tail 设为 NULL。如果成功，说明确实没有其他线程在等待。如果失败，说明有新线程正在加入队列，短暂自旋等待其完成链接，然后唤醒它。

### 2.2 关键创新点

**Local Spinning（本地自旋）**：每个线程只在自己的 qnode 的 `locked` 字段上自旋。当前驱释放锁时，只需修改后继的 `locked` 字段，只会 invalidate 一个处理器的缓存行。这将锁释放时的缓存一致性流量从 O(N) 降低到 O(1)。

**FIFO 公平性**：线程按照到达顺序排列在队列中，严格按 FIFO 顺序获得锁。不存在饥饿问题。

**空间效率**：每个线程只需要一个 qnode（通常可以在栈上分配），锁本身只需要一个指针。总空间开销为 O(L + N)，其中 L 是锁的数量，N 是线程数量。

## 3. 重要技术细节

### 3.1 原子操作的选择

MCS lock 的实现依赖两个原子操作：

- **fetch-and-store（swap）**：用于将新节点原子地挂到队列尾部。这个操作在大多数架构上都有高效的硬件支持。
- **compare-and-swap（CAS）**：仅在 unlock 路径中使用，用于处理"队列可能为空"的边界情况。

值得注意的是，论文还提出了一种只需要 fetch-and-store 的变体（不需要 CAS），通过在 unlock 时短暂自旋等待后继节点完成链接来避免 CAS。这对于不支持 CAS 的硬件架构很重要。

### 3.2 缓存行对齐

为了确保 local spinning 的效果，每个 qnode 必须位于独立的缓存行上。如果两个 qnode 共享同一缓存行（false sharing），一个 qnode 的修改会 invalidate 另一个 qnode 所在处理器的缓存，破坏 local spinning 的性能优势。论文强调了缓存行对齐的重要性。

### 3.3 NUMA 感知

在 NUMA（Non-Uniform Memory Access）架构中，访问本地内存比访问远程内存快得多。MCS lock 的 local spinning 特性天然适合 NUMA：每个线程在本地分配的 qnode 上自旋，自旋操作只访问本地内存。但队列的链接操作（设置前驱的 next 指针）可能涉及远程内存访问。后续的 NUMA-aware 锁（如 HCLH lock）进一步优化了这一点。

### 3.4 与其他队列锁的比较

论文同时提出并比较了多种锁算法：

- **Anderson's Array-based Lock**：使用一个数组实现队列，每个线程在数组的不同槽位上自旋。也实现了 local spinning，但空间开销为 O(L × N)（每把锁需要一个 N 元素的数组），在锁数量多时不可接受。
- **CLH Lock**（Craig, Landin, Hagersten）：另一种队列式自旋锁，线程在前驱的节点上自旋（而非自己的节点）。CLH lock 在某些架构上比 MCS lock 更简单，但在 NUMA 架构上不如 MCS，因为自旋发生在远程节点上。
- **Ticket Lock**：使用两个计数器（next_ticket 和 now_serving）实现 FIFO 顺序，但所有线程仍在同一个 now_serving 变量上自旋，不具备 local spinning 特性。

### 3.5 性能评估

论文在 BBN Butterfly（128 处理器）和 Sequent Symmetry（20 处理器）上进行了评估。关键发现：

- TAS lock 在处理器数增加时性能急剧下降，甚至出现超线性退化（性能比线性退化更差）。
- TTAS lock 比 TAS 好，但在锁释放时仍有明显的性能尖峰。
- MCS lock 和 Anderson lock 的性能随处理器数增加几乎保持平稳，展现了优秀的可扩展性。
- MCS lock 在空间效率上优于 Anderson lock，是综合最优的选择。

## 4. 优缺点分析

### 优点

- **可扩展性**：O(1) 的缓存一致性流量使得 MCS lock 在大量处理器上仍能保持良好性能。
- **公平性**：FIFO 顺序保证消除了饥饿问题，提供了确定性的等待时间。
- **空间效率**：O(L + N) 的空间开销，远优于 Anderson lock 的 O(L × N)。
- **适应性**：可以扩展支持 try-lock、超时、读写锁等高级功能。

### 缺点

- **无竞争时开销较高**：在没有竞争的情况下（只有一个线程访问锁），MCS lock 需要执行 fetch-and-store 和可能的 CAS，比简单的 TAS lock（一次原子操作即可）开销更大。
- **实现复杂度**：相比 TAS/TTAS 的几行代码，MCS lock 的实现涉及链表操作和多个原子操作，更容易出错。
- **需要额外存储**：每个线程需要为每个可能持有的锁分配一个 qnode，增加了内存管理的复杂性。
- **不适合短临界区**：如果临界区非常短（几条指令），MCS lock 的获取/释放开销可能超过临界区本身的执行时间。

## 5. 历史影响与后续发展

MCS lock 是并发编程领域最具影响力的算法之一，其影响持续至今。

**Linux 内核的采用**：Linux 内核从 4.2 版本开始，将其默认的 spinlock 实现从 ticket lock 替换为基于 MCS 的 qspinlock。这个决定的直接原因是 ticket lock 在大型 NUMA 系统上的性能问题——所有线程在同一个变量上自旋导致的缓存一致性流量。qspinlock 在无竞争时退化为简单的 CAS 操作（快路径），在有竞争时使用 MCS 队列（慢路径），兼顾了两种场景。

**Java 的 AbstractQueuedSynchronizer (AQS)**：Java 并发库中的 AQS 框架（ReentrantLock、Semaphore 等的基础）使用了 CLH lock 的变体，而 CLH lock 与 MCS lock 是同一时期提出的姊妹算法。可以说，Java 中几乎所有的锁实现都受到了这篇论文的影响。

**NUMA-aware Locks**：MCS lock 启发了一系列 NUMA 感知的锁算法，如 HCLH lock（Hierarchical CLH）、Cohort Locks 等。这些算法在 MCS 的基础上进一步优化，让同一 NUMA 节点上的线程优先传递锁，减少跨节点的内存访问。

**Lock-free 和 Wait-free 算法**：MCS lock 展示了精心设计的原子操作可以构建高效的并发数据结构，这种思路推动了无锁（lock-free）和无等待（wait-free）算法的发展。

**硬件事务内存（HTM）**：现代处理器（如 Intel TSX）提供的硬件事务内存可以看作是对锁的硬件级替代。但在 HTM 事务失败时，系统通常会回退到传统锁，而 MCS lock 是常见的回退选择。

MCS lock 的持久价值在于它揭示了一个深刻的系统设计原则：**在共享内存系统中，减少共享才是提升性能的关键**。这个看似矛盾的洞察——在共享内存上减少共享——贯穿了从 MCS lock 到 RCU、从 per-CPU 数据结构到 Barrelfish multikernel 的整个系统设计演进。
