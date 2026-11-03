---
name: feedback_changelog_rules
description: sr/docks/changelog.txt is a player-facing record of what changed; prose, reverse-chronological, bump build/version.txt with each block
metadata:
  type: feedback
---

sr/docks/changelog.txt is the source of truth for what shipped. It is a record, not a manual: player-facing prose, one idea per entry, newest block on top under a "New in X.Y." style header. Each new block pairs with a bump of build/version.txt to the same number ([[feedback_update_build_version_txt]]).

**Why:** players read it; engine internals, file names and how-to instructions don't belong there.

Newest on top applies inside a block too, not just between blocks (dev, 2026-11-02): the latest entry is the first line under the header, and the oldest is the last line of the block.

A version block holds at most 20 entries (dev, 2026-11-02: with 14 entries, "1.0 has room for 6 more entries"). When a block is full, the next entry starts a new block on top with the next version number, paired with a build/version.txt bump. Blocks have no intro or summary line: the dev removed "The first release of Stride Rush..." from 1.0, so every line under the header is an entry.

1.0 CLOSED (dev, 2026-11-03): tagged V1.00 at commit ca6f256 with all 20 entries. The next player-facing change opens a "New in 1.1." block on top, and build/version.txt goes from 1.0 to 1.1 at the same time ([[feedback_update_build_version_txt]]). Never add to a closed, tagged block.

**How to apply:** describe the observable change in a sentence or two. Trust the changelog over the readme or todo list when they disagree. Keep lines short ([[feedback_dock_line_length_1024]]).
