# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## GitHub

- **Repo:** git@github.com:fengsxy/paper_reading.git
- **SSH Key:** `~/.ssh/id_ed25519` (ed25519, added to GitHub 2026-02-18)
- **Workspace:** `/home/ubuntu/.openclaw/workspace`

## Secrets Location

敏感信息存放在 `~/.openclaw/secrets/`（不进 git）：

- **YouTube Cookies:** `~/.openclaw/secrets/youtube_cookies.txt`
  - 用于 yt-dlp 下载 YouTube 视频
  - 使用: `yt-dlp --cookies ~/.openclaw/secrets/youtube_cookies.txt <url>`
- **API Keys:** 需要设置环境变量
  - `GROQ_API_KEY` - 用于 Whisper 转录（免费，https://console.groq.com/keys）
  - `OPENAI_API_KEY` - 备用转录方案

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
