---
name: project_environments_plan
description: STARTED, NO QUESTIONS YET (2026-11-10, for 2.0) - sounds/environments/<env>/{audio,platforms,traps}, chosen before a run or switched automatically during one (zones folded in); background, the design so far and the questions to ask; Q&A log
metadata:
  type: project
---

Status: STARTED (2026-11-10), questions not asked yet, like [[project_combined_obstacles_plan]]. The dev: "Yes. You can start this plan." Ask the open questions below one per turn once the dev says to go on.

Background:
- The dev's idea (2026-11-10), in their words: "Remember when I removed nearly all of the run surfaces in an earlier commit in v1x? I was thinking of bringing them back, but this time, I'd create an environments folder. This folder will have the following. An env name, such as factory. In that factory, you'd have the objects folder with the current audio/platform/trap folders in it. That way, only sounds that belong to that env can go in there, and then you can switch to a different one in the game, either automaticly durring a run, and or manually if it asks witch env you want to play on."
- The surfaces: objects/platforms held 132 folders from 2026-11-03 ([[project_sound_layout]]); the dev's 1.8 sound commit (5c885c4) removed most, leaving 46 (concrete variants and ledge among them). They come back sorted into environments.
- Zones, Claude's suggestion 5 ([[project_suggestions]]), fold in as the automatic mode: the belt passes from one environment to the next, perhaps at real doors, each with its own ambience, surfaces and favoured obstacle mix.
- Now: objects/audio (tracks, ambiences), objects/platforms (surfaces, ledge) and objects/traps (one theme folder per obstacle type) are single shared pools; surface.nvgt, run.nvgt (start_run_audio(), the ambience crossfade), spawner.nvgt and each obstacle file pick themes from them at runtime with get_pack_sound_folders(); the learn sounds menu is built from the folders.

The design so far (Claude, 2026-11-10, not yet confirmed point by point):
- Layout (corrected by the dev, 2026-11-10: "The objects folder will be gone. Instead of environments/envname/objects, it will just be, environments/envname/, then the 3 main folders."): sounds/environments/<env>/audio, /platforms and /traps per environment, with no objects level; the top-level objects folder goes too; equipments, misc, ui and anything not tied to a place stay shared at the top level.
- Two ways to play: manual (choose an environment before a run, perhaps after the difficulty) and automatic (the run moves between environments, perhaps at each real door: zones).
- Each environment needs at least one theme for every obstacle type with its own sounds, or a shared fallback; the ledge lives in each environment or stays shared.
- The learn sounds menu would show environments, perhaps a category each.
- A rule change to record: [[project_sound_layout]] says sounds/ never gets a level that switches whole sets (no packs). Environments are a deliberate partial version of that, the dev's decision; record it there when settled.

Open questions, to ask one per turn later:
1. Which environments to start with, and which sounds go in each (the dev gathers and sorts the sounds; nothing is built until they exist, [[feedback_sounds_before_features]]).
2. What stays shared: is any obstacle type, the ledge, the music, or the countdowns shared across environments?
3. Missing sounds: if an environment lacks an obstacle type's theme, does that type not spawn there, or fall back to a shared folder?
4. Manual choice: where the environment menu sits (after the difficulty, or after the mode), whether practice and debug runs get it too, and whether choices are locked like difficulties.
5. Automatic switching: at real doors, after a time, or per speed section; announced or silent; the order (fixed or random); and whether each environment favours some obstacles (zones' "favoured mix").
6. Is there a "mixed" choice (every environment's sounds together, as today) or does every run belong to one environment at a time?
7. Music and ambience: per environment, with the shuffle and crossfade working inside the current one; what happens to the music at a switch.
8. Statistics and achievements: environments reached, a furthest environment, per-environment records.
9. The learn sounds menu layout.
10. Moving today's sounds: which current folders go to which environment, and whether that happens in one go.

Q&A log:
- Correction (dev, 2026-11-10): no objects folder: sounds/environments/<env>/audio, platforms and traps, and the top-level sounds/objects folder is gone, its three folders moving into the environments.
- First step done (dev, 2026-11-10: "I just started the sound reorg. The default will be the main env used in the game. We will not be adding new enviornments yet. In the code, all you have to do right now is to just repoint the old sound paths."): the dev moved sounds/objects to sounds/environments/default (707 files, unchanged); Claude repointed every objects/<audio|platforms|traps> path to environments/default/<...> (38 places in 15 files: animal, barrier, door, endrun, forcefield, hazard, mine, player, projectile, run, spawner, spike, surface, wall and learn_sounds_menu). No behavior change; the plan's questions stay unasked.
