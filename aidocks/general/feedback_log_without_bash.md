---
name: feedback_log_without_bash
description: log test results and small plan or memory notes with the Read and Edit tools, not Bash and Python, so the dev isn't asked to approve a command for each one
metadata:
  type: feedback
---

Log test results, Q&A lines and other small notes in plans and memories with the Edit tool (after a Read of the spot), not a Bash or Python command (dev, 2026-11-18, during the free run combinations tests: "when you log things, try not to ask me for the bash commend each time. I mean do it without approval.").

**Why:** each Bash call asks the dev for approval, which interrupts testing; Edit and Read don't.

**How to apply:** Read the end of the plan, then Edit to append the line. Edit keeps a file's CRLF endings, so no eol.py check is needed for these. Keep Bash for real checks (git log, line-ending checks after big code edits) and multi-file dock writes. Related: [[feedback_test_steps_one_at_a_time]], [[feedback_no_crlf_normalization]].
