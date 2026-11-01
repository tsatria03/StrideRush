---
name: feedback_stage_commits_before_big_changes
description: Proactively flag a commit break point before a large or risky change so safe pieces land first
metadata:
  type: feedback
---

Before starting a large or risky stage, say so and suggest the dev commit what's finished first, so the risky change sits in its own commit.

**Why:** it keeps history reviewable and makes the risky change easy to revert. The dev commits their own work ([[feedback_check_git_log_for_commits]]) but likes being told when a break point arrives.

**How to apply:** flag the break point, then proceed once they've had the chance.
