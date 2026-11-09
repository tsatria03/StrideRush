---
name: project_practice_deaths_plan
description: SETTLED, not built (2026-11-09, for 1.8; 2 sections) - in a practice run, losing your last life (or a hazard fall) is a death like the real game's, "You died." and Enter, then you try again from just past the obstacle with everything back; Q&A log
metadata:
  type: project
---

Status: SETTLED, nothing built. Started 2026-11-09, after the difficulty scaling plan was settled and committed (a89e742).

Background:
- The dev (2026-11-09): "I was thinking for practice. It will behave like hazards where you will dye, but you are able to press entry to try again, and it will pass the obstical for you."
- Now ([[project_game_menu_refactor_plan]]): a practice run is one obstacle type at a fixed speed, with practice_lives 2 and 2 steel shields, and can't be lost; every hit but a hazard takes health (full damage, settled in [[project_difficulty_scaling_plan]]) and the last life never goes, so health just refills. A hazard fall already works the way the dev describes: practice_set_down() in hazard.nvgt pauses the run, plays the fall, shows "You died." (dlgmessage_return, Enter), waits for the key to be let go, sets you on the ledge just past the hazard (me.x = h.x + 1), catches the spawner up, resumes and plays a landing.

Q&A log:
- Q (2026-11-09): does every hit stop you like a death, dropping health, lives and the practice shields? Claude recommended yes. A (dev, 2026-11-09): "Every hit is not supposed to stop you dead. I was thinking that it will use up your 2 lives, then it will kill you like in the real game, but let you try again." SETTLED: practice keeps health, its 2 lives and its shields; hits take health as now; when the last life would go, you die as in the real game (death sounds, "You died."), then Enter lets you try again, set down just past the obstacle that killed you; a hazard fall stays an instant death, as now.
- Q (2026-11-09): what trying again gives back: a fresh start (full health, 2 lives, shields topped back up to 2, keys kept, same speed, from just past the obstacle) or only health and 1 life? Claude recommended the fresh start. A (dev, 2026-11-09): "Yes. It gives you everything back." SETTLED: full health, practice_lives 2, steel shields topped up to 2, keys kept.
- Q (2026-11-09): a hazard fall in practice: also give everything back, or set you past it keeping health, lives and shields as now? Claude recommended giving everything back. A (dev, 2026-11-09): "yes, for consistency" SETTLED: every practice death, a hazard fall or a last life lost, gives everything back.
- Q (2026-11-09): how a practice death from a hit sounds: the run frozen as the pause menu freezes it (only the ambience plays on), the hit and the player death sound, no tile fall, "You died." for Enter, then set down just past the obstacle with everything back, the paused sounds resuming and a landing as after a practice hazard? A (dev, 2026-11-09): "yes" SETTLED as proposed.
- SETTLED (2026-11-09), every question answered. Build sections (one per go-ahead):
  1. Practice deaths: when a practice run's last life would go (lives.nvgt, where a real run calls end_run_hit()), and on a practice hazard fall (practice_set_down() in hazard.nvgt), one shared practice death: pause_game(), the death sounds, "You died.", wait for the key to be let go, set down just past the obstacle that caught you, spawner_catch_up(), then the fresh start (full health, practice_lives 2, steel shields topped up to 2, keys kept), resume_game() and a landing. Endless and debug runs unchanged.
  2. Docks: a 1.8 changelog entry, the readme's practice runs part, the todo item to finished, this plan COMPLETE, MEMORY.md and CLAUDE.md.
- CHANGED (dev, 2026-11-09, before the build): dlgmessage_return() no longer takes space or mentions it (the dev edited deps/dlg.nvgt: "now it's just press enter to continue"), so every "You died." here closes with Enter only.
