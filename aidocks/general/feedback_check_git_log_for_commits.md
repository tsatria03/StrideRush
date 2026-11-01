---
name: feedback_check_git_log_for_commits
description: The dev commits their own work between turns; check git log/status before assuming commit state, and don't commit unless asked
metadata:
  type: feedback
---

Once this project is a git repository, the dev will commit their own work between turns. Before assuming or asking about commit state, check git log and git status. Never commit or push unless asked.

**Why:** guessing commit state leads to wrong advice and redundant questions. Carried over from SimpleFighter and ToyMania.

**How to apply:** as of 2026-11-01 this folder is not a repo yet ([[project_runner_overview]]), so this applies once the dev creates it. Related: [[feedback_stage_commits_before_big_changes]].
