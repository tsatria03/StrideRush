---
name: feedback_changelog_rules
description: sr/docks/changelog.txt is a player-facing record of what changed; prose, reverse-chronological, bump build/version.txt with each block
metadata:
  type: feedback
---

sr/docks/changelog.txt is the source of truth for what shipped. It is a record, not a manual: player-facing prose, one idea per entry, newest block on top under a "New in X.Y." style header. Each new block pairs with a bump of build/version.txt to the same number ([[feedback_update_build_version_txt]]).

**Why:** players read it; engine internals, file names and how-to instructions don't belong there.

Newest on top applies inside a block too, not just between blocks (dev, 2026-11-02): the latest entry is the first line under the header, and the oldest is the last line of the block.

REVISED (dev, 2026-11-03): MAJOR versions (x.0, such as 1.0) hold up to 20 entries, and MINOR versions (1.1, 1.2 and so on) hold up to 10. 1.1 had 8 of 10 then, so 2 were left. The original rule follows. A version block holds at most 20 entries (dev, 2026-11-02: with 14 entries, "1.0 has room for 6 more entries"). When a block is full, the next entry starts a new block on top with the next version number, paired with a build/version.txt bump. Blocks have no intro or summary line: the dev removed "The first release of Stride Rush..." from 1.0, so every line under the header is an entry.

1.0 CLOSED (dev, 2026-11-03): tagged V1.00 at commit ca6f256 with all 20 entries. The next player-facing change opens a "New in 1.1." block on top, and build/version.txt goes from 1.0 to 1.1 at the same time ([[feedback_update_build_version_txt]]). Never add to a closed, tagged block.
1.1 CLOSED (dev, 2026-11-03): tagged V1.10 at commit abcb495 with all 10 entries. The tag format is V<major>.<minor>0 (V1.00, V1.10). The next player-facing change opens "New in 1.2." on top and bumps build/version.txt from 1.1 to 1.2.

Wording (dev, 2026-11-03): an entry for something new starts "Added ...". An entry that changes how something already in the game behaves starts "Made it so ...", like the dev's rewrite of the first 1.1 entry ("Made it so every trap now plays its full five-step warning countdown at any speed, instead of ..."). ToyMania's changelog uses the same two openings. The dev also adds "now" after "Made it so ..." ("Made it so you can now crouch again ...", "Made it so the ground now changes ..."), so write it that way.

**How to apply:** describe the observable change in a sentence or two. Trust the changelog over the readme or todo list when they disagree. Keep lines short ([[feedback_dock_line_length_1024]]).
1.2 OPENED (2026-11-03) by keys ([[project_keys_plan]]): "New in 1.2." holds 3 of 10 entries, and build/version.txt is 1.2. Shields ([[project_shields_plan]]) added 2 more on 2026-11-03, so 1.2 holds 5 of 10.
