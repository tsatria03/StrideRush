---
name: feedback_changelog_rules
description: sr/docks/changelog.txt is a player-facing record of what changed; prose, reverse-chronological, bump build/version.txt with each block
metadata:
  type: feedback
---

sr/docks/changelog.txt is the source of truth for what shipped. It is a record, not a manual: player-facing prose, one idea per entry, newest block on top under a "New in X.Y." style header. Each new block pairs with a bump of build/version.txt to the same number ([[feedback_update_build_version_txt]]).

**Why:** players read it; engine internals, file names and how-to instructions don't belong there.

Newest on top applies inside a block too, not just between blocks (dev, 2026-11-02): the latest entry is the first line under the header, and the oldest is the last line of the block.

**How to apply:** describe the observable change in a sentence or two. Trust the changelog over the readme or todo list when they disagree. Keep lines short ([[feedback_dock_line_length_1024]]).
