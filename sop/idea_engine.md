# Idea Engine SOP

## Goal
Deliver one actionable idea per day for Yu, with clear implementation path and rollback.

## Cadence
- Hourly: scan OpenClaw best-practice updates (YDC search only).
- Daily (09:00 America/Los_Angeles): deliver one new idea.
- Weekly (Sunday 10:00 America/Los_Angeles): review idea quality and backlog health.

## Idea Quality Gate
Each idea must include:
1. Problem
2. Idea
3. Why now
4. 1-hour MVP implementation
5. Risk + rollback

## Scoring (0-5 each)
- Impact
- Effort (reverse-scored: lower effort = higher score)
- Reversibility
- Reliability improvement
- User value today

Priority score = Impact + Effort + Reversibility + Reliability + User value

## Execution Rules
- Prefer low-risk, reversible changes first.
- No secrets in git.
- Verify externally visible claims with curl/HTTP status before reporting.
- If no high-value idea exists, deliver a micro-optimization.
