---
name: project_core_code_history
description: decision history moved out of the core files' comments (game, spawner, decpool, environments, player, surface, lane, lives, endrun, difficulty, practice, practice_hints) by the comment cleanup's Section 2 (2026-11-15); read before changing how one of them behaves
metadata:
  type: project
---

Moved here from the comments of twelve files in src/includes/main/globals/ on 2026-11-15 ([[project_comment_cleanup_plan]], Section 2), so the code keeps only what it does and why. Dates are when the dev decided; quotes are the dev's own words. The plans named hold the full Q&A. tuning.nvgt's history is in [[project_tuning_history]].

## game.nvgt
- The player as vector me: the lanes plan's Section 3 (2026-11-04, "vector me"); me.x and me.y took over the meanings of the old me_x and me_y.
- Practice runs: the game menu refactor plan's Section 3 (2026-11-05). Practice speed stays fixed all run (2026-11-05: "keep it as is"), except rising (the rising practice plan, 2026-11-12).
- Run music and ambience: the music and ambience plan (2026-11-06), repointed that day from the old, empty musics and sources folders. Shuffle: "a playlist behavior that shuffles a track, then plays another one when it ends".
- After an environment switch the current track finishes first (2026-11-10: "I want to finish the song").
- P is the pause menu only, and Escape goes straight to the quit run question (2026-11-03).
- F1 bindings and F2 settings with Game, Menu and Speech tabs (2026-11-01 and 2026-11-04).
- V environment readout, like L for the lane (2026-11-12).
- C readout (2026-11-06): steps a second instead of "Your speed is 470 ms.", at first rounded down to whole steps, then "I meant switch it to 1 dessimal place, so it says 2.1, 2.2, etc.", since whole steps read 2 all the way from 500 to 334 ms. Whole numbers drop their ".0" (2026-11-06: "I want it to say 2, unless the speed increases"). C in milliseconds for debug runs (2026-11-08: "speaking of debug, please make the C key read in milliseconds").
- Z says steps (2026-11-06: "say x steps, not x tiles").
- Volume keys stop silently at either end (2026-11-06: "When you reach the top and bottum of a value, it should stop repeating it. Example, pressing home passed 0 keeps saying source 0."). Volumes are saved for the next launch (2026-11-04).
- Items in lanes: the lanes plan's Section 4. A force field throw lands without the player's land sound, at the dev's request.

## spawner.nvgt
- Real doors at the 50 ms speed marks, and one key before each real door (2026-11-03).
- Theme folders moved into each type's general folder beside its countdown (2026-11-10). Countdown cues lived in misc/trap/<type> until 2026-11-10.
- Items in lanes: the lanes plan's Section 4 (2026-11-05). Each item got three debug lane choices like barriers (2026-11-05: "I want to do some further testing to see if what I discovered was an actual bug, or if my ears were playing a trick on me").
- Practice doors' keys come one at a time in a random lane, never with a pair's second item (2026-11-05). Practice's real doors joined that rule on 2026-11-09, then mixed obstacles' keys and the debug real doors choices (2026-11-13: "I should only see keys"), and free run's items one at a time.
- Survival items and the second item of a pair: the item balance plan (2026-11-10).
- The hand window shared by force field switches and item pickups: the dev's items rule (2026-11-02).
- Cues are exempt from the behind-pitch drop (2026-11-04). Layered countdown sets (2026-11-03).
- No warnings on a slide: the slides plan (2026-11-11). Mixed walls: the ladders plan's debug choice.
- The structure of choose_next_obstacle() and its helpers: [[project_spawner_reorg_plan]].

## decpool.nvgt
- behind_pitch_decrease 5, with a Game tab setting to turn it off (2026-11-04 and 5).
- The forward belt, x across and y along: the lanes plan's Section 3 (2026-11-04).
- Pausing keeps the ambience playing (2026-11-08: "every sound should be paused, excluding the ambience").

## environments.nvgt
- Environments: the environments plan (2026-11-10), Section 1 the folders and Section 2 the switching ([[project_environments_plan]]).
- Traps versus transitions: the transitions plan (2026-11-13). Vehicles got a category of their own: the vehicles plan (2026-11-13).
- Start environment: random, automatic only (2026-11-10). The starting announcement only with more than one environment (2026-11-10).
- The environment announcement interrupts the "fist equipped." weapon line (2026-11-11: "the env switch should be interupted when you start a turn. RIght now the weapon equip speaks first").
- "You've entered the ... environment." in the misc buffer, no sound (2026-11-10).

## player.nvgt
- play_landing(false) for throws and teleports (2026-11-03): it "should not play your character's land sound".

## surface.nvgt
- The source-only debug option "Do you want to hear your footsteps while running?" (2026-11-04).
- footstep_volume: the footstep volume plan (2026-11-10, [[project_footstep_volume_plan]]).

## lane.nvgt
- Lanes came in 2026-11-04, for 1.4: Section 1 of the lanes plan, recoded by hand after the 1.3 undo ([[project_lanes_plan]]). Sounds followed Section 1B's settled rules so they wouldn't need redoing when the belt turned forward. Footsteps and landings stay centred ("all platform sounds should stay in the center").
- turn into the middle lane is centred (2026-11-04: "If I go in the middle, it's supposed to play in the center").
- Lane keys do nothing at a floor breaker's edge (2026-11-13).
- The six inventory items joined lanes in the lanes plan's Section 4.
- The HRTF fixed angle (2026-11-05): with HRTF, one unit across sounded almost straight ahead while the thing was far off.

## lives.nvgt
- Health and lives (2026-11-03, for 1.2, [[project_player_health_plan]]). Damage past 0 is dropped ("It should not carry into the next life").
- lives_can_end false only from the source-only debug options (2026-11-02).
- The "health potions" debug run starts at half health (2026-11-04).
- The no-life-sound refill on the last life: a bug found by the dev (2026-11-04), when it played life.ogg anyway.
- The H readout "70 percent health remaining, 2 lives." (2026-11-03). Free run's fuller H format, after SimpleFighter's fullest format (2026-11-13): "60 percent, 300 of 500 health remaining, 3 lives."

## endrun.nvgt
- restart_run_requested: the debug "end the run when out of lives?" No answer (2026-11-02).
- run_died, so play_game() asks whether to play again (2026-11-03).
- Floor breaker death: the floor breakers plan (2026-11-13); after testing, its fall and the player's death are "supposed to play at the same time".
- Practice deaths: the practice deaths plan (2026-11-09, [[project_practice_deaths_plan]]): "it will use up your 2 lives, then it will kill you like in the real game, but let you try again." Set down with everything back: "It gives you everything back."
- The death dialog naming what caught you, and the "What would you like to do now?" menu: the practice guidance plan's Section 3 (2026-11-12, [[project_practice_guidance_plan]]).
- A free run on no deaths takes you straight back with no dialog or menu: the free run tools plan (2026-11-14: it should take you straight back, as the debug does).
- "retry free run" instead of "retry practice": a free run on practice deaths isn't a practice run (2026-11-13).
- A worn shield comes off at a practice death (2026-11-10: it had stayed on).

## difficulty.nvgt
- The run's difficulty: the game menu refactor plan's Section 4 (2026-11-05).
- The locks: Section 6. A run counts only after passing a real door you opened (2026-11-05: "you need to open a door and get past it."); a crash doesn't count.
- The schedule (has_joined()): Section 5.
- The difficulty menu line (2026-11-05). The locked level dialog (2026-11-06: "it should say something like. This difficulty is Unlocked after completing 5 more easy runs.").
- level_damage(): the difficulty scaling plan's Section 1 (2026-11-09). run_top_step_time(): its Section 2.

## practice.nvgt
- Practice locks: the practice locks plan (2026-11-10, for 1.9, [[project_practice_locks_plan]]).
- The last choice has no goal (2026-11-10: "No goal. It should just say available"). That was barriers until combinations came after them (the combined obstacles plan, 2026-11-11); barriers then got "dodge past", the dev's earlier wording.
- Order of the chain, as each choice was added: winds between barriers and combinations, and trampolines last after combinations (2026-11-11); real and mixed walls after fake walls, and mixed obstacles last with trampolines opening it (2026-11-12); floor breakers after mixed doors, and vehicles after winds (2026-11-13).
- Weapons only where needed: the practice guidance plan's Section 1 (2026-11-12: "Weapons should not be available for obsticals that don't need them"). Vehicles kept weapons because you shoot them (the vehicles plan, 2026-11-13).
- Endless run opens with spikes (2026-11-10: "jumpping over 5 hazards"). Its lock line adds "in a practice run" (2026-11-10).
- The practice menu line: Section 2 (2026-11-10).
- Unlock announcements (2026-11-10: "It's just 2 unlocks"). After testing Section 1: "the mode unlock should appear first in the misc buffer".
- The returning player check (2026-11-10).
- The one-time unlock checks, each from its plan: combinations (2026-11-11), winds (2026-11-11), trampolines (2026-11-11), walls (the ladders plan, 2026-11-12), floor breakers (2026-11-13), vehicles (2026-11-13).

## practice_hints.nvgt
- Practice hints: the practice guidance plan's Section 2 (2026-11-12). No keyboard keys in lines (2026-11-12, [[feedback_no_key_names_in_hints]]).
- Hints restart after a hit or a missed key (2026-11-12: "it should reset the hints, and re-speak them"; "it should repeat if you miss an item, like a key"). After the closing line the run stays quiet (2026-11-12).
- Mixed obstacles gives one hint per kind (the practice mix plan, 2026-11-12). practice_mix_count was 14, then 16 with floor breakers and vehicles (2026-11-13).
- The practice death dialog: Section 3 (2026-11-12).
