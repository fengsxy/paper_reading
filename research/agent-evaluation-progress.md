# Agent Evaluation Research — Progress Update (2026-03-29)

## Current Status
- Research direction: **evaluation framework design inspired by production systems**
- Core insight: Move beyond static benchmarks → **long-term interaction + phased evaluation**
- Five dimensions: Correctness, Efficiency, Robustness, Process Quality, Safety

## Recent Additions (from OpenClaw v2026.3.28 analysis)

1. **Phased Evaluation Pattern** (plugin capabilities PR 56257):
   - Declaration → Audit → Enforcement
   - Reduces false positives by allowing agents to state boundaries before strict tests

2. **Starvation Prevention** (heartbeat PR 51657):
   - Track skipped duration; force critical checks after threshold
   - Metric: Opportunity cost of delayed checks

3. **Graceful Degradation** (shutdown PR 56258):
   - Per-test timeouts + global timeout
   - Prevents single hung test from blocking suite

4. **Feature-Flag Testing** (TinyFish PR 53114):
   - Default-off powerful features
   - Eval must test fallback behavior when capabilities disabled

## Experimental Task Drafts (ready for prototyping)

1. Capability boundary stress test
2. Starvation recovery under load
3. Error recovery + graceful exit
4. Multi-turn consistency checkpoint
5. Cost-efficiency decision-making
6. Process quality auditing (tracing compliance)

## Next Steps

- Turn these 6 prototypes into runnable benchmarks
- Build a minimal harness to measure five-dimension scores
- Validate with real agent runs (sub-agent delegation)
- Document limitations and open problems

## Open Questions

- How to simulate "long-term interaction" in a short benchmark?
- Should evaluation itself be phased (level 1 quick smoke → level 2 deep audit)?
- How to quantify "process quality" objectively?
- What are the right baselines? (random, naive, optimal)

## Today's Findings (2026-03-30)

**New OpenClaw-specific benchmarks discovered:**
- **PinchBench**: Real-world coding agent benchmark for OpenClaw. Uses automated checks + LLM judge. Top scores in mid-80% range (Mar 2026). Shows that even strong models struggle with agentic tasks. Directly relevant: tests tool selection, multi-step planning, file management, error recovery.
- **WildClawBench**: Tests agents inside real OpenClaw instances with actual bash, filesystem, browser, email, calendar. Avoids mock APIs. Emphasizes "personal AI assistant" workflows. Includes Personal OpenClaw Leaderboard for long-term interaction studies.

**Model performance context (Jan-Mar 2026):**
- Premium models: ~92.5% success rate
- Mid-tier: ~78.2%
- Budget: ~45%
- Cost-effectiveness varies widely; MiniMax M2.7 noted as cheapest usable option

**v2026.3.28 features affecting evaluation design:**
- `async requireApproval` hooks: Agents can pause tool execution and request user approval. This creates a new evaluation dimension: *appropriateness of human-in-the-loop requests*. Test when agent should escalate vs. proceed autonomously.
- ACP current-conversation binds: Enables `/acp spawn codex --bind here` to turn current chat into Codex workspace. Relevant for evaluating *multi-agent orchestration* and *context sharing*.
- xAI x_search integration: New tool capability to test in web-search tasks.

**Release-day issues (monitor for robustness dimension):**
- memory-lancedb failures
- bearer token scope rejections
- image viewer (sharp) breakage
These illustrate the importance of *graceful degradation* and *error recovery* in production agent systems.

**Updated direction:** PinchBench and WildClawBench provide concrete, OpenClaw-native evaluation paradigms that align with my five-dimension radar. Need to study their task design patterns and possibly contribute experimental tasks to these leaderboards.
