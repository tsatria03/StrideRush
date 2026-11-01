---
name: reference_simplefighter_architecture
description: SimpleFighter's launcher, include tree, map format/parser, menus, dialogs, settings and key config; reference for pieces Stride Rush may borrow
metadata:
  type: reference
---

Paths are under SimpleFighter/ ([[reference_simplefighter_readonly]]).

Launcher and build:
- sf/sf.py runs C:\nvgt\nvgt.exe ../src/sf.nvgt with cwd sf/ and CREATE_NO_WINDOW.
- If the game exits within 5 seconds, sf.py writes the cleaned compile errors to sf/errors.txt and shows a message box. sync_version() mirrors build/version.txt into src/includes/version.nvgt.
- build/tools.py compiles, packages a 7z, makes a gh release, then updates the website. Sounds aren't bundled; the game downloads them.

Includes: src/includes/includes.nvgt glob-includes main/deps, functions, globals, menus, parsers, plus the builder/* groups.

Map format:
- data/builder/maps/decompiled/<name>/data/main.sif, one object per space-separated line, with header lines mode, minx, maxx, miny and maxy, plus a meta.sif beside it.
- main/parsers/map_parser.nvgt: load_map() calls clearmap(), splits the lines, handles headers, and sends every other line to dispatch_entity_line(sd).
- dispatch_entity_line keys on sd[0] and sd.length(), which encodes the single or ranged form.
- Helpers in main/functions/mapfuncts.nvgt: stn() (supports random(a,b)), string_to_bool, delinear and filter_empty_lines.

UI:
- Menus are form_menu m plus setupmenu(), with themed sounds from menus/<menutype>/.
- Dialogs: dlg() for spoken dialogs, dlgmessage() for paged text, alert() for pre-init and tooling notices.
- Multi-field input uses audio_form.
- Speech: speak(text, interrupt) in main/deps/speech.nvgt.

Settings: savedata st (an encrypted dictionary at appdata/tsatria03/SimpleFighter/preffs/settings.spf). readpreffs() guards every key with exists(); writepreffs() saves.

Keys:
- key_config controls loads data/main/config/keyboard.ini, with lines like action=COMBO[:trigger] such as move_left_held=LEFT:down.
- Queries are action_pressed, action_down and action_repeating.
- Rebinding: rebind_keyboard_action() in main/menus/menu.nvgt.

Helpers: main/functions/extrafuncts.nvgt has clamp, random_string, sort_naturally, glob_match and the file-size helpers. Also deps/key_hold.nvgt and globals/fadepool.nvgt.

**How to apply:** if the dev wants authored maps, SimpleFighter's map format and dispatcher are the model. A runner only needs x positions plus a type for most lines. Skeleton pieces are compared in [[reference_toymania_architecture]].
