---
name: project_difficulty_comparison
description: The five difficulty levels side by side (speed, obstacles, ladders, damage, survival items, expected outcomes), worked out from tuning.nvgt on 2026-11-12 at 2.1; re-check the constants before quoting after any tuning change
metadata:
  type: project
---

Worked out by Claude on 2026-11-12 (2.1 open), from tuning.nvgt, and approved by the dev ("I love that. Please save this comparison"). Every figure comes from a constant, named in brackets, so check those first if tuning has changed since. Order throughout: easy, medium, hard, insane, chaos.

Speed:
- Starting speed (difficulty_start_times 500/450/400/350/300 ms): 2, 2.2, 2.5, 2.9, 3.3 steps a second.
- Top speed (difficulty_top_step_times 200/150/100/75/50 ms): 5, 6.7, 10, 13.3, 20 steps a second.
- Time to top speed (speedup_amount 10 ms every speedup_period 10 s): about 5 min on easy, medium and hard, 4 min 40 s on insane, 4 min 10 s on chaos.
- Open belt between obstacles (difficulty_min_floor_times / difficulty_max_floor_times): 2-5, 1.75-4.75, 1.5-4.5, 1.25-4.25, 1-4 s.

Obstacles:
- At the start (schedule_types / schedule_join_times; chaos ignores the schedule): easy hazards, spikes and mines; medium adds projectiles (450); hard adds force fields (400); insane adds animals (350); chaos everything. Every level has everything by 5 steps a second (200 ms, the last joins: barriers, winds, powerups).
- Combinations (difficulty_combo_percents 5/10/15/20/25): 1 obstacle in 20, 10, about 7, 5, 4.
- Real doors per run (door_section_ms 50 marks from below the start down to the top speed): 6, 6, 6, 5, 5. (Every Door Open asked for 9 until 2.1: [[project_door_achievements_plan]].)
- Ladder heights (ladder_rungs_min / ladder_rungs_max): 6-8, 7-9, 8-10, 9-11, 10-12 rungs.
- Time per rung (ladder_rung_min_times / ladder_rung_times): 0.2-2, 0.25-1.75, 0.3-1.5, 0.35-1.25, 0.4-1 s.

Damage and survival:
- Damage taken (difficulty_damage_percents): 60, 70, 80, 90, 100 percent; a barrier (barrier_damage 80) costs 48, 56, 64, 72, 80.
- Survival items scale by difficulty_item_percents 25/20/15/10/5 (survival_roll()): health potions (health_potion_chance 10) about 1 spawn in 40, 50, 67, 100, 200; steel shields (shield_chance 16) 64, 80, 107, 160, 320; life capsules (life_capsule_chance 20) 80, 100, 133, 200, 400; slides and trampolines (slide_chance, trampoline_chance 6) 24, 30, 40, 60, 120. Rough, ignoring the rolls ahead of each in choose_next_obstacle().
- Ammo packs (1 in 8), player teleporters (1 in 16) and powerups (1 in 10) don't scale.
- Every endless run: 200 health (player_hp), 1 life (starting_lives).

Expected outcomes:
- Easy, learning: obstacles arrive one at a time, mistakes are cheap, healing common; most players reach top speed.
- Medium, settling in: a little faster and harsher, still forgiving; top speed takes steady play.
- Hard, the real test: 10 steps a second at the top, a combination every 7 obstacles, noticeably less healing; ladders get serious.
- Insane, endurance: over 13 steps a second, nearly full damage, healing scarce; reaching the top takes consistency, lasting there skill.
- Chaos, mastery: everything from the first step, full damage, almost no healing, 20 steps a second; reaching top speed is the achievement.

Each level is harder in many small ways at once (faster start and top, shorter gaps, more combinations, taller and tighter ladders, more damage, less healing), a steady climb rather than one big jump. Claude's per-obstacle difficulty ratings (1 to 10, from the design, 2026-11-12): slides 2 (a helpful break, not an obstacle; rolled like survival items); spikes, mines, animals 3; hazards, projectiles, force fields 4; fake walls, barriers 5; real doors, fake doors, trampolines 6; winds 7; real walls with ladders, combinations 8 (the dev, after play: real walls at top speed are the hardest traps).
