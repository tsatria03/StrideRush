---
name: project_doors_plan
description: SETTLED, NOT BUILT (2026-11-03, for 1.1; sections: doors without weapon hits, fake doors broken by weapons, docks) - doors, real and fake; what real doors do, how fake doors are broken, warnings, and how keys will tie in; Q&A log
metadata:
  type: project
---

Status: SETTLED 2026-11-03 (started on top of d43cbc2, after walls were finished). The dev wants doors before keys: "Keys are things doors will use to unlock them, but we should talk about doors first." Not built: build one section per go-ahead ([[feedback_describe_dont_show_code]]).

Build sections:
Section 1: real and fake doors, without weapon hits. Fake doors can't be broken yet, so every one gets crashed into.
- New globals/door.nvgt with doorpool and the door entity (x, theme, pitch, real flag, hp, countdown_start, loopslot, opened, destroyed and crashed flags).
  - The loop plays at the door's pitch. Every door sound passes the door's pitch through the extended 2d play.
  - Real doors open with either hand in hand_window_start(): open, then move as you pass the tile, then close behind you. A crash on any standing door plays hit, misc/player/hit and life, with no death sound, costing door_life_cost 3; a fatal one plays its hit through p, then end_run_hit().
- spawner.nvgt: track the last 50 ms mark reached. When step_time first drops to or below a new mark (450 ... 50), the next spawn is forced to be a real door. Fake doors join the random mix as their own type, using the folder objects/transitions/doors, so place_obstacle() needs a door case that isn't under objects/traps. No countdown cues; the countdown length is still reserved for spacing and the hand window.
- hand_check(): a field first, then a real door, then an ammo pack.
- Wiring: all_pools, clear_run_objects(), the check call in step_check(), the testing spawn menu (fake doors), and tuning (door_life_cost 3; door_pitches 80, 90, 110, 120; door_section_ms 50).
- BUILT 2026-11-03 on top of 9424d2c. SECTION 1 COMPLETE: all 5 tests passed (2026-11-03): fake doors, opening a real door (after the ToyMania-style move rework), missing a real door (checked on both real-door options), a fatal door crash, and section doors in a normal run plus no real doors after top speed. As built:
  - door.nvgt: play_door() wraps play_extended_2d() with the door's pitch. spawn_door() rolls the pitch (real 100, fake from fake_door_pitches) and the hp (wall_spawn_hp(), unused until Section 2). open_door() is called from hand_check() after the force field search and before the ammo pack pickup.
  - door_check() runs in step_check() after wall_check(): a crash on a standing door; move on an opened door's tile; close on the next step, at the door's tile behind you. A fatal crash plays its hit through p with play_stationary_extended() at the door's pitch.
  - spawner.nvgt: next_door_mark starts at the first 50 ms mark below the starting speed ((step_time - 1) / 50 * 50, so 500 gives 450 and 400 gives 350). choose_next_obstacle() forces "real_doors" once step_time reaches the mark, then lowers it by door_section_ms, until it passes min_step_time. Real doors come in every run, whatever the testing spawn menu picked.
  - "fake_doors" is in obstacle_types (the spawn menu says "fake doors"). type_folder() maps both door types to objects/transitions/doors/ and everything else to objects/traps/<type>/.
  - tuning.nvgt: door_life_cost 3, door_section_ms 50, fake_door_pitches {80, 90, 110, 120}.
  - Test 1 (fake doors) passed. The dev asked how fake doors are pitched; the pitch is per door at play time, and the files are never changed.
  - ADDED for testing (dev, 2026-11-03): "real doors" in the testing spawn menu, right after fake doors. Choosing it makes EVERY spawn a real door (spawn_only "real_doors"), so opening doesn't have to wait for a mark. "real_doors" is not in obstacle_types, so it never joins the "all" mix.
  - Test 2 passed "sort of". CHANGED (dev, 2026-11-03, pointing at ToyMania's doors): "as soon as the real door opens, it plays the move sound, then closes behind you. The footsteps are not meant to be played while you are moving through a real door. Also you are not allowed to use weapons, jump or duck either while it's moving you."
    - ToyMania reference (read only, globals/door.nvgt): opening plays open and starts move as a LOOP, sets doormove (which blocks weapons, reload, ammo, pause and other keys in game.nvgt), and carries you tile by tile. On arrival, move stops and close plays.
    - As now built: open_door() cancels any jump or crouch silently, plays open, starts move as a stationary loop at the door's pitch (door_moveslot), and sets door_moving. finish_door_move() runs once you're past the door's tile: it stops the loop, plays close at the door behind you, and clears door_moving.
    - The move loop's length: the dev asked whether it follows the sound's length or a fixed time. It's neither: it plays from opening until you're past the door's tile, so it depends on when you opened and your speed. KEEP AS IS (dev, 2026-11-03).
    - open now plays STATIONARY at the door's pitch (dev, 2026-11-03), not positioned at the door. move is stationary too; close still plays at the door, behind you.
    - While door_moving: play_step() is silent, jump_check() won't start a jump, can_duck() is false, hand_check() returns at once, and weapon_input() returns after reload_check(), so a reload already running still finishes. Pause still works, unlike ToyMania. destroy_all_doors() clears door_moving and the move loop.
  - The dev noticed that the "real doors" testing choice spawns a real door within seconds, which is as built (every spawn). ADDED (dev, 2026-11-03): a second choice, "real doors, spread" (spawn_only "real_doors_spread"). It spawns ONLY the real doors at the 50 ms marks, with the slots in between left empty, so both kinds can be tested. The menu order is now ... fake doors, real doors, real doors spread, ammo packs, all.
  - CHANGED (dev, 2026-11-03): "in the fake doors menu, remove the real doors from being spawned. It should strictly spawn fake doors." The section-mark real doors now come only when spawn_only is "all". Every single-type testing run (fake doors, walls, spikes and so on) spawns strictly that type, which also replaces the earlier "real doors in every run" note above.
Section 2: fake doors broken by weapons. weapon_strike() checks the nearest standing fake door ahead alongside walls, whichever is nearer. Hurt per hit, death at 0 hp, with hp from wall_spawn_hp().
Section 3: docks in 1.1 (changelog, readme, and doors moved to finished on the todo list).

Already decided (parked in [[project_obstacles_plan]], 2026-11-01 and 2026-11-02):
- Doors are full height. There are four door sound sets, door to door4, picked at random per door.
- Real door: plays at pitch 100 and is opened with an interact hand, as long as you don't run into it.
- Fake door: plays at exactly one of 80, 90, 110 or 120, never near 100, so it's always audibly different. It can't be opened with a hand. It must be destroyed with weapons (hurt on each hit, death when destroyed), or you smash into it (hit).
- Door type: SimpleFighter's normal doors, not passages. The dev put the move sounds in for a reason.
- Door sound flow: the loop plays while a door is present. Opening a real door plays open, then move, then close. grant, deny and jam are never played (Claude's proposals to use grant and deny were declined).
- Hand sounds are stationary and centered, never panned ([[project_controls_plan]]).
- Still open from 2026-11-01: how to keep the open, move and close sequence from sounding like an ending. Claude's options were open only; open and move with no close; or all three, with close placed behind the player and fading.
- Keys (objects/interaction/items/other/<color>_key, seven colors) will unlock doors. That's a later step, after doors.

Built pieces doors can reuse:
- The hand window and hand_check() from force fields, and the items rule for pickups.
- weapon_strike() and the target-hook pattern from walls, for fake doors.
- The countdown and the testing spawn menu.

Sounds (rescanned 2026-11-03):
- objects/transitions/doors/door, door2, door3, door4: close, death, deny, grant, hit, hurt, jam1-2, loop, move, open.
- There is NO misc/trap/doors warn set. Doors are under objects/transitions, not objects/traps, so they also need their own folder path in the spawner.

Q&A log:
- Q: What does a real door do when you open it in time? Claude's options: you just pass through (open, move, close, no other effect); it carries you forward like a SimpleFighter door, a few steps ahead with move playing (a safe skip); or something else. (Asked 2026-11-03; Claude recommended carrying you forward a few steps, since that's what move is for.) A (dev, 2026-11-03): a different idea for move. "At each 50 ms, the real door plays it, then moves to the next speed section. After the top speed, only fake doors will appear." So REAL doors become gates between speed sections, one at each 50 ms mark (450, 400 and so on down to 50), and opening one plays move as you go through into the next section. Once you're at top speed there are no more real doors, only fake ones.
- Q: Does going through a real door CAUSE the speed change (the speed holds steady inside a section, then drops 50 ms at each door), or does the run keep speeding up 10 ms every 10 s as now, with the real door marking each 50 ms milestone? (Asked 2026-11-03; Claude recommended keeping the smooth speed-up, with the door as the milestone marker, since 50 ms jumps get big late on: 100 to 50 ms doubles the pace in one step.) A: the door MARKS the section (dev, 2026-11-03). The speed-up stays as it is, 10 ms every 10 s, and a real door spawns each time the step time reaches a new 50 ms mark (450, 400 ... 50), opening into that section with move. The dev added: FAKE doors appear no matter what. They're part of the normal random mix at every speed, while real doors come only at the 50 ms marks and stop after top speed.
- Q: What happens if you don't open a real door in time? Claude's proposal: like an unswitched force field, you smash into it (hit, the player hit and life, 1 life), but you still go through into the new section, with no move. (Asked 2026-11-03.) A (dev, 2026-11-03): you smash into it LIKE A FAKE DOOR, and it costs 3 LIVES, not 1. So door_life_cost 3, the steepest cost so far after hazards (mines 2; spikes, force fields, projectiles and walls 1). The section still begins.
- Q: Does smashing into a fake door cost the same 3 lives? (Asked 2026-11-03; Claude recommended yes, one door cost for both kinds, since the dev described the real-door crash as "like a fake door".) A: yes, 3 for any door (dev, 2026-11-03). One door_life_cost 3 for real and fake.
- Q: How much hp does a fake door have? (Asked 2026-11-03; Claude recommended the walls' speed-scaled hp, 20 at 500 ms up to 2000 at 50 ms with a 20 percent spread, kept as separate door tuning values starting at the same numbers.) A: the same speed-scaled hp as walls, "since you need to destroy them" (dev, 2026-11-03). Whether they share wall_spawn_hp() or get door copies of the values is a build detail; Claude suggests sharing, with a note in tuning.
- Q: Doors have no warning set yet, and real and fake doors need different actions (a hand versus weapons). Should they share ONE misc/trap/doors set, played at the door's own pitch (100 for real, 80, 90, 110 or 120 for fake), so the countdown carries the same tell as the loop? Or have two separate sets? (Asked 2026-11-03; Claude recommended one set played at the door's pitch.) A (dev, 2026-11-03): NO countdown cues for doors. "Doors are not in the traps folder for a reason, so therefore it does not need any notes like walls did." Doors aren't traps, so you judge them by their loop and its pitch alone, like ammo packs. The spawner still reserves the countdown length for their spacing and hand window, but plays no cues.
- Testing menu (dev, 2026-11-03, "I need this for door markers"): the speed menu now offers only 500, 400, 300, 200 and 100. 450, 350, 250, 150 and 50 are gone. Done straight away in menus/menu.nvgt (the loop steps by 100 and stops at 100). Real doors STAY at every 50 ms mark (dev confirmed, 2026-11-03), so each test start sits between two doors, and a run started at 400 gets its first real door at 350.
- Q: Are Claude's proposed defaults for the rest of doors OK (listed below)? (Asked 2026-11-03.) A: yes, all eight (dev, 2026-11-03), and the dev asked for a recap of the whole plan.
  1. Real doors: when the step time reaches a new 50 ms mark (450, 400 ... 50), the next spawn is a real door. None come after top speed, and the first real door in a run is at the first mark below your starting speed.
  2. Fake doors: an obstacle type in the random mix at every speed, with an equal chance, and in the testing spawn menu. Each picks a random door set and one of the pitches 80, 90, 110 or 120.
  3. Every sound a door makes (loop, open, move, close, hit, hurt, death) plays at that door's pitch, so a fake door sounds off throughout.
  4. Opening a real door: either hand within the usual hand window (the countdown steps, at least the last half second), like the force field switch. open plays at the door and its loop stops; move plays as you pass through its tile; close plays at the door behind you, fading as you run on. All are centered or positioned, never panned to the hand.
  5. A hand on a fake door does nothing (deny stays unused). Weapons don't affect real doors, so you can't skip one by shooting it.
  6. Breaking a fake door: weapon hits through weapon_strike(), like walls. Hurt on each hit, death at 0 hp, after which you run through. Its hp is the walls' speed-scaled hp.
  7. Crashing into a door (an unopened real door, or a fake door still standing): its hit, the player hit and the life sound, costing door_life_cost 3, with no death sound (like walls). On the last lives that make it fatal: its hit through p, then your death, then the tile's fall. The section still begins after a missed real door.
  8. Normal spacing; pause freezes doors; door sounds come from objects/transitions/doors, picked per door.
