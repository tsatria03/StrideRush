---
name: project_bullets_plan
description: COMPLETE (2026-11-03, in 1.1, which it filled to 10 of 10) - traveling bullets for the guns, so ammo weapons stop hitting instantly like melee; speed, range, what they hit; Q&A log
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
- BUILT 2026-11-03 on top of e1c2247. SECTION 1 COMPLETE: all 4 tests passed (2026-11-03): a bullet in flight (after the shell was moved back to the target), firing too early, the machine gun stream plus a real door plus pause in a mix, and the new ammo amounts with packs going to the equipped gun only. As built:
  - bullet.nvgt: next_move is on runtimer, so pause freezes bullets with no extra timer. bullet_flight() runs every frame from run_loop() after projectile_flight(); its while loop catches up if a frame was slow. Each move updates the loop with update_sound_2d (whole tiles are fine here, since a bullet moves a tile at a time). bullet_hits() checks wall_at() first, then fake_door_at(), on the exact new tile; the hit check comes before the range check, so a target exactly at the range still gets hit.
  - wall.nvgt wall_at(x) and door.nvgt fake_door_at(x) were added.
  - weapons.nvgt fire_weapon(): a gun plays fire and shell stationary at you and calls spawn_bullet(), with no instant strike. Melee plays fire, then weapon_strike(), then hit at the target; melee no longer plays a shell at all, since only guns have shells.
  - The dev asked whether the pistol plays its loop: it does, but at slow speeds its flight is about 0.1 to 0.2 s, hidden under the pistol's long fire sound. ToyMania's car bullets use 20 ms a tile (and a range of 0, a bug that removes them on the first move). The dev then set bullet_tile_time to 50 to try it (2026-11-03). Claude flagged that at 50 ms steps a bullet only keeps pace with you, so at top speed it can't get ahead to a wall before you do.
  - TEMPORARY TEST (dev, 2026-11-03): the pistol's fire sound is muted in fire_weapon() (marked TEMPORARY TEST) so its bullet loop can be heard on its own. It MUST be restored before committing or writing the docks. RESTORED (dev, 2026-11-03): the loops were confirmed audible ("The bullet loop sounds play"), and the pistol's fire sound is back.
  - bullet_tile_time SETTLED at 40 (dev, 2026-11-03), after 30 and a 50 trial: a longer, more audible flight than 30 that still outruns you at 50 ms steps.
  - Ammo (dev, 2026-11-03): "you have too much reserved ammo". Each gun had ToyMania's 50 loaded and 250 reserve, about 17 top-speed walls before needing a pack. Claude suggested 50 and 100 with a cap of 150. The dev chose 50 loaded and 50 in reserve, since "you can always collect more ammo" from packs, which go into the reserve that reloading draws on. gun_start_reserve is now 50. The reserve cap gun_max_reserve is now 200 (dev, 2026-11-03: "the max cap should be 200. I mean in reserve. You can only reload 50 at a time"). The magazine stays at 50, so a reload loads at most 50, which is how reload_check() already works (it fills up to gun_start_loaded). The readme's "250 in reserve" and "up to the 250 they start with" will need updating in the docks.
  - Ammo packs (dev, 2026-11-03): "It should only give between 5 and 10, not all 50 at once." ammo_pack_refill 50 was replaced by ammo_pack_min 5 and ammo_pack_max 10. One random roll is given to each gun, like ToyMania's random(5, 10), still capped at 200. The speech now says the amount: "You got N rounds of ammo for each gun." This changes the weapons plan's earlier "both guns by 50" answer ([[project_weapons_plan]]), and the readme's "adds 50 rounds" line needs updating in the docks.
  - CHANGED again (dev, 2026-11-03): ToyMania's single shared reserve meant a pack fed every gun; here it should only go to the gun you have EQUIPPED. use_ammopack() now adds the 5 to 10 to the current gun only, and says "You got N rounds of ammo." The count is trimmed to what fits under the 200 cap, so the number spoken is the number actually added. With a melee weapon out it says "This weapon doesn't take any ammo."; when that gun's reserve is full, "This weapon's reserve is already full." Both keep the pack.
  - tuning.nvgt bullet_tile_time 40; bulletpool in all_pools; destroy_all_bullets() in clear_run_objects().
Section 2: weapons breaking items. Melee's weapon_strike() and bullets both consider unspent ammo packs (and future items) as targets, the nearest winning. A broken item plays its break sound and is lost.
- BUILT 2026-11-03 on top of 509b237. SECTION 2 COMPLETE: all 3 tests passed (2026-11-03): shooting a pack, swinging at a pack (and picking one up still works), and the nearest target winning. As built: ammopack.nvgt has ammopack_at(x), ammopack_in_reach(reach) and strike_ammopack() (break_ammopack(), then return its x). weapons.nvgt weapon_strike() now picks the nearest of wall, fake door and pack, with a wall winning ties, then a door. bullet.nvgt bullet_hits() checks wall, then fake door, then pack on its tile. A broken pack also gets the weapon's hit (and, for bullets, the shell) at its spot. Keys will add their own _at and _in_reach pair when they exist.
Section 3 WRITTEN (2026-11-03, before the dev's commit), so BULLETS ARE COMPLETE:
- Changelog: two "Made it so" entries fill 1.1 to 10 of 10 (bullets plus the new starting reserve and cap; weapons breaking packs plus packs giving 5 to 10 to the gun you hold). 1.1 is FULL, so the next player-facing change opens 1.2 with build/version.txt going to 1.2.
- Readme: the weapons section explains traveling bullets and wasted early shots, gives 50 loaded and 50 reserve up to 200, and says weapons hit the nearest thing including packs. The packs section says weapons break them and that a pack gives 5 to 10 to the gun you're holding.
- Todo list: "Add bullets that fly ahead of you when you fire a gun." added to finished.
Original Section 3 plan: docks in 1.1 (bullets travel and break items; melee breaks items). 1.1 is a minor version, capped at 10 entries (dev, 2026-11-03), and has 8, so these two entries FILL it. The next player-facing change opens 1.2 with a version bump.

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
  4. The shell plays at YOU as you fire (the casing drops at the gun), not at the target as it does now. REVERSED during testing (dev, 2026-11-03): "The shell sound is supposed to play upon hitting the object, not when you fire the gun." The shell now plays with the hit, at the target, from bullet_hits().
  5. (Replaced, see above: the gun's loop.ogg plays at the bullet while it flies.)
  6. Bullets pass straight through real doors (weapons can't harm them), and through every trap that isn't a target (spikes, mines and so on).
  7. Pause freezes bullets in flight, a new run clears them, and several can fly at once.
