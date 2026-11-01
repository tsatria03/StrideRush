---
name: project_sound_layout
description: sr/sounds/ follows ToyMania's folder tree but with NO top-level sound packs (sounds/ is the root); wildcard lookup picks a random numbered variant
metadata:
  type: project
---

sr/sounds/ copies ToyMania's tree, not SimpleFighter's. Scaffolded folders as of 2026-11-01: equipments/items, equipments/weapons, misc/game, misc/player, misc/store, objects/doors, objects/platforms, objects/sources/ambiences, objects/sources/tracks, ui/dialogs/default, ui/menus/default, ui/other. No sound files yet, and no pack folder level yet.

How ToyMania does it (reference, in ToyMania's src/includes/main/functions/extrafuncts.nvgt):
- Packs: sounds/<pack>/..., with three selectors soundpack, dlgpack and menupack, each defaulting to "default".
- get_sound(path) builds "sounds/"+soundpack+"/"+path and passes it to find_sound_in_disk(), which globs and returns a random match. So get_sound("misc/player/*heal*") picks one of heal1-3. More variations just means more numbered files.
- Typical clip names: platforms have step1-5, land and fall; misc/game has countdown, launch, logo, pause and resume; misc/PLAYER has death, hurt and heal1-3; menus have click, close, edge, enter, music, open and wrap; dialogs have open, close, scroll and copy.
- Folder-driven content: find_directories() over a category plus random_string() picks a random variant. A new folder is new content, with no code change.
- Menu wiring: setupmenu() points custom_menu's sounds at ui/menus/<menupack>/*x*.

Pitfall to avoid: ToyMania's folder is misc/PLAYER but its code asks for misc/player. That works on Windows only. Stride Rush's folder was renamed to misc/player by the dev on 2026-11-01. Keep every sound folder and every path in code lowercase.

The lookup code itself will be SimpleFighter's packfuncts glob functions, not ToyMania's get_sound ([[project_tech_decisions]]). The folder tree stays ToyMania-style.

Settled 2026-11-01: no top-level sound packs. There will never be a sounds/<packname>/ level, so sr/sounds/ is the root and paths go straight to the category (sounds/misc/game/...). The ui/menus/<theme>/ and ui/dialogs/<theme>/ subfolders (default) stay as they are; those are themes inside the tree, not top-level packs.

**How to apply:** get_pack_sound builds "sounds/" + path, with no pack name and no decompiled/ level. Don't add soundpack/dlgpack/menupack selectors. Related: [[reference_toymania_readonly]], [[project_audio_model]].
