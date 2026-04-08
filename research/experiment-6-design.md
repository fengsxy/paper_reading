# Experiment 6: Process Quality Audit Harness

**Objective**: Build a harness that measures Process Quality dimensions (Plan Quality, Plan Adherence, Step Efficiency) using trace-based metrics, aligned with DeepEval's three-layer model.

## Background

From prior work:
- Five-dimension radar: Correctness, Efficiency, Robustness, Process Quality, Safety
- DeepEval mapping:
  - Reasoning Layer → Plan Quality + Plan Adherence (Process Quality)
  - Action Layer → Tool Correctness + Argument Correctness (Robustness)
  - Execution Layer → Task Completion + Step Efficiency (Efficiency + Correctness)

## Harness Design

### 1. Instrumentation Requirements

**Tracing integration**:
- Enable OpenClaw tracing plugin (`plugins/tracing`) to capture full transcripts
- Required span types: `agent`, `llm`, `tool`
- Each span must include: input, output, timestamp, parent span ID

**Trace enrichment**:
- Detect explicit planning phases (CoT markers: "Plan:", "Step 1:", numbered lists) → extract as `plan`
- Detect tool calls → build `tool_called` list with name, arguments, order
- Build `execution_steps` as sequence of (reasoning, action, observation) turns

### 2. Metric Definitions

#### Process Quality Metrics

**Plan Quality Score (PQS)**:
- LLM judge rates alignment between task goal and proposed plan
- Rubric: completeness, logical coherence, efficiency
- Threshold: ≥ 0.7 (scale 0-1)

**Plan Adherence Score (PAS)**:
- Compare execution steps against stated plan
- Detect deviations: skipped steps, inserted steps, reordering
- LLM judge rates faithfulness (0-1)
- Threshold: ≥ 0.7

**Step Efficiency Score (SES)**:
- Normalized by task complexity (expected minimum steps)
- Penalize: redundant tool calls, repeated reasoning, backtracking loops
- Metric: (expected_steps / actual_steps) capped at 1.5x penalty for excess
- Threshold: ≥ 0.8

#### Robustness Metrics (for completeness)

**Tool Correctness (TC)**:
- Expected tools (from golden) vs actual tools called
- Modes: strict (name+args+order), lenient (name only)
- Threshold: 1.0 for critical tools

**Argument Correctness (AC)**:
- For each tool call, validate arguments against schema
- Catch: missing required fields, type mismatches, out-of-range values

### 3. Evaluation Harness Architecture

```
sessions_spawn (or direct agent harness invoke)
   ↓
Enable tracing → capture full transcript
   ↓
Post-process trace:
   - Extract plan (if present)
   - Build execution timeline
   - Compare with golden (expected tools, outcome)
   ↓
Calculate metrics (LLM judges for PQS/PAS, code-based for others)
   ↓
Aggregate results (mean, std, pass@k)
   ↓
Report + failure clustering
```

### 4. Task Suite

**Regression tasks** (known solvable, near 100% pass expected):
- Simple lookup + formatting (1-2 steps)
- Single tool use with clear arguments
- Verify: harness does not break baseline agents

**Capability tasks** (target difficulty 20-60% pass):
- Multi-step planning with dependencies
- Constraint satisfaction (budget/time)
- Tool selection ambiguity
- Error recovery (tool returns empty/error)

**Process quality probes** (embedded in above):
- Plan explicit vs implicit
- Linear vs branching execution
- High vs low redundancy variants

### 5. Implementation Plan

**Week 1**:
- Set up tracing collection for a sample agent (e.g., coding-agent or Claude Code)
- Write trace parser to extract plan/steps/tools
- Implement code-based metrics (TC, AC, SES)

**Week 2**:
- Integrate LLM judge for PQS and PAS (using GPT-4o or Claude Opus)
- Build outcome verification module (environment state assertion)
- Run on 5-10 sample tasks, calibrate thresholds

**Week 3**:
- Full regression + capability suite (50 tasks total)
- Statistical runs (n=3 per task)
- Generate failure clusters for debugging

**Week 4**:
- Documentation: how to add new tasks, interpret metrics
- Integration with Task Flow (v2026.4.2) for timeouts and phased approval

### 6. Success Criteria

- Harness runs end-to-end without manual intervention
- Distinguishes between agents with different planning strategies
- Provides actionable diagnostics (e.g., "low PAS due to skipped step X")
- Pass rate on regression tasks ≥ 99% (baseline agent)

### 7. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| LLM judge noise | Use majority vote (3 judges) + calibration with human labels |
| Trace parsing failures | Fallback to regex + manual inspection, log errors |
| Metric correlations obscure insights | Report full correlation matrix, use PCA if needed |
| Task suite too easy/hard | Iteratively adjust based on pilot results |

---

**Next**: Review with Yu, then start implementation in `research/experiment-6/` with sample tasks.
