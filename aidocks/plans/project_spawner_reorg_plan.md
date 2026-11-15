---
name: project_spawner_reorg_plan
description: SETTLED, NOT BUILT (2026-11-15, the dev: "write, but not build"): split choose_next_obstacle() in spawner.nvgt into a dispatcher with one function per kind of run (real game, debug, practice, free run), plus the quick fix for place_obstacle()'s if/else; three sections, behavior unchanged; Q&A log
metadata:
  type: project
---

Started 2026-11-15 from Claude's whole-game evaluation, point 3 (the spawner is the riskiest file). The dev agreed with all three sections and asked for the plan written but not built. Not player-facing: no changelog entry, no version bump.

## The problem (measured 2026-11-15)
- choose_next_obstacle() mixes the real game's logic with about 15 early-return special cases keyed on spawn_only strings for debug, practice and free run.
- spawn_only is checked 51 times: 36 in spawner.nvgt, the other 15 spread over animal, barrier, combo, freebelt, freerun, game, lives, shield and menu (1 to 3 each). 24 distinct strings: "all" (the real game, 10 checks), free run's "free", practice's practice_doors, practice_mixed, practice_trampolines and mixed_walls, and the rest debug choices (barriers_random, animals_dogs, the item _random and _multiple choices turned into item_lane_mode by set_spawn_only(), and so on). A single-obstacle practice run uses the plain type as spawn_only (such as "hazards") and goes through the generic path.
- The fragile spot, place_obstacle() at spawner.nvgt:436 to 441: after the belt-wide types' practice_hint() call, the trampolines, ladders, floor_breakers and vehicles spawn calls are else-ifs chained onto that hint check, not onto the spawn chain. Correct today only because the hint list and those four types don't overlap; adding one of them to the hint list would stop it spawning, with no error.

## The order that must survive (choose_next_obstacle() as of 2026-11-15)
The order of the cases is part of the game's rules; every section checks the new code against this list.
1. real_doors (debug): a key, then a real door, in turn.
2. practice_doors: after a key its real door; otherwise a key or a fake door, half and half.
3. free: free_next_type(), a combination through choose_combo().
4. nothing (debug): no spawns.
5. keys (debug): every spawn a key.
6. animals_birds, animals_dogs (debug): every spawn an animal.
7. barriers, barriers_random, barriers_multiple (debug): every spawn a barrier.
8. In "all" and real_doors_spread, unless slide_holds(): the next real door's key when key_due().
9. Same condition: the real door at the next speed mark.
10. real_doors_spread (debug): nothing between the marks.
11. combo_debug_only() (debug): every spawn a pair.
12. The available list: types matching spawn_only (all, practice_trampolines and mixed_walls take several), ladders only when ladders_ready(), has_joined() for the difficulty schedule, a theme folder present, barriers barrier_weight times.
13. practice_mixed: a random kind from practice_mix_kinds(), a real door as its key then the door.
14. practice_trampolines: every other spawn a trampoline, otherwise from the available list.
15. The item roll, in this order: the single-item debug choices, slides, trampolines, life capsules, health potions, teleporters, powerups, steel shields, ammo packs (survival items also pass survival_roll()); otherwise a random obstacle from the available list, which in "all" becomes a combination combo_percent() of the time.
next_countdown is set the same way at every exit: countdown_steps(), or 0 when nothing spawns.

## Sections
1. The quick fix and the real game. place_obstacle(): every type's spawn call in one if/else-if chain, the practice_hint() call for the belt-wide types on its own after it. choose_next_obstacle() becomes a short dispatcher, and the real game's path (cases 8, 9, 12 and 15 for "all") moves into its own function, untouched in order. Tests: an endless run on easy and on a higher level (doors, keys, items, combinations, slides and trampolines still come), and one single-obstacle practice run.
2. The debug choices: cases 1, 4 to 7, 10, 11 and the single-item choices from 15 into one debug function the dispatcher calls first. Tests: a sample of debug spawn choices (real doors, real doors spread, nothing, keys, an animal, a barrier choice, combinations, an item's three lane choices).
3. Practice and free run: cases 2, 3, 13 and 14 (and mixed_walls' share of 12) into a practice function and a free run function. Tests: practice doors, mixed obstacles, trampolines, mixed walls, a rising practice run, and a free run with a batch and a continuous rule.

## Rules
- Behavior unchanged: code moves, almost nothing is rewritten; the order above is kept exactly, random() calls in the same order so the odds stay the same.
- The other 9 files' spawn_only checks stay as they are.
- Out of scope unless the medium version proves not enough: splitting the kind of run from the obstacle type (replacing strings like barriers_random with two settings), which reaches into the debug menu, practice and free run.
- New code follows [[feedback_short_code_comments]]; CRLF; the usual NVGT gotchas ([[project_angelscript_braceless_if]] matters most here, since the quick fix is about a braceless else-if chain).
- One section per go-ahead, the latest commit checked first, test steps one at a time ([[feedback_test_steps_one_at_a_time]]).

## Q&A log
- Q (Claude, 2026-11-15): how big is this change? A: two levels. The quick fix is about five lines in one file; the reorganization is medium, about 200 of spawner.nvgt's 485 lines moving, mostly in one file; the real cost is testing every path by ear. Three sections proposed.
- A (dev, 2026-11-15): "I agree with all 3 sections, and yes, write, but not build." Settled; waiting for the dev's go-ahead to build Section 1.
