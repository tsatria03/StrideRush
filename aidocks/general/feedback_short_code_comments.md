---
name: feedback_short_code_comments
description: code comments stay short and say what the code does and why; no dated dev quotes, dates or decision history in .nvgt files, which live in aidocks instead
metadata:
  type: feedback
---

The dev agreed (2026-11-15) with Claude's evaluation that the code has too many comments: "I feel like there are too many code commants here." Comments carried dated quotes like (dev, 2026-11-10: "..."), plan names and the history of earlier values, all of which already live in aidocks (the plans' Q&A logs and [[project_version_history]]).

**Why:** the history makes the files long and hard to read, and it duplicates the memory folder.

**How to apply:** in new or edited .nvgt code, write a comment only when the code isn't obvious, and keep it to what the code does and why it must be that way. No dev quotes, no dates, no "was X until Y", no plan names. Decisions and their reasons go in the plan file or the version history; anything that sounds like it fits better in a memory file goes into aidocks (dev, 2026-11-15: "if the comments sound like they would fit better in a memmory file, then it should deffenatly be moved"). Multi-line comments are still one /* */ block ([[feedback_multiline_comment_style]]). The cleanup of existing comments is planned in [[project_comment_cleanup_plan]].
