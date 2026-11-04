---
name: feedback_sounds_before_features
description: Nothing gets built until its sounds exist; a feature whose sounds aren't in sdr/sounds yet is designed and recorded, but deferred
metadata:
  type: feedback
---

In Stride Rush, a feature isn't built until the sounds it needs exist in sdr/sounds/. Its design can be discussed and recorded in its plan, but it's marked deferred until the dev has the sounds.

**Why:** the dev applied this twice on 2026-11-01. The warning cues were deferred "until I find the proper sounds", and duck-under obstacles were held back because no duck-under sounds exist yet, while jump-over obstacles go ahead using the hazard, spike and mine sounds already there. In an audio-only game, a feature without its sounds can't be played or judged.

**How to apply:** before proposing a build section, rescan sdr/sounds/ and check the feature's clips exist ([[project_sound_layout]]). If they're missing, say which clips are needed and keep the feature in the plan as deferred. Related: [[feedback_plans_record_qna]].
