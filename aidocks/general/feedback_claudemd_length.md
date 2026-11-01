---
name: feedback_claudemd_length
description: Keep CLAUDE.md a lean dispatcher under 40,000 characters; detail goes in aidocks memory files
metadata:
  type: feedback
---

When this project gets a CLAUDE.md, keep it a lean dispatcher under 40,000 characters: what the game is, layout, running, and one trigger line per load-bearing rule pointing at a [[memory]] in aidocks/. Move detail out of it rather than expanding it.

**Why:** CLAUDE.md loads every session; memory files load on demand. Same rule as the dev's other games.

**How to apply:** add a pointer line to aidocks/MEMORY.md for every new memory ([[feedback_memory_folder_layout]]).
