---
name: feedback_check_git_log_for_commits
description: The dev commits their own work between turns; ALWAYS check the latest commit before starting each section; check git log/status before assuming commit state; don't commit unless asked
metadata:
  type: feedback
---

The dev commits their own work between turns. Before assuming or asking about commit state, check git log and git status. Never commit or push unless asked.

**Why:** guessing commit state leads to wrong advice and redundant questions. Carried over from SimpleFighter and ToyMania.

Dev rule (2026-11-01): always check the latest commit (git log -1 plus git status) before starting each plan section, and say what it is. The dev commits between sections, and the new section must build on what actually landed.

**How to apply:** the repo was created 2026-11-01 (branch main, remote tsatria03/StrideRush; see [[project_runner_overview]]). Related: [[feedback_stage_commits_before_big_changes]].
