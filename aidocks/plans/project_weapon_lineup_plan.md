---
name: project_weapon_lineup_plan
description: COMPLETE (2026-11-06; built, tested and docked, the 10th 1.5 entry, so 1.5 is FULL) - the dev's weapon sound changes (boot and laser removed, axe and sword added) need the weapon list redone: alphabetical, guns on 9 and 0, damages remapped by key; Q&A log
metadata:
  type: project
---

Status: COMPLETE 2026-11-06. Code BUILT and tested (all 3 passed: melee lineup, guns and strength, and the learn sounds names); docks DONE (the readme's three mentions, and the changelog's "Made it so the boot and laser are now replaced by an axe and a sword ..." as 1.5's 10th entry; the learn sounds death-to-destroy rename left out, dev: "leave the sound renames out of that entry") (dev: "Now all we need to do is fix up the broken weapons in the code, and the docks."): weapon_names is axe, bat, club, feat, fist, hammer, knife, sword, machine_gun, pistol; the comments in weapons.nvgt and tuning.nvgt name the axe as the start weapon and the 12-damage one; the readme has three mentions to fix (the walls line's "few swings of the bat", the weapons paragraph, the 1 through 0 key line) plus a changelog entry. Was SETTLED and PARKED 2026-11-06, nothing built (dev: "Keep it alphabetical, and remap the damages to it. We can do this later. Set this aside as another plan."). Raised while the game menu refactor plan's Section 4 was awaiting tests ([[project_game_menu_refactor_plan]]).

What happened: the dev reworked sdr/sounds/equipments/weapons (2026-11-06). Removed entirely: melee/boot and melee/laser. New: melee/axe and melee/sword (draw, fire1-3, hit1-3 each). Reworked: bat (one fire, one hit), club (fire1-2, hit1-2), fist (one fire, hit1-3), knife (one fire, hit1-3), feat (fire1-3, hit1-5), hammer re-recorded, pistol's draw and fire new; machine gun unchanged. Still ten weapons.

What the code has (weapons.nvgt): weapon_names = bat, boot, club, feat, fist, hammer, knife, laser, machine_gun, pistol on keys 1 to 0; weapon_damage = 3, 6, 9 ... 30 by position (ToyMania's draw_weapon() bases), each hit times weapon_damage_multiplier (4, tuning.nvgt); is_gun() and weapon_folder() go by name; a run starts with key 1's weapon drawn. With the sounds as they are, keys 2 and 8 have no sounds and the axe and sword can't be reached. The learn sounds menu reads the folders, so it needs nothing.

Q&A log:
- Q: The order on the keys, which also sets each weapon's strength and the starting weapon? Claude's proposal: alphabetical as now, guns on 9 and 0: axe, bat, club, feat, fist, hammer, knife, sword, machine gun, pistol, noting the axe becomes key 1, the weakest and the one every run starts with. (Asked 2026-11-06; Claude recommended this.)
- A (dev, 2026-11-06): "Keep it alphabetical, and remap the damages to it." SETTLED: weapon_names becomes axe, bat, club, feat, fist, hammer, knife, sword, machine_gun, pistol; weapon_damage stays 3 to 30 by key, so the axe (key 1) is 3 and the weakest, up to the pistol's 30; a run starts with the axe drawn.

Settled summary (one small build, then docks):
- weapons.nvgt: the new weapon_names; weapon_damage unchanged by position; anything naming "bat" as the start weapon checked.
- Docks: a changelog entry (in whichever version is open then), the readme's weapons paragraph ("the bat, boot ... laser ...", "Each run starts with the bat") and its keyboard line for 1 through 0.
