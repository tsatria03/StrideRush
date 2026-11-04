---
name: feedback_docks_later
description: HOLD LIFTED 2026-11-02 - sdr/docks/ was held until first-build Section 7, which is now written (readme, changelog, todo list); from now on player-facing changes get docks entries; todo list is player-facing only
metadata:
  type: feedback
---

As of 2026-11-01 the dev expects most early work (the launcher, the skeleton, the dep shims) not to be player facing for a while. sdr/docks/ will need updating eventually, but not now.

**Why:** the docks are player-facing records ([[feedback_changelog_rules]]). Writing them for internal plumbing is noise, and the dev wants to choose when they start.

When each file starts (agreed 2026-11-01, then updated the same day):
- UPDATE: the readme, changelog and todo list are all written together as Section 7 of the first build plan, after Section 6 is done, not after Section 5 ([[project_first_build_plan]]).
- readme.txt: the first readme comes in Section 7.
- changelog.txt: its first block, "New in 1.0.", also comes in Section 7.
- credits.txt: when outside sounds or code need crediting.
- todo list.txt: holds only player-facing entries, never internal or plumbing tasks. Developer tasks go in aidocks/plans/.

UPDATE 2026-11-02: Section 7 is written, so the hold is lifted. From here on, player-facing changes get changelog entries (a new block pairs with a version bump), and finished todo entries move to the "already finished" section.

**How to apply:** don't add changelog, readme or todo entries as part of building sections. Track what would need documenting in the relevant aidocks/plans/ file instead, and raise it when the dev says the docks are due.
