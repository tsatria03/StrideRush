---
name: project_end_of_run_plan
description: BUILT in the first build (2026-11-02; results dialog deferred to scoring) - what happens when a run ends (a game-ending hazard, or losing the last life): the sounds at the moment of loss, any spoken results, and where the player goes next; Q&A log
metadata:
  type: project
---

Status: BUILT and tested in the first build (Sections 4 and 6, committed by 69dedf8; code in globals/endrun.nvgt and lives.nvgt). Settled 2026-11-01. Death sounds are per obstacle kind, then straight back to the main menu.

Already settled elsewhere:
- The player starts with 1 life. Hazards end the game regardless; spikes cost 1 life and mines 2. So in the basic game any mishap ends the run ([[project_obstacles_plan]]).
- The obstacle's own clip plays on contact: hazard fall, spike hit, or mine explode then hit.
- Lives readout is L; H is unused ([[project_controls_plan]]).
- Sounds-first rule: misc/player/death and misc/player/hit now exist (added 2026-11-01). There's still no separate game-over or results sound (misc/game has only pause and resume), so any such sound waits until the dev adds it ([[feedback_sounds_before_features]]).

Reference: ToyMania's death flow (end of toygame() in globals/game.nvgt) does this:
1. record_game_completion(), and a heartstop sound if the heartbeat was on.
2. Cleans up every spawner, object, buffer and the inventory.
3. Blocking dlgplay of misc/player death, then the floor tile's fall clip.
4. A results dialog: level, mode, toys, keys, guards, cars, steps and time.
5. Adds playtime, offers an optional copy or export menu, saves, and calls mainmenu().

Borrow the two-sound death and the results dialog. Avoid its copy-pasted cleanup, the recursive mainmenu(), playtime counted only at the end, and "Better luck next time!", which breaks [[feedback_one_sentence_game_messages]].

Death sounds by obstacle kind (dev, 2026-11-01, modeled on SimpleFighter at the dev's direction):
- Hazards: the death sound IS the hazard's own objects/traps/hazards/<name>/fall clip. No player death and no tile fall.
- Mines: three sounds start at once: the mine's explode, the mine's hit, and misc/player/hit. If the run ends, misc/player/death plays next, then the current platform tile's fall clip. Each of those two waits for the one before it to finish.
- REVISED after testing (dev, 2026-11-02): on a FATAL spike or mine hit, misc/player/hit does NOT play. The object's sounds (spike hit; mine explode and hit) play together with misc/player/death, then the tile's fall. misc/player/hit is only for hits you survive. The object's sounds go through the player pool so the run's silencing doesn't cut them off. The tile's fall waits until BOTH the death and the object's sounds have finished (dev: "the hit/explode/player death sound should play first, then the tile's fall sound").
- Spikes, and force fields later: the obstacle's hit and misc/player/hit play together. On a run-ending hit, misc/player/death plays, then the tile's fall clip, the same as mines.
- SimpleFighter reference: builder/traps/mine.nvgt plays explode, hit and the character's hurt (painslot) at once. Then checkdeath() leads to playerdeath() in construction/checkpoint.nvgt, which does a blocking dlgplay of the character's death clip, then dlgplay of the tile's fall (gmt(x, y)). spike.nvgt and forcefield.nvgt follow the same pattern, and hazards play their own fall instead.
- Recap confirmed by the dev, one type at a time (2026-11-01):
  - Hazards: "exactly right". Only the hazard's fall plays, waited on, then the run ends.
  - Spikes: confirmed after trimming the folder to loop and hit. Hit plus player hit together, costing 1 life. With lives left, life plays and the run continues; on the last life, player death then tile fall, each waited on. Spikes are non-destroyable.
  - Mines: confirmed. spawn, then light arms it a few tiles out, then the loop ticks; jumped over, it goes quiet behind you. On contact, explode, the mine's hit and player hit start at once, costing 2 lives. On the last life, player death plays, then the tile's fall plays after it ("the tile fall sound plays after the death, upon 1 life").
- Where a life is lost but the run continues (later, with more lives): the hit sounds plus misc/player/life, with no death or fall.

After the death sounds (basic build; dev, 2026-11-01): the game goes straight back to the main menu, with no results dialog. For spikes and mines that's after the tile's fall clip; for hazards, after the hazard's own fall clip. A results dialog (distance, time and so on) is deferred to the later scoring work ([[reference_toymania_scoring_difficulty]]). Mid-run, the Q, E, T and F readouts still give distance, speed, time and score.

The return must not re-call mainmenu() from inside the game loop the way ToyMania and the friend's template do. The run function returns, and main()'s existing while loop reopens the menu.

Q&A log:
- Q: After a run ends: straight to the main menu, results then the menu, or results then "Play again"? (Claude recommended results then the menu.) A: The dev first asked how ToyMania ends a game; the reference above was the answer. Still open.
- Q: Death order: the obstacle's sound, then player death, then the tile's fall? A: The dev refined it by kind (2026-11-01). misc/player/hit is for force fields, mines and spikes hitting you. misc/player/death plays only for force fields, mines and spikes. The tile's fall clip also plays only for those, since hazards come with their own fall sound.
- Q: Exact order for a mine? A: For hazards, the death sound is hazards/<name>/fall.ogg. For mines, all three sounds play at once (explode, the mine's hit, the player's hit), followed by the tile's fall. The dev pointed to SimpleFighter's death sounds to resolve it, and SimpleFighter also plays the player's death between the hits and the tile fall, so that's how it's recorded (2026-11-01).
- Q: Does a mine death play the player's death before the tile's fall? A: Yes. The tile's fall plays after the death, on the last life (dev, 2026-11-01).
- Q: After the death sounds, a results dialog then the main menu? A: For the basic build, it goes back to the main menu right after the tile's fall sound for those traps (dev, 2026-11-01). No results dialog yet.
