---
name: project_entity_pattern
description: One-file-per-object template adapted from SimpleFighter's hazard.nvgt - pool, handle array, class, spawn/check/remove/destroy_all, sentinel-null removal, clearmap registry
metadata:
  type: project
---

The pattern to adapt for Stride Rush objects (hazards, pickups, platforms), taken from SimpleFighter's src/includes/builder/traps/hazard.nvgt ([[reference_simplefighter_readonly]]). BUILT in the first build (2026-11-02): globals/hazard.nvgt, spike.nvgt and mine.nvgt follow it. As built:
- spawn_x() reuses the first null slot before appending, and returns nothing.
- x_check() runs once per step from run.nvgt's step_check(), not every frame. spike_swing() is the one per-frame check.
- The single clear registry is clear_run_objects() in globals/endrun.nvgt. A new type's destroy_all_x() goes there, and its pool goes into all_pools ([[project_audio_model]]).
- Its spawn goes into spawner.nvgt's choose_next_obstacle() and place_obstacle().
- Objects are dropped once they're spawn_distance() behind the player.
mine.nvgt is the fullest example, with a state flag and a kept looping handle.

One file per object type contains:
- its own sound_pool (registered in the shared pool list; see [[project_audio_model]])
- a global handle array, e.g. hazard@[] hazards(0)
- a class holding the state, whose constructor starts the looping cue sound
- spawn_x(...), which inserts and returns the index
- xcheck() or xloop(), called once per frame from the game loop
- remove_x(id) for one object, and destroy_all_x() to clear between runs

Load-bearing rules:
- Sentinel-null removal: remove with @xs[i] = null and destroy its sound. Never use remove_at, because other objects may hold indexes into the array. Every loop starts with if (@xs[i] == null) continue;. Only destroy_all_x() may resize(0).
- Register destroy_all_x() in one clear function (SimpleFighter's clearmap() in map.nvgt calls them all alphabetically). Otherwise objects leak into the next run.
- Glob-include folders mean dropping a new file in is the only wiring needed. That's what makes the game "easy to expand in code".

Useful SimpleFighter files to read:
- moving_hazard.nvgt: a timer-driven move() that wraps a child hazard and re-centres its sound.
- checkpoint.nvgt: a repeating beacon sound.
- platform.nvgt: tile lookup, gmt(x, y).

**How to apply:** a runner can drop SimpleFighter's builder forms, the 3d per-z tiles and topdown. It keeps the class, spawn, check, remove and destroy_all shape plus sentinel-null removal. Related: [[project_game_design]].
