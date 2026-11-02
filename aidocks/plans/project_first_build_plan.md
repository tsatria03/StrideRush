---
name: project_first_build_plan
description: PLANNED AND SETTLED (all 7 open questions answered), NOT BUILT - build plan for the first playable runner, in 7 sections (tuning and run loop, surfaces and footsteps, jump and duck, lives and end of run, hazards with spawner and ledges, spikes and mines, then player docs); files, functions, and open questions; built one section per go-ahead
metadata:
  type: project
---

Status: COMPLETE (2026-11-02). All 7 sections are built, tested and committed; the game is in 69dedf8 and the docks in 0f0ccff.
Written 2026-11-01 at the dev's request, on top of commit 44e4172. All 7 open questions were settled the same day, one at a time. No sections built yet. (Question 4's speak_buffer and the all/misc buffers were built early, at the dev's request.) Build one section per go-ahead, with no plan recap per section and no code in chat ([[feedback_describe_dont_show_code]]). Check the latest commit before each section ([[feedback_check_git_log_for_commits]]). Rescan sr/sounds before each section ([[feedback_sounds_before_features]]). Flag a commit point after each section.

Designs this plan implements: [[project_run_plan]], [[project_obstacles_plan]], [[project_end_of_run_plan]], [[project_controls_plan]]. Object files follow [[project_entity_pattern]]. Sounds follow [[project_sound_layout]].

Where files go: new files go in the existing glob-included folders (main/globals, main/functions, main/menus), so includes.nvgt doesn't change. Object types each get one file in main/globals, like ToyMania's entity files.

All input goes through controls.action_triggered() with the keyboard.ini action names. All tunable numbers live in one file.

Section 1: tuning, run loop, pause, readouts and volume. BUILT 2026-11-01, on top of 4baed8b; all 11 tests passed 2026-11-02.
- As built: globals/tuning.nvgt, globals/run.nvgt, menus/pause.nvgt (all new); globals/decpool.nvgt (pause_pools, resume_pools, and muspool and ambpool added to all_pools); menus/menu.nvgt (start game calls m.fade_music() then start_run()).
- Differences from the plan:
  - tuning.nvgt holds only Section 1's values. Each later section adds its own, so no number is invented before its design is used.
  - The volume step constant is named volume_change, to avoid confusion with sound_pool's own volume_step member.
  - The quit confirm is a small menu of its own, with items "Yes" then "No" and the prompt "Do you want to quit to the main menu?". form_menu's yes_no() uses lowercase items and puts the prompt in the list, which breaks [[feedback_yes_no_menu_labels]]. No or Escape speaks "canceled" and returns to the pause menu.
  - Escape in the pause menu resumes with the resume sound and doesn't say "canceled", since resuming is the action, like SimpleFighter.
- Volume runs from -50 to 0 dB, starting at 0 dB (changed from -10 at the dev's request, 2026-11-02). It's spoken the ToyMania way, "track -10" for music and "source -10" for ambience, at the dev's request during testing (2026-11-02). The first version spoke percentages.
- Test results (one step at a time, [[feedback_test_steps_one_at_a_time]]):
  - Passed: 1 distance, 2 speed, 3 time, 4 lives.
  - 5 volume: passed, with the wording changed to track and source, and the step changed from 2 to 1 per press, like ToyMania (dev, 2026-11-02). The retest passed. The dev then set both starting volumes to 0 dB instead of -10.
  - Passed: 6 pause, 7 resume (the run stays frozen while paused), 8 quit with No or Escape (says canceled and returns to the pause menu), 9 quit with Yes (back to the main menu), 10 a fresh second run, 11 speech buffer (comma, period and Shift with each, with the choose click).
  - SECTION 1 COMPLETE: all 11 tests passed (2026-11-02). Music and ambience are silent until objects/audio/musics and sources have files.
- The engine's timer.restart() also unpauses (Legacy-NVGT timestuff.cpp), so a run started after quitting from pause begins unpaused.
- globals/tuning.nvgt: every tunable number as a named constant, in one place.
  - start step 500 ms; speed-up 10 ms every 10 s; floor 50 ms
  - surface stretch 50 to 200 tiles
  - ledge minimum 2 tiles, plus the ledge target time
  - minimum obstacle gap as a time, plus the maximum gap
  - spawn-ahead distance
  - jump height 5 and jump tick 100 ms; duck time 1500 ms
  - mine arm distance
  - starting lives 1; life costs (spike 1, mine 2, hazard "ends the run")
  - volume step sizes
- globals/run.nvgt: run state and the loop.
  - State: player x (double), step interval, step timer, speed-up timer, run timer, lives, a running flag, and two pools (muspool for music, ambpool for ambience).
  - reset_run(): sets every run value back to its start.
  - start_run(): called by "start game". It resets, starts a random music track and ambience (from objects/audio/musics and sources, which are silent while those folders are empty), then runs the loop until the run ends. Then it cleans up and RETURNS, so main()'s loop reopens the menu. No recursive mainmenu() call.
  - run_loop(): the wait(5) frame loop. Each frame it calls the checks in a fixed order, then the input.
  - step_check(): when the step timer passes the interval, x advances one tile. Section 2 adds the footstep here.
  - speedup_check(): every period, shortens the interval down to the floor.
  - run_input(): pause, readouts, volume and buffercheck().
- Readouts (one sentence each, spoken through speak_buffer into "misc"): L lives, Z distance in tiles, C speed as the step time in ms, T run time. (Built with Q and E and steps per second; the keys moved to Z and C on 2026-11-02 when Q and E became the hands, and speed changed to ms.) F (score) waits for scoring (open question 6).
- Volume: Home and End change the ambience pool's volume; Page Up and Page Down change music.
- globals/decpool.nvgt: adds pause_pools() and resume_pools() (from SimpleFighter) and registers the new pools.
- menus/pause.nvgt: pause_menu(), a form_menu loop with exactly "resume game" and "quit game". Quit game ends the run and returns to the main menu after a Yes/No confirm and reads the confirm menu's OWN result (the ToyMania bug). pause_game() and resume_game() pause and resume every timer and pool. Escape in the pause menu resumes.
- menus/menu.nvgt: "start game" calls start_run() instead of the placeholder dialog.
- F1 (view bindings) and F2 (settings) are both left OUT of this build (dev, 2026-11-01; open question 5). Their keyboard.ini actions (view_bindings, settings) stay in the file, unused for now.
- Test: start a run, hear the readouts change, pause and resume, exit to the menu.

Section 2: surfaces and footsteps. BUILT 2026-11-02, on top of 778fcab; all 5 tests passed.
- As built:
  - globals/surface.nvgt (new) with reset_surface(), pick_surface(), surface_check(), tile_at() and play_step().
  - tuning.nvgt: surface_min_tiles 50 and surface_max_tiles 200.
  - run.nvgt: reset_run() calls reset_surface(); step_check() calls surface_check() and then play_step() after each move, so a new surface is heard on its first step.
- Surfaces at build time: carpet, cement, concrete and marble, with ledge excluded.
- Also changed during Section 2 testing (dev, 2026-11-02): the E readout now says "Your speed is <step_time> ms." (for example 500 ms, falling toward 50 ms) instead of steps per second.
- play_step() has no ground check yet. Section 3 adds it once jumping exists. Footsteps play in pool p, which pauses with the run.
- Tests, one at a time:
  1. footsteps at the start
  2. footsteps speed up
  3. the surface changes after a while
  4. each new run starts on a random surface
  5. pause stops footsteps and resume continues them
- SECTION 2 COMPLETE: all 5 tests passed (2026-11-02).
- Final keyset applied after Section 2 (dev, 2026-11-02): hands on Tab/A and Enter/D, lanes on Left/Q and Right/E, readouts on Z (distance) and C (speed). Tested: Z and C speak, and A, D, Q and E do nothing yet.
- globals/surface.nvgt:
  - State: the current surface tile and the x where the stretch ends.
  - pick_surface(): random from get_pack_sound_folders("objects/construction/platforms/*"), always skipping "ledge" and the current tile so it audibly changes. If no tiles exist, footsteps are silent.
  - surface_check(): when x reaches the stretch end, picks a new surface and a new random 50 to 200 tile stretch.
  - tile_at(x): "ledge" if x is inside any hazard's ledge range (section 5 fills those in); otherwise the current surface.
  - play_step(): a oneshot of objects/construction/platforms/<tile_at(x)>/*step* on every step, never thinned. It plays whenever you're on the ground, ducked or not (ducking is a crouch).
- step_check() calls play_step().
- Test: hear the surface change every so often.

Section 3: jump and duck. BUILT 2026-11-02, on top of f824cef; all 7 tests passed (2026-11-02). Added after testing at the dev's request: Alt+F4 quits the whole program from inside a run (exit_program in keyboard.ini, checked in run_input()). Tested and passed.
- As built:
  - globals/player.nvgt (new): me_y, jump_state, ducked, jumptimer and ducktimer, plus reset_player(), is_grounded(), is_ducked(), jump_check(), start_jump(), player_land(), duck_check(), start_duck() and stop_duck().
  - tuning.nvgt: jump_height 5, jump_tick 100, duck_time 1500.
  - run.nvgt: reset_run() calls reset_player(); run_loop() calls jump_check() and duck_check() after step_check().
  - surface.nvgt: play_step() is silent in the air. A crouch originally still stepped; it's silent too since the Section 4 revision.
  - pause.nvgt: pause_game() and resume_game() also pause and resume jumptimer and ducktimer.
- Sound lookups: the crouch uses "misc/player/duck*" and the stand-up "unduck*", because "*duck*" would also match unduck.ogg. Jump plays *jump* and *rise* together; landing plays misc/player *land* with the tile's *land*.
- On landing, a Down still held starts a crouch (from open question 2).
- Tests, one at a time:
  1. jump sounds and silence in the air
  2. landing sounds
  3. crouch sounds and steps while crouched
  4. auto stand-up after 1.5 s
  5. Up while crouched jumps
  6. Down in the air, then held on landing
  7. pause mid-jump
- globals/player.nvgt:
  - State: height y (0 is ground), jumping/rising/falling, a jump timer, ducked, a duck timer.
  - jump_check(): on "jump" while on the ground, play misc/player jump and rise together. If you're crouched, the crouch is cancelled first, with no unduck sound. Then rise 1 per jump tick up to the jump height, and fall back the same way.
  - On landing, play misc/player land together with the tile's land clip.
  - duck_check(): on "duck" while on the ground and not jumping, play misc/player duck and hold ducked. On "duck_release" or after the duck time, unduck and play unduck.
  - is_grounded() and is_ducked(): used by obstacle contact checks.
- Overlap (open question 2, settled): Up while crouched jumps at once; Down in the air is ignored.
- Test: jump and duck at different speeds; at high speed one jump covers many tiles.

Section 4: lives and the end of a run. BUILT 2026-11-02, on top of fd2cd49; check passed.
- As built:
  - globals/lives.nvgt (new): lose_lives(cost) returns true if the run continues (with the life sound) or false if the caller must end the run.
  - globals/endrun.nvgt (new): end_run_hazard(fall_clip), end_run_hit(), silence_run(), clear_run_objects() (empty until Sections 5 and 6 add their destroy_all calls) and finish_run().
  - tuning.nvgt: ends_run = -1, hazard_life_cost = ends_run, spike_life_cost 1, mine_life_cost 2.
  - run.nvgt: run_loop() breaks right after step_check() if the run ended on that step. After the loop, start_run() also calls clear_run_objects() and p.destroy_all(), so quitting from pause cleans up the same way a death does.
- Design detail: both endings call silence_run() BEFORE the blocking death sounds, so music, ambience and other obstacles' loops never play over the death. In the hit ending, the tile is read before silencing.
- Nothing triggers these until Section 5, so the check is: it compiles, and a normal run (including quit from pause) still works. PASSED (2026-11-02).
- Change made alongside Section 4 at the dev's request: play_step() is silent while crouched (open question 1, revised).
- Also at the dev's request (2026-11-02): a crouch cooldown, so Down can't be spammed.
  - After standing up, or after a crouch is cancelled by a jump, crouching is blocked for duck_cooldown, 1000 ms in tuning.nvgt, about as long as a jump lasts.
  - player.nvgt: duckcooldowntimer and can_duck(), used by both the Down press and the held-Down-on-landing crouch. reset_player() forces the timer so a new run can crouch at once.
  - pause.nvgt pauses and resumes the cooldown timer too.
- Tests passed (2026-11-02): no footsteps while crouched, and the crouch cooldown blocks repeat presses for about a second.
- globals/lives.nvgt:
  - lose_lives(cost): with lives left after the cost, play misc/player life and keep running. Otherwise end the run. A cost meaning "ends the run" always ends it.
- globals/endrun.nvgt:
  - end_run_hazard(fall_clip): stop the belt, stop music and ambience, dlgplay the hazard's own fall clip (blocking), then finish the run.
  - end_run_hit(): stop the belt and audio, dlgplay misc/player death, then dlgplay the current tile's fall clip, then finish the run.
  - finish_run(): calls every destroy_all_<type>(), clears state, and sets running false. The loop exits, start_run() returns, and the main menu reopens. No results dialog.
- Test: temporary debug only if needed. The real test comes with section 5.

Section 5: spawner, hazards and ledges. BUILT 2026-11-02, on top of a92870a; all tests passed, with several changes made during testing (below).
- As built:
  - globals/hazard.nvgt (new): hazardpool, class hazard (x, theme, loopslot, ledge_start, ledge_end), spawn_hazard() (reuses the first null slot), hazard_check(), remove_hazard(), destroy_all_hazards() and on_ledge().
  - globals/spawner.nvgt (new): next_spawn_x, reset_spawner(), spawn_distance(), next_gap(), spawn_check() and place_obstacle(), which picks a random hazard theme for now.
  - decpool.nvgt: hazardpool added to all_pools; new update_listeners() moves every pool's listener to me_x.
  - run.nvgt: reset_run() clears objects and resets the spawner and listeners. step_check() updates listeners and spawns before the surface and footstep. run_loop() calls hazard_check() every frame AFTER step, jump and duck, then stops the frame if the run ended.
  - surface.nvgt: tile_at() returns "ledge" on a ledge range.
  - endrun.nvgt: clear_run_objects() calls destroy_all_hazards().
  - tuning.nvgt: spawn_ahead_time 3000, min_gap_time 2000, max_gap_time 5000, min_gap_tiles 6, first_obstacle_tiles 10, ledge_target_time 1000, ledge_min_tiles 2, ledge_after_tiles 2.
- Behavior notes:
  - BUG FIX during testing (dev agreed, 2026-11-02): hazard_check() first ran every frame, so landing on a hazard tile also killed you. With a 1000 ms jump and 500 ms steps, you had to jump during exactly the one step before the hazard, and a landing racing the next step could still kill you. Jumping on the first ledge step was always fatal, and the dev died on the 4th hazard after clearing 3.
  - Now hazard_check() runs only inside step_check(), right after the move. You die only if you're grounded at the moment you step onto the hazard tile; landing while still over it is safe, and the next step carries you off.
  - run_loop() now calls jump_check() and duck_check() BEFORE step_check(), so a jump pressed on the same frame as a step counts before that step's check.
  - SECOND FIX during testing (dev agreed, 2026-11-02): ledges ran together into 4 or 5 ledge steps when hazards were close.
    - Cause: the 6-tile minimum gap left only 1 floor tile at the start, and none once the ledge before widened with speed (3 tiles at 400 ms, 4 at 300 ms).
    - Now there's always at least min_floor_time (1000 ms) of normal floor, never under min_floor_tiles (2), between one hazard's ledge after and the next one's ledge before.
    - spawner.nvgt: next_gap(ledge_before) requires ledge_after_tiles + floor_tiles() + ledge_before + 1. The spawner decides next_ledge_before when it sets the gap and passes it to spawn_hazard(x, theme, ledge_before), so a later speed-up can't widen that ledge into the floor.
    - hazard.nvgt: new ledge_before_tiles(). Gaps are now 7 to 10 tiles at the start, and 43 to 100 at 50 ms.
    - Retest passed (2026-11-02).
  - TESTING TOOL (dev request, 2026-11-02): a starting-speed menu after "start game".
    - menus/menu.nvgt: choose_start_speed() offers start_step_time down to min_step_time in 50 ms steps (500 to 50), and Escape says "canceled" and returns to the main menu.
    - It's shown only when running from source (SCRIPT_COMPILED false, the engine property SimpleFighter uses for its server menu). A compiled release always starts at start_step_time.
    - run.nvgt: start_run() and reset_run() take an optional starting_step_time.
    - Remove it, or keep it source-only, before release; the docks in Section 7 shouldn't mention it.
  - THIRD CHANGE during testing (dev, 2026-11-02): ledges are a fixed 2 tiles before and after at every speed. The dev didn't like ledges growing with speed.
    - tuning.nvgt: ledge_target_time and ledge_min_tiles removed, replaced by ledge_before_count = 2.
    - ledge_before_tiles() returns ledge_before_count.
    - The floor stretch between ledges still scales with speed (min_floor_time), so ledges never merge. Gaps at the start are unchanged at 7 to 10 tiles; at 50 ms they're 40 to 100.
    - CORRECTED ROOT CAUSE of the first "died on the 4th hazard" bug (the dev spotted it, 2026-11-02): the widening ledge was probably the main cause.
      - At 490 ms, after only 10 s, the 1-second ledge rounded up to 3 tiles. Jumping on the first ledge step then reached the hazard about 1.4 s later, after the 1 s jump had already landed: death, even under the arrival-only check.
      - The every-frame landing check was a real but secondary problem.
      - With a fixed 2-tile ledge and the arrival-only check, a jump on either ledge step always clears a hazard, because the 1 s jump covers at least 2 steps at any speed of 500 ms or faster.
      - Lesson: a warning that lengthens with speed is only safe if the action it cues lengthens too.
  - FOURTH CHANGE (dev, 2026-11-02): the ledge before is now one step per 100 ms of step time, rounded up (5 at 500 down to 1 at 100), to carry the countdown later. The speed cap is 100 ms, not 50.
    - tuning.nvgt: min_step_time 100; ledge_before_count replaced by ledge_ms = 100.
    - hazard.nvgt: ledge_before_tiles() = ceil(step_time / ledge_ms), at least 1.
    - The testing speed menu now runs 500 to 100. Jump on the last 2 ledge steps at 500 and 400 ms; any step at 300 and below. See [[project_obstacles_plan]] for the countdown design.
  - COUNTDOWN BUILT (dev added the sounds, 2026-11-02): sr/sounds/misc/game/hazcount1 to hazcount5.
    - hazard.nvgt hazard_countdown() runs once per step, after the footstep, from step_check().
    - On each ledge step before a hazard it plays hazcount(6 - steps_left), so the final ledge step is always hazcount5.
    - Cues play in 2d through hazardpool (the dev asked for positioned, never stationary), as fire-and-forget oneshots.
    - Position: first built at the hazard's tile, which sounded like the cue came from past the last ledge step. Changed at the dev's request (2026-11-02) to the ledge tile just stepped onto (me_x), so each cue sounds where you are on the ledge.
    - This lifts the earlier "warning cues deferred" status for hazards.
  - SPACING REWORK (dev asked that hazards be spread out given the 5-step ledge, 2026-11-02):
    - Gaps are now built from a random stretch of normal floor, min_floor_time 1000 to max_floor_time 4000 ms (new) at the current speed and never under min_floor_tiles 2. gap = ledge_after_tiles + floor + ledge_before + 1, never under min_gap_tiles 6.
    - min_gap_time, max_gap_time and first_obstacle_tiles were removed.
    - Hazards now spawn spawn_ahead_time (3 s) before their LEDGE starts, not before the hazard, so the loop is always heard 3 s before the countdown begins.
    - The first hazard sits at spawn_distance + ledge + minimum floor (13 tiles at 500 ms).
    - Resulting gaps: 10 to 16 tiles at 500 ms (5 to 8 s), 14 to 44 tiles at 100 ms.
    - Before this, gaps at 500 ms were 10 to 11 tiles, with the loop heard only about 0.5 s before the countdown.
  - Countdown and spacing tests PASSED (2026-11-02): the 5 cues at 500 ms (the dev called it "perfect"), 3 cues at 300 and 1 at 100, and the spacing at 500 and 100.
  - Remaining tests PASSED (2026-11-02): jumping clears a hazard and its loop fades behind; failing plays only the hazard's fall, then the main menu (which also confirms Section 4's hazard ending); pause freezes the hazard loop and countdown; a longer run where the countdown shrinks from 5 cues to 4 to 3. Test 5 (landing on a hazard ends the run) no longer applies.
  - SECTION 5 COMPLETE (2026-11-02). The game is properly playable: hazards, ledges, countdown and death.
  - Removal (changed during testing, dev, 2026-11-02): a hazard is removed once you're spawn_distance() tiles past it (about 3 s at the current speed), never before its ledge ends. Its loop now fades out behind you the way it faded in. First built as "removed right after the ledge", which cut the loop off abruptly about 3 tiles past.
  - At the start (500 ms): the first hazard is at tile 10 and heard from tile 4. Gaps are 6 to 10 tiles. The ledge before is 2 tiles and after is 2.
- Tests, one at a time:
  1. a hazard loop approaches and fades in (PASSED)
  2. ledge footsteps before and after (PASSED after the step-only hazard check fix; then the floor-between-ledges fix)
  3. jumping clears it and the loop goes quiet behind
  4. failing plays its fall, then the main menu
  5. landing on a hazard ends the run
  6. pause freezes the hazard loop
  7. a longer run at higher speed
- globals/hazard.nvgt (entity pattern):
  - hazardpool, a handle array, and class hazard (x, theme, loop handle).
  - spawn_hazard(x, theme): reuses the first null slot, or appends. Because no other object stores hazard indexes, reusing slots keeps the array bounded in an endless run without breaking the sentinel-null rule.
  - hazard_check(): on the step that lands on its x while grounded, end_run_hazard(objects/traps/hazards/<theme>/fall). Once passed, it's removed (destroy its loop, then set the slot to null).
  - destroy_all_hazards().
  - Each hazard records its ledge range: before = max(2, enough tiles to last the ledge target time at the current speed); after = 2.
- globals/spawner.nvgt:
  - State: next_spawn_x.
  - spawn_check(): when x plus the spawn-ahead distance reaches next_spawn_x, place an obstacle. Its type is random among the types this build has, its theme is random from that type's folders, and the next gap is random between the speed-aware minimum and the maximum.
  - min_gap(): tiles needed for the minimum gap time at the current speed, never less than a jump's clearance plus the ledges.
- Listener: every pool's listener follows x (2d). Obstacle loops are positioned at their x. Each obstacle pool is registered in all_pools (decpool.nvgt), so it gets max_distance 0 and the 2.5 pan and volume steps.
- Test: hazards approach, ledge footsteps play before and after, jumping clears them, and failing plays the hazard's fall and returns to the menu.

Section 6: spikes and mines. BUILT 2026-11-02, on top of 4d47f6c; SECTION 6 COMPLETE, all 5 tests passed (2026-11-02): the obstacle mix, spikes, mines, pause with an armed mine, and a longer mixed run. Changes made during testing are below (spike swing, fatal hit sounds, waiting for object sounds, the testing lives menu).
- As built:
  - globals/spike.nvgt (new): spikepool, class spike (x, theme, loopslot), spawn_spike(), spike_check(), remove_spike(), destroy_all_spikes().
  - globals/mine.nvgt (new): minepool, class mine (x, theme, armed, spent, loopslot), mine_arm_distance(), spawn_mine(), mine_check(), silence_mine(), remove_mine(), destroy_all_mines().
  - spawner.nvgt: choose_next_obstacle() picks the next type at random among hazards, spikes and mines (only those with theme folders), together with its ledge (hazards only), before the gap is set. place_obstacle(x, type, ledge_before) dispatches to the right spawn function.
  - run.nvgt: step_check() runs hazard_check(), spike_check() and mine_check() in turn, each followed by a stop if the run ended.
  - decpool.nvgt: spikepool and minepool added to all_pools. endrun.nvgt: clear_run_objects() also destroys spikes and mines.
  - tuning.nvgt: mine_arm_time 1500 and mine_arm_min_tiles 2 (3 tiles at 500 ms).
- Behavior:
  - Contact is checked on arrival while grounded, like hazards.
  - Spike: its hit plus misc/player hit together, then lose_lives(1). Its loop fades out behind you once passed.
  - Mine: spawn plays when it appears; light and the ticking loop start at the arm distance. Jumped over, it goes quiet behind you; stepped on, explode, the mine's hit and the player's hit play together, then lose_lives(2).
  - With 1 life, spikes and mines end the run through end_run_hit(): player death, then the tile's fall, then the main menu.
  - The hit sounds can overlap the start of the death sound, as in SimpleFighter's checkdeath flow.
- SPIKE SWING (dev, 2026-11-02), like SimpleFighter's configurable spike speed:
  - Each spike gets a random swing_time between spike_swing_min (500) and spike_swing_max (1000) ms when it appears, so some are fast and some slow.
  - The theme's loop clip is ONE swing, played once per swing as a positioned oneshot; hit is the spike hitting you.
  - The contact rule is unchanged (hit on arrival while grounded). Swings are sound only, not timed danger, since the belt controls arrival.
  - spike.nvgt: spike_swing() runs every frame from run_loop(); next_swing is timed off runtimer, so a pause freezes the rhythm. There's no kept loop handle any more. destroy_all_spikes() calls spikepool.destroy_all() to cut any swing still sounding.
- FATAL HIT SOUNDS (dev, 2026-11-02): when a spike or mine hit is fatal, the player hit no longer plays; only the player's death does.
  - Before, the player hit and death overlapped, and the object's hit got cut off because silence_run() clears spikepool and minepool.
  - lives.nvgt: new is_fatal(cost), checked first.
  - On a fatal hit, spike.nvgt and mine.nvgt play the object's hit (plus explode for a mine) through p, which silence_run() leaves alone, then call end_run_hit().
  - Non-fatal hits are unchanged: the object's hit at its tile, the player's hit, then the life sound.
  - This revises the end-of-run plan's mine and spike death order ([[project_end_of_run_plan]]): object sounds and player death, with no player hit, then the tile's fall.
  - Follow-up fix (dev, 2026-11-02): mine sounds were still cut off. The death's dlgplay only waited for itself, so a longer explode or hit overlapped the tile's fall and was then cleared by finish_run(). end_run_hit() now calls the new wait_for_pool(p) after the death, waiting until the object's sounds have finished (Enter skips) before the tile's fall.
- TESTING TOOL (dev request, 2026-11-02): a lives menu after the speed menu.
  - menus/menu.nvgt: choose_start_lives() lists max_test_lives (5, in tuning.nvgt) down to 1, in the order the dev asked for: 5, 4, 3, 2, 1. It's source-only via SCRIPT_COMPILED, like the speed menu; a compiled release starts with starting_lives. Escape says "canceled" and returns to the main menu.
  - run.nvgt: start_run() and reset_run() take an optional starting_life_count.
  - This makes spike and mine hits with lives left testable: the hit, then the life sound, and the run continues.
- Not given ledges or the countdown: per [[project_obstacles_plan]], those are for hazards. Ask the dev after testing whether spikes and mines should get them too.
- Tests, one at a time:
  1. the obstacle mix
  2. spikes cleared and hit
  3. mines armed, cleared and hit
  4. pause with an armed mine
  5. a longer mixed run
- globals/spike.nvgt (entity pattern):
  - spikepool, the array and class spike, with a loop.
  - spike_check(): on contact while grounded, the spike's hit and misc/player hit together, then lose_lives(spike cost). On the last life, end_run_hit().
  - spawn, remove and destroy_all as with hazards. Spikes have no ledges.
- globals/mine.nvgt (entity pattern):
  - minepool, the array and class mine, with an armed flag.
  - On spawn, the mine's spawn clip plays. At the arm distance, light plays and the loop starts ticking.
  - On contact while grounded: explode, the mine's hit and misc/player hit all at once, then lose_lives(mine cost).
  - Once passed, the loop goes quiet.
- spawner.nvgt adds spikes and mines to the random type pick.
- Test: all three obstacle types mixed. With 1 life, any hit ends the run with the right sounds.

Section 7: player docs (added by the dev, 2026-11-01). Done only after Section 6 is built and tested; no docs during Sections 1 to 6.
- sr/docks/readme.txt: the first real readme, covering what the game is, the goal, the keys (jump, crouch, the L, Q, E and T readouts, pause, volume, buffer keys), the obstacle types and how each ends or costs lives, and the lives system.
- sr/docks/changelog.txt: the first block, a "New in 1.0." header and player-facing entries for everything the first build ships ([[feedback_changelog_rules]]).
- sr/docks/todo list.txt: player-facing entries only, such as warning cues, duck-under obstacles, lanes, weapons, doors, force fields, scoring, settings (F1 and F2), and levels ([[feedback_docks_later]]).
- credits.txt isn't in this section unless the dev asks.
- All lines stay at or under 1024 characters ([[feedback_dock_line_length_1024]]). As of 2026-11-01 all four dock files are empty.
- WRITTEN (dev's go-ahead, 2026-11-02, after Section 6 was committed in 69dedf8): readme.txt, changelog.txt ("New in 1.0.") and todo list.txt, in the dev's earlier readme style ("Keyboard commands", "Letter L: ..., if pressed."; todo "****Unfinished." and "##...finished" sections). build/version.txt stays 1.0. The source-only testing menus aren't mentioned. Music and ambience are described only through their volume keys, since sounds/objects/audio/musics and sources are empty for now. Awaiting the dev's review.

Open questions to settle before or while building, one at a time:
1. SETTLED (dev, 2026-11-01): ducking is a crouch, not a slide. REVISED after playtesting (dev, 2026-11-02): footsteps do NOT play while crouched. Steps on a crouch felt wrong, and other similar runners go silent too. The duck sound marks the start, unduck the end, and the silence between them is the crouched state. A slide, with its own sliding sound, could come later if the dev finds the sound.
2. SETTLED (dev agreed, 2026-11-01): Up while crouched cancels the crouch and jumps right away. The jump and rise sounds play; unduck is skipped. Down in mid-air is ignored; there's no fast-fall sound, and a still-held Down starts a crouch on landing anyway.
3. SETTLED (dev agreed, 2026-11-01): obstacles spawn a fixed TIME ahead, about 3 seconds at the current speed (tunable), so the warning never shrinks as the run speeds up. Within that window the loop fades in by distance, using the pool settings already in decpool.nvgt: pan_step and volume_step 2.5 per tile, the dev's usual values, and max_distance 0, so no cutoff. Every obstacle pool must be registered in all_pools to get those settings. Reference: the friend's template placed a whole level's hazards at once and relied only on distance fading, which works for short fixed levels but not an endless run.
4. SETTLED and BUILT (dev, 2026-11-01): the buffer categories are "all" and "misc". sr.nvgt calls create_buffer("misc") at startup, which creates "all" first. Readouts and other run speech go through speak_buffer(text) (default "misc") rather than bare speak(). More categories, such as achievements or events, come later, created in alphabetical order like CookieCraze.
   - Speech module: the base stays SimpleFighter's speech.nvgt, which is newer: it sends braille, has the text-processing hook and keeps voice pitch.
   - Added to it: speak_buffer(), written fresh from CookieCraze's idea for SimpleFighter's speak() settings, and a default-voice fix in tts_dump_config(). Unlike CookieCraze's version, the fix still saves rate, pitch, volume and the screen-reader setting when no voice is chosen.
   - buffer.nvgt's interrupt default flipped to true (CookieCraze-style), so misc lines interrupt each other. Set it false on a category to make it queue.
   - The dev's relaunch passed with these changes (2026-11-01).
5. SETTLED (dev, 2026-11-01): leave F1 and F2 out for now. F2 needs a preferences design (what's in the Game, Menu and Speech tabs, plus saving and loading), which will be its own plan later. F1's bindings screen comes back with it.
6. SETTLED (dev, 2026-11-01): leave F out for now. No code reads info_score until scoring is designed; the binding stays in keyboard.ini.
7. SETTLED (dev, 2026-11-01): the pause menu has exactly two items, "resume game" and "quit game". More options can be considered later. "quit game" ends the run and returns to the main menu, like ToyMania's pause-menu Quit game (dev confirmed: quit = main menu). It asks Yes/No first and reads the confirm menu's own result.
