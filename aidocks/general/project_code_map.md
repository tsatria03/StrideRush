---
name: project_code_map
description: Where Stride Rush's code lives (the core globals files, one file per obstacle or item type, the main/game splits) and every file a new obstacle type touches; moved out of CLAUDE.md 2026-11-27 to keep it under 10,000 characters
metadata:
  type: project
---

Moved out of CLAUDE.md on 2026-11-27 (dev: "I highly recommend splitting claude.md into memmory files because it's nearly at 10k chars."). CLAUDE.md keeps a one-line trigger pointing here.

## Core code

Core code lives in src/includes/main/globals/:
- tuning.nvgt: every tunable number (its history in [[project_tuning_history]]).
- game.nvgt: the run loop, step order, readouts.
- surface.nvgt and player.nvgt: footsteps, jump, crouch.
- spawner.nvgt: picks and places everything.
- lane.nvgt, lives.nvgt and endrun.nvgt: lanes, health, lives, how a run ends.
- difficulty.nvgt, practice.nvgt.
- decpool.nvgt: the pool registry ([[project_audio_model]]).

One file per obstacle or item type lives in src/includes/game/.

## The main and game splits

Code and sdr/sounds are each split into main/ (core) and game/ (gameplay content), as are sdr/data/config/ and sdr/docks/lang/<language>/. sdr/data/lang/ holds the .lng files.

## A new obstacle type

It touches ([[project_entity_pattern]]):
- its own file in src/includes/game/;
- spawner.nvgt: obstacle_types and place_obstacle();
- clear_run_objects() in endrun.nvgt;
- all_pools (decpool.nvgt);
- step_check() (game.nvgt);
- sounds: themes in sounds/game/environments/<env>/traps/<type>/general/ and warning cues in .../<type>/countdown/; creatures such as animals in traps/npc/<type>/, listed in npc_types in environments.nvgt;
- a pair-able type also needs its pair hooks (combo.nvgt).
