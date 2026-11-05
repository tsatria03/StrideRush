---
name: feedback_stage_commits_before_big_changes
description: Proactively flag a commit break point before a large or risky change so safe pieces land first; before a big commit, tell the dev how many changes git shows and what they are
metadata:
  type: feedback
---

Before starting a large or risky stage, say so and suggest the dev commit what's finished first, so the risky change sits in its own commit.

**Why:** it keeps history reviewable and makes the risky change easy to revert. The dev commits their own work ([[feedback_check_git_log_for_commits]]) but likes being told when a break point arrives.

**How to apply:** flag the break point, then proceed once they've had the chance.

Say the count before a big commit (dev, 2026-11-04: "in the future, please tell me how many changes git shows before I make a huge commit"): after the dev's sound reorganization plus code showed 202 entries in git, which surprised them. Whenever a turn ends with a lot uncommitted (a sound move, a rename sweep, many files), run git status and tell the dev the number of entries git will show and roughly what they are (for example 180 deleted at old paths, 6 new folders, 9 code files), noting that a moved file counts twice (a delete and an add) until it's staged. Do it in the turn's wrap-up, before the dev commits, not after.
