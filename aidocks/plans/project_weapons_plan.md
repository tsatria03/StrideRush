---
name: project_weapons_plan
description: SETTLED for Section 1, NOT BUILT (2026-11-02; sections: weapon system, ammo packs after their own Q&A, docks) - the weapon system, based on ToyMania's (not SimpleFighter's); needed before walls; which weapons, how you get them, firing, ammo, reload and targets; Q&A log
metadata:
  type: project
---

Status: SETTLED for Section 1 on 2026-11-02 (started on top of d956876). It comes before walls, which need something to smash them with ([[project_walls_plan]]). Not built: build one section per go-ahead ([[feedback_describe_dont_show_code]]). The ammo pack details (Section 2) get their own questions before that section is built.

Build sections:
Section 1: the weapon system.
- New globals/weapons.nvgt:
  - One weapon table: name, category (melee or artillery), damage, range in tiles, and whether it takes ammo, from ToyMania's draw_weapon() values. Key order: bat to laser, machine_gun, pistol.
  - A single weapon_damage_multiplier (2, tuning.nvgt) applied to every weapon's base damage on every hit (dev, 2026-11-02: "This multiplier applies to all weapons, tunable"). First discussed as 3; after seeing the x3 table the dev chose 2 "for now". So damage runs bat 6, boot 12, club 18, feat 24, fist 30, hammer 36, knife 42, laser 48, machine gun 54, pistol 60. Hits to break 100 and 500 hp walls: bat 17 and 84, boot 9 and 42, club 6 and 28, feat 5 and 21, fist 4 and 17, hammer 3 and 14, knife 3 and 12, laser 3 and 11, machine gun 2 and 10, pistol 2 and 9.
  - Range: horizontal only (dev, 2026-11-02: "We only need the horizontal one"). ToyMania's weprange, in tiles ahead: bat 1, boot 2, club 3, feat 4, fist 5, hammer 6, knife 7, laser 8, machine gun 9, pistol 10. Its second, vertical range (weprange2) is dropped. In time that's range times step_time: bat 0.5 s to pistol 5 s at 500 ms, and bat 0.05 s to pistol 0.5 s at 50 ms. Whether walls switch this to a time-based reach is still open in [[project_walls_plan]].
  - Per-gun ammo state (loaded, reserve), with tuning values gun_start_loaded 50 and gun_start_reserve 250.
  - draw: the number keys, the draw sound, and "<name> equipped." Drawing a weapon cancels any reload.
  - fire: per press with a 50 ms minimum; the machine gun repeats every 100 ms while held. Guns use ammo or play empty, and are blocked while reloading.
  - reload with R: any time not full, timed by get_sound_length() of the reload sound, ping when done, and spoken refusals. The ammo check on X.
  - A generic target hook for walls to fill in later: weapon_strike(range, damage) returns whether anything was hit, and is a no-op for now.
  - reset_weapons() runs from reset_run(): the bat drawn, guns full.
- keyboard.ini: a new fire_held = SPACE:down.
- run.nvgt run_input() calls the weapon input. pause.nvgt pauses and resumes the weapon timers.
- BUILT 2026-11-02 on top of 0493547. SECTION 1 COMPLETE: all 5 tests passed (2026-11-02): drawing, melee, the pistol's ammo and reload, the machine gun running dry plus reload refusals and cancel, and separate ammo with pause and a fresh run. As built:
  - globals/weapons.nvgt uses parallel arrays (weapon_names, weapon_damage, weapon_range, weapon_loaded, weapon_reserve) indexed 0 to 9. is_gun() marks machine_gun and pistol.
  - weapon_input() runs every frame from run_input(): reload_check(), then the number keys, fire or fire_held, R and X.
  - The run-start bat was first drawn quietly. CHANGED (dev, 2026-11-02): reset_weapons() (called from reset_run()) now draws it the normal way, with the draw sound and "bat equipped.", at the start of every run. Pressing 1 while holding it does nothing, as agreed.
  - weapon_strike(range, damage) returns -1 for now. On a hit it will return the target's x, and fire_weapon() then plays the weapon's hit there, plus shell for guns, through p.
  - reload_length comes from p.get_sound_length() of the reload slot, in ms. The refusals: "This weapon is still reloading.", "This weapon doesn't take any ammo.", "This weapon is already fully loaded.", and "This weapon has no more reserved ammo to reload." (that last one also plays empty).
  - keyboard.ini gains fire_held=SPACE:down. pause.nvgt pauses and resumes firetimer and reloadtimer. tuning.nvgt gains weapon_damage_multiplier 2, gun_start_loaded 50, gun_start_reserve 250, weapon_fire_gap 50 and machine_gun_fire_gap 100.
Section 2: ammo packs and the inventory. SETTLED 2026-11-02 (Q&A below):
- New globals/ammopack.nvgt: ammopackpool and the pack entity (x, countdown_start, loopslot, spent).
  - Spawned with the spawn sound and its loop. Picked up by either hand within the switch window: get, panned, and "You picked up an ammo pack.", then into the inventory.
  - Arriving on its tile on the ground, or landing while on it, plays break and loses it. Missed by a clean jump, its loop fades behind you until it's dropped.
- New globals/inventory.nvgt: item counts, a cursor, I and Shift+I cycling with the panned inv sound, and U to use. The ammo pack's use refills both reserves by 50, capped at 250.
- The spawner: packs as a separate, rarer spawn type (tunable chance) with their own folder, and in the testing spawn menu. hand_check() also checks packs, and player_land() checks for landing on one. Also all_pools, clear_run_objects(), and reset_run() clearing the inventory.
- keyboard.ini: inventory_next=I, inventory_previous=SHIFT+I, item_use=U. Tuning: ammo_pack_refill 50, gun_max_reserve 250, ammo_pack_chance.
Section 3 WRITTEN for the weapon system (2026-11-02, on top of 07501f2). The dev asked for the docks before the ammo pack Q&A ("ready for docks"), so the docks were done ahead of Section 2:
  - Changelog: 1 weapons entry (19 of 20). The 20th stays reserved for ammo packs.
  - Readme: a Weapons section, and the keys 1 to 0, Space, R and X. It says there's nothing to hit yet and walls are planned.
  - Todo list: weapons moved to finished; "walls that you smash through" and "ammo packs that refill your guns" added as unfinished.
  - Section 2 (ammo packs) is still open. Its first question, how you collect a pack, was asked but not answered.

Ammo packs (Section 2) Q&A:
- Q: How do you collect an ammo pack? (Asked 2026-11-02; Claude recommended running over it on the ground.) A (dev, 2026-11-02): you pick it up with your HANDS, and either hand works. Running on top of one BREAKS it (break plays, and it's lost). Pick it up from a few steps before it, "sort of like the traps". Per the hands rule, the pickup sound plays panned to the hand used ([[project_controls_plan]]).
- Q: Is the pickup window the same as the force field switch: any step of the usual countdown before the pack, and always at least the last half second? Packs have no misc/trap warn set, so there'd be no countdown cues, only the pack's own loop to judge by. (Asked 2026-11-02; Claude recommended yes.) A: yes, the same window as the switch (dev, 2026-11-02). The dev added that the same will apply to FUTURE ITEMS such as the keys: picked up with either hand, panned to that hand, within the switch window, and broken if you run onto them. Recorded as a game-wide items rule in [[project_controls_plan]].
- Q: What does a pack refill: the reserve of the gun you're holding, or both guns' reserves, and by how much? (Asked 2026-11-02; Claude recommended both guns' reserves, by 50 each, one full magazine, never above the 250 they start with.) A: both guns' reserves, by 50 each, capped at 250 (dev agreed, 2026-11-02). Tuning: ammo_pack_refill 50, gun_max_reserve 250.
- NEW (dev, 2026-11-02, same reply): after you get a pack, you need to OPEN it. So a picked-up pack goes into an INVENTORY, and using it from there opens it (the use sound) and refills the reserves. This needs an inventory, plus keys to cycle it and to use an item, which don't exist yet. The dev asked how ToyMania's inventory works.
- ToyMania reference (read only): globals/inventory.nvgt and the game loop in game.nvgt.
  - A dictionary inv of item name to count. give(item, amount) adds to it, and deletes the item at 0 or below. An invpos cursor indexes the alphabetically sorted key list.
  - cycle_inv(dir): Tab cycles forward and Shift+Tab back, wrapping. It plays misc/player/inv (1 to 6, random), panned by the item's position across the list from -25 to 25, and speaks "<item>. Item N of M", or "<item>s, <count>. Item N of M" for more than one.
  - useitem(): Shift+Enter uses the focused item. For ammo_pack it refuses with "You already have enough reserved ammo." when full; otherwise it plays use, removes one, adds a random 5 to 10 reserve rounds, and speaks "You received N rounds of ammo from this pack." Keys and toys only speak a description from an info.tmf file.
  - I opens an inventory menu, and "Your inventory is currently empty." when there's nothing.
  - Pitfalls not to copy: one hard-coded branch per item, find_directories() run on every use, invpos not clamped after the last of an item is removed, naive "s" plurals, and two description paths (speak versus dialog).
- Stride Rush already has misc/player/inv1-6 and give. Tab and Enter are the left and right hands here, so the inventory needs different keys.
- Q: Which keys cycle the inventory and use the focused item? (Asked 2026-11-02; Claude recommended I to cycle forward, Shift+I back, and U to use, all unused letters.) A: I, Shift+I and U (dev, 2026-11-02). NO inventory menu: the dev doesn't think one is needed, so ToyMania's I menu is not ported and I is the cycle key instead.
- Q: Are Claude's proposed defaults for the rest of ammo packs and the inventory OK (listed below)? (Asked 2026-11-02.) A: yes, all seven (dev, 2026-11-02), with number 3 refined: a pack also breaks if you're right on top of it, OR if you jump onto it by mistake, meaning you LAND while on its tile. A clean jump that's still in the air across its tile and lands beyond it misses it without breaking.
  1. Spawning: packs join the spawner as their own type with their own folder (objects/interaction/items/common/ammo_pack), at a lower, tunable chance than the obstacles (about 1 spawn in 8). They use normal spacing and never overlap an obstacle. spawn plays when one appears, then its loop plays at its tile. They also appear in the testing spawn menu.
  2. Pickup: either hand within the switch window plays get (get1 or get2), panned to that hand, and speaks "You picked up an ammo pack." The pack goes into the inventory and its loop stops.
  3. Running onto a pack on the ground, standing or crouched, plays break (one of break1-6) and it's lost. Jumping over it just misses it, and its loop fades behind you.
  4. Inventory: item counts that start empty every run. I and Shift+I cycle with ToyMania's panned misc/player/inv sound, speaking "ammo pack. Item 1 of 1", or "ammo packs, 3. Item 1 of 1", with correct plurals. With nothing: "Your inventory is empty." The cursor is corrected whenever an item runs out.
  5. U uses the focused item. For an ammo pack: if both reserves are already at 250, "Your guns' reserves are already full." and the pack is kept. Otherwise use plays, one pack is removed, both reserves gain 50 (capped at 250), and "Your guns' reserves have been refilled." is spoken. With nothing in focus: "You don't have anything to use."
  6. New keyboard.ini bindings: inventory_next=I, inventory_previous=SHIFT+I, item_use=U.
  7. Pause freezes packs like the obstacles. The inventory works any time in a run.
Original Section 3 plan: The changelog's last 2 entries in 1.0 go to weapons (dev, 2026-11-02: "We can fill in the last 2 entries with the weapon sections"), one for the weapon system and one for ammo packs, filling 1.0 to 20. No 1.1 block yet. Also the readme (the weapon keys) and the todo list.

Base (dev, 2026-11-02): ToyMania's weapon system, not SimpleFighter's. The dev wasn't sure SimpleFighter's would fit, since it parses its weapons from data files.

Sounds (rescanned 2026-11-02), in equipments/weapons/<category>/<name>:
- melee: bat, boot, club, feat, fist, hammer, knife, laser. Most have draw, fire1-3 and hit1-3; fist has fire1-2; laser has a single draw, fire and hit.
- artillery: machine_gun and pistol, with draw, empty, fire, hit, ping, reload and shell1-2 (fail.ogg was removed by the dev on 2026-11-02).

Controls already bound in keyboard.ini, unread so far ([[project_controls_plan]]): Space fires or swings, X checks ammo, R reloads, and 1 to 0 pick weapons 1 to 10.

ToyMania reference (read only): src/includes/main/globals/weapons.nvgt, plus the game loop in game.nvgt.
- draw_weapon(category, name) sets per-weapon damage, a two-axis range, fire times and reload time, plays draw, and speaks "<name> equipped". The number keys draw bat, boot, club, feat, fist, hammer, knife, laser, machine_gun, pistol, in that order.
- fire_weapon() plays fire (a gun with no ammo plays empty instead and doesn't fire), then fire_on_target() checks every enemy list within range: weapon hit (plus shell for guns), the target's hurt, and damage.
- The guns only exist in its endless mode. Each starts with 50 loaded and 250 in reserve, and reloading takes 2 to 2.5 s, then plays ping. The machine gun fires while Space is held, every 100 ms; everything else fires per press, at most every 50 ms.
- reload_weapon() refuses with spoken reasons: still reloading, takes no ammo, already loaded, or no reserve left.
- The ammo check speaks "You have X out of Y rounds of ammo loaded, and Z rounds of ammo in reserve."
- Pitfalls not to copy:
  - One shared ammo, maxammo and reserve for both guns, so switching guns carries the other gun's ammo over.
  - fire_on_target() is copy-pasted once per enemy type.
  - get_weapon_damage() is a second, separate damage table that disagrees with draw_weapon()'s.
  - Reload only works on an empty magazine.
  - Ammo is clamped once per frame in the game loop instead of where it changes.

Q&A log:
- Q: Which weapons can you use, and how do you get them: all ten on 1 to 0 from the start of every run (starting with one drawn), or only some at first with the rest picked up later? (Asked 2026-11-02; Claude recommended all ten from the start, starting with the fist drawn.) A: all ten available from the start (dev, 2026-11-02). Collectibles come "much later". A run starts with the BAT drawn (dev, 2026-11-02: "it should start with the bat, as that's tied to number 1"), not the fist Claude had suggested.
- Q: Gun ammo in an endless run with no pickups: ToyMania's 50 loaded and 250 in reserve for each gun, which can run out for the rest of the run; unlimited reserve; or a reserve that refills over time? (Asked 2026-11-02; Claude recommended ToyMania's numbers, with SEPARATE ammo per gun, able to run out until collectibles bring refills.) A: ToyMania's ammo (dev, 2026-11-02): 50 loaded and 250 in reserve per gun, able to run out for the rest of the run. Separate counts per gun, as recommended (ToyMania's shared count is a bug, not a feature). Values in tuning.nvgt.
- Q: When can you reload: only on an empty magazine like ToyMania, or any time it isn't full, topping up from the reserve? (Asked 2026-11-02; Claude recommended any time it isn't full.) A: any time it isn't full, topping up from the reserve (dev: "do what you recommend", 2026-11-02). Refusals: still reloading, takes no ammo, already full, no more reserved ammo.
- Sounds changed (rescan, 2026-11-02, same reply): machine_gun and pistol LOST fail.ogg (now draw, empty, fire, hit, ping, reload, shell1-2). NEW objects/interaction/items/common/ammo_pack: spawn, loop, get1-2, use, break1-6, a likely ammo pickup.
- Q: Should ammo packs be part of the weapons build, appearing during a run to refill gun reserves, or wait for the later collectibles plan as said before? (Asked 2026-11-02; Claude recommended including them as the LAST section of the weapons build, since ammo can now run out for good and the pack's sounds exist.) A: yes, ammo packs are the last section of the weapons build (dev agreed, 2026-11-02). Their details get their own questions when we reach them.
- Q: Weapons will have nothing to hit until walls are built: spikes are non-destroyable, and projectiles, hazards, mines and force fields have no hurt or death sounds. Is it OK that the weapons build only covers drawing, firing (fire plays; melee hits land on nothing), ammo, reload and the ammo check, with a generic target hook that walls plug into next? (Asked 2026-11-02; Claude recommended yes.) A: agreed (dev, 2026-11-02).
- Q: Are Claude's proposed defaults for the remaining weapon details OK (listed below)? (Asked 2026-11-02.) A: yes, all eleven, with number 5 revised to use the reload sound's length (dev, 2026-11-02: "agreed with the rest").
  1. Keys, in ToyMania's order: 1 bat, 2 boot, 3 club, 4 feat, 5 fist, 6 hammer, 7 knife, 8 laser, 9 machine gun, 0 pistol.
  2. Drawing plays draw and speaks "<name> equipped." through the speech buffer, with underscores read as spaces ("machine gun"). Drawing the weapon you already hold does nothing.
  3. Firing: one shot or swing per Space press, at most one every 50 ms. The machine gun keeps firing every 100 ms while Space is held. That needs a new fire_held binding (SPACE:down) in keyboard.ini.
  4. A gun with nothing loaded, or one that's mid-reload, plays empty and doesn't fire.
  5. Reloading takes 2 s for the pistol and 2.5 s for the machine gun, and ping plays when it's done. Drawing another weapon mid-reload cancels the reload.
     REVISED (dev, 2026-11-02, asking about SimpleFighter's reload length check): the reload lasts exactly as long as the gun's reload sound, not a fixed time. SimpleFighter reference (read only): start_reload() in src/includes/main/globals/weapon.nvgt plays reload, then sets reload_duration = p.get_sound_length(slot); check_reload() loads the ammo and plays ping once reload_timer passes it. Stride Rush's deps/sound_pool.nvgt has the same get_sound_length(). The fixed 2 and 2.5 s times are dropped.
  6. X with a gun speaks one sentence, "You have X out of 50 rounds loaded, and Y rounds in reserve." With a melee weapon: "This weapon doesn't take any ammo."
  7. Each weapon's damage and range (tiles ahead) come from ToyMania's draw_weapon() table, kept as one table in code. Range uses only the x axis. They do nothing until walls exist.
  8. You can fire while jumping or crouched.
  9. Pause freezes the reload and fire timers.
  10. Every run starts fresh: the bat drawn, and both guns at 50 loaded and 250 in reserve.
  11. The player's own weapon sounds (draw, fire, empty, reload, ping) play stationary through p. Hit and shell will play at the target once targets exist.
