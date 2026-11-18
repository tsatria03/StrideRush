---
name: project_free_run_spacing_plan
description: SETTLED (2026-11-18), not built: a free run spacing choice, so obstacles and items come closer together or further apart than the usual gap; first of the todo list's four free run items for 2.5; Q&A log
metadata:
  type: project
---

Started 2026-11-18 (dev: "Yes, the spacing option will come first.", after reordering the todo list's free run items: spacing, lanes, powerups, combination pairs), on 3500a42. 2.5 holds 5 of 10. Built on [[project_free_run_plan]] and [[project_free_run_tools_plan]]. Not built; no sections yet.

## Findings (2026-11-18)
- The todo item: "Add a spacing choice to a free run, so obstacles and items can come closer together or further apart than the usual gap for your speed."
- spawner.nvgt's next_gap(): ledge_after_tiles (2) + a random stretch of floor, floor_tiles(run_min_floor_time) to floor_tiles(run_max_floor_time), + the next one's countdown (countdown_length, always 5 steps) + 1, never under min_gap_tiles (6). floor_tiles() turns ms into tiles at the current speed, never under min_floor_tiles (2).
- difficulty.nvgt: a free run has no difficulty, so it uses min_floor_time 1000 to max_floor_time 4000 ms, chaos's floor (easy 2000 to 5000). So today's free run spacing is 1 to 4 seconds of floor between one obstacle and the next one's countdown.
- The countdown itself can't shrink (five cues, one per step), so "closer" means less floor, down to the 2-tile minimum, never overlapping countdowns (only combinations do that).

## Q&A log
- Q1 (Claude, 2026-11-18): the choice's form. Proposed: a console item "modify spacing" with five settings, as seconds of floor between one thing and the next one's countdown: very close (just the 2-tile minimum), close (0.5 to 2 seconds), normal (1 to 4, today's, the default), far (3 to 6) and very far (6 to 10); "Currently set to normal spacing." and opening on the current one, like the other modify items. Recommended: as proposed, presets rather than typing numbers, since a range of two numbers is awkward to enter and these cover the useful span.
- A1 (dev, 2026-11-18): "I like that. Menu items for obstical spaces." The five presets as menu items.
- Q2 (Claude, 2026-11-18): the details. Proposed: "modify spacing" sits in the console in alphabetical order, after modify shield strength (shown only with a shield worn, so otherwise after modify running speed) and before start running and view current setup, offered both standing and running; it covers everything the belt brings, obstacles and items alike, since they share one spawner gap; a change applies from the next gap on, not to what's already placed; "Your spacing is now close." in the misc buffer; view current setup gains "spacing, close"; every new free run starts on normal, and a replay or restart keeps the choice, as speed and the other settings do. Recommended: as proposed.
- A2 (dev, 2026-11-18): "yes."
- Q3 (Claude, 2026-11-18): the sections. No sounds needed. Proposed: 1. Spacing: freerun.nvgt's free_spacing (0 very close to 4 very far, 2 normal), reset to normal by reset_free_settings() and kept through replays; tuning.nvgt's free_spacing_min_times {0, 500, 1000, 3000, 6000} and free_spacing_max_times {0, 2000, 4000, 6000, 10000}; spawner.nvgt's next_gap() uses them in a free run (0 to 0 gives just the 2-tile floor minimum); the console's "modify spacing", its menu "Choose how far apart things come on the belt. Currently set to normal spacing." with very close, close, normal, far and very far spacing, then back, opening on the current one; "Your spacing is now close." in misc; view current setup's "spacing, close". Tests. 2. Docks: one changelog entry on top of 2.5 (6 of 10, wording proposed then); the readme's free run section; the todo item to finished; the version history and CLAUDE.md. Recommended: as proposed.
- The dev (2026-11-18): "Review the change log wording first, then I'll commit. Do that for a plan before I commit it." (saved as [[feedback_changelog_wording_in_plan]]). Q4 (Claude): the entry, on top of 2.5 (6 of 10): "Added a spacing choice to a free run's console, from very close to very far, so obstacles and items can come closer together or further apart than usual."
- A3 and A4 (dev, 2026-11-18): the sections were proposed and the entry approved ("Yes.").

## THE PLAN IS SETTLED (2026-11-18)
1. Spacing: freerun.nvgt's free_spacing (0 very close, 1 close, 2 normal, the default, 3 far, 4 very far), reset by reset_free_settings(), kept through replays; tuning.nvgt's free_spacing_min_times {0, 500, 1000, 3000, 6000} and free_spacing_max_times {0, 2000, 4000, 6000, 10000} (ms of floor); spawner.nvgt's next_gap() uses them in a free run; the console's "modify spacing" (alphabetical, standing and running): "Choose how far apart things come on the belt. Currently set to normal spacing.", very close, close, normal, far and very far spacing, back, opening on the current one; "Your spacing is now close." in misc; view current setup's "spacing, close". Tests.
2. Docks: the entry on top of 2.5 (6 of 10): "Added a spacing choice to a free run's console, from very close to very far, so obstacles and items can come closer together or further apart than usual."; the readme's free run section; the todo item to finished; the version history and CLAUDE.md.

## Build log
- Not started.
