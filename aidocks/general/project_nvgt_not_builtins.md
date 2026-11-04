---
name: project_nvgt_not_builtins
description: Names that look like engine built-ins but aren't in the legacy fork - min, max (game-defined in extrafuncts) and vd (declared in the game's dec.nvgt); when porting, verify a name before assuming it's built in
metadata:
  type: project
---

These look like engine built-ins but aren't. The dev's games define them in their own code:
- min and max: defined in each game's functions/extrafuncts.nvgt as double min(double, double) and double max(double, double). Stride Rush has them since 2026-11-01.
- vd: the virtual_dialogs object is declared in each game's globals/dec.nvgt (virtual_dialogs vd;), not inside deps/virtual_dialogs.nvgt. Stride Rush declares it since 2026-11-01.

Real built-ins seen while porting (no definition needed): round, random, parse_int, string_split and string_to_number (bgt_compat), file_exists, natural_number_sort, clipboard_copy_text, DIRECTORY_APPDATA, DATE_*.

**Why:** the first launch after porting CaveDefender's buffer failed with "No matching symbol 'max'" and "No matching symbol 'vd'" (sdr/errors.txt, 2026-11-01). A dependency scan had listed max, but Claude wrongly waved it off as a built-in, and assumed vd lived in virtual_dialogs.nvgt from a grep hit that was really SimpleFighter's dec.nvgt.

**How to apply:** when porting code, any name a scan finds defined in a reference game's own src (not its deps) must be checked against Stride Rush's src, never assumed built in. Grep the reference repo to see whether it's a function or a global declaration, then check the legacy engine source if unsure. Related: [[project_engine_pinned_nvgt]], [[feedback_verify_code_while_fixing]].
