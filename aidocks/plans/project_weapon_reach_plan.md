---
name: project_weapon_reach_plan
description: FOR LATER (2026-11-15): per-weapon reach, after the weapon swing plan is built and played; what's known so far, the key unlock split, the ToyMania comparison and the open questions; no Q&A yet
metadata:
  type: project
---

Created 2026-11-15 at the dev's request ("Please rename this plan, and create a new weapon reach plan for later."), when the first weapon plan was split: per-weapon melee swing went to [[project_weapon_swing_plan]], built first, and reach waits here. Not started; pick it up only when the dev asks, after the swing plan is built and played. Its changelog entry is a third one beside the swing plan's two (dev, 2026-11-15: "The ranges will get a third one when we get to that later.").

## What's known (2026-11-15)
- Every weapon reaches weapon_reach_time (2000 ms) ahead, turned into tiles at the current speed by weapon_reach() in weapons.nvgt: 4 tiles at 500 ms, 40 at 50 ms. Bullets vanish after weapon_reach() tiles (bullet.nvgt, b.range).
- weapon_reach() is also the key's unlock range for real doors (door.nvgt). Per-weapon reach must not leak into unlocking, so the first step is giving the key its own reach (today's 2000 ms) whatever this plan decides.
- Reach must stay time-based: a fixed tile count breaks across the belt's tenfold speed range (1 tile is half a second at 500 ms, 50 ms at top speed).
- ToyMania (read only): draw_weapon() gives each weapon a tile range in lockstep with damage, bat 1 by 2 tiles up to pistol 10 by 11, so the strongest also reaches furthest; recorded under suggestion 23 in [[project_suggestions]]. Not a model to copy as it is.
- CaveDefender (read only): every melee weapon has the same range (5), its weapons differing by swing speed alone; see [[project_weapon_swing_plan]].
- Claude's earlier recommendation, before the swing work: pair reach against damage (strong and short, or weak and long), not in step with it. With the swing plan's speeds already trading against damage, that needs revisiting once the swing has been played.

## Open questions (one at a time, when the plan starts)
1. Is per-weapon reach still wanted after playing the new swings?
2. What does reach trade against: damage, swing speed, or neither (a flavor difference)?
3. The values: a reach time per weapon in tuning.nvgt.
4. Melee only, or the guns' bullet range too?
5. The key's own unlock reach: keep 2000 ms?
6. Docs: the readme's weapons section and the third changelog entry.

## Q&A log
(none yet)
