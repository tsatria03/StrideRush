---
name: project_tech_decisions
description: Settled tech choices - offline single player with no networking, form_menu (not ToyMania's custom_menu), no map files for now, SimpleFighter's sound glob functions, SimpleFighter's updater later, deps copied from SimpleFighter
metadata:
  type: project
---

Settled by the dev on 2026-11-01:

- Offline, single player. No networking systems: no server, no client netcode, no chats, no keepalive callbacks. Strip any networking from code ported from CaveDefender. The one exception is the future updater, a plain HTTP download through the nvgt_curl plugin. The dev confirmed on 2026-11-01 that it stays, because it isn't part of the game mechanics.
- Menus: form_menu plus setupmenu (SimpleFighter's), not ToyMania's custom_menu. Both are already in src/includes/main/deps/.
- No customizable or authored map files. That's "much much later". Obstacles come from game code, not a map parser. src/includes/main/parsers/ exists but has no map role for now.
- Sound lookup: wildcard globbing (find_sound_in_disk picks a random match). Use whichever of SimpleFighter's packfuncts.nvgt or ToyMania's extrafuncts.nvgt is more up to date.
  - Comparison: find_sound_in_disk is identical in both. SimpleFighter's layer is newer: get_pack_sound, get_pack_sound_folders (natural sort), pack file caches and a folder index. ToyMania's is a thin get_sound() over a soundpack folder.
  - So use SimpleFighter's, trimmed of the map and builder pack parts.
  - Settled: no top-level sound packs, ever. sounds/ is the root, with no sounds/<packname>/ or decompiled/ level ([[project_sound_layout]]). SimpleFighter's .spack pack-file layer (find_sound_in_pack, the pack caches and the folder index) goes too, leaving the disk glob functions with a "sounds/" prefix.
- Updater: needed "much much later". Take SimpleFighter's main/globals/updater.nvgt (139 lines, check_for_updates and get_download_url), not ToyMania's 220-line one. The SimpleFighter-specific parts to change are the 7z password, the archive name, sf.exe in restart, the "sf folder" text and the downloadsounds() URLs.
- No JAWS keyhook: the dev doesn't want it. Don't add deps/keyhook.nvgt, a kh keyhook global or an install_keyhook() call, even though both reference games have them.
- deps/ (added by the dev on 2026-11-01) are byte-identical copies of SimpleFighter's, except form.nvgt. That file has SimpleFighter's keyboard-theme typing sounds (the get_pack_sound("main/keyboards/...") calls) removed, so Stride Rush has no keyboard themes.

**How to apply:** don't reach for custom_menu, a map parser or ToyMania's get_sound. Related: [[project_sound_layout]], [[reference_simplefighter_architecture]], [[project_build_pipeline]].
