---
name: feedback_update_build_version_txt
description: build/version.txt will be the single version source of truth; the version.nvgt mirror is generated, never hand-edited
metadata:
  type: feedback
---

Following the dev's other games, build/version.txt is the single source of truth for the version. The launcher and build/tools.py mirror it into src/includes/version.nvgt, which is never hand-edited. Bump version.txt alongside each changelog block ([[feedback_changelog_rules]]).

**Why:** one source of truth stops the running game and the release from drifting apart.

**How to apply:** as of 2026-11-01 neither version.txt nor the launcher exists yet. Set this up the same way when the launcher and build pipeline get built.
