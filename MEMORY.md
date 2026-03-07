# MEMORY.md - Long-Term Memory

Last updated: 2026-03-07

## Yu's Preferences & Work Style

- **Work philosophy**: "我希望我不在的时候你能一直在思考" - expects continuous work, no asking for breaks
- **Communication style**: Prefers deep technical discussions, "关门弟子"式详细讲解
- **Decision making**: Switches priorities quickly, expects fast turnaround
- **Learning approach**: Understands concepts from "设计者思维"角度 ("他当时怎么想的")
- **Conversation preference**: Wants continuous flowing conversation, not strict Q&A format (feedback 2026-03-03)

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

### CS 202 Exam Prep (2026-02-27 - 2026-02-28)
- **Exam date**: March 20, 2026 (Friday 3-6pm)
- **Format**: Short answer (not T/F like Fall 2022)
- **Status**: Prep materials complete
  - 78 T/F questions + answers
  - 20 blog posts (~200KB, 2000字 each)
  - 5 review notes by topic
  - Mock exam created
- **Yu's approach**: Zero lectures attended, relying on PPT + AI tutoring

### Research Discussions

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

## Technical Setup

### OpenClaw
- **Version**: 2026.3.2 (updated 2026-03-03)
- **Host**: AWS EC2 Ubuntu 24.04 (34.229.201.123)
- **Update script**: `~/update_openclaw.sh`
- **Security**: yunyi token in `~/.openclaw/secrets/yunyi_token` (chmod 600)

### API Quotas
- **Yunyi**: Daily quota model (20,000/day), expires 2026-03-23
- **YDC Search**: Key in `~/.openclaw/secrets/ydc_api_key`
- **Groq**: GROQ_API_KEY for Whisper transcription
- **Grok**: xai-grok provider (grok-4-latest), configured as fallback (added 2026-03-04)

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

### Security (2026-02-26)
- **Issue**: HEARTBEAT.md had yunyi Bearer token in plaintext
- **Fix**: Moved to `~/.openclaw/secrets/yunyi_token`, updated HEARTBEAT.md to use $(cat ...)
- **Backup repo**: Rebuilt with orphan branch, old history force-pushed away

### System Stability (2026-03-03)
- **Issue**: Yu perceived "interruptions" during conversation
- **Root cause**: Frequent compaction attempts (every 20-30s) + Telegram network fallback
- **Not resource issue**: Memory/CPU/disk all sufficient
- **Solution**: Updated to OpenClaw 2026.3.2

### Conversation Style (2026-03-03)
- **Feedback**: "你怎么总是聊聊天就中断啊"
- **Issue**: Too strict Q&A format, not flowing conversation
- **Adjustment needed**: More proactive, continuous dialogue

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
- **MSFT**: 5 shares @ $403.21 cost basis
- **Tracking**: Daily via xueqiu_daily.py script

### Current Events (2026-03-03)
- **Iran War**: Major US-Israel conflict since Feb 28, Supreme Leader killed
- **Market impact**: Stock markets down ~2%, oil prices surged
- **Duration estimate**: 4-5 weeks expected

## TODOs

### Immediate
- [ ] Complete National Social Science Fund application (waiting for Yu's info)
- [ ] CS 202 exam on March 20 (prep materials ready)

### Ongoing
- [ ] Daily 减肥 check-in (weight + meals)
- [ ] Heartbeat checks (email, calendar, weather - rotate 2-4x/day)
- [ ] Agent 手记 (daily at 06:00 UTC)

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
