---
name: project_bullets_plan
description: SETTLED, NOT BUILT (2026-11-03, for 1.1; sections: traveling bullets, weapons breaking items, docks) - traveling bullets for the guns, so ammo weapons stop hitting instantly like melee; speed, range, what they hit; Q&A log
metadata:
  type: project
---

Status: SETTLED 2026-11-03 (started on top of 45573ec, after doors were finished). The dev: "ammo based weapons act exactly like melee weapons. I mean the bullets do not actually travel." Its own feature (dev). Not built: build one section per go-ahead ([[feedback_describe_dont_show_code]]).

Build sections:
Section 1: traveling bullets for the guns.
- New globals/bullet.nvgt: bulletpool and the bullet entity (x, start_x, range, damage, weapon index, loopslot, a move timer that pauses with the game).
  - spawn_bullet() at me_x starts the gun's loop at the bullet.
  - bullet_flight() runs every frame and moves each bullet a tile per bullet_tile_time, updating its loop. On each new tile it checks for the first standing wall, fake door or unspent item there. On a hit, it plays the gun's hit there and calls the target's strike, then stops its loop and removes the bullet. Past its range it stops and is removed.
- weapons.nvgt fire_weapon(): for a gun, play fire and the shell at you and spawn a bullet, with no instant strike. Melee keeps the instant weapon_strike().
- Tuning: bullet_tile_time 30. Wiring: all_pools, clear_run_objects(), pause (the bullet timers), and run_loop() for the per-frame flight.
Section 2: weapons breaking items. Melee's weapon_strike() and bullets both consider unspent ammo packs (and future items) as targets, the nearest winning. A broken item plays its break sound and is lost.
Section 3: docks in 1.1 (bullets travel and break items; melee breaks items).

As built now ([[project_weapons_plan]], [[project_walls_plan]]): fire_weapon() calls weapon_strike(), which damages the nearest wall or fake door within weapon_reach() at once, for melee and guns alike.

ToyMania reference (read only): globals/bullet.nvgt.
- A bullet has bullx and bully, range and range2, damage, speed in ms per tile, a direction and a speedtimer.
- bulletloop() moves each bullet one tile per speed ms. Reaching the player within 2 tiles does damage and removes it; going past its range removes it.
- A bullet also breaks any item, key or toy it passes through, playing that object's break sound.
- In ToyMania ONLY enemy cars fire bullets (car.nvgt spawn_bullet). Its player guns hit instantly through fire_on_target(), which is what Stride Rush copied.
- Pitfalls: remove_at() inside the loop followed by return (one bullet per frame at most), and copy-pasted per-target checks.

Plan direction: guns (machine gun, pistol) fire a bullet that travels ahead; melee weapons stay instant within reach.

Q&A log:
- Q: How fast does a bullet fly? (Asked 2026-11-03; Claude recommended tying it to your speed, about 5 times the belt's pace.) A: a fixed 30 ms per tile (dev, 2026-11-03), as bullet_tile_time 30 in tuning.nvgt. So it's about 16 times your pace at 500 ms, and about 1.7 times at 50 ms.
- Q: How far does a bullet go before it vanishes? (Asked 2026-11-03; Claude recommended the same reach as now: weapon_reach() tiles from where it was fired, 2 s of your running, so guns and melee can still reach the same distance.) A: agreed (dev, 2026-11-03). A bullet vanishes after weapon_reach() tiles from where it was fired (the value at firing time).
- Q: (dev) Can you spray bullets before reaching a door or wall? A (Claude): you can fire whenever you like, and every shot uses a round. But a bullet fired while the target is still beyond reach vanishes before it gets there, so early spraying only wastes ammo. Shots fired once the target is within reach all land. Several bullets can be in flight at once (the machine gun fires every 100 ms, and a bullet needs up to 1.2 s to cross 40 tiles at 30 ms each). If the target breaks while some are still flying, they carry on to the next target within their range, or vanish.
- Q: Do bullets break ammo packs they pass through, as ToyMania's break items and keys? (Asked 2026-11-03; Claude recommended yes.) A: yes (dev, 2026-11-03: "I completely agree with this"). A bullet that reaches an unspent ammo pack, and later a key, breaks it: break plays at the pack and the bullet is used up. Same for future items.
- The dev added: "I think melee weapons also break items as well." (Checked: ToyMania's melee doesn't; fire_on_target() only hits enemies.)
- Q: Should a melee swing break an item that's the nearest thing within reach, the same nearest-target rule that picks between a wall and a fake door, so a swing breaks the pack instead of reaching past it to the wall? (Asked 2026-11-03; Claude recommended yes.) A: yes, for keys and ammo packs (dev, 2026-11-03). weapon_strike()'s nearest-target search then covers walls, fake doors and unspent items.
- Q: Are Claude's proposed defaults for the rest of bullets OK (listed below)? (Asked 2026-11-03.) A: agreed (dev, 2026-11-03), with number 5 REPLACED: the dev added loop.ogg to equipments/weapons/artillery/machine_gun and pistol as the bullet-in-flight sound. SimpleFighter reference (read only, globals/bullet.nvgt): the bullet plays its weapon's loop as a looping 3d sound at the bullet's position when fired, updates it on every tile move (update_sound_3d in bulletloop()), and destroys it on a hit or at the end of its range. So in Stride Rush each bullet loops its gun's loop at its tile, the loop moves with it, and it stops when the bullet lands or vanishes.
  1. Only the guns (machine gun, pistol) fire bullets. Melee stays instant within reach, now including items.
  2. A bullet starts at your tile and moves one tile every bullet_tile_time (30 ms). After each move it checks its tile: the first standing wall, fake door or unspent item there takes the hit.
  3. On a hit, the gun's hit plays at the target, then the target's own hurt, death or break, and the bullet is gone. Damage is the gun's, times the multiplier, as now.
  4. The shell plays at YOU as you fire (the casing drops at the gun), not at the target as it does now.
  5. (Replaced, see above: the gun's loop.ogg plays at the bullet while it flies.)
  6. Bullets pass straight through real doors (weapons can't harm them), and through every trap that isn't a target (spikes, mines and so on).
  7. Pause freezes bullets in flight, a new run clears them, and several can fly at once.
