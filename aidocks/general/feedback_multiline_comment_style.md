---
name: feedback_multiline_comment_style
description: Multi-line code comments use one /* */ block, not stacked // lines; single-line comments stay //
metadata:
  type: feedback
---

A comment longer than one line is a single /* */ block, not several stacked // lines. One-line comments use //.

**Why:** the dev's preferred style; a screen reader announces every // separately.

**How to apply:** watch the star-slash trap inside block comments ([[project_angelscript_block_comment_star_slash]]).
