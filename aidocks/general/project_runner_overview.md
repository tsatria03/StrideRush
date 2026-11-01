---
name: project_runner_overview
description: What this game is (an audio runner in legacy NVGT), its name and repo status, folder names, and the excluded user/ folder
metadata:
  type: project
---

An audio-only runner game in NVGT. The player rides a one-way, constantly moving belt (rightward in 2d) past obstacles placed on a map. A timer in the game script advances the player and plays a oneshot footstep on each tick, and the tick interval shrinks over time so the run speeds up. Goal: a simple core that users can easily expand in code.

Name chosen 2026-11-01: Stride Rush (picked over Echo Stride and Full Stride). The project folder is games/StrideRush (was ClassicRunner), the asset folder sr/ (was csr/), and the release folder releases/windows/StrideRush.

Status as of 2026-11-01: a git repo on branch main with remote origin https://github.com/tsatria03/StrideRush. As of commit d0e340f the game has a launchable skeleton: the sr/sr.py launcher, src/sr.nvgt, the dep shims and a two-item form_menu main menu, with no gameplay yet ([[project_skeleton_plan]]). The build tools in build/ are adapted ([[project_build_pipeline]]).

Engine: the legacy fork at C:\nvgt, source at misc/Legacy-NVGT. The user/ folder is gitignored and mostly not yet discussed. Only read inside it where the dev points; so far that's user/CaveDefender-main for the buffer system ([[reference_cavedefender_buffer]]).

CLAUDE.md was written for Stride Rush on 2026-11-01, as a lean dispatcher pointing into aidocks/ ([[feedback_claudemd_length]]). An earlier SimpleFighter copy had been pasted by mistake and deleted. Update CLAUDE.md's triggers when a new load-bearing rule or memory area appears.

**How to apply:** treat design as open discussion until the dev says go ahead. Related: [[feedback_memory_folder_layout]].
