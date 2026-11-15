---
name: project_obstacle_code_history
description: decision history moved out of the 16 obstacle files' comments (hazard, spike, mine, forcefield, projectile, wall, door, barrier, animal, wind, combo, slide, ladder, floor_breaker, vehicle, trampoline) by the comment cleanup's Section 3 (2026-11-15); read before changing how an obstacle behaves
metadata:
  type: project
---

Moved here from the comments of sixteen obstacle files in src/includes/main/globals/ on 2026-11-15 ([[project_comment_cleanup_plan]], Section 3), so the code keeps only what it does and why. Dates are when the dev decided; quotes are the dev's own words. The plans named hold the full Q&A, and [[project_obstacle_recap]] describes every obstacle as it plays today. The core files' history is in [[project_core_code_history]], tuning's in [[project_tuning_history]].

## hazard.nvgt
- The statistic for times fell into hazards (2026-11-06).
- A hazard fall in practice became a practice death (2026-11-06), then gave everything back (the practice deaths plan, 2026-11-09, [[project_practice_deaths_plan]]).

## spike.nvgt
- The spike sounds (2026-11-02): the loop clip is one swing, played on the spike's own random rhythm.

## mine.nvgt
- A jumped mine keeps ticking and fades out behind you like a hazard's loop (2026-11-02).

## forcefield.nvgt
- Force fields (2026-11-02, [[project_force_fields_plan]]). The switch works on any step of the countdown (2026-11-02).
- The press plays centered, not panned to the hand (2026-11-02: panning sounded too far to the side).
- Shielded or not, a field still throws you past it (2026-11-03).
- A switched-off field's countdown stops (2026-11-03).
- left_used_on_field and right_used_on_field (2026-11-11, from the combined obstacles plan's testing: one clap cleared a force field and an animal at once).
- The switch press comes from the field's environment, a random switches theme (the transitions plan, 2026-11-13).
- Empty-hand sounds (2026-11-04): both hands clap and one hand plays woosh, both centred (at first the left hand panned 50 left and the right 50 right); a clap scares the nearest animal, the dev's use for claps (the birds plan, 2026-11-04); a lone woosh waits for a possible clap ("I don't like how it plays the clap and woosh at the same time").

## projectile.nvgt
- Projectiles (2026-11-02, [[project_projectiles_plan]]).

## wall.nvgt
- Walls (2026-11-03, for 1.1, [[project_walls_plan]]). A crash has no death sound; death is only for a wall your weapons destroy (2026-11-03).
- A destroyed wall's countdown stops (2026-11-03).
- Since the ladders plan (2026-11-12, [[project_ladders_plan]]), these are fake walls at odd pitches. The saved statistic keys keep their old names.
- Fake doors use their own tougher hp range (2026-11-05: "Doors are meant to be much stronger than walls").
- The level's share of wall toughness: the difficulty scaling plan's Section 3 (2026-11-09).

## door.nvgt
- Doors: 2026-11-03, for 1.1 ([[project_doors_plan]]). At first doors had no countdown cues. Since 2026-11-04 the dev moved them into environments/default/traps (from objects/interaction) and added the doors countdown, so every standing door counts down like a trap.
- Real doors start locked since 1.2 ([[project_keys_plan]]). A hand on a fake door, and a key on one, plays jam (2026-11-03).
- Close plays behind you, fading as you run on (2026-11-03). Open plays stationary, at the dev's request.

## barrier.nvgt
- Barriers: 2026-11-04, Section 2 of the lanes plan. First built in 1.3, undone, and brought back for 1.4 on top of the rebuilt lanes ([[project_lanes_plan]]).
- Since Section 3 turned the belt forward (2026-11-05), the loop is placed like every belt sound. Before, while the belt ran to the right, it played stationary with its own pan and fade.
- A hit's loop passes through and fades behind you, like a spike's (2026-11-05).
- The lane rules (2026-11-04): "I highly recommend making them random in the real game so it's not super predictable"; "sometimes 2 of them can appear, but one of them has to be on the lane you are not at".
- The HRTF fixed angle (2026-11-05): left and right barriers sounded "sort of in the front, but not quite".

## animal.nvgt
- Animals: 2026-11-04, for 1.4, the birds plan ([[project_birds_plan]]). The type is "animals" ("in the future, you'll be able to scare off other types of animals, such as dogs"). Belt-wide at the dev's word ("belt wide").
- The clip is named scare, not flight (2026-11-04), since "dogs cannot fly". Kinds are one folder per kind, then one per animal (2026-11-04): bird to bird24, dog and dog2.
- Every kind gets an equal share however many animals it has (2026-11-04: "I'd rather go based off the animal kind").

## wind.nvgt
- Winds: the winds plan (2026-11-10 and 11, Section 1, [[project_winds_plan]]). Not in combinations (2026-11-11).
- A brace by crouching (2026-11-11). The countdown plays only in your lane (2026-11-11).
- shove_dir() (2026-11-11, after testing): at an edge the wind only bumped you, since a wind reaching an edge lane was always drifting toward that edge. Now an edge shoves toward the middle.

## combo.nvgt
- Combined obstacles: the combined obstacles plan (2026-11-11, Section 1, with pair clearing as Section 2, [[project_combined_obstacles_plan]]). Pairs only, never three: "That will just make the game too hard".
- The three debug choices, including combinations_mixed (2026-11-11). Gaps by the first part's action (2026-11-11).

## slide.nvgt
- Slides: the slides plan (2026-11-11, Section 1, with statistics in Section 2, [[project_slides_plan]]). Its sounds were first shared in misc/game (slideground, slidestart, slidemove, slidestop), beside the powerups'. Themes moved to transitions/slides/general with the transitions plan (2026-11-13).
- The back-to-back slide loop fix (2026-11-14): the old ride's move loop stops when a new slide is reached.

## ladder.nvgt
- Ladders and real walls: the ladders plan's Section 2 (2026-11-12, [[project_ladders_plan]]). The ladder stands ladder_wall_gap steps before its wall because, after testing, the two loops were heard as one.
- The countdown came when the dev added cues (2026-11-12: "Some times I never know when to grab it").
- The grab plays only as you take hold, not per rung (2026-11-12). The climb sounds were renamed from climb to step1 to step5 by the dev (2026-11-12).
- Rushing a rung makes you fall off, as a lane key does (2026-11-12). Rung timing by level (2026-11-12).
- Straight onto it without the run-up was tried after the run-up (2026-11-12); the run-up stayed (ladder_grab_runup true).
- The land sound is stationary, after trying 2d. A fall plays stationary after trying 2d; a collapse plays in 2d at the ladder (2026-11-12).

## floor_breaker.nvgt
- Floor breakers: the floor breakers plan's Section 1 (2026-11-13, [[project_floor_breakers_plan]]); Section 2 brought floor_breakers_repaired, caught_floor_breakers and the practice hint.
- The open sound is stationary, like a door (2026-11-13).
- The player's death plays with the fall, at the same time (2026-11-13).

## vehicle.nvgt
- Vehicles: the vehicles plan's Section 1 (2026-11-13, [[project_vehicles_plan]]); Section 2 brought the statistics, last_caught and the practice hint.
- Sound names: shoot was fire until the dev renamed it; impact (a shot striking you) was added by the dev (2026-11-13). The first kind is cars, with themes small_car to small_car3.
- vehicle_fade: the shots were lost at a distance, and the engine was heard only after the first shots (2026-11-13).
- The ram's hit plays like a barrier's (2026-11-13: "Hit.ogg means the ram sound, like the barior").
- The aim delay before a burst (2026-11-13: "How do you even avoide a shot?").
- Within ram range it stops firing (2026-11-13: "It should ram into you instead").
- A timed run counts a burst as one hit, however many shots land (2026-11-13).

## trampoline.nvgt
- Trampolines: the trampolines plan's Section 1 (2026-11-11, [[project_trampolines_plan]]); Section 2 brought worn_bounces and trampoline_flights.
- Jumping never avoids a pad (2026-11-11), reversing the first rule. The four kinds' names are the dev's.
- A lane pad's spawn comes from its lane like a barrier's (2026-11-11: the spawn was heard in the centre).
- A worn pad gives only a normal jump's worth (2026-11-11).
