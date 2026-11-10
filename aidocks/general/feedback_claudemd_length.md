---
name: feedback_claudemd_length
description: Keep CLAUDE.md a lean dispatcher under 10,000 characters (40,000 until 2026-11-10); detail goes in aidocks memory files, version history in project_version_history
metadata:
  type: feedback
---

When this project gets a CLAUDE.md, keep it a lean dispatcher under 40,000 characters: what the game is, layout, running, and one trigger line per load-bearing rule pointing at a [[memory]] in aidocks/. Move detail out of it rather than expanding it.

REVISED (dev, 2026-11-10: "claude.md seems pritty long, about 23 thousand characters ... Try not to make the claude.md file over 10k chars. It should be less to play it safe."): the limit is 10,000 characters, with room to spare (8,281 after the split). The long "Current state" paragraph, a summary of every version, moved to [[project_version_history]]; CLAUDE.md keeps only the latest release, the next version and the open plans. When a version closes, its summary goes in that memory, never in CLAUDE.md.

**Why:** CLAUDE.md loads every session; memory files load on demand. Same rule as the dev's other games.

**How to apply:** add a pointer line to aidocks/MEMORY.md for every new memory ([[feedback_memory_folder_layout]]).
