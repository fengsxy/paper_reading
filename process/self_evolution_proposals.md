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

