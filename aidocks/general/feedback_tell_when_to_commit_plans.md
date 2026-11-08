---
name: feedback_tell_when_to_commit_plans
description: Tell the dev when a plan is settled so they can commit it, then WAIT: never start building until the dev says the plan (or plans) is committed
metadata:
  type: feedback
---

When a plan's discussion reaches a settled point and all its answers are in the plan's Q&A log, say so plainly: "the X plan is settled; this is a good time to commit it". The dev asked for this on 2026-11-01.

**Why:** the dev commits each plan with its recorded answers, so that every design decision lands in history as a unit. They rely on me to flag the moment, rather than tracking it themselves.

**How to apply:**
- After the last open question of a plan is answered and logged, check git status and tell the dev which aidocks files are ready to commit.
- Also flag it mid-plan if a big batch of answers has piled up.
- Then wait. Don't build a settled plan, not even after a go-ahead like "build the 2 plans", until the dev says they've committed it; check git status shows the plan files committed (dev, 2026-11-08: "Oh wait I need to commit the plans first. Remember to always wait untill I commit a plan, and or plans.", after I started editing code with both 1.7 plans still untracked).
- Never commit myself ([[feedback_check_git_log_for_commits]]).
- Related: [[feedback_plans_record_qna]], [[feedback_stage_commits_before_big_changes]].
