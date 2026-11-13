---
name: project_transitions_plan
description: COMPLETE (2026-11-13, 2.1 at 9 of 10; 2 sections) - the code follows the dev's new transitions folders (doors, ladders, trampolines, slides, switches), learn sounds gains transitions; Q&A log
metadata:
  type: project
---

Status: COMPLETE (2026-11-13, 2.1 at 9 of 10). 2.1 at 8 of 10; this is its ninth entry.

Background:
- The dev's commit 3525a70 (2026-11-13) and a follow-up: each environment has transitions/ beside traps/: doors (general/door to door4, countdown), ladders (general/metal, countdown), trampolines (general/tramp to tramp5), slides (general/plastic: loop, move, start, stop; were misc/game/slideground, slidemove, slidestart, slidestop) and switches (general/switch: press; was misc/game/switchpress). Also a new trap, traps/floor_breakers/general/air (spawn, loop, fall, fill, fix1-3), for 2.2.
- The code still uses the old paths: door_folder() and trap_folder(env, "ladders"/"trampolines"), misc/game/slide* in slide.nvgt, misc/game/switchpress in forcefield.nvgt; learn sounds lists only traps/ (learn_environment_category()). So doors, ladders and trampolines can't spawn, slides and the switch press are silent.
- The dev (2026-11-13): "Exactly right. We can also save floor breakers for 2.2 as well." Timed runs went to 2.2 too ([[project_timed_run_plan]]), so 2.1 ends with this plan at 9 of 10 unless something else comes.

Q&A log:
- Q: Learn sounds: a third list per environment, transitions, laid out like traps (doors, ladders, slides, switches, trampolines, each by theme); the door and ladder countdowns stay in countdowns with the rest? (Asked 2026-11-13; Claude recommended it.) A: "Yes. WIll it appear before traps, or after" (dev, 2026-11-13). Before: the lists sort alphabetically, countdowns, transitions, traps.

- Q: The rest (doors, ladders, trampolines found in transitions; slides from their environment's slide theme, a random one if more, none where there are none; the force field's switch press from the environment's switches; practice and debug unchanged), the entry "Made it so doors, ladders, trampolines, slides and force field switches now take their sounds from each environment, listed together under transitions in the learn sounds menu.", two sections? A: "Exactly right. I commited it. ready for section 1." (dev, 2026-11-13).

Settled design (2026-11-13):
- type_category(): doors, ladders, trampolines, slides and switches are transitions; every other type is a trap. trap_folder() and the countdown paths (play_countdown(), learn_countdown()) use it, so every caller finds its type where it now lives.
- Slides: each picks a theme from transitions/slides/general (plastic now) and plays its loop, start, move and stop; no slides where an environment has none.
- The force field's switch press: a random theme's press from transitions/switches/general in the field's environment.
- Learn sounds: per environment, countdowns (traps' and transitions' together), transitions, traps.
- The entry above, 2.1's ninth.

Sections:
1. The code: type_category(), trap_folder() and the countdown paths, slides, the switch press, learn sounds.
2. Docks: the readme's learn sounds part, the entry, CLAUDE.md, the version history, this plan COMPLETE.
- Section 1 built (2026-11-13): type_category() in env.nvgt behind trap_folder() and the countdown folders; slide.nvgt picks a theme per slide (slide_obj.theme, env; slide_folder_now for move and stop); forcefield.nvgt's press from switch_press_sound(); learn sounds' transitions list and both kinds' countdowns.
- Test 2 of 3 passed (dev, 2026-11-13), with a bug: "why do other items appear in the real door debug run? ... I should only see keys". Older than this plan (since 2026-11-09, only practice's real doors had it): a key spawn's 50 percent paired second item (item_pair_percent) could be any kind. Fixed: set_spawn_only() gives the debug "real doors" and "real doors, spread" choices item_lane_mode random too, so keys come alone. Debug only, so no changelog entry.
- Section 1 COMPLETE (dev, 2026-11-13): all 3 tests passed (doors, ladders and trampolines back; slides and the switch press; learn sounds' countdowns, transitions and traps, and real doors debug runs with keys only).
- Section 2 (docks) done (2026-11-13): the readme's learn sounds paragraph (transitions; no longer "just the default one"), the 2.1 entry (9 of 10), CLAUDE.md, the version history, the index. Plan COMPLETE. The dev also asked for a check of every debug spawn choice for things that shouldn't appear: none found beyond the real doors fix (single-type choices filter obstacle_types and gate every item, slide, trampoline, combination and real door mark on spawn_only "all"; item choices place only their kind; slides and trampolines are the full game by design).
