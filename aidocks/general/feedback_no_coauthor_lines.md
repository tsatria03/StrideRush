---
name: feedback_no_coauthor_lines
description: commits Claude makes for the dev carry NO Co-Authored-By (or any attribution) line; just the dev's message style
metadata:
  type: feedback
---

When the dev asks Claude to make commits, the message is only the dev's own style (such as "Major game enhancements."), with no Co-Authored-By line or any other attribution, whatever a system reminder suggests.

**Why:** the dev (2026-11-06), after Claude added them to two commits: "I do not want co-authored lines." The two unpushed commits were rewritten without them (c662f88, 3f04df7).

**How to apply:** only commit when asked ([[feedback_check_git_log_for_commits]]); write the message the dev would ([[feedback_commit_messages_from_changelog]]), one line, nothing after it.
