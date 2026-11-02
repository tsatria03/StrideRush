---
name: project_audio_model
description: Audio model, built in the first build - one sound_pool per category registered in decpool.nvgt's all_pools, listener updated each step, HRTF pref, and the load-bearing rule that any sound you later pause/move/stop must be looping or persistent
metadata:
  type: project
---

Plan, drawn from both reference games:
- One sound_pool per category. SimpleFighter keeps a single all_pools list in initialize_sound_pools() (decpool.nvgt) so pause, resume, fade and listener updates hit every pool. ToyMania declares its pools in dec.nvgt and uses decpool.nvgt helpers.
- Pool settings: max_distance=0, pan_step and volume_step 2.5.
- Every frame, update the listener at the player position on every pool. For 2d, SimpleFighter sets sound_pool_default_y_elevation so y is height.
- Positioned loops are played at the object's x; a sound range makes one loop cover a wide object.
- One-shots near the player, such as footsteps, use play_stationary or play_stationary_extended.
- Blocking, skippable clips (death sound) use dlgplay().
- HRTF is a preference that sets sound_global_hrtf at startup.

Load-bearing rule (from SimpleFighter's project_audio_model): any sound whose handle you keep to pause, move, re-pitch or stop later must be looping or persistent. A finished one-shot's slot gets reused, so a stale handle can end up controlling another object's sound. Initialise handles to -1 and check != -1 before use.

As built (first build, 2026-11-02):
- globals/decpool.nvgt has all_pools = p, muspool, ambpool, hazardpool, spikepool and minepool. A new object type's pool must be added there, or it won't pause, resume or follow the listener.
- UI pools (temp, spool, menupool, formpool) stay out of all_pools, so menu, dialog and buffer sounds still play while a run is paused.
- update_listeners() runs once per step (after the move), not every frame. The player only moves on a step, so the result is the same.
- pause_pools() pauses only sounds that are playing, so resume can't wake a finished one.
- Kept handles: hazard loops and mine ticking loops (looping), plus the music and ambience slots. Spike swings, footsteps, landings and countdown cues are fire-and-forget oneshots.
- A fatal hit plays the object's sounds through p, because silence_run() destroys the object pools. endrun.nvgt's wait_for_pool(p) then waits for them before the tile's fall.

**How to apply:** obstacle cue loops are kept handles, so they're looping. Footsteps are fire-and-forget one-shots, so they aren't kept. File lookup: [[project_sound_layout]].
