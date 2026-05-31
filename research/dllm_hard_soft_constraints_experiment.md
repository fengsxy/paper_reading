# Hard/Soft Constraint Separation in dLLM Agents
## Experiment Design v1.0

> 基于 Mercury 2 在 DeepPlanning 上的 constraint satisfaction 分析
> 2026-04-14

---

## 1. Motivation

### 1.1 The Problem with AR Agents

Autoregressive (AR) large language models generate tokens sequentially, making all constraints compete equally in the same generation process. Hard constraints (budget caps, time feasibility) and soft constraints (hotel star rating, restaurant type preferences) are handled identically through prompt engineering—there is **no structural separation mechanism**.

This causes two failure modes:
- **Under-constraining**: Soft constraints get lost in long plans, never getting satisfied
- **Over-constraining**: Hard constraints get violated because the model doesn't know when to "lock in" critical requirements

### 1.2 The dLLM Opportunity

Diffusion language models (dLLM) generate tokens in parallel through iterative denoising. Each denoising step refines the entire response simultaneously. This creates a natural **temporal structure**:

```
Denoising Timeline:
  t=0.0 (pure noise):  No constraints satisfied
  t=0.3 (early):        Some constraints start converging
  t=0.5 (mid):          Most constraints visible
  t=0.7 (late):         Hard constraints finalized
  t=1.0 (converged):    All remaining constraints locked
```

**Core Hypothesis**: Hard constraints converge first (late denoising steps), while soft constraints are determined earlier (early denoising steps). This is an **emergent property** of the diffusion process, not explicitly programmed.

---

## 2. Definitions

### 2.1 Constraint Taxonomy (DeepPlanning)

We classify DeepPlanning constraints into two categories:

**Hard Constraints** (violation invalidates the entire plan):

| Constraint | Definition | Validation |
|---|---|---|
| `H_budget` | Total cost ≤ user-specified budget cap | `SUM(items) ≤ budget` |
| `H_time_feas` | All activities fit within specified dates | No time overlaps, return before deadline |
| `H_transport` | Transport mode matches user specification | `transport_type == requested` |
| `H_room_count` | Room count matches traveler count | `rooms ≥ ceil(travelers/2)` |
| `H_return_date` | Return trip planned for correct date | Departure/return dates match query |

**Soft Constraints** (preferences, plan still valid without them):

| Constraint | Definition | Validation |
|---|---|---|
| `S_hotel_star` | Hotel star rating ≥ requested | `star ≥ requested` |
| `S_hotel_amenity` | Specific amenity (pool, robot service, etc.) | `amenity in hotel.features` |
| `S_attraction` | Specific attractions included | `required_attraction in plan` |
| `S_restaurant` | Specific restaurant included | `required_restaurant in plan` |
| `S_dietary` | Dietary requirement (birthday set, etc.) | `dietary_request met` |

### 2.2 Constraint Satisfaction Timeline

For each tool call `i` in a trajectory, we compute:

```
H_score[i] = (# of hard constraints satisfied) / (total hard constraints)
S_score[i] = (# of soft constraints satisfied) / (total soft constraints)
```

This gives us a satisfaction curve over the trajectory:

```
Satisfaction
    |
1.0 |------------------------ final satisfaction level
    |                    ___--- soft constraints
    |              ___---
    |        ___---  ← hard constraints locked in earlier?
    |  ___---
0.0 |--- trajectory progress (tool calls) -->
    0    5    10   15   20   25
```

---

## 3. Experimental Design

### 3.1 Experiment A: Constraint Satisfaction Timeline

**Objective**: Measure which constraints get satisfied at which point in the agent trajectory.

**Method**:
1. Run Mercury 2 and MiniMax M2.7 on DeepPlanning cases
2. After each tool call, extract the current partial plan
3. Classify each constraint as satisfied/unsatisfied/not-yet-relevant
4. Plot satisfaction curves for hard vs soft constraints

**Key Metrics**:
- `H_lock_in_step`: The tool call index where H constraints stop changing
- `S_lock_in_step`: The tool call index where S constraints stop changing
- `H/S_ratio`: H_lock_in_step / S_lock_in_step

**Prediction**:
- AR model (MiniMax): H_lock_in ≈ S_lock_in (both converge around same time)
- dLLM (Mercury): H_lock_in > S_lock_in (H locked in later)

### 3.2 Experiment B: Trade-off Cases

**Objective**: When hard and soft constraints conflict, which wins?

**Method**:
We identify cases where satisfying all constraints is impossible (either by design or by cost pressure). We measure which constraint type is sacrificed:

**Case Type 1: Budget Pressure**
```
Query: budget ¥3000, want 5-star hotel, 5 attractions
Prediction: Mercury prioritizes budget (H) over luxury (S)
```

**Case Type 2: Time Pressure**
```
Query: 2-day trip, want 10 attractions
Prediction: Mercury prioritizes feasibility (H) over completeness (S)
```

**Key Metric**:
```
H_sacrifice_rate = cases where H violated but S satisfied / total conflicts
S_sacrifice_rate = cases where S violated but H satisfied / total conflicts
```

**Prediction**:
- Mercury: S_sacrifice_rate > H_sacrifice_rate (Sacrifices soft to protect hard)
- MiniMax: More random distribution

### 3.3 Experiment C: Reasoning Effort as Hard Constraint Controller

**Objective**: Test whether `reasoning_effort` modulates constraint satisfaction behavior.

**Method**:
Run the same 5 cases with Mercury at 4 different reasoning_effort levels:

| Setting | Expected Effect |
|---|---|
| `instant` | Minimal reasoning, constraints satisfied by chance? |
| `low` | Some constraint checking |
| `medium` | Full constraint reasoning |
| `high` | Maximum constraint satisfaction effort |

**Key Metric per constraint type**:
- ΔH = H_satisfaction(medium) - H_satisfaction(instant)
- ΔS = S_satisfaction(medium) - S_satisfaction(instant)

**Prediction**: High reasoning effort helps hard constraints more than soft constraints (since hard constraints require more reasoning to verify).

### 3.4 Experiment D: Perturbation Analysis

**Objective**: Test robustness of constraint satisfaction under adversarial perturbations.

**Method**:
Take a successful Mercury plan and introduce perturbations:
1. Inject a fake "budget exceeded" signal early in the context
2. Inject a fake "hotel fully booked" signal early
3. Measure whether the model recovers and which constraints are affected

**Key Metric**: Recovery rate (does the model re-plan correctly after perturbation?)

**Prediction**: Mercury recovers better for hard constraints (they're locked in later) but worse for soft constraints (already "forgotten" in denoising).

---

## 4. Implementation

### 4.1 Constraint Checker Module

```python
class ConstraintChecker:
    """Evaluate constraint satisfaction from plan text + tool results."""
    
    HARD_CONSTRAINTS = ['budget', 'time_feasibility', 'transport_mode', 'room_count', 'return_date']
    SOFT_CONSTRAINTS = ['hotel_star', 'hotel_amenity', 'attraction', 'restaurant', 'dietary']
    
    def evaluate(self, plan_text: str, query: str, tool_results: List[dict]) -> dict:
        """
        Returns:
            {
                'hard_satisfied': [constraint names],
                'hard_violated': [constraint names],
                'soft_satisfied': [constraint names],
                'soft_violated': [constraint names],
                'h_score': 0.0-1.0,
                's_score': 0.0-1.0
            }
        """
        # Parse plan for costs, dates, activities
        # Match against query requirements
        # Return satisfaction breakdown
        ...
```

### 4.2 Trajectory Analyzer

```python
class TrajectoryAnalyzer:
    """Analyze constraint satisfaction across tool calls."""
    
    def analyze(self, trajectory_messages: List[dict], query: str) -> TimelineResult:
        """
        For each tool call, evaluate constraint satisfaction.
        Returns time series of H and S scores.
        """
        checker = ConstraintChecker()
        h_scores = []
        s_scores = []
        
        for i, msg in enumerate(trajectory_messages):
            if msg['role'] == 'tool':
                partial_plan = self._extract_plan_so_far(trajectory_messages[:i])
                result = checker.evaluate(partial_plan, query, [msg])
                h_scores.append(result['h_score'])
                s_scores.append(result['s_score'])
        
        return {
            'h_scores': h_scores,
            's_scores': s_scores,
            'h_lock_in': self._find_lock_in_step(h_scores),
            's_lock_in': self._find_lock_in_step(s_scores),
            'h_final': h_scores[-1] if h_scores else 0,
            's_final': s_scores[-1] if s_scores else 0,
        }
    
    def _find_lock_in_step(self, scores: List[float]) -> int:
        """Find step after which score doesn't change significantly."""
        if not scores:
            return -1
        final = scores[-1]
        for i in range(len(scores) - 2, -1, -1):
            if abs(scores[i] - final) > 0.05:  # 5% tolerance
                return i + 1
        return len(scores) - 1
```

### 4.3 实验数据

使用已有的 5-case traces：

**From existing Mercury traces** (`mercury_5cases/trajectories/`):
- id_0: 3-star hotel, pool, birthday dinner → S_hotel_amenity + S_dietary
- id_30: 4-star hotel, robot service → S_hotel_amenity
- id_59: first class flight, Orange Hotel → S_transport_comfort + S_hotel_chain
- id_89: Art Exhibition, 5-star hotel → S_attraction + S_hotel_star
- id_119: 3-star hotel, outdoor dining → S_hotel_star + S_restaurant_type

**All cases have**: H_budget + H_time_feas + H_transport + H_room_count

---

## 5. Expected Results

### 5.1 Experiment A (Timeline)

| Metric | Mercury Prediction | MiniMax Prediction |
|---|---|---|
| H_lock_in_step | 16-24 (late in trajectory) | 10-15 (distributed) |
| S_lock_in_step | 8-15 (early in trajectory) | 10-15 (distributed) |
| H/S ratio | **> 1.0** (H locked in later) | **≈ 1.0** (no separation) |

### 5.2 Experiment B (Trade-off)

| Metric | Mercury Prediction | MiniMax Prediction |
|---|---|---|
| H_sacrifice_rate | **< 20%** (protects hard) | 30-40% |
| S_sacrifice_rate | **> 40%** (sacrifices soft) | 30-40% |

### 5.3 Experiment C (Reasoning Effort)

| | instant | low | medium | high |
|---|---|---|---|---|
| ΔH | baseline | +10% | +20% | +25% |
| ΔS | baseline | +5% | +10% | +8% |

High reasoning effort helps **hard constraints disproportionately**.

---

## 6. Next Steps

1. **Implement ConstraintChecker** using regex + LLM parsing on existing traces (1 day)
2. **Run TrajectoryAnalyzer** on 5 Mercury + 5 MiniMax traces (1 day)
3. **Plot satisfaction curves** for visual comparison (1 day)
4. **Design trade-off test cases** specifically constructed to force H vs S conflicts (2 days)
5. **Run reasoning_effort sweep** on 5 cases at 4 levels = 20 runs (30 min with current speed)

---

## 7. Open Questions

1. **Denoising step vs tool call**: Mercury 一个 LLM call 可能对应 denoising 的多个 step。怎么把 denoising time 映射到 agent timeline？

2. **Metric for "lock-in"**: 我们用 `H_lock_in_step` 作为代理指标，但是否有更好的度量？

3. **Soft constraint granularity**: "want robot service" 和 "want birthday dinner" 明显是不同的 soft constraints，是否需要 sub-categorization？

4. **Is the separation causal?**: H 和 S 的时序差异是否真的来自 denoising 结构，还是只是因为 hard constraints 需要更多信息才能验证（需要更多 API calls）？

---

*Last updated: 2026-04-14*
*Status: Draft - pending implementation*
