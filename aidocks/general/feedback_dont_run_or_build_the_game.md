---
name: feedback_dont_run_or_build_the_game
description: Never launch or compile the game; the dev runs and verifies. Read-only inspection is fine
metadata:
  type: feedback
---

Never launch or compile Stride Rush yourself: not the sr/ launcher, not build/tools.py, not nvgt -c. Make the edits, report them, and stop.

**Why:** the game runs from source, so the dev is the one who exercises it and catches compile and runtime errors. An AI-triggered launch or build is noise and can leave stray processes or artifacts. Same rule as SimpleFighter and ToyMania.

**How to apply:** hand changes back with a "relaunch to test" note ([[feedback_list_modified_files]]). Reading and grepping is always fine.
