---
name: project_sound_layout
description: sr/sounds/ layout - no top-level packs (sounds/ is the root); objects/ grouped by SimpleFighter builder categories (audio, construction, interaction, kombat, transitions, traps) with one theme folder per type; wildcard lookup picks a random numbered variant
metadata:
  type: project
---

No top-level sound packs: there will never be a sounds/<packname>/ level, so sr/sounds/ is the root and paths go straight to the category. Settled 2026-11-01. *.ogg and *.wav are gitignored, so this memory is the repo's only record of which clips exist; keep it in step with the folder.

Current tree (rescanned 2026-11-01 after the dev's second reorganization; 234 files with the weapons and switch added). objects/ is now grouped the way SimpleFighter's builder categories are; the rest keeps ToyMania's top level.
- equipments/weapons (added 2026-11-01, 69 files; ToyMania's ten weapons). Weapons keep a category level, weapons/<category>/<weaponname>/.
  - melee: bat, boot, club, feat, fist, hammer, knife, laser. Most have draw, fire1-3 and hit1-3; fist has fire1-2; laser has a single draw, fire and hit.
  - artillery: machine_gun and pistol, with draw, empty, fail, fire, hit, ping, reload and shell1-2.
  - Ten weapons is exactly the ten number-row slots (1 to 0) in [[project_controls_plan]].
- misc/game: pause, resume.
- misc/player: jump, duck, unduck, life, give, turn, and inv1 to inv6.
- objects/audio/musics and objects/audio/sources: empty. Music tracks and ambience loops for runs go here (they replaced the old objects/sources/tracks and ambiences).
- objects/construction/platforms: empty; the dev's favorite floor tiles go here (each with step1-5, land, fall, hurt, death). objects/construction/walls: empty.
- objects/interaction/items/other/<color>_key: black, green, orange, pink, purple, red and yellow keys (ToyMania keys). Clips: spawn, loop1-4, get, use, break; yellow has spawn1-2, use1-2 and a single loop. Items now sit under interaction with an "other" grouping level (the earlier equipments/items folder is gone).
- objects/kombat/projectiles: empty.
- objects/transitions/doors/door, door2, door3, door4: open, close, move, loop, grant, deny, jam1-2, hurt, death.
- objects/transitions/teleporters/tp: loop, move.
- objects/interaction/switches/switch: press (added 2026-11-01, for the future hand-operated force field). Moved there from transitions by the dev the same day, matching SimpleFighter's builder, which files switches under interaction.
- objects/traps/force_fields/electric, electric2: on, off, hit. Renamed from "force fields" by the dev on 2026-11-01, so no folder name has a space.
- objects/traps/hazards: chasm, chasm2, electricity, electricity2, electricity4, fire, lava, pit, quicksand, water, water2. Each has loop and fall.
- objects/traps/mines/mine, mine2, mine3: spawn, light, loop, hit, explode.
- objects/traps/spikes/electric_ray, large_spike: loop, hit, hurt (.wav), death1-2.
- ui/dialogs/default, ui/menus/default: empty so far. ui/other was removed.

misc/player notes:
- duck plays when the player presses and holds Down/S; unduck plays on release, or when ducking auto-unducks after about 1 to 2 seconds (dev, 2026-11-01).
- There's no land clip here; landing comes from the platform tile's land clip.
- life plays when a life is lost but the run continues. In the basic game (1 life) it's never heard.
- give and inv1-6 are ToyMania-style inventory sounds. turn is a ToyMania clip; its use is open, possibly lane changes.

Themes and type folders:
- Menus use ui/menus/<name>/ (menutype) and dialogs use ui/dialogs/<name>/ (dlgtype); both default to "default". Dialog clips are open, close, scroll, copy and error.
- Every object type is a named theme folder holding that type's clips, so a new folder is new content with no code change. Code lists them with get_pack_sound_folders(), e.g. "objects/traps/hazards/*".
- Clip names follow SimpleFighter's builder conventions (loop, fall, hit, hurt, death, on, off, spawn, explode, open, close, grant, deny and so on; see [[reference_simplefighter_builder_objects]]).
- Item grouping: the earlier lean was flat items/<name>/, but the dev has now put keys under items/other/. Confirm when items are designed.

Naming rule: multi-word folder names use underscores, never spaces (as in force_fields, electric_ray, black_key), so names survive any later space-split text format such as map lines or commands.

Pitfall: keep every folder and every path in code lowercase. ToyMania's misc/PLAYER folder versus its code's misc/player only works on Windows. Stride Rush's player folder is lowercase.

**How to apply:** get_pack_sound builds "sounds/" + path. The only selectors are the menu and dialog theme names, never a whole-tree soundpack selector. Lookup code is SimpleFighter's glob functions ([[project_tech_decisions]]). Related: [[project_audio_model]], [[reference_toymania_readonly]].
