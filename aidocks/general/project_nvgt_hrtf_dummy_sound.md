---
name: project_nvgt_hrtf_dummy_sound
description: A global sound dummy must be loaded with dummy.load("dummy") before sound_global_hrtf is set, or HRTF doesn't work in the legacy engine; never remove it as dead code
metadata:
  type: project
---

The legacy NVGT fork needs a throwaway sound loaded before HRTF is switched on. The pattern, from Legacy-NVGT test/interact/hrtf.nvgt ("temporary solution to a fixed bug"), is used by SimpleFighter and ToyMania:
- a global sound dummy; in globals/dec.nvgt
- dummy.load("dummy"); as one of the first lines of main(), before sound_global_hrtf = hrtf;

**Why:** it looks like dead code (it loads a file that doesn't exist and is never played), so it's easy to drop when porting. The dev caught it being dropped from Stride Rush's sr.nvgt on 2026-11-01.

**How to apply:** keep both lines, in that order. Related: [[project_audio_model]], [[project_engine_pinned_nvgt]].
