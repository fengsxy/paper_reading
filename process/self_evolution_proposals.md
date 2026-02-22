# Self-Evolution Proposals

每小时自动研究 OpenClaw 最佳实践并提案。Yu 审阅后决定是否执行。

---

## Proposal #1 — 2026-02-19 20:20 UTC
**创建 YouTube 转录 Skill（`~/.openclaw/skills/youtube-transcribe/`）**
来源：OpenClaw 社区最佳实践（Substack 技能指南）
问题：当前 yt-dlp + Whisper 转录流程的指令散落在 TOOLS.md 和各 cron prompt 中，每次 session 都要重复加载 cookies 路径、API key 等上下文。
方案：创建第一个 managed skill `youtube-transcribe`，包含 SKILL.md（cookies 路径、转录命令模板、输出格式规范）+ refs/（常用参数参考）。所有 cron 和 session 只需一句"用 youtube-transcribe skill"即可。
收益：消除重复上下文 ~200 tokens/session，单点更新，为后续 skill 化（podcast、scholar、hackernews）打样。
风险：零——只是新增文件，不改现有配置。

---

## Proposal #2 — 2026-02-19 21:20 UTC
**创建 MEMORY.md 长期记忆文件**
来源：AGENTS.md 自身规范 + 社区记忆管理最佳实践
问题：workspace 有 1349 行 daily memory（8个文件），但 MEMORY.md 不存在。AGENTS.md 明确要求主 session 加载 MEMORY.md 作为"策展后的长期记忆"，当前每次主 session 启动都没有长期上下文。
方案：从现有 `memory/2026-02-15.md` 到 `memory/2026-02-19.md` 中提炼关键决策、偏好、项目状态，创建 MEMORY.md（控制在 80 行以内）。内容分类：Yu 的偏好/习惯、活跃项目状态、重要决策记录、工具配置要点。
收益：主 session 立即获得持续上下文，减少重复解释，agent 表现更连贯。
风险：零——纯新增文件。建议 Yu 审阅初版内容确认准确性。

---

## Proposal #3 — 2026-02-20 17:20 UTC
**为 openclaw.json 添加 context pruning 配置，降低 token 消耗**
来源：Skywork "Clawdbot Developer Lessons" 生产模式指南 + Hostinger OpenClaw 最佳实践
问题：当前配置只有 `compaction: { mode: "safeguard" }`，缺少 `pruning` 设置。大量 cron job 和 subagent 的 tool 输出（web_fetch、exec 等）会在活跃上下文中累积，浪费 token。
方案：在 `agents.defaults` 中添加 pruning 配置：`"pruning": { "mode": "cache-ttl", "ttl": "1h", "keepLastAssistants": 3 }`。这会自动丢弃超过 1 小时的大体积 tool 结果，只保留最近 3 轮 assistant 回复。
收益：显著减少长 session 的 token 消耗，compaction 触发频率降低，session 响应更快。
风险：低——pruning 只影响上下文窗口中的旧 tool 结果，不删除 transcript 持久化数据。可随时调整 ttl 值。

---

## Proposal #4 — 2026-02-20 18:20 UTC
**为 subagent 和 cron session 启用 sandbox 隔离**
来源：OpenClaw 官方 sandboxing 文档 + Hostinger 安全最佳实践（"Use isolated environments for execution"）
问题：当前配置无 sandbox 设置，所有 cron job 和 subagent 的 exec/web_fetch 等工具直接在宿主机运行。self-evolution cron 每小时抓取外部网页，web_fetch 内容可能包含恶意 prompt injection，无隔离意味着 blast radius 是整个系统。
方案：在 `agents.defaults` 中添加：`"sandbox": { "mode": "non-main", "scope": "session", "workspaceAccess": "ro" }`。主 session（直接对话）不受影响，仅 cron/subagent 在 Docker 容器中运行。需先执行 `scripts/sandbox-setup.sh` 构建镜像。
收益：cron 和 subagent 的文件系统/进程访问被隔离，即使处理恶意外部内容也不影响宿主机。符合最小权限原则。
风险：中——需要 Docker 环境，sandbox 内无网络（默认），需配置 `docker.network` 允许出站；部分依赖宿主机路径的操作（如 yt-dlp cookies）需通过 `docker.binds` 挂载。建议先测试一个 cron job 再全面启用。

---

## Proposal #5 — 2026-02-20 19:20 UTC
**配置 model fallbacks 实现多 provider 自动故障转移**
来源：OpenClaw 官方 Model Failover 文档（`/concepts/model-failover.md`）
问题：当前配置了 3 个 provider（yunyi-codex、fucheers-claude、yunyi-claude），但 `agents.defaults.model` 只设了 `primary`，没有 `fallbacks`。如果 yunyi-codex 宕机或限流，所有 session（包括 cron）会直接失败，无自动恢复。
方案：添加 fallback 链：`"model": { "primary": "yunyi-codex/gpt-5.2", "fallbacks": ["yunyi-claude/claude-opus-4-6", "fucheers-claude/claude-opus-4-5-20251101"] }`。当主模型所有 auth profile 失败后，自动切换到 Claude，保证服务连续性。
收益：零停机——任一 provider 故障时自动降级到备用模型，cron job 和主 session 均不中断。利用已有的 3 个 provider 配置，无额外成本。
风险：极低——fallback 仅在主模型失败时触发，正常情况下不影响行为。不同模型的输出风格可能略有差异，但胜过完全无响应。

---

## Proposal #6 — 2026-02-20 20:20 UTC
**将例行 hourly cron job 切换到零成本模型（gpt-5.2），仅保留高质量任务用 opus**
来源：OpenClaw 官方 Cron Jobs 文档（model overrides 章节）+ 当前 cron 配置分析
问题：当前 4 个 hourly cron job 全部使用 `yunyi-claude/claude-opus-4-6`（cost: input=5, output=25），包括 "Hourly Progress Report"、"Self-Evolution Research"、"Transcribe Watchdog"、"Podcast 300 Progress Drive"。而 `yunyi-codex/gpt-5.2` 成本为零，完全能胜任这些例行任务。
方案：用 `openclaw cron edit` 将 4 个 hourly job 的 model 改为 `yunyi-codex/gpt-5.2`。仅保留每日任务（Paper Digest、Karpathy RSS 等需要深度分析的）继续用 opus。
收益：每小时节省 4 次 opus 调用的 token 费用，每天节省 ~96 次 opus 调用。gpt-5.2 对于 web 抓取、状态汇报、文件检查等例行任务绑绑有余。
风险：低——如果 gpt-5.2 质量不够，可随时改回。建议先切 1 个 job 观察一天再全面推广。

---

## Proposal #7 — 2026-02-20 21:20 UTC
**添加 session.maintenance 配置，自动清理过期 session transcript 文件**
来源：OpenClaw 官方 Configuration Examples（`session.maintenance` 章节）+ 当前配置审计
问题：当前 `openclaw.json` 完全没有 `session` 配置。9 个 cron job（4 个 hourly）每次运行都创建独立 session transcript（`.jsonl` 文件），这些文件会无限累积在磁盘上。与 Proposal #3（内存中 context pruning）不同，这是磁盘层面的清理。
方案：添加 `"session": { "maintenance": { "mode": "warn", "pruneAfter": "30d", "maxEntries": 500, "rotateBytes": "10mb" } }`。超过 30 天的 session 文件会被清理，单个 transcript 超过 10MB 会轮转。`mode: "warn"` 先只告警不删除，确认安全后改为 `"prune"`。
收益：防止磁盘空间被废弃 session 文件逐渐吃满；hourly cron 每天产生 ~96 个 session 文件，一个月就是 ~2880 个。
风险：极低——`mode: "warn"` 只记录日志不执行删除，可以先观察哪些文件会被清理，确认无误后再启用实际清理。

---

## Proposal #8 — 2026-02-20 22:20 UTC
**启用 compaction.memoryFlush，在上下文压缩前自动保存记忆**
来源：OpenClaw 官方 Memory 文档（`/concepts/memory.md` — "Automatic memory flush" 章节）
问题：当前 compaction 配置仅 `{ "mode": "safeguard" }`，没有 `memoryFlush`。当主 session 长对话触发 auto-compaction 时，上下文中的重要决策、偏好、临时笔记会被压缩摘要替代，如果 agent 没有主动写入 memory 文件，这些信息就永久丢失了。
方案：扩展 compaction 配置：`"compaction": { "mode": "safeguard", "memoryFlush": { "enabled": true, "softThresholdTokens": 4000 } }`。在 compaction 触发前 ~4000 tokens 时，自动插入一个静默 agent turn 提醒写入 `memory/YYYY-MM-DD.md`。
收益：长对话中的关键上下文不再因 compaction 而丢失；与 Proposal #2（创建 MEMORY.md）互补——有了文件还需要有自动写入机制。
风险：极低——flush turn 默认静默（NO_REPLY），用户无感知；仅在接近 compaction 阈值时触发一次，不增加常规 token 消耗。

---

## Proposal #9 — 2026-02-21 16:20 UTC
**添加 logging 配置，启用结构化日志记录**
来源：OpenClaw 官方 Configuration Examples（`logging` 章节）
问题：当前 `openclaw.json` 完全没有 `logging` 配置。9 个 cron job（4 个 hourly）+ 多个 subagent 每天产生大量运行，但错误、rate limit、provider 故障等事件完全不可见。排查问题只能靠猜测或手动 `openclaw logs` 实时查看，无法回溯历史。
方案：添加 `"logging": { "level": "info", "file": "/tmp/openclaw/openclaw.log", "consoleLevel": "warn", "consoleStyle": "pretty", "redactSensitive": "tools" }`。日志写入 `/tmp/openclaw/` 避免占用 workspace，`redactSensitive: "tools"` 自动脱敏 tool 输出中的 API key 等敏感信息。
收益：provider 故障、cron 失败、rate limit 等问题可通过日志快速定位；`redactSensitive` 防止敏感信息泄露到日志文件；为后续监控告警（Proposal #4 sandbox 等）提供基础设施。
风险：极低——只是新增日志输出，不影响任何现有行为。`/tmp` 目录重启自动清理，不会无限增长。

---

## Proposal #10 — 2026-02-22 16:20 UTC
**启用 boot-md hook 并创建 BOOT.md 网关启动自检脚本**
来源：`openclaw hooks list` 显示 `boot-md` hook 已 ready 但未启用；ClawHub 社区 startup-validation 最佳实践
问题：gateway 重启后（手动或崩溃恢复），没有任何自动验证机制。cron job 是否正常注册、API provider 是否可达、磁盘空间是否充足、关键文件（cookies、SSH key）是否存在——全靠人工检查。当前 9 个 cron job + 3 个 provider，任何一个静默失败都可能数小时后才发现。
方案：1) 在 `hooks.internal.entries` 中添加 `"boot-md": { "enabled": true }`；2) 创建 `BOOT.md`，内容为：检查 cron 数量是否符合预期、ping 各 provider endpoint、检查磁盘使用率、验证 cookies/key 文件存在、将结果发送到 Telegram。
收益：gateway 每次启动自动执行健康检查，问题在秒级发现而非小时级；与 Proposal #9（运行时日志）互补——这是启动时的一次性验证。
风险：极低——boot-md 仅在 gateway 启动时运行一次，不影响正常运行；BOOT.md 内容可随时调整。

---

