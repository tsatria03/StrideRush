---
name: reference_simplefighter_movement_jump
description: SimpleFighter's 2d step, footstep, jump, fall and hazard-death code paths; the reference for the runner's jump-on-cue and death handling
metadata:
  type: reference
---

Paths are under SimpleFighter/src/includes/ ([[reference_simplefighter_readonly]]). Line numbers are from 2026-11-01, so find things by symbol.

Game loop:
- game() in main/globals/game.nvgt is while(!exit_game){ wait(5); ... }.
- Each pass runs the per-frame xcheck() pass, then the xloop() pass alphabetically, then game_input().
- Speeds are recomputed every frame: airtime, falltime, jumptime, runtime and walktime, from modspeed.

Steps:
- A held key repeats when movetimer.elapsed >= movetime.
- step_left() and step_right() in map.nvgt check bounds and walls, do me.x--, then call playstep().
- playstep() plays builder/construction/platforms/<tile>/*step* for the tile from gmt(x, y). playland() and playfall() do the same for land and fall.

Jump (handle_jump_keys in main/globals/game_handlers.nvgt):
1. Start: only if not jumping, jumpable, and not falling. Play rise/jump, set ty1=me.y, ty2=me.y+jumpheight, and ascending.
2. Rise: me.y+=1 every jumptime ms, stopping early on a platform hit.
3. Apex: one tick.
4. Fall: me.y-=1 per tick until checkforplatforms() finds ground or the player reaches ty1.

Gravity:
- fallcheck() in map.nvgt starts a fall when the tile underfoot is "" or "air", then does me.y-- every falltime ms.
- On landing, fall damage applies if the fall was at least fall_threshold (8) tiles.

Hazard death:
- hazardcheck(): with 2 or more lives, play *life*, remove a life, and knock the player back with pbounce(5).
- On the last life, either return to a checkpoint or play the hazard's fall clip via dlgplay, then clearmap(true) and show_death_prompt().
- show_death_prompt() is in main/functions/charfuncts.nvgt.

Pause:
- pause_game() and resume_game() in src/sf.nvgt flip about 16 capability flags together and pause or resume the pools.
- See [[project_transient_flags_per_frame_reset]].

**How to apply:** for Stride Rush, x advances automatically on the step timer instead of from a key. Jump is the main input. A hazard kills if the player is on the ground (y at ground level) when the hazard's x reaches the player's x.
