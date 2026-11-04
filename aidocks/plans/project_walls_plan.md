---
name: project_walls_plan
description: COMPLETE (2026-11-03, in 1.1; walls and the layered countdown, weapon hits, docks) - walls as a full-height obstacle from sounds/objects/traps/walls; how they're passed (weapons), warned, hit and placed; Q&A log
metadata:
  type: project
---

Status: SETTLED 2026-11-03, for 1.1 (started 2026-11-02 on top of d956876; parked for weapons, which are now built). The dev chose walls ahead of doors ("Not yet. Let's talk about walls first"). COMPLETE: every section was built, tested and documented.

Build sections:
Section 1: walls and the layered countdown. Weapons can't hurt walls yet, so every wall gets crashed into, which tests everything except weapon hits.
- spawner.nvgt play_countdown(): play warn<k> as now, or, when the folder has layered files, every warn<g>-<k> group together (g = 1, 2, and so on, until one is missing).
- New globals/wall.nvgt, with wallpool and the wall entity (x, theme, hp, countdown_start, loopslot, destroyed and crashed flags).
  - Spawn plays the loop at the wall's tile, with random hp from wall_min_hp to wall_max_hp.
  - Contact on arrival hits at any height. A survivable crash plays hit, misc/player/hit, life and death (shatter), costs wall_life_cost and is marked crashed. A fatal one plays hit through p, then end_run_hit().
- Wiring, per the new-obstacle checklist: obstacle_types ("walls"), place_obstacle(), all_pools, clear_run_objects(), and the check and countdown calls. Tuning: wall_life_cost 1, wall_min_hp 100, wall_max_hp 500.
- BUILT 2026-11-03 on top of 031345e. SECTION 1 COMPLETE: all 5 tests passed (2026-11-03): the approach with layered cues, a crash, jumping or crouching still crashing, the last life, and other traps unchanged in a 50 ms mix with pause. As built:
  - play_countdown() checks for warn1-1 in the trap's folder. If it's there, it plays warn1-<note>, warn2-<note> and so on until a group is missing. Otherwise it plays warn<note> as before. It uses a while loop rather than an empty for-condition.
  - wall.nvgt: wall_standing() (not destroyed or crashed); wall_check() in step_check() after projectile_check(), with a stop when the run has ended; wall_countdown() after projectile_countdown(). A survivable crash plays hit and death through wallpool at the wall, plus the player hit and the life sound. hp is rolled at spawn but unused until Section 2.
  - "walls" is in obstacle_types, so the testing spawn menu shows "walls" between projectiles and ammo packs.
Section 2: weapon hits.
- weapons.nvgt weapon_strike(): the nearest standing wall ahead within weapon_reach_time (2000 ms, in tiles at the current speed) takes the damage. It returns the wall's x, so the weapon's hit (and shell) plays there. wall.nvgt then plays hurt, and at 0 hp death, stopping the loop and marking it destroyed.
- The unused weapon_range table is removed.
- BUILT 2026-11-03 on top of e5d036a; awaiting tests. As built:
  - weapons.nvgt: weapon_range removed. weapon_reach() = ceil(weapon_reach_time / step_time), at least 1, so 4 tiles at 500 ms and 40 at 50 ms. weapon_strike(damage) returns strike_wall(weapon_reach(), damage).
  - wall.nvgt strike_wall(): the nearest standing wall from 1 to reach tiles ahead takes the damage. It plays hurt at the wall, or at 0 hp death, stopping its loop and setting destroyed. It returns the wall's x, so fire_weapon() plays the weapon's hit (and shell) there.
  - A destroyed wall is no longer standing, so wall_check() lets you run through it.
  - tuning.nvgt: weapon_reach_time 2000.
  - CHANGED during testing (dev, 2026-11-03): "The death sound for a wall should not play when you run into it, now that we have working weapons." A crash now plays only the wall's hit, the player hit and the life sound, and its loop stops. death is only for a wall destroyed by weapons. This supersedes the crash "shatters with its death sound" answer above.
  - Test 1 (breaking a wall with the pistol, and a crash with no death sound) passed. CHANGED (dev, 2026-11-03): the countdown kept playing after a wall was destroyed. wall_countdown() now skips walls that aren't standing, so it stops the moment a wall breaks.
  - Test 2 (countdowns stopping for destroyed walls and switched-off fields) and Test 3 (the bat, then the held machine gun) passed. The dev, still tuning, raised weapon_damage_multiplier from 2 to 4 (2026-11-03). Damage is now bat 12, boot 24, club 36, feat 48, fist 60, hammer 72, knife 84, laser 96, machine gun 108, pistol 120. Hits to break a 100 or 500 hp wall: bat 9 and 42, boot 5 and 21, club 3 and 14, feat 3 and 11, fist 2 and 9, hammer 2 and 7, knife 2 and 6, laser 2 and 6, machine gun 1 and 5, pistol 1 and 5.
  - Test 4 (top speed with a mix) passed. SECTION 2 COMPLETE (2026-11-03). The dev then said they have a new idea for wall hp:
  - Wall hp idea (dev, 2026-11-03): hp scales with your speed, so walls get tougher the further you go, never below 200 and never above 2000. weapon_damage_multiplier stays at 4. This would replace the flat random 100 to 500.
  - Claude's check: at 500 ms the plan is 200 hp, 2 pistol shots or 17 bat swings. At 50 ms it's 2000 hp: 17 pistol shots, or 19 machine gun shots, about 1.9 s held, just inside the 2 s reach. Late walls then need the guns, and ammo packs become important. The bat would need 167 swings, so it's useful only early.
  - Q: At a given speed, is a wall's hp exact, or a random spread around that speed's value? (Asked 2026-11-03; Claude recommended a random spread of about 20 percent either way, always within 200 to 2000.) A: random ranges, not a flat amount (dev, 2026-11-03).
  - BUILT 2026-11-03: tuning.nvgt wall_min_hp 200, wall_max_hp 2000, wall_hp_spread 20. wall.nvgt wall_spawn_hp(): the center rises linearly from wall_min_hp at start_step_time to wall_max_hp at min_step_time, then hp is random within plus or minus 20 percent, clamped to 200 to 2000. That gives about 200 to 240 at 500 ms, 800 to 1200 at 300 ms, and 1600 to 2000 at 50 ms. The flat 100 to 500 is gone. Awaiting a test.
  - Multiplier discussion (2026-11-03): Claude recommended keeping weapon_damage_multiplier at 4. At 3 or below, top-speed walls outlast the 2 s reach. At 4 the held machine gun breaks a 2000 hp wall in about 1.9 s, and the laser needs 21 swings, about 10 presses a second. The bat can't break a top-speed wall at all (40 swings of 12). The dev accepted it: "definitely possible with most of the weapons, but you need extremely good reflexes." If walls feel easy later, raise the hp cap rather than lower the multiplier.
  - CHANGED before testing (dev, 2026-11-03): "make the lower end of the health to 20, not 200." wall_min_hp is now 20. That gives about 20 to 24 at 500 ms (2 bat swings, 1 shot from anything else), 720 to 1080 at 300 ms, and still 1600 to 2000 at 50 ms. The wall hp test passed (2026-11-03; the dev called it "test 4"). Walls Sections 1 and 2 are COMPLETE. Section 3 (docks) was WRITTEN 2026-11-03 on top of 09c2980, so WALLS ARE COMPLETE:
    - Changelog: three new 1.1 entries, newest first: walls ("Added walls ..."), the force field countdown stopping ("Made it so ..."), and the new surfaces ("Added over a hundred new ground surfaces ..."). 1.1 has 6 of 20.
    - Readme: the opening line adds "smash through", the exceptions line says three, a walls paragraph after projectiles, walls added to the countdown and lives lines, and the weapons line no longer says there's nothing to hit.
    - Todo list: walls moved to finished.
  - With a 5-step countdown, at 500 ms the reach (4 tiles) starts on warn2. Faster than 400 ms it covers the whole countdown and more.
Section 3: docks in 1.1. Changelog "Added walls ..." (plus the new surfaces entry, if the dev still wants it), the readme (walls, and weapons now having something to hit), and the todo list (walls to finished).

Sounds (rescanned 2026-11-02):
- objects/traps/walls/window (moved and renamed by the dev, 2026-11-03, from objects/construction/walls/wallglass): loop, hit1-2, hurt1-3, death1-2. It's the only wall theme so far. Being under objects/traps, walls fit the spawner's objects/traps/<type> path like every other trap.
- ADDED by the dev (2026-11-03): misc/trap/walls, with ten files in two groups, warn1-1 to warn1-5 and warn2-1 to warn2-5. That's a different shape from the other traps' warn1 to warn5. The dev will describe how they work. Code note: play_countdown()'s pattern "warn" + n + "*" would match warn1-1 to warn1-5 for n = 1, picking one at random, so walls will need their own path. (The older note follows.)
- EXPLAINED by the dev (2026-11-03):
  - Every trap's warn1 to warn5 are five notes of the chromatic scale.
  - The walls set is LAYERED across two octaves. warn1-1 to warn1-5 are the lower octave (-1, or -12 semitones), taken from the force fields' notes. warn2-1 to warn2-5 are the higher octave (0 semitones), taken from the hazards' notes. The dev renamed both into the walls folder rather than re-recording layered notes in Reaper.
  - Countdown step k plays BOTH warn1-k and warn2-k together, so both registers sound at once.
  - Future traps may layer several octaves the same way.
- Code plan: generalize play_countdown(). If a trap's folder has warn<k> files, play that as now. If it has layered warn<g>-<k> files, play every group g (1, 2, and so on, until one is missing) for step k at once. The exact patterns "warn<g>-<k>*" avoid the wildcard clash. Any future layered trap then works with no extra code.
- Before then there was no misc/trap/walls warn set. The five warn sets are force_fields, hazards, mines, projectiles and spikes. Under the sounds-first rule, a wall countdown needs either its own warn set or a decision to borrow one ([[feedback_sounds_before_features]]).
- Weapons: equipments/weapons has 8 melee (bat, boot, club, feat, fist, hammer, knife, laser) and 2 artillery (machine_gun, pistol), none built yet.

Already recorded elsewhere:
- Obstacles plan ([[project_obstacles_plan]]): walls are FULL height in the three-height model, "smash them with a weapon". Jumping or crouching can't pass one.
- Controls ([[project_controls_plan]]): Space fires or swings, X checks ammo, R reloads, and 1 to 0 pick a weapon. All are bound but unread.
- SimpleFighter reference (read only): walls take weapon hits (hurt), break (death), can leave debris, and bump when run into ([[reference_simplefighter_builder_objects]]).

Walls as described by the dev (2026-11-02, while the weapons plan was being committed):
- The loop plays as you get closer to a wall. Your goal is to destroy it with your weapons.
- Health: each wall spawns with a random 100 to 500 hp, and 500 is the most a wall can have. Weapon damage (the weapons plan's table, 3 to 30 per hit) wears it down; presumably hurt plays on each weapon hit and death when destroyed.
- hit is the sound of smashing into a wall you didn't destroy in time.
- Still to settle when walls resume: what smashing into one costs and does, the warning (there's no warn set for walls), and how damage and range from the weapons plan apply. At 3 to 30 damage per hit, a 500 hp wall takes from about 17 to about 167 hits, which needs checking against how long a wall is in reach.

Q&A log:
- Q: How far ahead can your weapons hit a wall? (Asked 2026-11-03; Claude recommended a fixed time-based reach of about 2 s ahead for every weapon, scaled with speed, with weapons differing only by damage.) A: agreed (dev, 2026-11-03). Every weapon reaches weapon_reach_time (about 2000 ms, tuning.nvgt) ahead, turned into tiles at the current speed like the hand window. weapons.nvgt's tile-based weapon_range table is no longer used for walls (kept for now, or removed when walls are built). Damage times weapon_damage_multiplier 2 is what sets weapons apart.
- Q: What happens when you smash into a wall you haven't destroyed? Claude's proposal: the wall's hit plays with misc/player/hit and the life sound, you lose 1 life (wall_life_cost), and the wall shatters (death plays), so the run carries on past it. On the last life: the wall's hit, then your death, then the tile's fall, as with the other traps. (Asked 2026-11-03.) A: yes. The dev asked whether running into a wall should destroy it; Claude suggested it shatters (it's a window, so the death sound fits) but does NOT count as destroying it, so later scoring can reward only weapon breaks. Dev (2026-11-03): "I like that." So a crash plays hit, misc/player/hit, life and death, costs wall_life_cost 1, and the run carries on, recorded as a crash rather than a destroy. Jumping or crouching doesn't help, since walls are full height.
- Q: Are Claude's proposed defaults for the rest of walls OK (listed below)? (Asked 2026-11-03.) A: yes, all seven (dev, 2026-11-03: "I like it", after a stray google-workspace skill load the dev asked to ignore).
  1. Spawning: walls join the random mix with an equal chance and a random theme (only window so far), and show up in the testing spawn menu. Each spawns with a random wall_min_hp 100 to wall_max_hp 500.
  2. Sound while approaching: the wall's loop plays at its tile, so it gets louder as you near it.
  3. Countdown: the usual 5 steps with no ledge, each step playing both octaves (warn1-k and warn2-k) together.
  4. Weapon hits: weapon_strike() picks the nearest standing wall ahead within the reach. Your weapon's hit (and shell, for guns) plays at the wall, then the wall's hurt (one of hurt1-3), and it loses the weapon's damage. At 0 hp its death plays, its loop stops, and it's gone, counted as destroyed. There's no speech for wall hits or hp.
  5. Only walls ahead of you can be hit. A wall that's already broken can't be hit again.
  6. A fatal crash plays the wall's hit through p, then your death, then the tile's fall.
  7. Normal spacing, pause freezes walls like everything else, and tuning gets wall_life_cost 1, wall_min_hp 100, wall_max_hp 500 and weapon_reach_time 2000.
- Q: (dev, 2026-11-02) Should the max hp for walls be lowered? A (Claude): hp alone isn't the real limit; reach is. With ToyMania's table, a weapon can only hit a wall within its range in tiles (bat 1 up to pistol 10), so the time you can hit for is range times step_time. The bat gets one step, 500 ms at the start (about 10 swings at 50 ms each, about 30 damage) and a single 50 ms swing at top speed. Even 100 hp is out of reach for melee. Suggested fix, to settle when walls resume: give every weapon a TIME-based reach, for example the last 2 s before the wall, scaled with speed like the countdowns, and set damage so a wall breaks in a fair number of hits. Then 100 to 500 hp can stay as a spread of tough and easy walls. Not decided; walls are parked.
- Q: (dev, 2026-11-02) What about a damage multiplier, such as weapon damage times 3 (pistol 30 x 3 = 90)? A (Claude): good, and it should be a tuning value. Alone it fixes guns, but not melee's short reach: the bat at 500 ms gets about 10 swings x 9 = 90, still under a 100 hp wall, and at top speed 1 swing. Paired with a time-based reach of about 2 s, the bat gets about 40 swings x 9 = 360 and the pistol breaks 500 hp in 6 shots. So the suggestion is both together, tuned in playtesting. The dev then clarified (2026-11-02): ONE multiplier for ALL weapons, tunable. It goes into the weapons build as weapon_damage_multiplier, set to 2 "for now" after the dev saw the x3 table (2026-11-02) ([[project_weapons_plan]]). The time-based reach is still open, for when walls resume.
- Q: How do you get past a wall? Weapons aren't built yet, so: build walls together with a first, simple weapon; give walls a non-weapon way past for now; or wait for the full weapons plan? (Asked 2026-11-02.) A: build the weapon system FIRST, then walls (dev, 2026-11-02: "we need to build the weapon system first before we do the actual walls"). Walls are PARKED until the weapons plan ([[project_weapons_plan]]) is built.
