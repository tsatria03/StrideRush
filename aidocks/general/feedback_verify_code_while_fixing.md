---
name: feedback_verify_code_while_fixing
description: Re-locate by symbol not stored line number, confirm a reported finding is true, and flag adjacent bugs
metadata:
  type: feedback
---

When fixing something, find the target by symbol name rather than a remembered line number, confirm the reported problem is real before patching, and mention related problems you notice nearby instead of silently ignoring or silently fixing them.

**Why:** the dev runs and verifies builds, so a wrong or half-right edit costs a round trip. Line numbers in memories and reports go stale.

**How to apply:** grep for the symbol, read the real code, verify, then edit. Related: [[feedback_confirm_before_implementing]].
