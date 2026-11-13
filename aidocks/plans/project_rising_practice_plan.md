---
name: project_rising_practice_plan
description: OPEN (2026-11-12, for 2.1) - a "rising" practice speed that starts at 2 steps a second and climbs to 10, beside the fixed speeds; Q&A log
metadata:
  type: project
---

Status: OPEN (2026-11-12), in Q&A. 2.1 at 6 of 10.

Background:
- The dev (2026-11-12): endless runs offer no speed choice; in practice, drop the speed menu and let the speed rise naturally up to 10 steps a second, or lock it at 5 (easy's top). Claude weighed both (rising: a real-run feel, but about 7 minutes from 2 to 10 at the endless rate, and no staying slow; locked at 5: simple, but too fast to learn on and too slow for hard or chaos; the menu's strength is drilling a weak spot) and suggested keeping the menu with a "rising" choice added.
- Practice today: choose_practice() in menus/menu.nvgt offers 2, 2.5, 3.3, 5 and 10 steps a second (500 to 100 ms); speedup_check() in run.nvgt returns early for a practice run, so its speed never changes; endless runs speed up speedup_amount (10 ms) every speedup_period (10 s).

Q&A log:
- Claude explained rising: last in the speed list; starts at 2 steps a second; speeds up as an endless run does; stops at 10 and stays; retry practice keeps the speed reached, restart run starts again from 2; everything else unchanged; about 6 min 40 s to reach 10, or about 3 min 20 s at twice the rate. The dev: "I like the rizing item, but should it increase twice as fast as endless?"
- Claude recommended twice the endless rate (sessions are short; endless teaches the real pace). A: "Yes. It should since practice sessions are ment to be much quicker." (dev, 2026-11-12): speedup_amount every half speedup_period, 5 s; 2 to 10 steps a second in about 3 min 20 s.

Settled design: not yet.

Sections: not yet.
