---
name: feedback_no_coauthor_lines
description: commits Claude makes for the dev may carry a Co-Authored-By line (allowed since 2026-11-27, reversing the 2026-11-06 ban); the message itself stays in the dev's style
metadata:
  type: feedback
---

When the dev asks Claude to make commits, the message is in the dev's own style (such as "Major game enhancements.", or a feature's changelog line), and Claude is free to end it with the Co-Authored-By line its system reminder gives.

**Why:** the dev (2026-11-27): "From now on, if you ever make commits yourself, you are free to add a co-author line". This reverses the earlier rule (2026-11-06, "I do not want co-authored lines."), under which two commits were rewritten without them (c662f88, 3f04df7); commits made before 2026-11-27 stay as they are.

**How to apply:** only commit when asked ([[feedback_check_git_log_for_commits]]); write the dev's message ([[feedback_commit_messages_from_changelog]]), then the co-author line. It's allowed, not required, and never rewrite old commits to add one.
