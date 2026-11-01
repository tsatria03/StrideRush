---
name: feedback_docks_later
description: Don't update sr/docks/ (readme, changelog, todo, credits) yet; early work isn't player facing, and the dev will say when docks need writing
metadata:
  type: feedback
---

As of 2026-11-01 the dev expects most early work (the launcher, the skeleton, the dep shims) not to be player facing for a while. sr/docks/ will need updating eventually, but not now.

**Why:** the docks are player-facing records ([[feedback_changelog_rules]]). Writing them for internal plumbing is noise, and the dev wants to choose when they start.

When each file starts (agreed 2026-11-01):
- readme.txt: at the first playable runner (Start game runs, the belt moves, jump and death work).
- changelog.txt: at the first real release, opening with a "New in 1.0." block.
- credits.txt: when outside sounds or code need crediting.
- todo list.txt: holds only player-facing entries, never internal or plumbing tasks. Developer tasks go in aidocks/plans/.

**How to apply:** don't add changelog, readme or todo entries as part of building sections. Track what would need documenting in the relevant aidocks/plans/ file instead, and raise it when the dev says the docks are due.
