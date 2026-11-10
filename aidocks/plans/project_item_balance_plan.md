---
name: project_item_balance_plan
description: SETTLED (2026-11-10, for 1.9; 3 sections) - a player could run an hour without dodging, on stocked shields and lives; rebalance how often survival items spawn; Q&A log
metadata:
  type: project
---

Status: SETTLED (2026-11-10), waiting for the dev to commit it before Section 1. Started 2026-11-10, with 1.9 at 7 of 10.

Background:
- A player's report, passed on by the dev (2026-11-10): "I was running like an hour or so, because i had 6 steel shields and over 10 lives and did not even have to jump or dodge anything, I could just listen how i was speedrunning and being hit by obstacles. I think you should decrease the spawning rate of items." The dev wasn't sure it's a bug.
- How items spawn now (choose_next_obstacle() in spawner.nvgt): each spawn rolls, in order, life capsule 1 in 20, health potion 1 in 10, player teleporter 1 in 16, powerup 1 in 10, steel shield 1 in 16, ammo pack 1 in 8, else an obstacle. Then item_pair_percent 50 adds a second random in-lane item (any of six kinds, keys included) half the time. Life capsules give 1 to 2 lives (max_lives 20), a shield takes 400 hp, a potion heals 5 to 10 percent of 200.
- Claude's estimate, once everything has joined: about 59 percent of spawns are obstacles and 41 percent items. Per spawn, capsules come about 7.7 percent of the time (5 rolled, 2.7 from pairs), so about 0.12 lives, worth about 23 health; shields about 7.2 percent, worth about 29 health; potions under 2. So about 54 health of protection arrives per spawn, while being hit by every obstacle costs about 0.59 x 45 average damage = 27 at full damage (chaos), about 16 on easy (60 percent). Taking every hit, a run gains protection faster than it loses it, at every difficulty; only hazards (an instant end) can stop it. So it is a balance problem, not a code bug.

Q&A log:
- Q: How should it be rebalanced: lower chances everywhere, scale by difficulty, or carry limits? (Asked 2026-11-10; Claude recommended scaling by difficulty, every level below the point where protection outpaces damage.) A: "To be consistent, we should try to scale the spawn rates by difficulty if possible." (dev, 2026-11-10).
- Q (dev, 2026-11-10): "WHat are the spawn rates for all 6 items, excluding powerups?" Claude's figures, everything joined: health potion 1 in 8 spawns (12.2 percent: 9.5 rolled, 2.7 from pairs), ammo pack 1 in 9 (11.2), player teleporter 1 in 12 (8.1), life capsule 1 in 13 (7.7), steel shield 1 in 14 (7.2), key 1 in 37 from pairs plus one before every real door; obstacles 59, powerups 8. Rolled in order, the first success winning, so later items are a little rarer than their tuning; pairs add 2.7 to each of the six.
- Q: Which items get rarer on harder levels? (Asked 2026-11-10; Claude recommended the three survival items, life capsules, steel shields and health potions, with the pair rule scaling too; ammo packs, teleporters and powerups unchanged.) A: "I agree with your suggestion." (dev, 2026-11-10).
- Q: How much rarer per level? (Asked 2026-11-10; Claude proposed a percentage of today's rates per level, like difficulty_damage_percents: easy 25, medium 20, hard 15, insane 10, chaos 5; debug at 100. Protection per spawn against what taking every hit costs: easy 13.5 vs 16, medium 10.8 vs 18.6, hard 8.1 vs 21.2, insane 5.4 vs 23.9, chaos 2.7 vs 26.5.) The dev asked about 30/25/20/15/10; Claude showed easy at 30 comes out even (16.2 vs 15.9), so taking every hit could still hold steady there, and suggested easy 25. A: the dev chose Claude's first set (dev, 2026-11-10: "Actually I like these more."): easy 25, medium 20, hard 15, insane 10, chaos 5.
- Q: When a pair's second item is a survival item that fails the level's percentage, no second item, or pick again from the other kinds? (Asked 2026-11-10; Claude recommended no second item, so ammo packs, keys and teleporters don't grow commoner in pairs.) A: "I'll do what you recommend." (dev, 2026-11-10). The dev added (same message): "I noticed that certain obsticals are als super rare, especially bariors."
- Barriers (dev's observation): no code bug; once joined, every obstacle type is an equal pick. They feel rare because 9 types share 59 percent of spawns (1 in 15 each), half of barriers pass in other lanes where their countdown doesn't play, and in-lane items crowd the lanes. The dev: rare "even after they've joined. Example, on easy". Claude noted the item rebalance alone makes every obstacle about a third commoner on easy (obstacles 59 to about 79 percent; chaos about 85); the dev: "If so, good".
- Q: Should barriers count twice in the obstacle pick? (Asked 2026-11-10; Claude recommended yes, about 1 spawn in 6 on easy with the rebalance, one weight in tuning.nvgt.) A: "yes" (dev, 2026-11-10).

Settled design:
- Survival items (life capsules, steel shields, health potions) spawn at a percentage of today's rates by level: easy 25, medium 20, hard 15, insane 10, chaos 5 (difficulty_item_percents in tuning.nvgt); debug runs at 100 (practice runs have none). Each one's roll keeps its 1 in <chance> and then must also pass the level's percentage, so a capsule on easy is about 1 spawn in 52 instead of 13.
- A pair's second item: if it comes up a survival item and fails the level's percentage, there's no second item that time.
- Ammo packs, keys, player teleporters and powerups unchanged. Spawns that used to be survival items become obstacles, so every obstacle type gets commoner (about a third on easy).
- Barriers count twice in the obstacle pick (barrier_weight 2 in tuning.nvgt), so they come about twice as often as each other type.

Sections:
1. Survival item scaling: difficulty_item_percents in tuning.nvgt; item_percent() in difficulty.nvgt beside level_percent() (100 when run_difficulty < 0); survival_roll() and its use in choose_next_obstacle()'s capsule, potion and shield rolls and in spawn_items()' pair, in spawner.nvgt.
2. Barrier weight: barrier_weight in tuning.nvgt; barriers added that many times to choose_next_obstacle()'s available list.
3. Docks: the readme's items and difficulty sections, the changelog (one entry each), CLAUDE.md, this plan COMPLETE.
- Section 1 built (2026-11-10): difficulty_item_percents in tuning.nvgt; item_percent() in difficulty.nvgt; survival_roll() and is_survival_item() in spawner.nvgt, the capsule, potion and shield rolls each needing survival_roll() too (a miss falls through to the next roll, as a failed chance always has), and a pair's survival item that misses gives no second item.
- Section 1 COMPLETE (dev, 2026-11-10): both tests passed (an easy endless run has survival items much rarer; a debug run with everything spawning has them as before).
- Section 2 built (2026-11-10): barrier_weight 2 in tuning.nvgt; choose_next_obstacle() adds barriers to its available list barrier_weight times.
- Section 2 COMPLETE (dev, 2026-11-10): the test passed (barriers clearly more often in a debug run with everything spawning).
