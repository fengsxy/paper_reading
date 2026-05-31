# Long-Horizon dLLM Agent Framework Design

> 基于 Mercury 2 + MiniMax M2.7 在 DeepPlanning 上的实验发现
> 2026-04-14

## 一、实验发现（5-Case Pilot）

### 1.1 Mercury 2 的关键行为特征

**Reasoning Effort = 隐藏 CoT 预算分配器**

| reasoning_effort | Reasoning Tokens | Completion Tokens | 用途 |
|---|---|---|---|
| `instant` | 0 | 484 | 快速响应，无内部推理 |
| `low` | 13 | 475 | 最小化推理 |
| `medium` | 76 | 412 | 标准平衡 |
| `high` | **489** | **0** | **全部转为内部推理，不输出** |

**关键发现**：`high` 模式把整个输出变成 hidden reasoning——这是 Mercury 独有的能力。

### 1.2 Speed vs Quality Trade-off

| 指标 | Mercury 2 | MiniMax M2.7 | 差异 |
|---|---|---|---|
| 总时间 (5 cases) | 222s | 2031s | **9.2x faster** |
| 平均 LLM call | 25 次 | 10 次 | Mercury 多 2.5x |
| Plan 长度 | 更短 (~3-6K chars) | 更长 (~4-8K chars) | MiniMax 详细 1.5x |
| LLM 评分的 plan 质量 | 45.0 avg | 62.8 avg | MiniMax 高 40% |
| Tool calls/LLM call | ~1.0 | ~4-6 | Mercury 更碎片化 |

**结论**：Mercury 选择了 "fast + many steps" 策略，MiniMax 选择了 "slow + detailed" 策略。

### 1.3 问题诊断

| 问题 | 表现 | 根因 |
|---|---|---|
| Rate Limit | 429 `input token limit exceeded` | Mercury 对长 context 输入有限流 |
| 碎片化 | Mercury 每 call 只做一个 action | denoising 收敛慢，每次置信度只够一个 action |
| 长任务失败 | id_119 Mercury 未完成 (0 chars plan) | 触达 max_calls，且每次 call 效率低 |
| Plan 质量 | Mercury 评分更低 | planning depth 不足，soft constraint 满足度低 |

---

## 二、Long-Horizon dLLM Agent 架构

### 2.1 核心洞察

dLLM 的三个独特能力，AR 模型没有：

1. **并行 denoising**：可以同时生成多个候选 action 序列
2. **迭代 refinement**：denoising 天然是多轮优化，不需要显式回溯
3. **Hidden reasoning** (`reasoning_effort=high`)：可以在不泄露 CoT 的情况下做深层规划

### 2.2 架构图

```
┌─────────────────────────────────────────────────────────────┐
│                    Long-Horizon dLLM Agent                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │   Context    │───▶│   Denoising  │───▶│   Action     │  │
│  │   Manager    │    │   Engine     │    │   Scheduler  │  │
│  │  (Selective  │    │  (Mercury)   │    │              │  │
│  │   Memory)    │    │              │    │              │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
│         ▲                   │                   │           │
│         │                   ▼                   ▼           │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │   Constraint │    │   Confidence │    │    Tool     │  │
│  │   Tracker    │◀───│   Estimator  │◀───│   Executor   │  │
│  │ (Hard/Soft)  │    │              │    │              │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
│                             ▲                              │
│                      ┌──────────────┐                      │
│                      │   Feedback   │                      │
│                      │   Loop       │                      │
│                      └──────────────┘                      │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 关键模块详解

#### Module 1: Adaptive Reasoning Effort Controller

```python
class ReasoningController:
    """
    动态控制 Mercury 的 reasoning_effort：
    - instant/low: 快速执行阶段（执行已确定的 action）
    - medium: 标准规划阶段（做下一步决策）
    - high: 深度规划阶段（不输出，在内部做完整规划）
    """
    
    def decide(self, state: AgentState) -> str:
        horizon = state.remaining_steps
        constraint_violations = state.constraint_tracker.violations()
        confidence = state.confidence_estimator.current()
        
        if horizon > 10 and constraint_violations == 0 and confidence > 0.8:
            return "high"      # 深度规划，隐藏 CoT
        elif horizon > 5 and confidence > 0.5:
            return "medium"    # 标准规划
        else:
            return "instant"   # 快速执行，不再犹豫
```

**关键创新**：用 `reasoning_effort` 作为 planning budget dial，不是靠 prompt engineering。

#### Module 2: Speculative Execution Scheduler

AR agent: 等 LLM 完全输出一个 action → 执行 → 等下一个
dLLM agent: 可以利用 denoising 的中间结果

```python
class SpeculativeScheduler:
    """
    在 denoising 过程中，提前执行已收敛的 action。
    
    Mercury denoising:
      Step 1: [Train? 0.3] [Hotel? 0.7] [Attraction? 0.2]
      Step 2: [Train? 0.6] [Hotel? 0.9] [Attraction? 0.5]
      Step 3: [Train? 0.95] [Hotel? 0.95] [Attraction? 0.85]
      
    Strategy: 当 Train 和 Hotel 置信度 > 0.9 时，
              立即并行执行这两个 action，不等 Attraction
    """
    
    def should_execute_early(self, action: str, confidence: float, 
                            other_confidences: dict) -> bool:
        # 执行条件：
        # 1. 单个 action 置信度 > threshold
        # 2. 不是 blocking action（不依赖其他未完成 action）
        # 3. 工具执行时间已知（可以 latency hiding）
        
        if confidence > 0.9 and not self.blocks_others(action):
            return True
        return False
```

**效果**：把串行的 38 步 Mercury call 压缩成 ~15-20 步并行执行。

#### Module 3: Selective Memory (替换全量 Context)

当前问题：每次 tool result 全加到 context → 429 rate limit

```python
class SelectiveMemory:
    """
    利用 Mercury 的 Gated DeltaNet 机制做 selective memory。
    不是 append-only context，而是选择性保留/遗忘。
    
    分类：
    - Working Memory: 当前 task 相关的 tool results（高 gating score）
    - Compressed Memory: 历史决策的摘要（低 gating score）
    - Discarded: 过期的中间状态
    """
    
    def process(self, tool_result: dict, gating_scores: dict) -> dict:
        # gating_scores 来自 Mercury 的内部注意力
        # 高分 = 需要保留，低分 = 可以压缩或丢弃
        
        relevant_parts = {
            k: v for k, v in tool_result.items() 
            if gating_scores.get(k, 0) > 0.7
        }
        
        compressed_summary = self.summarize(tool_result)
        
        return {
            "full": tool_result,      # 用于早期 denoising steps
            "compressed": compressed_summary,  # 用于后期 steps
            "gating": gating_scores   # 元数据
        }
```

#### Module 4: Hard/Soft Constraint Tracker

```python
class ConstraintTracker:
    """
    Hard constraints: 必须在 late denoising steps 满足
    Soft constraints: 可以在 early denoising steps 处理
    
    利用 Mercury denoising 的自然分层：
    - Early steps (t > 0.7): soft constraint 优化
    - Late steps (t < 0.3): hard constraint 强制执行
    """
    
    HARD = ["budget_cap", "time_feasibility", "transport_mode"]
    SOFT = ["hotel_star", "restaurant_type", "attraction_preference"]
    
    def check_at_denoising_step(self, action_plan: str, step_t: float) -> dict:
        # step_t: denoising 时间步 (0=纯噪声, 1=完全收敛)
        
        violations = {}
        
        if step_t < 0.3:  # Late denoising = hard constraint check
            for constraint in self.HARD:
                if not self.satisfies(action_plan, constraint):
                    violations[constraint] = "HARD_VIOLATION"
        
        elif step_t > 0.7:  # Early denoising = soft constraint hint
            for constraint in self.SOFT:
                if not self.satisfies(action_plan, constraint):
                    violations[constraint] = "SOFT_MISSED"
        
        return violations
```

#### Module 5: Error Recovery via Denoising Backtrack

AR agent 错误恢复：`action failed → retry same action`
dLLM agent 错误恢复：`confidence drop → revert to earlier denoising step`

```python
class ErrorRecovery:
    """
    Mercury 的迭代 refinement 允许"回退"到早期 denoising 步。
    不是重试同一个 action，而是从那个 point 重新生成。
    """
    
    def on_tool_failure(self, failed_action: str, denoising_step: int):
        # 记录失败的 denoising step
        self.failed_trajectories.append({
            "action": failed_action,
            "step": denoising_step,
            "context_snapshot": self.context_manager.snapshot()
        })
        
        # 回退到 step - 2，重新生成
        new_step = max(0, denoising_step - 2)
        return self.denoising_engine.refine_from(new_step)
```

---

## 三、改进效果预估

基于 5-case 实验数据：

| 改进项 | 当前 Mercury | 改进后预估 | 提升来源 |
|---|---|---|---|
| 执行时间 | 222s | ~100s | Speculative execution (并行化) |
| Plan 质量 | 45.0 | 55-65 | Reasoning effort + constraint tracking |
| Rate limit 触发 | 2次 | 0次 | Selective memory (context 压缩) |
| 长任务完成率 | 4/5 | 5/5 | Adaptive reasoning budget |

---

## 四、下一步实验计划

### Exp 1: Speculative Execution (2 周)
- 实现 SpeculativeScheduler
- 在 Mercury 上加 early execution 逻辑
- 测 speed/quality trade-off

### Exp 2: Selective Memory (2 周)
- 实现 SelectiveMemory 模块
- 对比 append-only context vs selective
- 测 rate limit 改善

### Exp 3: Adaptive reasoning_effort (1 周)
- 实现 ReasoningController
- 自动在 instant/medium/high 之间切换
- 对比 fixed vs adaptive

### Exp 4: Full 120-Case Evaluation (ongoing)
- 当前：5 分钟/case，约 10 小时跑完
- 用改进后的框架重跑，对比质量分数

---

## 五、开放问题

1. **Speculative execution 的正确性**：如何保证提前执行的 action 不需要被撤销？
2. **Selective memory 的压缩粒度**：多大程度上压缩 tool results 而不丢失关键信息？
3. **Hard/soft constraint 的自动分类**：能不能从 data 中自动学习这个分层，而不是手工指定？
4. **Multi-agent 版本**：多个 Mercury agent 并行，每个负责不同方面（交通/住宿/餐饮），最后合并？

---

*待更新：实验结果将持续追加到此文档*
