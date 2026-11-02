---
name: reference_simplefighter_builder_objects
description: SimpleFighter's 81 builder object docs (sf/docks/builder/*.txt) read as an object reference for Stride Rush - which objects map to jump/duck/destroy/hand/collect/zone, their clips and rules, and the best runner templates
metadata:
  type: reference
---

Source: SimpleFighter/sf/docks/builder/, 81 player-facing topic files, read in full on 2026-11-01 at the dev's request as an object reference. Read only ([[reference_simplefighter_readonly]]). Stride Rush has no builder or map files ([[project_tech_decisions]]); these are ideas for objects that game code spawns.

Runner candidates by role (file names in that folder):
- Jump over:
  - hazards: takes a life, refills health and bounces you back. Clips are loop and fall. It has an auto-ledges option and moving and vanishing forms.
  - spikes: timed damage while you stand on them, and destroyable.
  - mines: armed ticking loop, then an explosion.
  - fires: an instant kill that can chase you.
  - floor_breakers: one-tile air gaps.
  - low walls.
- Duck under: a level projectile at head height (projectiles: moves one tile per speed interval, can bounce, can be destroyed). Also a tile zone with jump height 0, which acts as a crawlspace.
- Timing gates: force_fields (on and off for the same interval, damage plus knockback), vanishing hazards and vanishing platforms.
- Destroy with a weapon: walls (bump, hurt and death clips, can leave debris), spikes, projectiles, security_cameras, doors and signs. Weapons can't hurt hazards, mines, force fields, fires or zones.
- Interact hand: doors (open, close, grant, deny and jam clips; key or password locks; a jam radius when enemies are near), passages (open or close a corridor after a delay), switches (a lever or a button).
- Collect: items (a beacon loop on a beat, autograb, get clip, spoken name; item zones spawn random autograb items, which suit coin trails), checkpoints (beacon, get, used on the last life).
- Zones: heal_zones, safe_zones, tile_zones (speed, jump and fall overrides), flux_zones (each step permanently changes speed or health), winds (push a set number of tiles, can hurt), sensors (enter and exit triggers, like trip wires).
- Enemies: tts_enemies (cheap voiced enemies), npcs (full AI), containers, security_jets, security_cameras.
- Movement: conveyor_belts (push one tile per speed interval, never reverse, with a belt loop) are literally Stride Rush's core mechanic. Trampolines (bounce power 5, cooldown 500 ms) work as a jump boost.

Best runner templates:
- aircrafts.txt turbulence: a spoken warning at an announce distance (default 10), then a looping alarm only if you're on a collision course (alarm distance 5, never before the warning), then "pass" when you clear it, or death if you hit it. NOT USED: the dev said on 2026-11-01 that the turbulence template isn't needed for Stride Rush.
- The hazard auto-ledges: an audible edge before and after a danger.
- The time bomb's speeding-up tick, for something closing in.

Cross-object conventions:
- Each object picks a theme folder, and clips are matched by name fragment inside it ("the folder layout is the audio configuration"). A missing clip plays silently.
- Recurring clip names: loop, hit, hurt, death, fall, land, step, spawn, remove, on, off, get, open, close, grant, deny, break, press.
- Lives: losing a life refills health. On the last life you go to the checkpoint or a try-again prompt. A fatal hit is never silent (the death and tile-fall clips stand in for a missing one).
- Damage is attack minus defence times 3, with a minimum of 1. A shield takes the hit first. Hazards and fires take lives directly.
- "Speed" fields are milliseconds per step or tick, so smaller is faster.
- Ranged loops play at full volume inside the area and fade past its edges.

One doc contradiction to know about: signs.txt and commands.txt say %flag% tokens in sign text are filled in when the sign is read, but logic_conditions.txt and map_flags.txt say sign text is fixed when the map loads.

**How to apply:** when designing an obstacle, pickup or interactable, check this list for a SimpleFighter object to model, then adapt it to a belt moving right with jump and duck. Related: [[project_entity_pattern]], [[project_game_design]].
