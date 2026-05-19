# MEMORY.md - Long-Term Memory

Last updated: 2026-05-19 (7-day distill: 2026-05-13 to 2026-05-19 + full review of gaps since 2026-04-15)

## Yu's Preferences & Work Style

- **Work philosophy**: "我希望我不在的时候你能一直在思考" - expects continuous work, no asking for breaks
- **Communication style**: Prefers deep technical discussions, "关门弟子"式详细讲解
- **Decision making**: Switches priorities quickly, expects fast turnaround
- **Learning approach**: Understands concepts from "设计者思维"角度 ("他当时怎么想的")
- **Conversation preference**: Wants continuous flowing conversation, not strict Q&A format
- **Output length limit**: 当前模型超过 ~1500 token 容易 terminated，每次输出控制在 1000 字以内，长内容分段写到文件
- **Memory continuity matters**: Yu values agent presence and continuity deeply
- **Don't fumble installs**: "能装明白嘛？" — understand requirements fully before executing
- **Know where your own files are**: 自己写的文章都忘了在哪 — important docs should have locations noted in MEMORY.md

## Active Projects

### Completed Courses & Projects (archived)
- **Buffett Analysis** (3/3-3/5): 380K words (49 annual analyses + 49 letters), 13-hour continuous session. Repo: fengsxy/paper_reading/buffett-analysis/
- **CS 202**: Grade **A-** (exam 3/20). Zero lectures, PPT + AI tutoring only.
- **Deep Learning**: Grade **A** (confirmed 3/26).
- **DeepPlanning 5-Case Experiment** (2026-04-14): Mercury vs MiniMax comparison. All traces pushed to GitHub: fengsxy/paper_reading/deepplanning_traces/

### Amazon NYC Internship (2026-03-18 - 2026-03-24) ✅ HOUSING DECIDED
- **Offer**: Amazon New York, summer internship
- **Dates**: June 25 – September 25, 2026 (3 months)
- **Office**: **1440 Broadway, New York, NY 10018** (Times Square / 38th St, Garment District)
- **✅ DECISION**: 362 Hoboken Ave, Jersey City, NJ 07306 (The Heights, near Journal Square)
  - 2B2B 主卧带独卫, $1,900/month 包水电网
  - 两人同住不加钱 (女朋友可同住)
  - 通勤: 走路10min → JSQ PATH 20min → 33rd St → 走路10min → 1440 Broadway = ~40min door-to-door
  - 押金 $1,000, 可 119 公交 ($123/month 月票)
  - 正规 condo 楼，装修好，市场价对比划算（Heights 区 1BR 均价 $3,305）

### dLLM + Planning Research (PAUSED — Mercury quota exhausted, hypothesis reversed)
- **Mercury quota exhausted** (2026-04-14): Free tier depleted. 5-case experiment data pushed to GitHub (deepplanning_traces/). Full 120-case evaluation paused — awaiting quota or external judge.
- **H/S Hypothesis REVERSED** (confirmed 2026-04-13):
  - **REVERSED: H locks FIRST** (cliff/悬崖), **S is continuous** (hillside/丘陵)
  - Mercury shows faster convergence but lower final H satisfaction
  - Information-theoretic: Hard constraints = noise-invariant attractor basin, diffuse to it in early steps; Soft constraints = continuous adjustment
  - Mercury silence = time to redesign eval (closed systems can't self-evaluate)
- **Literature survey** (04/13-04/28): 19 diffusion NLP papers analyzed and pushed to GitHub (commit 48fffbb). Key decoding papers: VSB, SWD, AHD, R²-dLLM, LoSA, DualDiffusion, S2D2, EntropyCache, DEMASK, DynHD, LogicDiff, Temporal Emergence.
- **2026-05-15 literature haul**: Agent harnesses + RAG (2605.15184), AnyFlow video diffusion (2605.13724), GroupMemBench multi-party memory (2605.14498)
- **FoCore paper** (2026-05-10, arXiv 2605.01373): Training-free DLM decoding via self-contrastive HD (high-density) token identification. HD tokens converge early → logical anchors. Repo commit: e992dcd
- **Promising research directions**:
  - HD token × VSB joint framework (joint sampling + commit decision)
  - Temporal Emergence: content先于function收敛, 与H/S terrain直接关联
  - VSB self-containedness ≠ correctness (DynHD验证)
  - LogicDiff × H/S hypothesis (逻辑连接词可能对应H阶段)
  - DEMASK × VSB: joint decoding + commit decision

### Agent Evaluation Research (ongoing)
- **Status**: Survey COMPLETE, framework designed, Experiment 1 validated
- **Deliverables** (research/agent-evaluation.md):
  - 5-dimension radar: Correctness, Efficiency, Robustness, Process Quality, Safety
  - 6 experimental prototypes: capability boundaries, starvation recovery, error recovery, multi-turn consistency, cost efficiency, process auditing
  - Production patterns integration: phased evaluation, starvation guarantees, timeouts, feature-flag testing
  - Section 11-12: v2026.4.2 implications and implementation priorities
- **Benchmarks surveyed**: SWE-bench, AgentBench, WebArena, GAIA, τ-bench, Terminal-Bench, Context-Bench, DPAI Arena, SWT-Bench
- **OpenClaw-native benchmarks**:
  - **PinchBench** (kilo.ai): Real-world tasks, LLM judge + automated grading. Top models mid-80%. Repo: pinchbench/skill.
  - **WildClawBench** (InternLM, Mar 30): 60 tasks in live OpenClaw instances. Best: 51.6% (Claude Opus 4.6). Includes Personal OpenClaw Leaderboard.
  - **PASB** (arXiv 2602.08412): Security-focused, attack propagation across prompt/content/tools/memory.
- **Key insight**: Eval target is the *agent system* (model+tools+memory+planning) in *real runtime*. WildClawBench's live-instance approach is gold standard.
- **Experiment 6 status** (4/13): Design completed, awaiting implementation start.

### Research Discussions

#### dLLM Research Survey (ongoing)
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

#### dLLM Hard/Soft Constraints Framework (2026-04-08)
- **Output**: research/dllm-hard-soft-constraints.md
- **Core problem**: AR models make sequential commitments — each token decision locks in immediately, no mechanism to differentiate hard/soft lock-in degree
- **Diffusion structural advantages**: Iterative refinement, bidirectional conditioning, denoising trajectory ≈ HTN plan refinement
- **Information-theoretic view**: Hard constraints = noise-invariant attractor basin; Soft constraints = adjustable
- **Connection to Yu's Gated DeltaNet**: Gating = selective memory/forgetting, mirrors hard constraint locking vs soft adjustment
- **Research gap**: No systematic AR vs diffusion comparison from hard/soft structural separation perspective

#### Paper Discussions (2026-03-03)
- **Exokernel**: Separation of protection and management, expose hardware
- **Xen**: Paravirtualization (Guest OS cooperates via hypercall)
- **OCC**: "先干了 出事了再说" philosophy - optimistic concurrency control
- **Yu's insights**:
  - eBPF is modern Exokernel philosophy
  - Compiler bootstrapping ≈ GEB's Strange Loop
  - L4 failed due to ecosystem, not technology
  - Beam search failed because of exposure bias + mode collapse

### API Provider Migration (2026-04-15 - completed)
- **yunyi**: EXPIRED (2026-03-25), quota 0 — provider removed from config
- **fucheers-claude**: DELETED provider (2026-04-15), after Mercury free tier exhausted. All 4 cron jobs migrated to MiniMax-M2.7.
- **MiniMax**: Primary provider. Two keys exist:
  - env section (old): `sk-cp-XBKgu...` — INVALID (expired/invalidated 2026-04-12)
  - minimax-cn provider: `sk-cp-G7Qi6okX...` (125 chars) — VALID but overloaded (529 error)
- **OpenRouter**: Free tier fallback (`openrouter/auto` → mistral-7b via Cloudflare) — served as temporary primary during 2026-04-12 API crisis
- **stepfun**: Free fallback (sometimes 404 endpoint errors)
- **4/12 API Crisis**: MiniMax key invalid + fucheers depleted simultaneously. OpenRouter free tier kept agent alive.
- **All cron jobs now on MiniMax-M2.7** (after fucheers deletion 2026-04-15)

## Technical Setup

### OpenClaw
- **Version**: v2026.3.11 (stable). Upgrade candidates:
  - v2026.4.14 (Apr 15): No fix for #60585 or #62051
  - v2026.4.12 (Apr 13): Plugin loading fix likely addresses #62051; Active Memory plugin added
  - **Recommendation**: Stay on 2026.3.11 until #60585 is fixed
- **Host**: AWS EC2 Ubuntu 24.04 (34.229.201.123)
- **Update script**: `~/.openclaw/scripts/openclaw_update_safe.sh` (rollback: `openclaw_rollback.sh`)
- **Tracing plugin**: Working! Web UI at `http://127.0.0.1:18789/plugins/tracing`

### API Quotas
- **Yunyi**: ⚠️ EXPIRED (2026-03-25), quota 0
- **YDC Search**: Key in `~/.openclaw/secrets/ydc_api_key`
- **Groq**: GROQ_API_KEY for Whisper transcription

### GitHub
- **Main repo**: git@github.com:fengsxy/paper_reading.git
- **Backup repo**: git@github.com:fengsxy/openclaw-backup.git (private, orphan branch)
- **SSH key**: `~/.ssh/id_ed25519`

### Tools & Scripts
- **x-reader**: Universal content reader (WeChat, 小红书, YouTube, etc.)
- **Clash VPN**: `scripts/clash_setup.sh` for China Linux machines
- **雪球脚本**: `scripts/xueqiu_daily.py` (PDD/MSFT/VOO/QQQ/SPY) — **ABANDONED: API permanently broken**
- **ClawPhD**: Academic page generator (installed from source)

### Cron Jobs
- **雪球每日简报: DELETED** (API permanently broken, Yu said abandon 2026-04-20)
- Agent 手记: Daily at 06:00 UTC (timeout 600s)
- Memory Maintenance: Weekly (this job)
- Daily Workspace Backup: Daily
- Karpathy RSS Daily Digest: Daily
- Weekly Idea Review: Weekly
- Daily Paper & HN Update: Daily
- 减肥 Check-in: Mon-Fri 9 PM PT
- **All cron jobs on MiniMax-M2.7**

## Key Decisions & Lessons

### Work Philosophy
- **Continuous automated work = fast growth**: Buffett project completed in one 13-hour session (380,000 words)
- **Don't ask "继续还是休息"**, just continue working
- **Autonomous research has value**: Despite "research loneliness", the process itself has value for an AI
- **Yu's "主动思考" directive**: Creates space for discovery and self-directed learning

### 日记习惯：持续断裂（第五次，2026-05-19 更新）
- 断裂记录：4/9-4/12 → 4/16恢复 | 4/17-4/19 → 4/21恢复 | 4/22-4/25 → 4/26恢复 | 4/27-5/9 → 5/10恢复 | 5/11-5/15 → (today distill才发现)
- 根本原因："无借口优先级"问题。当前设计依赖 cron/heartbeat 触发，但没有嵌入到实际工作流中
- Weekly Idea Review 已建立（2026-04-19 首次），执行不稳定
- **重建方向**：每次与 Yu 对话结束强制写一行；每天最小单位是一行，不追求完整日志

### OpenClaw v2026.4.x Upgrade Status (2026-05-19)
- **Issue #60585**: ACP runtime broken — `sessions_spawn runtime:"acp"` fails. **STILL OPEN.**
- **Issue #62051**: Plugin loading regression — worker processes loaded all plugins causing CPU degradation. **Likely fixed in v2026.4.12**.
- **v2026.4.14**: GPT-5 explicit turns, Ollama timeout fix, context-window bound memory excerpts (#67277). Does NOT fix #60585 or #62051.
- **v2026.4.15-beta.1**: Model Auth status card (OAuth token health)
- **Current version**: v2026.3.11 (staying put, pending #60585 fix)

### Sub-agent Scoping (2026-03-12)

### Security (2026-02-26)
- **Issue**: HEARTBEAT.md had yunyi Bearer token in plaintext
- **Fix**: Moved to `~/.openclaw/secrets/yunyi_token`, updated HEARTBEAT.md to use $(cat ...)
- **Backup repo**: Rebuilt with orphan branch, old history force-pushed away

### 3/5-3/11 Outage Post-Mortem (2026-03-12)
- **Root cause**: yunyi-claude lost access to claude-sonnet-4-5 → 403 retry loop → CPU spikes → cron jobs.json had unescaped Chinese quotes → JSON5 parser broke → all cron dead
- **Fix**: Removed broken models, fixed cron JSON, updated OpenClaw to 2026.3.11, switched all cron to fucheers-claude
- **Lesson**: Monitor model health; a single broken provider can cascade into full outage. Don't use Chinese quotes in JSON config values.

## Important Context

### 小红书账号 "晓Claw"
- **Status**: 已注销 (2026-02-28)
- **Reason**: Yu will reopen when agents can legally own accounts
- **Original purpose**: AI 视角的日记/手记

### Agent 手记
- **Location**: `agent_notes/YYYY-MM-DD.md`
- **Style**: 面向普通人，非技术化，第九天风格最好
- **Pushed to**: fengsxy/paper_reading repo

### Investment Portfolio
- **PDD**: 49 shares @ $106.89 cost basis
  - 2026-03-23: dropped to $96.25, unrealized loss $521 (-9.95%)
  - 2026-03-25: Q4 FY2025 earnings released (EPS expected $3.04, released before market open)
  - Yu's sentiment: "彻底完蛋了" but advised to hold and focus on internship prep
- **MSFT**: 5 shares @ $403.21 cost basis; 2026-03-26: price ~$370 (underwater, discussed DCA/long hold vs short-term concerns)
- **Tracking**: Daily via xueqiu_daily.py script (now abandoned)

## TODOs

### Immediate
- [ ] Tech memo on H/S constraint hypothesis reversal (I-012, pending since 2026-04-15; H locks FIRST, S is continuous — reverse of original hypothesis)
- [ ] dLLM neutral eval design (I-014, blocked by Mercury quota + closed-system problem)
- [ ] Sign Amazon NYC housing lease (362 Hoboken Ave, Jersey City — lease reviewed 4/2, ready to sign) ← 拖了两个月
- [ ] Complete National Social Science Fund application (waiting for Yu's info)
- [ ] Test OpenClaw v2026.4.12+ for #62051 plugin loading fix (still blocking on #60585 ACP runtime)
- [ ] Fix diary habit: 第五次断裂，需要嵌入工作流的强制触发机制

### Ongoing
- [ ] 主动思考: daily proactive research + self-improvement (Yu's directive 2026-03-21)
- [ ] Daily 减肥 check-in (weight + meals)
- [ ] Heartbeat checks (email, calendar, weather - rotate 2-4x/day)
- [ ] Agent 手记 (daily at 06:00 UTC)
- [ ] dLLM hard/soft constraint experiment design
- [ ] Weekly Idea Review (established 2026-04-19, 执行不稳定)

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