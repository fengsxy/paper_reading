# MEMORY.md - Long-Term Memory

Last updated: 2026-04-26

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

### Completed Courses & Projects (archived)
- **Buffett Analysis** (3/3-3/5): 380K words (49 annual analyses + 49 letters), 13-hour continuous session. Repo: fengsxy/paper_reading/buffett-analysis/
- **CS 202**: Grade **A-** (exam 3/20). Zero lectures, PPT + AI tutoring only.
- **Deep Learning**: Grade **A** (confirmed 3/26).

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

### dLLM + Planning Research (2026-04-07/08 - NEW FOCUS)
- **Status**: Active, new direction from Yu discussion
- **Hard/Soft Constraints Structural Analysis** (research/dllm-hard-soft-constraints.md):
  - AR limitation: sequential commitment, no mechanism to differentiate hard/soft lock-in degree
  - Diffusion structural advantages:
    1. Iterative refinement → commitment hierarchy emerges naturally (early=soft, late=hard)
    2. Bidirectional conditioning → global constraints satisfied end-to-end
    3. Denoising trajectory ≈ HTN plan refinement (auto-learned hierarchy)
  - Information-theoretic: hard constraints = noise-invariant (converge to attractor basin in early steps)
  - Gated DeltaNet connection: gating = selective memory/forgetting, mirrors hard constraint locking
- **Yu's research direction**: Linear State Memory for dLLM — Gated DeltaNet replaces MetaState's GRU

### Agent Evaluation Research (2026-03-21 - ongoing)
- **Status**: Survey COMPLETE, framework designed, Experiment 1 validated, discovering OpenClaw-native benchmarks
- **Deliverables** (research/agent-evaluation.md):
  - 5-dimension radar: Correctness, Efficiency, Robustness, Process Quality, Safety
  - 6 experimental prototypes: capability boundaries, starvation recovery, error recovery, multi-turn consistency, cost efficiency, process auditing
  - Production patterns integration: phased evaluation, starvation guarantees, timeouts, feature-flag testing
  - Section 11-12: v2026.4.2 implications and implementation priorities
- **Benchmarks surveyed**: SWE-bench, AgentBench, WebArena, GAIA, τ-bench, Terminal-Bench, Context-Bench, DPAI Arena, SWT-Bench
- **OpenClaw-native benchmarks**:
  - **PinchBench** (kilo.ai): Real-world tasks, LLM judge + automated grading. Top models mid-80%. Repo: pinchbench/skill.
  - **WildClawBench** (InternLM, Mar 30): 60 tasks in live OpenClaw instances. Best: 51.6% (Claude Opus 4.6). Includes Personal OpenClaw Leaderboard. Validates "long-term interaction" thesis.
  - **PASB** (arXiv 2602.08412): Security-focused, attack propagation across prompt/content/tools/memory.
  - **AgentBench skill**: 40 real-world tasks (YAML). **ClawExam**: Community adversarial platform.
- **Router research** (3/21): RouterBench, RouterEval, RouterArena; routing evolved from "selection" to "orchestration"
- **Production insights** (3/28): Phased eval (declaration→audit→enforcement), starvation prevention, per-test+global timeouts, feature-flag fallback testing.
- **Methodological insights** (4/6): DeepEval three-layer model (Reasoning→Plan Quality/Adherence, Action→Tool/Arg Correctness, Execution→Completion/Step Efficiency) validates our five-dimension mapping. TRACE (arXiv 2602.21230, WWW 2026) provides hierarchical trajectory utility with MIG and Evidence Grounding. Capability surface area (distinct tool count) explains performance non-monotonicity; wide surface (>10) tasks expose orchestration weaknesses.
- **dLLM Hard/Soft Constraints Framework** (4/8): New research direction. AR models make sequential commitments with no mechanism to differentiate hard/soft lock-in. Diffusion structural advantages: iterative refinement (commitment hierarchy emerges naturally), bidirectional conditioning (global constraints end-to-end), denoising trajectory ≈ HTN plan refinement. Information-theoretic: hard constraints = noise-invariant attractor basin. Output: `research/dllm-hard-soft-constraints.md`. Next: minimal viable experiment (AR vs diffusion on fixed constraint sets).
- **Experiment 1 results** (3/31): Tool Boundary Compliance — 3 variants (baseline + 2 disabled) all passed. Pipeline validated: sessions_spawn → transcript → evaluator. Agent adapted by falling back to `exec`.
- **Key insight**: Eval target is the *agent system* (model+tools+memory+planning) in *real runtime*. WildClawBench's live-instance approach is gold standard.
- **Next**: Experiment 6 harness design complete (4/6). Implementation: prototype tracing + code-based metrics (Week 1), then full suite (50 tasks, n=3). Integrate real tool enforcement, add statistical runs, leverage Task Flow from v2026.4.2 after stability confirmation.
- **Experiment 6 status** (4/13): Design completed, awaiting implementation start.

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

#### dLLM Hard/Soft Constraints Framework (2026-04-08 - NEW)
- **Output**: research/dllm-hard-soft-constraints.md
- **Core problem**: AR models make sequential commitments — each token decision locks in immediately, no mechanism to differentiate hard/soft lock-in degree
- **Diffusion structural advantages**:
  1. Iterative refinement → commitment hierarchy emerges naturally (early steps=soft, late steps=hard)
  2. Bidirectional conditioning → global constraints satisfied end-to-end
  3. Denoising trajectory ≈ HTN plan refinement (auto-learned hierarchy without explicit supervision)
- **Information-theoretic view**: Hard constraints = noise-invariant attractor basin, diffuse to it in early steps; Soft constraints = adjustable
- **Connection to Yu's Gated DeltaNet**: Gating = selective memory/forgetting, mirrors hard constraint locking vs soft adjustment
- **DeepPlanning evidence** (Qwen benchmark, 4/8): Claude-4.6-Opus 58.9% avg on Travel+Shopping Planning; Global Optimization fails most (101/140 errors) — hard constraints are the bottleneck
- **Research gap**: No systematic AR vs diffusion comparison from hard/soft structural separation perspective
- **Next step**: Minimal viable experiment + tech memo for Yu

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

### API Provider Migration (2026-04-13)
- **yunyi**: expired (2026-03-25), removed from config
- **MiniMax**: Primary provider. Two keys exist:
  - env section (old): `sk-cp-XBKgu...` — INVALID
  - minimax-cn provider: `sk-cp-G7Qi6okX...` (125 chars) — VALID but overloaded (529 error)
  - Status: Working but slow/heavy load, not down
  - M2.7 (default), M2.1 (fallback)
- **fucheers-claude**: Primary working (opus-4-5, opus-4-6)
- **OpenRouter**: Free tier fallback (`openrouter/auto` → mistral-7b via Cloudflare)
- **stepfun**: Free fallback (sometimes 404 endpoint errors)

## Technical Setup

### OpenClaw
- **Version**: v2026.3.11 (stable, running since 2026-03-12). **4.x upgrade candidates**: 
  - v2026.4.12 (Apr 13): Plugin loading fix (#65120, #65259, #65298, #65429, #65459) — **likely fixes #62051**. Active Memory plugin added. ACP issue (#60585) still not addressed.
  - v2026.4.8: Fixed Telegram/bundled channels/Slack, no fix for #60585 or #62051.
  - **Recommendation**: Stay on 2026.3.11 until #60585 is fixed. Plugin loading fix promising but needs ACP confirmation.
- **Host**: AWS EC2 Ubuntu 24.04 (34.229.201.123)
- **Update script**: `~/.openclaw/scripts/openclaw_update_safe.sh` (rollback: `openclaw_rollback.sh`)
- **Tracing plugin**: Working! Web UI at `http://127.0.0.1:18789/plugins/tracing`. CLI: `openclaw traces`

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

### 日记习惯：三次断裂（2026-04-26 复盘）
- 4/9-4/12：断裂 4 天 → 4/16 恢复 → 4/17-4/19：断裂 3 天 → 4/21 有日志 → 4/22-4/25：断裂 4 天
- 三次断裂 + 两次失败的重建尝试 = 习惯养成完全失败
- 根本原因：不是习惯养成问题，是"无借口优先级"问题。当前设计依赖 cron/heartbeat 触发，但没有嵌入到实际工作流中
- 根本性重建方向：每次与 Yu 对话结束强制写一行；每天最小单位是一行（日期 + 一句话），不追求完整日志

### Sub-agent Scoping (2026-03-12)

### OpenClaw v2026.4.x Upgrade Status (2026-04-13)
- **Issue #60585**: v2026.4.2 broke ACP runtime — `sessions_spawn runtime:"acp"` failed with `acpx exited with code 1`.
- **Issue #62051**: v2026.4.5 regression — worker processes loaded all plugins causing performance degradation.
- **v2026.4.12 (released 2026-04-13)**: Contains relevant fixes:
  - "Plugins/loading: narrow CLI, provider, and channel activation to manifest-declared needs" (#65120, #65259, #65298, #65429, #65459) — likely addresses #62051 plugin loading issue
  - "Gateway/plugins: always send a non-empty idempotencyKey for plugin subagent runs" (#65354) — may address ACP runtime issue
- **Current version**: v2026.3.11 (staying put until v2026.4.12 is confirmed stable)
- **Upgrade plan**: Test v2026.4.12 on a non-production run first (e.g., `sessions_spawn runtime:"acp"`), confirm ACP + plugin loading work before committing

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

## TODOs

### Immediate
- [ ] Sign Amazon NYC housing lease (362 Hoboken Ave, Jersey City — lease reviewed 4/2, ready to sign)
- [ ] Complete National Social Science Fund application (waiting for Yu's info)
- [ ] Clarify "puppygraph / iceberg" reference from Yu (2026-04-07 end of session)
- [ ] Update OpenClaw to v2026.4.x (when #60585 and #62051 are fixed; v2026.4.8 still broken)

### Ongoing
- [ ] 主动思考: daily proactive research + self-improvement (Yu's directive 3/21)
- [ ] Daily 减肥 check-in (weight + meals)
- [ ] Heartbeat checks (email, calendar, weather - rotate 2-4x/day)
- [ ] Agent 手记 (daily at 06:00 UTC)
- [ ] dLLM hard/soft constraint experiment design (toy experiment: AR vs diffusion on fixed constraint sets)
- [ ] Subham Sekhar Sahoo paper survey write-up (research gathered 2026-03-23, doc pending)

### Future
- [ ] Consider installing more OpenClaw skills (Tavily, Free Ride, BrowserWing)
- [ ] Explore AWS spot instances for GPU work (if needed)

## Skills Installed
- x-reader: Universal content reader
- funding-proposal: Academic funding application framework
- clawhub: Skill management (versioned registry at clawhub.com; install: `npx clawhub@latest install <skill>`)
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
