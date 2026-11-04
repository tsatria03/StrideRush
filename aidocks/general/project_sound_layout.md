---
name: project_sound_layout
description: sdr/sounds/ layout - no top-level packs (sounds/ is the root), no menu or dialog themes (flat ui/menu, ui/dialog, ui/buffer, ui/other); objects/ grouped by SimpleFighter builder categories (audio, interaction, platforms, traps since the 2026-11-03 reorg; items and weapons under equipments) with one theme folder per type; wildcard lookup picks a random numbered variant
metadata:
  type: project
---

No top-level sound packs: there will never be a sounds/<packname>/ level, so sdr/sounds/ is the root and paths go straight to the category. Settled 2026-11-01. Since 2026-11-04 the sounds are TRACKED in git (the dev removed *.mp3, *.ogg and *.wav from .gitignore; sdr/sounds is about 27 MB), so git status and git log now show added, removed and renamed clips. Before that they were ignored and this memory was the only record of which clips existed; keep it in step with the folder anyway, as a readable summary.

Current tree (rescanned 2026-11-01 after the dev's second reorganization; 300 files with the weapons, the switch, the construction examples, the new player clips, the shield and the flat ui folders added). objects/ is now grouped the way SimpleFighter's builder categories are; the rest keeps ToyMania's top level.
- equipments/weapons (added 2026-11-01, 69 files; ToyMania's ten weapons). Weapons keep a category level, weapons/<category>/<weaponname>/.
  - melee: bat, boot, club, feat, fist, hammer, knife, laser. Most have draw, fire1-3 and hit1-3; fist has fire1-2; laser has a single draw, fire and hit.
  - artillery: machine_gun and pistol, with draw, empty, fire, hit, loop, ping, reload and shell1-2 (fail.ogg removed by the dev, 2026-11-02). loop.ogg was added by the dev on 2026-11-03 as the bullet-in-flight sound, then replaced the same day by loop1 to loop5 in each gun ([[project_bullets_plan]]). The *loop* wildcard picks one at random per bullet.
  - Ten weapons is exactly the ten number-row slots (1 to 0) in [[project_controls_plan]].
- misc/game: pause, resume. hazcount1 to hazcount5 were here (added earlier on 2026-11-02) but the dev removed them later that day, replacing them with misc/trap.
- misc/trap/walls (added by the dev, 2026-11-03): warn1-1 to warn1-5 and warn2-1 to warn2-5. Every trap's warn cues are five chromatic-scale notes. Walls LAYER two octaves: warn1-k is the lower octave (-12 semitones, from the force fields' notes) and warn2-k is the higher one (0 semitones, from the hazards' notes), and both play together on countdown step k. The naming rule for layered sets is warn<group>-<step>, and future traps may layer more octaves ([[project_walls_plan]]).
- misc/trap/<type>/warn1 to warn5 (added by the dev, 2026-11-02): a distinct 5-step warning countdown per obstacle type, for force_fields, hazards, mines, projectiles and spikes. warn5 is the last, "act now" cue. Folder names match objects/traps/<type> (projectiles matches objects/kombat/projectiles), so code can build the path from the type name. This resolves the old "warning cues deferred until sounds exist" problem ([[project_run_plan]]).
  - hazard.nvgt's countdown was repointed from misc/game/hazcount to misc/trap/hazards/warn the same day (it had gone silent when hazcount was removed).
  - Lesson (from when sdr/sounds was gitignored): a removed or renamed sound never showed in git status. Since 2026-11-04 it does, so check git status on sdr/sounds after a reorganization, then still grep src for any old path, since nothing checks code paths against the folder.
- misc/player: jump, rise, land, duck, unduck, life, death1-5, hit1-5, give, turn, and inv1 to inv6. rise, land, death and hit were added 2026-11-01. On 2026-11-03 the dev replaced the single death and hit with five variants each. The code's *death* and *hit* wildcards pick one at random, so no code change was needed.
  - Jump plays misc/player/jump and misc/player/rise together. Landing plays misc/player/land together with the platform tile's land clip (dev, 2026-11-01).
  - hit: plays when a force field, mine or spike hits the player, at the same moment as the obstacle's own clips (dev, 2026-11-01). It's Stride Rush's version of SimpleFighter's character hurt sound.
  - death: plays when the player dies, but only from force fields, mines and spikes. Hazards don't use it, since they bring their own fall clip (dev, 2026-11-01).
- equipments/shields/steel: wear, hit, break, remove (added 2026-11-01; renamed from the misspelled "steal" by Claude at the dev's request the same day). For later; the dev will describe it when its time comes.
- objects/audio/musics and objects/audio/sources: empty. Music tracks and ambience loops for runs go here (they replaced the old objects/sources/tracks and ambiences).
- objects/construction (example elements added 2026-11-01; 279 files total in sounds/ now):
  - platforms: REPLACED by the dev on 2026-11-03 with 132 folders, so the sound tree went from about 375 files to 1524. carpet and marble are gone; ledge is unchanged.
    - The new folders are ash, cement to cement4, concrete to concrete47, deapsand, dirt to dirt20, grass to grass11, gravel to gravel12, hay, largerock, lawn, leaves to leaves6, pavement, pine, rocks to rocks5, sand to sand8, shortgrass, soil, stone to stone5, thickforrest and weed to weed3.
    - Most have step1-5 (some more), land and fall. Their hurt and death clips, which the game doesn't use, were deleted by Claude at the dev's request on 2026-11-03: 262 files, one death.ogg and one hurt.ogg in each of the 131 non-ledge folders. The platforms folder now holds 928 files.
    - The surface picker finds them at runtime, so no code change is needed.
    - grass11 (no land or fall, .wav steps) and sand8 (no fall) were incomplete, and the dev deleted both on 2026-11-03. That leaves 130 folders (129 surfaces plus ledge). Every one has step, land and fall, all .ogg.
    - Spellings: "deapsand" and "thickforrest" are the dev's names.
  - "ledge" is for hazards (dev, 2026-11-01): the ground turns to ledge just before and after a hazard, like SimpleFighter's hazard auto-ledges. It is NOT a normal surface, so the random surface picker must exclude it ([[project_obstacles_plan]]).
  - MOVED (dev, 2026-11-03): walls now live in objects/traps/walls/window (wallglass renamed to window), beside the other traps, so the spawner's objects/traps/<type> path works. There is still no misc/trap/walls warn set. Earlier history: walls/wallglass (dev, 2026-11-02): loop, hit1-2, hurt1-3, death1-2. It REPLACED walls/walldirt (bump, death, hurt1-3), which is gone. Still the first full-height obstacle sound and the first thing for weapons to hit: loop as you get closer, hurt on each weapon hit, death when destroyed, and hit for smashing into it (confirmed by the dev, 2026-11-02). Walls are parked until weapons are built ([[project_walls_plan]]).
- objects/interaction/items/common/ammo_pack (dev, 2026-11-02): spawn, loop, get1-2, use, break1-6. A new "common" grouping beside "other"; likely the gun ammo pickup ([[project_weapons_plan]]).
- objects/interaction/items/other/<color>_key: black, green, orange, pink, purple, red and yellow keys (ToyMania keys). Clips: spawn, loop1-4, get, use, break; yellow has spawn1-2, use1-2 and a single loop. Items now sit under interaction with an "other" grouping level (the earlier equipments/items folder is gone).
- objects/kombat/projectiles: GONE (dev, 2026-11-02). The projectiles first went here, then the dev moved them to objects/traps/projectiles (below) and the kombat folder no longer exists.
- objects/traps/projectiles (dev, 2026-11-02): boulder (loop, hit1-3; first named "bolder", fixed by the dev), car (loop1-6, hit), car2 (loop1-5, hit1-5), firewall, missile, missile2, missile3, missile4 (loop, hit). Under traps like every other obstacle, so the spawner's objects/traps/<type> path works unchanged.
- objects/transitions/doors/door, door2, door3, door4: open, close, move, loop, grant, deny, jam1-2, hit, hurt, death. hit was added to all four by the dev on 2026-11-02, for smashing into a fake door you didn't destroy (confirmed by the dev).
- objects/transitions/teleporters/tp: loop, move.
- objects/interaction/switches/switch: press (added 2026-11-01, for the future hand-operated force field). Moved there from transitions by the dev the same day, matching SimpleFighter's builder, which files switches under interaction.
- objects/traps/force_fields/electric, electric2: on, off, hit. on and off are both LOOPS, a distinct one for each state: on while the field is active, off while it's inactive (dev, 2026-11-02). Don't assume a clip is a oneshot just because it isn't named loop. Renamed from "force fields" by the dev on 2026-11-01, so no folder name has a space.
- objects/traps/hazards: chasm, chasm2, electricity, electricity2, electricity3, electricity4, fire, lava, pit, quicksand, water, water2. Each has loop and fall. electricity3 was added 2026-11-02; a briefly misspelled "electrisity4" was fixed by the dev the same day.
- objects/traps/mines/mine, mine2, mine3: spawn, light, loop, hit, explode.
- objects/traps/spikes/electric_ray, large_spike: loop and hit only. The dev trimmed these for Stride Rush on 2026-11-01, removing hurt (.wav) and death1-2, so spikes have no clips for being smashed.
  - Meaning (dev, 2026-11-02): loop.ogg is ONE SWING, played once per swing on the spike's random rhythm (500 to 1000 ms), not looped continuously. hit.ogg is the spike hitting you.
- ui (flattened 2026-11-01; 300 files total in sounds/ now):
  - ui/menu: click, close, edge, enter, open, wrap, speaker. There's no music clip, so menu music is silent for now. speaker is a speaker-test clip.
  - ui/dialog: open, close, scroll, copy, error. Renamed from ui/dlg; the dev also fixed "coppy" to copy and added error.
  - ui/buffer: choose, switch. These are the CaveDefender buffer's item and category cues. The enable and disable clips were removed again.
  - ui/other: complete, copied, export, toggleon, toggleoff. toggleon and toggleoff are back (for buffer mute and unmute). They live in ui/other, not CaveDefender's ui/misc; the adapted buffer.nvgt uses ui/other. copied.ogg was renamed from the misspelled "coppied" by Claude at the dev's request (2026-11-01).
  - Two different copy sounds (dev, 2026-11-01): ui/dialog/copy is for plain C on a dialog (dlg()'s copy key; the dev confirmed plain C, not Ctrl+C). ui/other/copied is for copying stats, for later with scoring, like ToyMania's copy-results option. Don't swap them.

misc/player notes:
- duck plays when the player presses and holds Down/S; unduck plays on release, or when ducking auto-unducks after about 1 to 2 seconds (dev, 2026-11-01).
- Landing layers misc/player/land with the platform tile's land clip; neither replaces the other.
- life plays when a life is lost but the run continues. In the basic game (1 life) it's never heard.
- give and inv1-6 are ToyMania-style inventory sounds. turn is a ToyMania clip; its use is open, possibly lane changes.

Themes and type folders:
- NO menu or dialog themes (dev, 2026-11-01; this supersedes the earlier ui/menus/<name> and ui/dialogs/<name> theme decision). Menu sounds live directly in ui/menu/ and dialog sounds directly in ui/dialog/. The menutype and dlgtype selectors are no longer needed.
- Every object type is a named theme folder holding that type's clips, so a new folder is new content with no code change. Code lists them with get_pack_sound_folders(), e.g. "objects/traps/hazards/*".
- Clip names follow SimpleFighter's builder conventions (loop, fall, hit, hurt, death, on, off, spawn, explode, open, close, grant, deny and so on; see [[reference_simplefighter_builder_objects]]).
- Item grouping: the earlier lean was flat items/<name>/, but the dev has now put keys under items/other/. Confirm when items are designed.

Naming rule: multi-word folder names use underscores, never spaces (as in force_fields, electric_ray, black_key), so names survive any later space-split text format such as map lines or commands.

Pitfall: keep every folder and every path in code lowercase. ToyMania's misc/PLAYER folder versus its code's misc/player only works on Windows. Stride Rush's player folder is lowercase.

**How to apply:** get_pack_sound builds "sounds/" + path. There are no sound selectors at all now: no whole-tree soundpack, and no menu or dialog themes. Lookup code is SimpleFighter's glob functions ([[project_tech_decisions]]). Related: [[project_audio_model]], [[reference_toymania_readonly]].

REORGANIZED by the dev (2026-11-03, during shields; this overrides the paths above): items moved from objects/interaction/items to equipments/items (common: ammo_pack, life_potion, player_teleporter, steel_shield; other: the 7 keys). Doors moved from objects/transitions/doors to objects/interaction/doors, beside switches/switch; objects/transitions is gone (teleporters/tp was removed earlier). Surfaces moved from objects/construction/platforms to objects/platforms (127 folders, ledge included); objects/construction is gone. equipments/shields/steel was replaced by equipments/items/common/steel_shield: spawn, loop1-2, get, break, use, hit, death. life_potion and player_teleporter: spawn, loop, get, break1-6, use. objects/ now holds audio, interaction (doors, switches), platforms and traps. Code paths updated the same day (ammopack, key, shield, door, surface, player, endrun).

ADDED by the dev (2026-11-04, for the lanes plan, [[project_lanes_plan]]; not used by code yet): objects/traps/barriers/ (boulder, car, car2, firewall, each with loop and hit variants), moved from objects/traps/projectiles, which now holds only missile to missile4; misc/trap/barriers/warn1-1 to warn3-5, a three-group layered countdown; misc/player/bump.ogg, the lane edge bump. Also present since 1.2: misc/game/powerget, powerground and powerflight for powerups ([[project_powerups_plan]]).
