---
name: project_tuning_history
description: how tuning.nvgt's values came to be (earlier values, the dev's reasons and dates), moved out of the code comments by the comment cleanup's Section 1 (2026-11-15); read before changing a tuning value
metadata:
  type: project
---

Moved here from src/includes/main/globals/tuning.nvgt's comments on 2026-11-15 ([[project_comment_cleanup_plan]], Section 1), so the code keeps only what each value means. Dates are when the dev decided; quotes are the dev's own words. The plans named hold the full Q&A.

## The belt, surfaces, jump and crouch
- min_step_time 50: was 50, then 100, back to 50 (2026-11-02).
- surface_min_time and surface_max_time, 10 to 20 s at any speed (2026-11-03, for 1.1, [[project_1_1_plan]]): it used to be 50 to 200 tiles, 25 to 100 s at 500 ms; first 10 to 30 s.
- duck_cooldown 500 (2026-11-03, for 1.1): was 1000.
- belt_fade_ms: the forward belt (2026-11-04, [[project_lanes_plan]]).
- countdown_length 5 at any speed (2026-11-03, for 1.1): it used to shrink with speed, 5 at 500 ms down to 1 at 100 ms.

## Difficulty, items, combinations and the schedule
- difficulty_names, start times and floor times: the game menu refactor plan (2026-11-05, [[project_game_menu_refactor_plan]]).
- difficulty_damage_percents: the difficulty scaling plan (2026-11-09: "I like option 2 much better", [[project_difficulty_scaling_plan]]); easy takes 60 percent, chaos the full amount.
- difficulty_item_percents: the item balance plan (2026-11-10, after a player ran an hour taking every hit, [[project_item_balance_plan]]).
- barrier_weight 2: the item balance plan (2026-11-10).
- difficulty_combo_percents, combo pairs and gaps: the combined obstacles plan (2026-11-11, [[project_combined_obstacles_plan]]).
- difficulty_top_step_times: the difficulty scaling plan (2026-11-09).
- schedule_types and schedule_join_times: Section 5 of the game menu refactor (2026-11-05), one obstacle type per 50 ms mark, in order of the action it needs. Later joins: slides at 300 (3.3 steps a second) and winds at 200 (5) (2026-11-11), trampolines with slides at 300 (2026-11-11), ladders at 250 (4) with fake doors (2026-11-12), floor breakers at 250 (2026-11-13), vehicles at 200 (2026-11-13).
- difficulty_unlock_runs 5: Section 6 (2026-11-05: "5 runs per level, and a user is required to reach at least 1 door").

## Slides, winds, ladders, floor breakers, vehicles, trampolines, timed runs
- Slides: [[project_slides_plan]] (2026-11-11). Trampolines: [[project_trampolines_plan]] (2026-11-11). Winds: [[project_winds_plan]] (2026-11-10 and 11). Floor breakers: [[project_floor_breakers_plan]] (2026-11-13).
- Ladders ([[project_ladders_plan]], 2026-11-12): rungs 6 to 8 on easy up to 10 to 12 on chaos after testing showed 5 felt too short; 60 damage for a collapse, 40 for a fall; ladder_rung_min_times by level; ladder_grab_runup true, the dev's choice after trying both; ladder_wall_gap 5 after testing.
- Vehicles ([[project_vehicles_plan]], 2026-11-13): vehicle_shot_gap 200 at first, then 50 ("50ms was way better"); vehicle_burst_pause 2000 at first, 1000 for a while, then 2000 again to give shooting room; vehicle_shot_tile_time 30 at first, then 50; vehicle_engine_fade 0.5 because 0.25 sounded too close as it appeared; vehicle_aim_delay, vehicle_fade and vehicle_ram_range the same day.
- Timed runs ([[project_timed_run_plan]], 2026-11-13): "I want medium to be 6/5" (pass and hit seconds); warnings "5, 10, 15, 30, 45"; the rearm the same day.

## Spikes, mines, lives, health and practice
- spike_swing_min and spike_swing_max (2026-11-02).
- mine_arm_lead_time (2026-11-02): 1 tile ahead of the countdown at 500 ms, 5 at 100 ms, 10 at 50 ms.
- Lives and health (2026-11-03, [[project_player_health_plan]]): the damages replaced the fixed life costs (spikes 1, mines 2, doors 3) and the shield-only damages.
- max_lives and capsules unlimited (2026-11-04); life capsules give 1 to 2 lives (2026-11-04: "between 1 to 2").
- starting_lives was 3 until 2026-11-04; debug_lives 2 since.
- practice_unlock_count 5: the practice locks plan (2026-11-10: "just like the diff modes", [[project_practice_locks_plan]]).
- practice_hint_limit: the practice guidance plan (2026-11-12). practice_rising_period: the rising practice plan (2026-11-12).
- practice_lives and practice_shields 1, not 2 (2026-11-09); only debug runs get 2 lives.

## Doors, walls, projectiles, force fields
- Doors (2026-11-03, [[project_doors_plan]]).
- Wall hp scaling (2026-11-03, [[project_walls_plan]]): a flat random 100 to 500, then 200 to 2000, then 20 to 2000; 50 to 500 since 2026-11-05, when guns couldn't break the fastest walls in time.
- Fake doors' own range (2026-11-05: "Doors are meant to be much stronger than walls"); they shared the walls' hp until then.
- projectile_speed_factor 2, forcefield_knockback_tiles 5 and switch_min_time 500 (2026-11-02; the switch window so top speed doesn't need mashing).

## Weapons and items
- weapon_damage_multiplier 4 (2026-11-03, while testing walls): was 2.
- gun_start_reserve 50 (2026-11-03): was 250, lowered so ammo packs matter.
- melee_fire_gap 200 and pistol_fire_gap 100 (2026-11-04): both were one shared 50 ms, too short for the weapon powerups to be heard. pistol_fire_gap 200 (2026-11-26, the dev: "Please make the pistol filre a lot slower", then "I rather do 200ms, not any slower."), matching CaveDefender's pistol.art spam time of 200; the machine gun's 100 already matched its repeat time.
- weapon_reach_time 2000 (2026-11-03).
- bullet_tile_time 30: first 30, tried at 50, settled on 40 (2026-11-03), back to 30 (2026-11-05), so bullets stay ahead of you even at 50 ms steps.
- Ammo packs (2026-11-02): a pack gave a flat 50 to both guns until 2026-11-03, now 5 to 10 to the gun you hold; gun_max_reserve 500 (2026-11-20, the dev), was 200 (2026-11-03), and 250 before that.
- shield_chance 16: first proposed as 20, the dev chose 16. shield_hp 400: first proposed as 100, then 200; 400 since 2026-11-04 ("armor is twice as strong as you").
- Powerups (2026-11-03 and 4, [[project_powerups_plan]]): powerup_time 15000, first 20000 (2026-11-04); powerup_speed_ms 50, first proposed as 100; the belt sound replays every 300 ms on the ground and 400 in flight, the dev's final choice after trying 500, 350, 250 and 500 for flight (2026-11-04).
- Health potions (2026-11-04, [[project_health_potion_plan]]). Life capsules and teleporters (2026-11-03).

## Lanes, barriers, animals, hands
- lane_pan_amount (2026-11-04); lane_pan_step (2026-11-05); barrier_hrtf_spread (2026-11-05).
- barrier_damage 80, the hardest blow, the dev's number. barrier_pair_percent 50 (2026-11-04: "half the time"). item_pair_percent 50 (2026-11-05: the barriers' rule for items).
- animal_damage 10 (2026-11-04, birds first, [[project_birds_plan]]). clap_window 100 (2026-11-04).

## Audio
- min_volume -100: -50 until 2026-11-08 (the volume sliders plan: "the ambience/music volumes should be able to go to -100", [[project_volume_sliders_plan]]). volume_change 1 per press (2026-11-02).
- music, ambience and menu music start at 80 percent (-20) since 2026-11-09; full volume until then.
- Ambience switch every 1 to 2 minutes (the music and ambience plan, 2026-11-06: "I like the 1 to 2minute switch", [[project_music_ambience_plan]]).
- Environment switch every 1 to 2 minutes (the environments plan's Section 2, 2026-11-10: "I'd say 1 to 2 minutes", [[project_environments_plan]]).
- Heartbeat ([[project_heartbeat_plan]], 2026-11-08): heart_start_bpm 5, set to 50 for a test that day then back ("5=500, and 150=200"); heart_max_bpm 155 at 150 ms, 150 at 200 ms until 2026-11-08; the breathing bands were taken out with the breath sounds.
