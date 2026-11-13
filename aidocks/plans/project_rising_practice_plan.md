---
name: project_rising_practice_plan
description: SETTLED (2026-11-12, for 2.1; 2 sections) - a "rising" practice speed that starts at 2 steps a second and climbs to 10, beside the fixed speeds; Q&A log
metadata:
  type: project
---

Status: SETTLED (2026-11-12), waiting for the dev to commit it before Section 1. 2.1 at 6 of 10.

Background:
- The dev (2026-11-12): endless runs offer no speed choice; in practice, drop the speed menu and let the speed rise naturally up to 10 steps a second, or lock it at 5 (easy's top). Claude weighed both (rising: a real-run feel, but about 7 minutes from 2 to 10 at the endless rate, and no staying slow; locked at 5: simple, but too fast to learn on and too slow for hard or chaos; the menu's strength is drilling a weak spot) and suggested keeping the menu with a "rising" choice added.
- Practice today: choose_practice() in menus/menu.nvgt offers 2, 2.5, 3.3, 5 and 10 steps a second (500 to 100 ms); speedup_check() in run.nvgt returns early for a practice run, so its speed never changes; endless runs speed up speedup_amount (10 ms) every speedup_period (10 s).

Q&A log:
- Claude explained rising: last in the speed list; starts at 2 steps a second; speeds up as an endless run does; stops at 10 and stays; retry practice keeps the speed reached, restart run starts again from 2; everything else unchanged; about 6 min 40 s to reach 10, or about 3 min 20 s at twice the rate. The dev: "I like the rizing item, but should it increase twice as fast as endless?"
- Claude recommended twice the endless rate (sessions are short; endless teaches the real pace). A: "Yes. It should since practice sessions are ment to be much quicker." (dev, 2026-11-12): speedup_amount every half speedup_period, 5 s; 2 to 10 steps a second in about 3 min 20 s.

- Q: The design below, the entry "Added a rising speed to practice runs, which starts at 2 steps a second and speeds up to 10, twice as fast as an endless run.", and two sections? A: "Looks good." (dev, 2026-11-12).

Settled design (2026-11-12):
- The practice speed menu: 2, 2.5, 3.3, 5, 10, then rising.
- Rising starts at 2 steps a second (500 ms), speeds up speedup_amount (10 ms) every 5 s (half speedup_period), and stays at 10 (100 ms) once there: about 3 min 20 s.
- Retry practice keeps the speed reached; restart run starts again from 2. C reads the speed as usual; the obstacle, spacing, hints, passes, lives and shield unchanged.
- The 2.1 entry above (7 of 10).

Sections:
1. The rising choice and its speed-up.
2. Docks: the readme's practice section, the entry, CLAUDE.md, the version history, this plan COMPLETE.
- Section 1 built (2026-11-12): choose_practice() adds "rising" after the speeds and sets practice_rising (practice.nvgt), starting at start_step_time; speedup_check() runs in a rising practice run every practice_rising_period (5000) down to practice_rising_top (100), tuning.nvgt; practice_death() never touches step_time, so retry keeps the speed; restart run reruns start_run() from 500 with practice_rising still set.
- Section 1 COMPLETE (dev, 2026-11-12): both tests passed (rising from 2 to 10 by about 3 min 20 s and holding; retry keeps the speed, restart run starts from 2, fixed speeds stay fixed).
