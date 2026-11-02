---
name: project_first_build_plan
description: PLANNED AND SETTLED (all 7 open questions answered), NOT BUILT - build plan for the first playable runner, in 7 sections (tuning and run loop, surfaces and footsteps, jump and duck, lives and end of run, hazards with spawner and ledges, spikes and mines, then player docs); files, functions, and open questions; built one section per go-ahead
metadata:
  type: project
---

Status: written 2026-11-01 at the dev's request, on top of commit 44e4172. All 7 open questions were settled the same day, one at a time. No sections built yet. (Question 4's speak_buffer and the all/misc buffers were built early, at the dev's request.) Build one section per go-ahead, with no plan recap per section and no code in chat ([[feedback_describe_dont_show_code]]). Check the latest commit before each section ([[feedback_check_git_log_for_commits]]). Rescan sr/sounds before each section ([[feedback_sounds_before_features]]). Flag a commit point after each section.

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
- Readouts (one sentence each, spoken through speak_buffer into "misc"): L lives, Q distance in tiles, E speed in steps per second, T run time. F (score) waits for scoring (open question 6).
- Volume: Home and End change the ambience pool's volume; Page Up and Page Down change music.
- globals/decpool.nvgt: adds pause_pools() and resume_pools() (from SimpleFighter) and registers the new pools.
- menus/pause.nvgt: pause_menu(), a form_menu loop with exactly "resume game" and "quit game". Quit game ends the run and returns to the main menu after a Yes/No confirm and reads the confirm menu's OWN result (the ToyMania bug). pause_game() and resume_game() pause and resume every timer and pool. Escape in the pause menu resumes.
- menus/menu.nvgt: "start game" calls start_run() instead of the placeholder dialog.
- F1 (view bindings) and F2 (settings) are both left OUT of this build (dev, 2026-11-01; open question 5). Their keyboard.ini actions (view_bindings, settings) stay in the file, unused for now.
- Test: start a run, hear the readouts change, pause and resume, exit to the menu.

Section 2: surfaces and footsteps
- globals/surface.nvgt:
  - State: the current surface tile and the x where the stretch ends.
  - pick_surface(): random from get_pack_sound_folders("objects/construction/platforms/*"), always skipping "ledge" and the current tile so it audibly changes. If no tiles exist, footsteps are silent.
  - surface_check(): when x reaches the stretch end, picks a new surface and a new random 50 to 200 tile stretch.
  - tile_at(x): "ledge" if x is inside any hazard's ledge range (section 5 fills those in); otherwise the current surface.
  - play_step(): a oneshot of objects/construction/platforms/<tile_at(x)>/*step* on every step, never thinned. It plays whenever you're on the ground, ducked or not (ducking is a crouch).
- step_check() calls play_step().
- Test: hear the surface change every so often.

Section 3: jump and duck
- globals/player.nvgt:
  - State: height y (0 is ground), jumping/rising/falling, a jump timer, ducked, a duck timer.
  - jump_check(): on "jump" while on the ground, play misc/player jump and rise together. If you're crouched, the crouch is cancelled first, with no unduck sound. Then rise 1 per jump tick up to the jump height, and fall back the same way.
  - On landing, play misc/player land together with the tile's land clip.
  - duck_check(): on "duck" while on the ground and not jumping, play misc/player duck and hold ducked. On "duck_release" or after the duck time, unduck and play unduck.
  - is_grounded() and is_ducked(): used by obstacle contact checks.
- Overlap (open question 2, settled): Up while crouched jumps at once; Down in the air is ignored.
- Test: jump and duck at different speeds; at high speed one jump covers many tiles.

Section 4: lives and the end of a run
- globals/lives.nvgt:
  - lose_lives(cost): with lives left after the cost, play misc/player life and keep running. Otherwise end the run. A cost meaning "ends the run" always ends it.
- globals/endrun.nvgt:
  - end_run_hazard(fall_clip): stop the belt, stop music and ambience, dlgplay the hazard's own fall clip (blocking), then finish the run.
  - end_run_hit(): stop the belt and audio, dlgplay misc/player death, then dlgplay the current tile's fall clip, then finish the run.
  - finish_run(): calls every destroy_all_<type>(), clears state, and sets running false. The loop exits, start_run() returns, and the main menu reopens. No results dialog.
- Test: temporary debug only if needed. The real test comes with section 5.

Section 5: spawner, hazards and ledges
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

Section 6: spikes and mines
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

Open questions to settle before or while building, one at a time:
1. SETTLED (dev, 2026-11-01): ducking is a crouch, not a slide, so footsteps keep playing while ducked. A slide, with its own sliding sound in place of footsteps, could come later if the dev finds the sound.
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
