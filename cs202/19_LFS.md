---
layout: default
title: "LFS"
description: "Log-Structured File System"
parent: CS 202 论文解读
nav_order: 19
---

# The Design and Implementation of a Log-Structured File System (LFS)

**Rosenblum & Ousterhout, 1992**

---

## 1. 论文背景与动机

1990 年代初，计算机系统的硬件格局正在发生深刻变化：CPU 速度飞速提升，内存容量快速增长，但磁盘的机械寻道时间却几乎没有改善。这种不对称的发展趋势对文件系统设计产生了两个重要影响：

第一，**内存越来越大意味着读缓存越来越有效**。操作系统可以将大量磁盘数据缓存在内存中，使得大部分读操作可以直接从缓存命中，不需要访问磁盘。这意味着磁盘的工作负载将越来越以写操作为主。

第二，**磁盘的顺序写带宽远高于随机写性能**。一块典型的磁盘，顺序写带宽可以达到数 MB/s，但如果是随机小写（每次写都需要寻道），有效带宽可能降低到几十 KB/s——差距可达两个数量级。

然而，当时的文件系统（包括 FFS）在写操作时仍然需要多次随机写。创建一个新文件至少需要：写 inode、写目录项、写数据块、更新 inode bitmap、更新 data bitmap——这些写操作分散在磁盘的不同位置，每次都需要寻道。即使每个单独的写操作很小，寻道时间的累积也使得小文件的写性能极差。

Rosenblum 和 Ousterhout 提出了一个激进的问题：**能否设计一个文件系统，使得所有写操作都是顺序的？** 如果能做到这一点，就可以充分利用磁盘的顺序写带宽，将写性能提升一到两个数量级。

## 2. 核心设计与关键创新

LFS（Log-structured File System）的核心思想极其大胆：**将整个磁盘视为一个追加写的日志（log）**。所有的写操作——无论是数据块、inode、目录项还是元数据——都被缓冲在内存中，然后以一个大的连续写操作追加到日志的末尾。磁盘上不存在"固定位置"的数据结构（除了少数引导信息），一切都在日志中。

### Segment：写操作的基本单位

LFS 将磁盘划分为固定大小的 **segment**（通常为 512KB 或 1MB）。内存中的写缓冲区积累到足够填满一个 segment 时，才一次性将整个 segment 顺序写入磁盘。这确保了每次磁盘写操作都是大块的顺序写，充分利用磁盘带宽。

一个 segment 中可能包含多个文件的数据块、inode、目录项等各种数据，它们被紧密打包在一起。每个 segment 还包含一个 **segment summary block**，记录该 segment 中每个块属于哪个文件的哪个偏移位置，这个信息对于后续的 segment cleaning 至关重要。

### Inode Map：解决 inode 定位问题

在传统文件系统中，inode 存放在磁盘的固定位置，通过 inode 号可以直接计算出其磁盘地址。但在 LFS 中，inode 和其他数据一样被追加写到日志中，每次修改都会写到新的位置。那么，如何找到一个 inode 的最新版本？

LFS 引入了 **inode map**（imap）：一个从 inode 号到其当前磁盘地址的映射表。inode map 本身也被写入日志（作为日志的一部分追加写），但其最新位置通过一个固定位置的 **checkpoint region**（CR）来记录。

查找一个文件的流程变为：读 checkpoint region → 找到 inode map → 找到 inode → 找到数据块。看似多了一层间接，但由于 inode map 很小且经常被访问，它几乎总是在内存缓存中，所以额外开销可以忽略。

### Segment Cleaning：回收空间

这是 LFS 设计中最关键也最复杂的部分。由于所有写操作都是追加的，当一个文件被修改时，旧版本的数据块仍然留在日志中，占据着磁盘空间。随着时间推移，日志中会充满大量"死"数据（已被新版本覆盖的旧块）。系统需要一种机制来回收这些空间。

LFS 的解决方案是 **segment cleaning**（段清理）：

1. 选择一个或多个包含大量死数据的 segment。
2. 读取这些 segment，识别其中仍然存活的块（通过 segment summary 和 inode map 判断）。
3. 将存活的块复制到新的 segment 中（compact）。
4. 将旧 segment 标记为空闲，可以被重新使用。

Segment cleaning 的策略选择对性能影响巨大。论文提出了两种策略：

- **Cost-benefit policy**：综合考虑 segment 的空闲比例和年龄。优先清理那些空闲比例高（死数据多）且年龄大（不太可能很快再被修改）的 segment。
- **Greedy policy**：简单地选择空闲比例最高的 segment。

实验表明 cost-benefit policy 显著优于 greedy policy，因为它避免了反复清理那些频繁被修改的"热" segment。

## 3. 重要的技术细节

### Checkpoint 与 Crash Recovery

LFS 通过 **checkpoint** 机制保证崩溃一致性。系统周期性地（或在关机时）将所有内存中的状态写入磁盘，并更新 checkpoint region。Checkpoint region 包含 inode map 的位置、当前日志末尾的位置等关键信息。

崩溃恢复时，系统从最近的 checkpoint 开始，然后通过 **roll-forward** 扫描 checkpoint 之后的日志段，恢复 checkpoint 之后但崩溃之前已写入磁盘的数据。这比 FFS 的 fsck（需要扫描整个文件系统）快得多。

LFS 维护两个 checkpoint region，交替更新，确保即使在写 checkpoint 的过程中崩溃，至少有一个完整的 checkpoint 可用。

### 目录管理

目录在 LFS 中也是普通文件，其内容（目录项）也被追加写到日志中。当一个文件的 inode 被写到新位置时，不需要更新其父目录——因为目录中存储的是 inode 号而非 inode 的磁盘地址，而 inode 号是不变的。inode map 负责将不变的 inode 号映射到变化的磁盘地址。

### 写缓冲与批量写

LFS 在内存中维护一个写缓冲区，将多个小写操作合并成一个大的顺序写。这不仅提高了磁盘带宽利用率，还减少了 segment 中的碎片。缓冲区的大小需要权衡：太小则无法充分利用顺序写带宽，太大则增加崩溃时的数据丢失风险。

## 4. 优缺点分析

### 优点

1. **写性能卓越**：对于小文件的创建和写入，LFS 的性能比 FFS 高出一个数量级。这是因为所有写操作都被转化为顺序写，完全消除了寻道开销。

2. **崩溃恢复快速**：基于 checkpoint + roll-forward 的恢复机制比 fsck 快得多，恢复时间与崩溃前未 checkpoint 的数据量成正比，而非与文件系统总大小成正比。

3. **天然的版本历史**：由于旧数据不会被立即覆盖，LFS 天然支持快照（snapshot）和版本恢复功能（虽然论文没有深入讨论这一点）。

4. **设计思想的前瞻性**：LFS 的"追加写"思想预见了后来 SSD 和闪存存储的需求——闪存不支持原地覆写，必须先擦除再写入，LFS 的写模式天然适合闪存。

### 缺点

1. **Segment cleaning 的开销**：这是 LFS 最大的争议点。Cleaning 需要读取旧 segment、复制存活数据、写入新 segment，这些额外的 I/O 被称为 **write amplification**（写放大）。在磁盘接近满载时，cleaning 的开销可能非常大，严重影响性能。

2. **读性能可能下降**：在传统文件系统中，相关的数据块被放在物理上相近的位置（如 FFS 的 cylinder group 策略）。但在 LFS 中，文件的数据块可能分散在不同时间写入的不同 segment 中，导致顺序读变成随机读。

3. **Cleaning 策略的复杂性**：选择合适的 cleaning 策略是一个复杂的问题，不同的工作负载可能需要不同的策略。论文提出的 cost-benefit policy 在某些场景下表现良好，但并非万能。

4. **磁盘空间利用率的权衡**：为了保持 cleaning 的效率，LFS 需要保留一定比例的空闲空间。如果磁盘使用率过高，cleaning 的效率急剧下降。

## 5. 历史影响与后续发展

LFS 的影响远超文件系统领域本身。它提出的"将所有写操作转化为顺序追加"的思想，成为了计算机系统设计中一个反复出现的模式：

- **数据库领域**：LSM-tree（Log-Structured Merge-tree）直接借鉴了 LFS 的思想，将随机写转化为顺序写。LevelDB、RocksDB、Cassandra 等现代数据库和存储引擎都基于 LSM-tree。

- **闪存文件系统**：F2FS（Flash-Friendly File System）等专为闪存设计的文件系统大量借鉴了 LFS 的设计，因为闪存的擦除-写入特性天然适合日志结构。

- **分布式存储**：许多分布式存储系统（如 HDFS 的写入模式）也采用了追加写的设计。

- **SSD 内部**：现代 SSD 的 FTL（Flash Translation Layer）本质上就是一个日志结构的映射层，其垃圾回收（garbage collection）机制与 LFS 的 segment cleaning 高度相似。

LFS 论文也引发了学术界关于 "log-structured vs. update-in-place" 的长期辩论。Seltzer 等人在 1993 年的论文中指出，在某些工作负载下 LFS 的性能并不优于 FFS，主要原因就是 segment cleaning 的开销。这场辩论推动了对 cleaning 策略和混合设计的深入研究。

从操作系统课程的角度看，LFS 是理解"设计权衡"（design trade-off）的绝佳案例。它展示了一个看似简单优雅的核心思想（所有写都追加到日志）如何引出一系列复杂的工程挑战（cleaning、空间回收、读性能），以及如何通过精心的策略设计来应对这些挑战。LFS 教会我们：在系统设计中，优化一个维度（写性能）往往会在另一个维度（读性能、空间效率）引入新的代价，而好的设计就是在这些维度之间找到最佳的平衡点。
