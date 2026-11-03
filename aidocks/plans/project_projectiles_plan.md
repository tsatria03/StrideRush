---
name: project_projectiles_plan
description: SETTLED, NOT BUILT (2026-11-02; 2 build sections: the obstacle, then docks) - projectiles, moving obstacles from sounds/objects/kombat/projectiles; how they're avoided, how they move, warned, hit and placed; Q&A log
metadata:
  type: project
---

Status: SETTLED 2026-11-02 (started on top of 0bf44b5, right after force fields were finished). The dev raised it after adding projectile sounds. Not built: build one section per go-ahead ([[feedback_describe_dont_show_code]]).

Build sections:
Section 1: the projectile obstacle.
- New globals/projectile.nvgt, with projectilepool, a projectile class (meet_x, theme, loopslot, countdown_start, plus the spent and hit flags), spawn, a per-frame flight update, check, countdown, remove and destroy_all.
  - Spawned with its loop at meet_x plus (meet_x minus me_x), so it starts as far beyond the meeting tile as you are before it.
  - The per-frame update places the loop at meet_x plus (projectile_speed_factor minus 1) times your fractional distance to meet_x (meet_x minus your position). With a factor of 2 it starts that distance beyond meet_x and reaches meet_x exactly when you do. Once the distance goes negative it carries on behind you. Your fractional position is me_x plus the step timer's progress through the current step. A ducked projectile keeps going behind you by the same rule.
  - Contact on the step you arrive at meet_x: crouched is safe; otherwise a survivable hit plays its hit, misc/player/hit and the life sound and stops its loop, and a fatal hit plays its hit through p, then end_run_hit().
- tuning.nvgt: projectile_life_cost 1 and projectile_speed_factor 2.
- Wiring, per the new-obstacle checklist: obstacle_types and place_obstacle() in spawner.nvgt, all_pools, clear_run_objects(), the check and countdown calls in step_check(), and the flight update in run_loop(). The testing spawn menu picks the type up automatically.
Section 2: docks. Changelog entries in 1.0 (it has room for 3 more), the readme (projectiles and the crouch now having a use), and the todo list (crouch-under obstacles to finished).

Sounds (rescanned 2026-11-02):
- objects/traps/projectiles (moved there from objects/kombat by the dev, 2026-11-02): eight themes, each with a loop and a hit, numbered variants picked by wildcard.
  - boulder: loop, hit1-3 (first "bolder", renamed by the dev).
  - car: loop1-6, hit.
  - car2: loop1-5, hit1-5.
  - firewall: loop, hit.
  - missile, missile2, missile3, missile4: loop, hit.
- misc/trap/projectiles/warn1-5: already there, their own countdown set ([[project_sound_layout]]).
- misc/player/hit, life and death exist for being hit.
- Note: the folder is objects/kombat/projectiles, not objects/traps, so the spawner's "objects/traps/" + type path needs a per-type folder, or a mapping, for this type.

Already recorded elsewhere:
- Obstacles plan ([[project_obstacles_plan]]): the three-height model lists "projectiles at head height" as a HIGH obstacle, ducked under with Down held. No duck-under obstacle exists yet, so crouching currently has no use.
- SimpleFighter reference (read only): builder/kombat/projectile.nvgt. A projectile plays its theme's loop, moves one tile per speed interval in a direction, can bounce at edges or be destroyed, and plays hit on contact. projectile_zone.nvgt spawns them at random within a range on a timer. In SimpleFighter, weapons can destroy projectiles ([[reference_simplefighter_builder_objects]]).
- The friend's runner template: a projectile moves along x and hurts on contact ([[reference_friend_runner_template]]).

Q&A log:
- Q: How does the player get past a projectile: duck under it, jump over it, or does it depend on the theme? (Asked 2026-11-02; Claude recommended ducking under all of them.) A: duck under all of them (dev, 2026-11-02: "I highly recommend ducking for all of these"). Projectiles are the first HIGH (duck-under) obstacle, which finally gives the crouch a use. One action for every theme, so the shared warn set always means "duck".
- Q: Does a projectile fly toward you, or sit still at head height? (Asked 2026-11-02; Claude recommended flying, with its sound moving toward you but timed to reach a fixed meeting tile exactly when you do, so the countdown stays as reliable as a still obstacle's.) A: it flies toward you (dev, 2026-11-02: "It doesn't just sit there waiting for you to run into it"). Claude's meeting-tile timing is the working approach unless the dev objects.
- Sounds moved (dev, 2026-11-02, same reply): the folder is now objects/traps/projectiles, and "bolder" is now "boulder". The note above about objects/kombat no longer applies, because the spawner's objects/traps/<type> path works as is.
- Q: A crouch stands you back up after 1.5 s, but at 500 ms the countdown is 2.5 s long. Crouch only on the last few cues (like jumping a hazard on its last two), or make a crouch last longer? (Asked 2026-11-02; Claude recommended keeping the 1.5 s crouch.) A: keep the 1.5 s crouch (dev: "do what you recommend", 2026-11-02, after asking for the whole projectile recap again). At 500 ms you crouch from about warn3 on; from about 300 ms and faster any cue works, the same pattern as jumping a hazard on its last steps. duck_time and duck_cooldown stay unchanged.
- Q: What does a projectile hit cost: 1 life like spikes and force fields, 2 like mines, or the whole run like hazards? (Asked 2026-11-02; Claude recommended 1 life.) A: 1 life for now (dev, 2026-11-02), as projectile_life_cost in tuning.nvgt, open to raising later.
- Q: Does jumping into a projectile also hit you, so only a crouch gets you past? (Asked 2026-11-02; Claude recommended yes: it's at head height, and a jump lifts you into it.) A: yes, a jump doesn't get you past a projectile (dev, 2026-11-02: "you cannot jump with projectiles"). Contact hits you unless you're crouched; in the air or standing both count as hits.
- Q: What happens on contact and after? Claude's proposal: ducked under, it keeps flying past you and its loop fades out behind you. A survivable hit plays the projectile's hit with misc/player/hit and the life sound, and the projectile stops there (its loop ends, like an exploded mine). A fatal hit plays its hit through p, then the death and the tile's fall, like spikes. (Asked 2026-11-02.) A: yes, as proposed (dev, 2026-11-02).
- Q: How fast does a projectile come at you? Claude's proposal: it closes in twice as fast as a still obstacle seems to. It appears at the usual 3 s before its countdown, but starts as far beyond the meeting tile as you are before it, and flies at your own speed toward you, so it covers double the distance in the same time. The factor is a tuning value. (Asked 2026-11-02; Claude recommended 2.) A: twice as fast, scaled with your movement speed (dev, 2026-11-02), as projectile_speed_factor 2 in tuning.nvgt.
- Q: Are Claude's proposed defaults for the remaining details OK (listed below)? (Asked 2026-11-02.) A: yes, all six (dev, 2026-11-02: "I agree with all of this").
  1. Spawning: projectiles join the random mix with an equal chance and a random theme. They show up in the testing spawn menu as "projectiles". Normal spacing, with no ledge and no extra gap.
  2. Countdown: the same countdown_steps() length and play_countdown() as the others, using misc/trap/projectiles/warn.
  3. Contact: checked on the step you arrive at the meeting tile. Crouched means safe; standing or in the air is a hit.
  4. Smooth flight: the loop's position moves every frame, not in one-tile jumps per step, so it sounds like it's flying. It's worked out from how far through the current step you are.
  5. After a duck, it keeps flying away behind you at the same speed until it's a spawn distance behind, then it's dropped.
  6. Pause freezes it with everything else.
