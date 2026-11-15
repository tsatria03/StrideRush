---
name: project_comment_cleanup_plan
description: IN PROGRESS (2026-11-15): Section 1 (tuning.nvgt) BUILT AND TESTED, Section 2 (core files) BUILT AND TESTED, Section 3 next; one test per section, shown only when the dev is ready; memory-like comments move to aidocks: shorten the code comments across src/, removing dated dev quotes, dates, plan names and old-value history, comment-only edits in six sections; Q&A log
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
- One test per section (dev, 2026-11-15: "For these, only show 1 test when I'm ready. These shouldn't change how the game already plays."): ask whether the dev is ready, then a single test, usually a launch plus a short run touching the files changed.
- Removed history with no better home goes into a topic memory for that file or area (Section 1 made [[project_tuning_history]]), rather than being checked line by line against the plans.
- The strip-and-compare check: a small Python script in Claude's scratchpad (strip_compare.py, run with python -I) removes // and /* */ comments outside strings and blank lines from the committed file (git show HEAD:path) and the new one, and prints OK only if the code lines match exactly. Rewrite it if the scratchpad was cleared.

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
- Resumed (dev, 2026-11-15): "Ready for the code comment removal sections. For these, only show 1 test when I'm ready." Built one section per go-ahead, as usual.
- Section 1 BUILT (2026-11-15, on 245490c): tuning.nvgt rewritten comment by comment, every code line kept in place; strip-and-compare OK (172 code lines identical); dated quotes 79 to 0; 289 lines changed, 17 fewer lines. The removed history (earlier values, the dev's reasons and quotes, dates, plan names) went into [[project_tuning_history]], grouped by area. Also fixed while there: floor_pieces_max carried ladder_wall_gap's comment ("steps from a ladder to its real wall"), now on ladder_wall_gap; the life capsule and teleporter comment had drifted above the powerups block and now sits with its chances, and the teleport range comment with teleport_min_time; the file summary no longer promises "later sections" and says five-entry arrays are by level. The test passed (dev, 2026-11-15): it compiled and an easy endless run played as before. Section 2 (the core files) is next, on the dev's go-ahead.
- Section 2 BUILT (2026-11-15, the dev: "commited. ready for section 2."; built on e5a439e). Done by three parallel forks with the same rules, each reporting its removed history; Claude then re-ran the checks on all twelve files: every one strip-and-compare OK, CRLF on every line, dated lines 96 to 0, no other game names added; 208 insertions, 242 deletions. History into [[project_core_code_history]], by file. Stale comments fixed along the way, among them: game.nvgt's summary ("dying in later sections"), "you can't lose" in practice, and the two C-key blocks merged; spawner.nvgt's 7-type summary, key_before_door "debug only" (practice uses it), hand_window_start()'s "a single step" countdown (always five now), play_countdown()'s old misc/trap path; decpool's "later listener updates"; environments' "Section 2 adds the switch"; surface's footsteps_on (free run too); lane's "won't need redoing when the belt turns forward" and its old barrier_side() pointer; lives' player_hp (now max_health()); endrun's "two ways a run ends" and "no results dialog"; difficulty's has_joined() and level_damage() comments sitting above the wrong functions; practice's nonexistent practice_mix_pick() and stale barriers goal note; practice_hints' "all 16 kinds". The test passed (dev, 2026-11-15): it compiled; an easy endless run with a lane switch, a jump, C and a pause played as before; a hazards practice death gave the fall, the death dialog and the retry menu. Section 3 (the obstacles) is next, on the dev's go-ahead.
- Approach note: forks suit these sections (independent files, a fixed rule set, a mechanical check), as long as each returns its history instead of writing to aidocks, so only Claude writes the shared memory file.
