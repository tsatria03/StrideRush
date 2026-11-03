---
name: project_walls_plan
description: PARKED until weapons are built (2026-11-02) - walls as a full-height obstacle from sounds/objects/construction/walls; how they're passed (weapons or otherwise), warned, hit and placed; Q&A log
metadata:
  type: project
---

Status: IN DISCUSSION, started 2026-11-02 on top of d956876. The dev chose walls ahead of doors ("Not yet. Let's talk about walls first"). No code until the plan is settled and the dev gives a go-ahead ([[feedback_plans_record_qna]]).

Sounds (rescanned 2026-11-02):
- objects/construction/walls/wallglass: loop, hit1-2, hurt1-3, death1-2. It replaced walldirt. It's the only wall theme so far.
- Unlike the obstacles, walls sit under objects/construction, not objects/traps, so the spawner's objects/traps/<type> path would need a folder per type.
- There's no misc/trap/walls warn set. The five warn sets are force_fields, hazards, mines, projectiles and spikes. Under the sounds-first rule, a wall countdown needs either its own warn set or a decision to borrow one ([[feedback_sounds_before_features]]).
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
- Q: (dev, 2026-11-02) Should the max hp for walls be lowered? A (Claude): hp alone isn't the real limit; reach is. With ToyMania's table, a weapon can only hit a wall within its range in tiles (bat 1 up to pistol 10), so the time you can hit for is range times step_time. The bat gets one step, 500 ms at the start (about 10 swings at 50 ms each, about 30 damage) and a single 50 ms swing at top speed. Even 100 hp is out of reach for melee. Suggested fix, to settle when walls resume: give every weapon a TIME-based reach, for example the last 2 s before the wall, scaled with speed like the countdowns, and set damage so a wall breaks in a fair number of hits. Then 100 to 500 hp can stay as a spread of tough and easy walls. Not decided; walls are parked.
- Q: (dev, 2026-11-02) What about a damage multiplier, such as weapon damage times 3 (pistol 30 x 3 = 90)? A (Claude): good, and it should be a tuning value. Alone it fixes guns, but not melee's short reach: the bat at 500 ms gets about 10 swings x 9 = 90, still under a 100 hp wall, and at top speed 1 swing. Paired with a time-based reach of about 2 s, the bat gets about 40 swings x 9 = 360 and the pistol breaks 500 hp in 6 shots. So the suggestion is both together, tuned in playtesting. The dev then clarified (2026-11-02): ONE multiplier for ALL weapons, tunable. It goes into the weapons build as weapon_damage_multiplier, set to 2 "for now" after the dev saw the x3 table (2026-11-02) ([[project_weapons_plan]]). The time-based reach is still open, for when walls resume.
- Q: How do you get past a wall? Weapons aren't built yet, so: build walls together with a first, simple weapon; give walls a non-weapon way past for now; or wait for the full weapons plan? (Asked 2026-11-02.) A: build the weapon system FIRST, then walls (dev, 2026-11-02: "we need to build the weapon system first before we do the actual walls"). Walls are PARKED until the weapons plan ([[project_weapons_plan]]) is built.
