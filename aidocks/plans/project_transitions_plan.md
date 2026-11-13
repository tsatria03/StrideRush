---
name: project_transitions_plan
description: OPEN (2026-11-13, for 2.1) - the code follows the dev's new transitions folders (doors, ladders, trampolines, slides, switches), learn sounds gains transitions; Q&A log
metadata:
  type: project
---

Status: OPEN (2026-11-13), in Q&A. 2.1 at 8 of 10; this is its ninth entry.

Background:
- The dev's commit 3525a70 (2026-11-13) and a follow-up: each environment has transitions/ beside traps/: doors (general/door to door4, countdown), ladders (general/metal, countdown), trampolines (general/tramp to tramp5), slides (general/plastic: loop, move, start, stop; were misc/game/slideground, slidemove, slidestart, slidestop) and switches (general/switch: press; was misc/game/switchpress). Also a new trap, traps/floor_breakers/general/air (spawn, loop, fall, fill, fix1-3), for 2.2.
- The code still uses the old paths: door_folder() and trap_folder(env, "ladders"/"trampolines"), misc/game/slide* in slide.nvgt, misc/game/switchpress in forcefield.nvgt; learn sounds lists only traps/ (learn_environment_category()). So doors, ladders and trampolines can't spawn, slides and the switch press are silent.
- The dev (2026-11-13): "Exactly right. We can also save floor breakers for 2.2 as well." Timed runs went to 2.2 too ([[project_timed_run_plan]]), so 2.1 ends with this plan at 9 of 10 unless something else comes.

Q&A log:
- Q: Learn sounds: a third list per environment, transitions, laid out like traps (doors, ladders, slides, switches, trampolines, each by theme); the door and ladder countdowns stay in countdowns with the rest? (Asked 2026-11-13; Claude recommended it.) A: "Yes. WIll it appear before traps, or after" (dev, 2026-11-13). Before: the lists sort alphabetically, countdowns, transitions, traps.

Settled design: not yet.

Sections: not yet.
