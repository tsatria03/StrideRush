---
name: project_angelscript_block_comment_star_slash
description: A star-slash sequence inside a /* */ comment closes it early, so the rest parses as code; easy to hit when a comment names a glob or path pattern
metadata:
  type: project
---

A /* */ comment ends at the first star followed by a slash, even mid-word. A comment that writes a glob like key_step_ star slash key_strafe (written with real asterisks) closes early and the remaining prose fails to compile.

**Why:** comments in the dev's games often name sound globs and paths. SimpleFighter hit this in 2026-09.

**How to apply:** in a block comment never put a slash right after an asterisk. Drop the asterisk, add a space, or use a // comment. Related: [[feedback_multiline_comment_style]].
