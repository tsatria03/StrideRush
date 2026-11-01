---
name: project_runner_overview
description: What this game is (an audio runner in legacy NVGT), its pre-repo status, the undecided name, and the excluded user/ folder
metadata:
  type: project
---

An audio-only runner game in NVGT. The player rides a one-way, constantly moving belt (rightward in 2d) past obstacles placed on a map. A timer in the game script advances the player and plays a oneshot footstep on each tick, and the tick interval shrinks over time so the run speeds up. Goal: a simple core that users can easily expand in code.

Status as of 2026-11-01: scaffolding only (src/includes/main/..., csr/ assets with docks, sounds, data, lib), no scripts yet. Not a git repository yet. Name chosen 2026-11-01: Stride Rush (picked over Echo Stride and Full Stride). The asset folder is sr/ (was csr/) and the release folder is releases/windows/StrideRush. The top-level project folder is still named ClassicRunner because the dev can't rename it mid-session; they will rename it later. The GitHub repo will be created later under the new name.

Engine: the legacy fork at C:\nvgt, source at misc/Legacy-NVGT. The user/ folder is excluded for now; the dev will discuss it later.

There is no CLAUDE.md yet (a SimpleFighter one was pasted by mistake and deleted on 2026-11-01).

**How to apply:** treat design as open discussion until the dev says go ahead. Related: [[feedback_memory_folder_layout]].
