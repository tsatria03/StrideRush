---
name: feedback_tell_when_to_commit_plans
description: Tell the dev when a plan's discussion is settled with all its Q&A recorded, so they can commit it; the dev does the commit
metadata:
  type: feedback
---

When a plan's discussion reaches a settled point and all its answers are in the plan's Q&A log, say so plainly: "the X plan is settled; this is a good time to commit it". The dev asked for this on 2026-11-01.

**Why:** the dev commits each plan with its recorded answers, so that every design decision lands in history as a unit. They rely on me to flag the moment, rather than tracking it themselves.

**How to apply:**
- After the last open question of a plan is answered and logged, check git status and tell the dev which aidocks files are ready to commit.
- Also flag it mid-plan if a big batch of answers has piled up.
- Never commit myself ([[feedback_check_git_log_for_commits]]).
- Related: [[feedback_plans_record_qna]], [[feedback_stage_commits_before_big_changes]].
