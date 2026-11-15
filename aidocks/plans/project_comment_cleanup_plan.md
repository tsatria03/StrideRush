---
name: project_comment_cleanup_plan
description: DEFERRED (2026-11-15, the dev: build it later, not now; the trimming question answered, memory-like comments move to aidocks): shorten the code comments across src/, removing dated dev quotes, dates, plan names and old-value history, comment-only edits in six sections; Q&A log
metadata:
  type: project
---

Started 2026-11-15 from Claude's whole-game evaluation, point 7; the dev: "I completely agree with this one. I feel like there are too many code commants here." The rule going forward is [[feedback_short_code_comments]].

## Size (measured 2026-11-15)
src/ holds 21,278 lines: 814 whole-line // comments, 850 trailing // comments, 536 /* */ blocks, and 559 lines with a dated dev quote across 61 files. The heaviest: tuning.nvgt 79, menu.nvgt 57, freerun.nvgt 37, settings_menu.nvgt and stats_menu.nvgt 21 each, spawner.nvgt 19, practice.nvgt 17, learn_sounds_menu.nvgt 16.

## Rules for every section (proposed)
- Comment-only edits: no code line changes. After each section, a check strips the comments from the old and new files and compares them, so any change to the code shows up.
- Remove: dev quotes, dates, plan names, "was X until Y" history, and comments that repeat what the line plainly says.
- Keep, shortened: each file's opening summary, the reason behind any order or value that isn't obvious (the jump-before-step order in run_loop(), the HRTF dummy sound, key_pressed being one-shot), and what each tuning value means and its unit.
- A comment that would fit better in a memory file moves to aidocks (dev, 2026-11-15): decisions and their reasons into the feature's plan or [[project_version_history]], lasting facts about a system into its topic memory (such as [[project_audio_model]]). Already recorded there, it's just deleted.
- Watch for an asterisk followed by a slash when rewriting a /* */ block ([[project_angelscript_block_comment_star_slash]]); preserve CRLF; don't touch indentation.
- Not a player-facing change, so no changelog entry.

## Sections (proposed)
1. tuning.nvgt alone: the heaviest file, and a sample of the new style for the dev to judge before the rest.
2. The core: game.nvgt, spawner.nvgt, player.nvgt, surface.nvgt, lane.nvgt, lives.nvgt, endrun.nvgt, difficulty.nvgt, practice.nvgt, practice_hints.nvgt, environments.nvgt, decpool.nvgt.
3. The obstacles: hazard, spike, mine, forcefield, projectile, wall, door, barrier, animal, wind, ladder, floor_breaker, vehicle, combo, slide, trampoline.
4. Items and the rest of globals: weapons, bullet, ammo, keys, shield, capsule, potion, teleporter, powerup, inventory, heartbeat, stats, achievements, timerun, freerun, freebelt, updater and the rest.
5. menus/.
6. functions/ and deps/: only the dated comments; the deps' own original comments stay.

## Q&A log
- Q (Claude, 2026-11-15): how far should the trimming go? Recommended: keep short comments that explain why, and remove only the history and comments that repeat the code; the alternative strips almost everything but file summaries and gotcha warnings. A (dev, 2026-11-15): "if the comments sound like they would fit better in a memmory file, then it should deffenatly be moved." So the recommended depth: short why-comments stay in the code, and anything memory-like moves to aidocks rather than being lost (the rule above).
- Deferred (dev, 2026-11-15): "Since you already wrote the plan, we can build it later, not now." Nothing built; no section started. Until then, new code follows [[feedback_short_code_comments]] anyway.
