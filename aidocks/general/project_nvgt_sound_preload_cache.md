---
name: project_nvgt_sound_preload_cache
description: sound.load caches decoded audio by filename; reloading changed audio under the same name replays the old clip
metadata:
  type: project
---

NVGT caches decoded audio by filename. If a file is replaced or regenerated at the same path and loaded again, the old cached clip plays.

**Why:** a feature that writes audio then plays it under a reused name silently plays stale audio. Shipped static sounds in sdr/sounds/ are unaffected.

**How to apply:** use a fresh filename for regenerated audio, or load with allow_preloads=false.
