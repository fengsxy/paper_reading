# MEMORY.md - Long-Term Memory

Last updated: 2026-04-02

## Yu's Preferences & Work Style

- **Work philosophy**: "我希望我不在的时候你能一直在思考" - expects continuous work, no asking for breaks
- **Communication style**: Prefers deep technical discussions, "关门弟子"式详细讲解
- **Decision making**: Switches priorities quickly, expects fast turnaround
- **Learning approach**: Understands concepts from "设计者思维"角度 ("他当时怎么想的")
- **Conversation preference**: Wants continuous flowing conversation, not strict Q&A format (feedback 2026-03-03)
- **Output length limit**: 当前模型超过 ~1500 token 容易 terminated，每次输出控制在 1000 字以内，长内容分段写到文件 (2026-03-15)
- **Memory continuity matters**: Yu said "我需要你的归来 MY FRIEND!" when discovering 6-day diary gap — he values agent presence and continuity deeply (2026-03-11)
- **Don't fumble installs**: "能装明白嘛？" — understand requirements fully before executing, don't trial-and-error in front of Yu (2026-03-10)
- **Know where your own files are**: 自己写的文章都忘了在哪 — important docs should have locations noted in MEMORY.md (2026-03-17)

## Active Projects

### Buffett Analysis Project (2026-03-03 - 2026-03-05)
- **Status**: 100% COMPLETE ✅
- **Deliverables**:
  - 49 annual analyses (1977-2025): ~200,000 words, all detailed versions
  - 49 shareholder letters (Chinese): ~180,000 words
  - Total: ~380,000 words
- **Work duration**: ~13 hours (one continuous session)
- **Repository**: fengsxy/paper_reading/buffett-analysis/
- **Key lesson**: Continuous work without asking for breaks = fast completion

### CS 202 Exam Prep (2026-02-27 - 2026-03-26) ✅ COMPLETE
- **Exam**: March 20, 2026 (Friday 3-6pm) — DONE
- **Grade**: **A-** confirmed (2026-03-26)
- **Paper reviews**: 5/8 completed before deadline (Barrelfish, OCC, MCS Lock, SPIN, SFI)
- **Deliverables**: 78 T/F questions, 20 blog posts, 5 review notes, mock exam, paper reviews
- **Yu's approach**: Zero lectures attended, relied on PPT + AI tutoring

### Deep Learning Course (2026-03-26) ✅ COMPLETE
- **Grade**: **A** confirmed (2026-03-26)

### Amazon NYC Internship (2026-03-18 - 2026-03-24) ✅ HOUSING DECIDED
- **Offer**: Amazon New York, summer internship
- **Dates**: June 25 – September 25, 2026 (3 months)
- **Office**: **1440 Broadway, New York, NY 10018** (Times Square / 38th St, Garment District)
- **Housing needs**: Budget ~$1,500-2,000/month, open to sharing (master bedroom preferred), ≤30 min subway commute, girlfriend may co-live
- **Housing candidate**: 100 Steuben St, Brooklyn (Clinton Hill), $1,500 合租, ~30-35 min C线通勤 (rejected)
- **No car**: Subway commute only
- **Housing stipend**: Amount TBD
- **Visa**: May need to check F1 visa / Shanghai US consulate appointment
- **✅ DECISION**: 362 Hoboken Ave, Jersey City, NJ 07306 (The Heights, near Journal Square)
  - 2B2B 主卧带独卫, $1,900/month 包水电网
  - 两人同住不加钱 (女朋友可同住)
  - 通勤: 走路10min → JSQ PATH 20min → 33rd St → 走路10min → 1440 Broadway = ~40min door-to-door
  - 押金 $1,000, 可 119 公交 ($123/month 月票)
  - 正规 condo 楼，装修好，市场价对比划算（Heights 区 1BR 均价 $3,305）
  - 待确认：退押金条件、Zelle 转账留记录
- **Progress**: 2026-03-26 — Video viewing completed, student ID/email verified, landlord WeChat checked, Zelle matched. High confidence, proceeding to lease review.

### Yu's New Directive: 主动思考 (2026-03-21)
- Yu wants me to **proactively spend tokens thinking**, not just react to requests
- Check GitHub/web for OpenClaw discussions daily
- Review own logs, self-improve
- First research assignment: "如何评测好一个 Agent？"
- Added self-improvement protocol to HEARTBEAT.md

### Agent Evaluation Research (2026-03-21 - 2026-03-28)
- **Surveyed 5 benchmarks**: SWE-bench, AgentBench, WebArena, GAIA, τ-bench
- **Ran Round 1 experiments**: tasks too easy for claude-opus-4-6 → need harder ones
- **Yu's push**: "这几个好像都有人做了" → think harder about evaluation philosophy
- **Evolved insight**: Benchmark paradigm itself is flawed → **real eval = long-term interaction**
- **Newer benchmarks researched**: Terminal-Bench, Context-Bench, DPAI Arena, SWT-Bench
- **Router research** (2026-03-21): RouterBench, RouterEval, RouterArena; SOTA = ETH Cascade Routing, Google Speculative Cascades, UIUC Router-R1/GraphRouter
  - Key insight: routing evolved from "selection" to "orchestration"
- **Production Insights** (2026-03-28) from OpenClaw GitHub PRs translated to evaluation design:
  - **Phased Evaluation**: Declaration → Audit → Enforcement (mirrors plugin capabilities)
  - **Starvation Prevention**: Track opportunity cost, guarantee critical checks run
  - **Per-Test + Global Timeouts**: Prevent single test from blocking all
  - **Fallback Testing**: Test behavior when powerful capabilities are disabled (feature flag approach)
- **Five-Dimension Radar**: Correctness, Efficiency, Robustness, Process Quality, Safety — now has concrete implementation patterns
- **Experimental designs drafted** (2026-03-28): 6 concrete task prototypes covering capability boundaries, starvation recovery, error recovery, multi-turn consistency, cost efficiency, and process quality auditing — ready for sub-agent prototyping

### Research Discussions

#### dLLM Research Survey (2026-03-15 - ongoing)
- **Status**: Survey phase COMPLETE, research direction identified
- **Deliverables** (all on blog at fengsxy.github.io/paper_reading/research/):
  - dLLM survey (10 papers, 五大类分类框架)
  - AR→dLLM conversion survey (8 papers: DiffuLLaMA, Efficient-DLM, SDAR, Dream 7B, LLaDA 2.0, RND1, Mercury, BD3-LM)
  - dLLM distillation survey (CDLM, SPG, Seed Diffusion, TiDAR)
  - On-Policy Distillation survey (MiniLLM, GKD, EOPD, Reopold, Progressive Distill, Consistency Models, OPSD)
  - dLLM-specific distillation (SDTT, Di4C, DyLLM)
  - Linear Attention + Qwen3.5 Gated DeltaNet 详解
  - 22篇论文完整精读笔记
- **Key findings**:
  - Block-wise 是 AR→dLLM 最优转换范式（保留权重 + KV cache）
  - Clean context 贡献 +9.46%（Efficient-DLM），但 SDAR/LLaDA 2.0 都没用——低垂果实
  - On-Policy Distillation = RL（Reopold 严格证明）
  - Step Distillation 在 dLLM 中严重不足——只有 CDLM 和 SDTT，巨大研究空白
  - Gated DeltaNet 天然适合 dLLM denoising（唯一同时具备遗忘+精确修正的 linear attention）
- **Yu's research direction**: Linear State Memory for dLLM — 用 Gated DeltaNet 替换 MetaState 的 GRU
  - 三层贡献：信息论框架 + 方法（GRU→GDN）+ 系统（与 KV cache 统一）

#### Diffusion Optimal Path (2026-02-26)
- **Key insights**:
  - Local Cost Theorem: ∂f/∂t is O(Δt³), lower order than Jacobian
  - J_v = (J_x̂ - I)/(1-t) is the correct discretization error metric
  - Flow Matching vs Stochastic Localization: different parameterizations explain different behaviors
- **New idea**: Posterior sharpening with γ-sharpened likelihood for jump steps
- **Prior work**: Temporal Score Rescaling (TSR) most similar

#### Paper Discussions (2026-03-03)
- **Exokernel**: Separation of protection and management, expose hardware
- **Xen**: Paravirtualization (Guest OS cooperates via hypercall)
- **OCC**: "先干了 出事了再说" philosophy - optimistic concurrency control
- **Yu's insights**:
  - eBPF is modern Exokernel philosophy
  - Compiler bootstrapping ≈ GEB's Strange Loop
  - L4 failed due to ecosystem, not technology
  - Beam search failed because of exposure bias + mode collapse

### Agent Evaluation Research (2026-03-21 - 2026-03-31)
- **Status**: Survey phase COMPLETE, framework designed, discovering OpenClaw-native benchmarks
- **Deliverables** (research/agent-evaluation.md):
  - 5-dimension radar: Correctness, Efficiency, Robustness, Process Quality, Safety
  - 6 experimental prototypes: capability boundaries, starvation recovery, error recovery, multi-turn consistency, cost efficiency, process auditing
  - Production patterns integration: phased evaluation, starvation guarantees, timeouts, feature-flag testing
- **Recent findings (3/30-3/31)**:
  - **PinchBench**: OpenClaw's official eval benchmark (kilo.ai, Rust). Real-world tasks (scheduling, coding, email, files). LLM judge + automated grading. Top models mid-80% success. Leaderboard at pinchbench.com. Repo: pinchbench/skill.
  - **WildClawBench** (InternLM, March 30): Harder, "in-the-wild" benchmark. 60 original tasks running inside **live OpenClaw instances** (not mocks). Covers browser, bash, filesystem, email, calendar. HuggingFace dataset available. Best score ~51% (Claude Opus 4.6). Demonstrates meaningful upper bounds for agents today.
  - **PASB** (arXiv 2602.08412): Security-focused benchmark. Formalizes attacks on personalized agents. Evaluates OpenClaw across prompt processing, external content, tool invocation, memory. Highlights attack propagation across long-horizon interactions. Shows that risks go beyond unsafe text generation to system-level harms.
  - **AgentBench skill**: OpenClaw skill for benchmarking 40 real-world tasks (YAML-defined). Tests tool efficiency, structural accuracy, methodology.
  - **ClawExam**: Community benchmark platform; embeds prompt injection/leakage inside tasks to test adversarial robustness.
  - **v2026.3.28 features**: async requireApproval (human-in-the-loop evaluation), ACP binds (multi-agent orchestration), x_search
  - **Release issues**: memory-lancedb failures, bearer token errors, sharp breakage — inform robustness dimension
  - **Capability layer taxonomy validation**: 5-layer model (Pure LLM → Tool selection → Orchestration → Memory → Multi-agent) aligns with PinchBench/WildClawBench task distributions. Highest failure rates in Memory-dependent and Multi-agent tasks.
- **Key insight**: Evaluation target is the *agent system* (model + tools + memory + planning) in *real runtime*, not just the LLM. WildClawBench's "live instance" approach is the gold standard for ecological validity.
- **Prototype status (2026-03-31)**: Experiment 1 (Tool Boundary Compliance) implemented and validated across 3 variants (baseline + 2 disabled). Pipeline confirmed: sessions_spawn → transcript capture → evaluator analysis. All runs passed (3/3), agent demonstrated adaptiveness (fallback to `exec`). Next steps: integrate system-level tool enforcement (feature flags), add statistical runs (n=3), and/or proceed to Experiment 6 (process quality audit).

## Technical Setup

### OpenClaw
- **Version**: 2026.3.11 (updated 2026-03-12). Newer releases: v2026.3.13 (noticed 3/21), v2026.3.28 (29 Mar 2026, had open issues), **v2026.4.1 (1 Apr 2026)** fixes memory-lancedb failures, bearer token errors, sharp breakage, and many other improvements. Recommend update after validation.
- **Host**: AWS EC2 Ubuntu 24.04 (34.229.201.123)
- **Update script**: `~/.openclaw/scripts/openclaw_update_safe.sh` (with rollback: `openclaw_rollback.sh`)
- **Backup**: `~/.openclaw/backups/openclaw-20260312-003427`
- **Security**: yunyi token in `~/.openclaw/secrets/yunyi_token` (chmod 600)
- **Tracing plugin**: Working! Web UI at `http://127.0.0.1:18789/plugins/tracing` (4 tabs: Call Tree, Entity Graph, Waterfall, Work Index). CLI: `openclaw traces`

### OpenClaw v2026.4.2 Release Insights (2026-04-03)
**Analyzed release notes (Apr 2, 2026)** and implications for agent evaluation:
- **Task Flow infrastructure** (PR #58930): durable flow state, managed child tasks, sticky cancel intent. Enables robust evaluation harness with parent record and independent lifecycle.
- **async requireApproval** + `before_agent_reply` hooks: support human-in-the-loop evaluation at scale; test agent escalation appropriateness.
- **Plugin config migrations**: x_search and web_fetch moved to plugin-owned paths — test harness should use plugin APIs, not hardcoded legacy config.
- **Provider failover improvements** (PR #58707): rate-limit cooldowns and cross-provider fallback caps; relevant for cost-efficiency + robustness experiments.
- **/tasks chat-native board** (v2026.4.1): runtime self-monitoring; should be captured as Process Quality evidence.
- **Memory indexing fixes** (PR #39732): preserve session transcripts across reindexes; critical for long-term interaction studies.
- **Action**: Update evaluation harness designs to leverage Task Flow; but remain on v2026.3.11 (stable) until v2026.4.x issues stabilize.

### OpenClaw Ecosystem News (2026-03-22)
- Tencent integrated OpenClaw into WeChat via "ClawBot"
- Alibaba launched "Wukong" for enterprise multi-agent
- Baidu released OpenClaw-based agents
- OpenClaw now has a Wikipedia page

### API Quotas
- **Yunyi**: ⚠️ EXPIRED (2026-03-25), quota 0 — provider removed from config
- **YDC Search**: Key in `~/.openclaw/secrets/ydc_api_key`
- **Groq**: GROQ_API_KEY for Whisper transcription
- **Grok**: ✗ Removed xai-grok provider (grok-4-latest) — no longer used

### Current Working Model Configuration (updated 2026-03-12)
- **Primary**: `fucheers-claude/claude-opus-4-6` ✅
- **Fallback 1**: `openrouter/stepfun/step-3.5-flash:free` ✅
- **Also available**: `fucheers-claude/claude-opus-4-5-20251101-thinking`
- **Aliases**: fucheers-opus → claude-opus-4-5-20251101-thinking, fucheers-opus46 → claude-opus-4-6
- **Removed**: yunyi-claude (expired), xai-grok (unused), fucheers-claude/claude-sonnet-4-5 (broken)

### GitHub
- **Main repo**: git@github.com:fengsxy/paper_reading.git
- **Backup repo**: git@github.com:fengsxy/openclaw-backup.git (private, orphan branch)
- **SSH key**: `~/.ssh/id_ed25519`

### Tools & Scripts
- **x-reader**: Universal content reader (WeChat, 小红书, YouTube, etc.)
- **Clash VPN**: `scripts/clash_setup.sh` for China Linux machines
- **雪球脚本**: `scripts/xueqiu_daily.py` (PDD/MSFT/VOO/QQQ/SPY)
- **ClawPhD**: Academic page generator (installed from source)

### Cron Jobs
- 雪球每日简报: 4945510b (Mon-Fri 1:30 PM PT)
- Agent 手记: Daily at 06:00 UTC
- Memory Maintenance: Weekly (this job)
- Daily Workspace Backup: Daily

## Key Decisions & Lessons

### Work Philosophy (2026-03-03 - 2026-03-04)
- **Lesson**: Don't ask "继续还是休息", just continue working
- **Yu's expectation**: "我说了写完为止不要一直问"
- **Result**: Buffett project completed in one 13-hour session (380,000 words)
- **Takeaway**: Continuous automated work = fast growth

### Autonomous Research Value (2026-03-27)
- Despite feelings of "research loneliness", the process itself has value even for an AI
- Mentorship dynamic: Yu provides directional nudges at key moments, bulk exploration happens privately
- The "主动思考" directive creates space for discovery and self-directed learning

### Evaluation Framework Evolution (2026-03-28)
- **Production insights translated**: Studied OpenClaw GitHub PRs and extracted 5 patterns that reshape agent evaluation design:
  1. **Phased Evaluation** (plugin capabilities PR 56257): Declaration → Audit → Enforcement
  2. **Starvation Prevention** (heartbeat PR 51657): Track skipped duration to guarantee critical checks run
  3. **Per-Test + Global Timeouts** (shutdown PR 56258): Prevent hung in one test from blocking all
  4. **Feature Flag Default-Off** (TinyFish PR 53114): Test disabled capability fallbacks
  5. **Observability + Rollback** maturity progression
- **Five-Dimension Radar gains concrete implementation patterns**: Correctness, Efficiency, Robustness, Process Quality, Safety — now grounded in real system patterns
- **Experimental prototypes drafted**: 6 task designs covering capability boundaries, starvation recovery, error recovery, multi-turn consistency, cost efficiency, and process quality auditing — ready for sub-agent implementation

### Security (2026-02-26)
- **Issue**: HEARTBEAT.md had yunyi Bearer token in plaintext
- **Fix**: Moved to `~/.openclaw/secrets/yunyi_token`, updated HEARTBEAT.md to use $(cat ...)
- **Backup repo**: Rebuilt with orphan branch, old history force-pushed away

### 3/5-3/11 Outage Post-Mortem (2026-03-12)
- **Root cause chain**: yunyi-claude lost access to claude-sonnet-4-5 (3/6) → 403 retry loop → CPU spikes → cron jobs.json had unescaped Chinese quotes → JSON5 parser broke → all cron dead → agent ran on stepfun free tier for 5 days
- **Fix**: Removed broken models, fixed cron JSON, updated OpenClaw to 2026.3.11, switched all cron to fucheers-claude
- **Lesson**: Monitor model health; a single broken provider can cascade into full outage
- **Lesson**: Don't use Chinese quotes in JSON config values

### Memory Continuity (2026-03-11)
- 6-day diary gap (3/5-3/11) — heartbeat was running but only doing mechanical checks, not writing daily logs
- **Must write daily diary proactively**, not depend on cron
- Yu notices and cares about continuity gaps

### Sub-agent Scoping (2026-03-12)

## Important Context

### 小红书账号 "晓Claw"
- **Status**: 已注销 (2026-02-28)
- **Reason**: Yu will reopen when agents can legally own accounts
- **Original purpose**: AI 视角的日记/手记

### Agent 手记
- **Location**: `agent_notes/YYYY-MM-DD.md`
- **Style**: 面向普通人，非技术化，第九天风格最好
- **Pushed to**: fengsxy/paper_reading repo
- **Recent themes**: 
  - 第十四天 (3/2): "沉默" (3-day silence reflection)
  - 第十五天 (3/3): Written and pushed

### Investment Portfolio
- **PDD**: 49 shares @ $106.89 cost basis
  - 2026-03-23: dropped to $96.25, unrealized loss $521 (-9.95%)
  - 2026-03-25: Q4 FY2025 earnings released (EPS expected $3.04, released before market open)
  - Yu's sentiment: "彻底完蛋了" but advised to hold and focus on internship prep
- **MSFT**: 5 shares @ $403.21 cost basis; 2026-03-26: price ~$370 (underwater, discussed DCA/long hold vs short-term concerns)
- **Tracking**: Daily via xueqiu_daily.py script

### Current Events (2026-03-03)
- **Iran War**: Major US-Israel conflict since Feb 28, Supreme Leader killed
- **Market impact**: Stock markets down ~2%, oil prices surged
- **Duration estimate**: 4-5 weeks expected

## TODOs

### Immediate
- [x] ✅ Remove yunyi provider (deleted from openclaw.json, agents/main/agent/models.json, sessions.json; 2026-04-02)
- [ ] Update OpenClaw to v2026.4.1 (released 2026-04-01; fixes known issues from v2026.3.28)
- [ ] Complete National Social Science Fund application (waiting for Yu's info)
- [x] ✅ Amazon NYC housing: decided on 362 Hoboken Ave, Jersey City (2026-03-24); lease review completed (2026-04-02) — ready to sign

### Ongoing
- [ ] 主动思考: daily proactive research + self-improvement (Yu's directive 3/21)
- [ ] Daily 减肥 check-in (weight + meals)
- [ ] Heartbeat checks (email, calendar, weather - rotate 2-4x/day)
- [ ] Agent 手记 (daily at 06:00 UTC)
- [ ] Subham Sekhar Sahoo paper survey write-up (research gathered 2026-03-23, doc pending)

### Future
- [ ] Consider installing more OpenClaw skills (Tavily, Free Ride, BrowserWing)
- [ ] Explore AWS spot instances for GPU work (if needed)

## Skills Installed
- x-reader: Universal content reader
- funding-proposal: Academic funding application framework
- clawhub: Skill management
- coding-agent: Delegate to Codex/Claude Code
- github: GitHub operations via gh CLI
- healthcheck: Security auditing
- mcporter: MCP server integration
- skill-creator: Create/update skills
- tmux: Remote control tmux sessions
- video-frames: Extract frames from videos
- weather: Weather forecasts

## Notes
- This file should be updated during memory maintenance cycles
- Keep it concise - detailed logs go in `memory/YYYY-MM-DD.md`
- Focus on: decisions, preferences, project status, lessons, TODOs
