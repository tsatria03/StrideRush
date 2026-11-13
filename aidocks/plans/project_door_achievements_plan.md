---
name: project_door_achievements_plan
description: COMPLETE (2026-11-12, 2.1 at 1 of 10) - Every Door Open asks for 9 real doors in one run, but no level has more than 6 since the top speed caps; fix its threshold and two door hints; Q&A log
metadata:
  type: project
---

Status: COMPLETE (2026-11-12, 2.1 at 1 of 10). The first plan for 2.1 (2.0 released, V2.00 at 888ae95).

Background:
- Found by Claude (2026-11-12) while comparing easy and chaos: Every Door Open ([every_door_open], session, real_doors_opened, threshold 9; hint "Only easy has nine doors in a run. Open every one, all the way to top speed.") can't be earned. The dev: "Oh yes. This needs fixed for 2.1 as a plan."
- Why: real doors come at each door_section_ms (50) mark from just below the starting speed while next_door_mark >= run_top_step_time() (spawner.nvgt). Since the difficulty scaling plan (1.8) capped top speeds (difficulty_top_step_times 200, 150, 100, 75, 50), the counts per run are: easy 6 (450 to 200), medium 6 (400 to 150), hard 6 (350 to 100), insane 5 (300 to 100), chaos 5 (250 to 50). Nine was a run from 500 down to 50 before the caps (debug runs still get it, but count nothing).
- Also stale: Master of Doors' hint ("Easy has the most doors in a run, nine of them. Start slow to open more."). Door to Door (3) and Open House (5) are fine. Achievements already earned stay earned.

Q&A log:
- Q: Every Door Open's threshold 6 (every door in a run on easy, medium or hard), its hint "Easy, medium and hard each have six doors in a run. Open every one, all the way to top speed.", and Master of Doors' hint "Easy, medium and hard have the most doors in a run, six of them. Long runs open more."? (Asked 2026-11-12; Claude recommended it.) A: "Those work." (dev, 2026-11-12).

- Q: The changelog entry, the first in 2.1 with build/version.txt to 2.1: "Fixed a bug where the Every Door Open achievement asked for nine real doors in one run, more than any difficulty has, so it now asks for six."? A: "Yes. Since there are only 2 small sections, you can try to do them all." (dev, 2026-11-12).

Settled design (2026-11-12): Every Door Open's threshold 6 and hint "Easy, medium and hard each have six doors in a run. Open every one, all the way to top speed."; Master of Doors' hint "Easy, medium and hard have the most doors in a run, six of them. Long runs open more."; the 2.1 entry above.

Sections (both built together, at the dev's word):
1. achievements.ini: the threshold and the two hints. Done.
2. Docks: "New in 2.1." with the entry, build/version.txt 2.1, CLAUDE.md, the version history, the index. Done. Plan COMPLETE.
- Tested (dev, 2026-11-12): the test passed (version 2.1; Every Door Open at 6 with its new hint; Master of Doors' new hint).
