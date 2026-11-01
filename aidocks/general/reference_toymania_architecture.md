---
name: reference_toymania_architecture
description: ToyMania's launcher, include tree, build pipeline, menus, keybinds and helpers; the closest template for Stride Rush's skeleton
metadata:
  type: reference
---

ToyMania is closer in shape to Stride Rush than SimpleFighter: no map parser, a single game loop, glob includes. This is the likely template for the skeleton ([[reference_toymania_readonly]]).

Skeleton:
- Entry: src/tm.nvgt main().
  - Startup order: load achievements, create the save folders, readdata, readpreffs, HRTF and pool setup, single-instance check (instance), speech buffers, setup_keybinds, logo, updater, then mainmenu().
  - The same file holds pause_game(), resume_game(), resetgame() and resetpreffs().
- Includes: src/includes/includes.nvgt is only glob includes: version.nvgt plus main/deps/*, main/functions/*, main/globals/* and main/menus/*. Stride Rush already has those four folders plus parsers/.
- Launcher: tm/tm.py.
  - It runs C:\nvgt\nvgt.exe ../src/tm.nvgt with cwd tm/, so bare sounds/, data/ and docks/ paths resolve under the asset folder.
  - It mirrors build/version.txt into src/includes/version.nvgt and writes compile errors to tm/errors.txt.
- Build: build/tools.py (via tools.bat).
  - Stages: compile (nvgt -c -Q, then copy data/docks/lib/sounds), package (7z plus an Inno Setup installer), gh release, then a website update.
  - Config lives in build/tools.ini.

Game loop: toygame() is while(true){ wait(5); ... }.
- Each pass runs the entity loops, input, update_listener_2d on every pool, autosave and timed spawns.
- Movement is one tile per step, gated by movetimer >= movetime.
- Each step plays objects/platforms/<tile>/*step* for the tile under the player, found with gmt(x, y). That's directly reusable for the runner's footsteps.

UI and input:
- custom_menu (1-based results, -1 on Escape).
- dlg.nvgt: dlgmessage_return() and dlgplay().
- speak_buffer() with reviewable buffers.
- audio_form settings windows saved by writepreffs().
- input_conf keybinds from data/config/keyboard.ini, in the format action=MOD+KEY:trigger. It includes a rebind UI (keybindmenu, capture_key_combo).

Pools: one sound_pool per category, declared in dec.nvgt. decpool.nvgt adds pause_pools, resume_pools and the fade helpers.

**How to apply:** when the dev asks for the skeleton, propose adapting these pieces with paths renamed (tm to sr) and the pitfalls in [[reference_toymania_scoring_difficulty]] avoided. Line numbers drift, so search by symbol.
