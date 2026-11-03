---
name: project_runner_overview
description: What this game is (an audio runner in legacy NVGT), its name and repo status (first build complete, v1.0 playable), folder names, and the excluded user/ folder
metadata:
  type: project
---

An audio-only runner game in NVGT. The player rides a one-way, constantly moving belt (rightward in 2d) past obstacles placed on a map. A timer in the game script advances the player and plays a oneshot footstep on each tick, and the tick interval shrinks over time so the run speeds up. Goal: a simple core that users can easily expand in code.

Name chosen 2026-11-01: Stride Rush (picked over Echo Stride and Full Stride). The project folder is games/StrideRush (was ClassicRunner), the asset folder sr/ (was csr/), and the release folder releases/windows/StrideRush.

Status as of 2026-11-02: a git repo on branch main with remote origin https://github.com/tsatria03/StrideRush. The skeleton came first (d0e340f, [[project_skeleton_plan]]). The first build is now COMPLETE ([[project_first_build_plan]]): game code in 69dedf8, player docks in 0f0ccff. Version 1.0 has a playable endless runner:
- An endless run on a step timer, 500 ms down to 100 ms, with footsteps on random platform surfaces.
- Jump and a silent crouch.
- Hazards with ledges and the hazcount countdown, spikes and mines.
- Lives, and death sounds by obstacle type.
- A pause menu, readouts, volume keys and the speech buffer.
- sr/docks/ holds the readme, the changelog ("New in 1.0.") and the todo list.
Since then (2026-11-02 and 3): force fields, projectiles, ten weapons, ammo packs and an inventory were added. 1.0 was CLOSED and tagged V1.00 at ca6f256 on 2026-11-03. Work now goes toward 1.1. Next features come from the todo list and the parked parts of the plans. The build tools in build/ are adapted ([[project_build_pipeline]]).

Engine: the legacy fork at C:\nvgt, source at misc/Legacy-NVGT. The user/ folder is gitignored and mostly not yet discussed. Only read inside it where the dev points; so far that's user/CaveDefender-main for the buffer system ([[reference_cavedefender_buffer]]).

CLAUDE.md was written for Stride Rush on 2026-11-01, as a lean dispatcher pointing into aidocks/ ([[feedback_claudemd_length]]). An earlier SimpleFighter copy had been pasted by mistake and deleted. Update CLAUDE.md's triggers when a new load-bearing rule or memory area appears.

**How to apply:** treat design as open discussion until the dev says go ahead. Related: [[feedback_memory_folder_layout]].
