---
name: project_version_history
description: Every released version of Stride Rush, newest first - its tag and commit, its 10 (or 20) changelog entries in engine terms, the plans behind them and the files they touched; moved out of CLAUDE.md's "Current state" (2026-11-10) to keep that file short
metadata:
  type: project
---

Moved out of CLAUDE.md on 2026-11-10 (dev: "claude.md seems pritty long ... I highly recommend splitting them into aido memmories to keep it shorter"; keep CLAUDE.md under 10,000 characters). When a version closes, add its section here at the top, and keep CLAUDE.md's "Current state" to the latest release, the next version and the open plans.

Version numbering: minor versions hold 10 changelog entries, majors (x.0) 20; after x.9 comes (x+1).0, never x.10 ([[feedback_changelog_rules]]). Tags are V<major>.<minor>0 (V1.90, V2.00).

## 2.0 (open, 9 of 20)
- Slides ([[project_slides_plan]]): globals/slide.nvgt, shared sounds misc/game/slideground, slidestart, slidemove, slidestop; belt-wide, 2 to 4 s (slide_min_time, slide_max_time), current_step_time() halved while sliding; sliding blocks jumping, crouching, hands, inventory and weapons (lanes allowed), silences footsteps, heartbeat and countdowns; obstacles pass through harmlessly; your lane's items caught by slide_update() with the pick_up_*() functions; real doors and keys held, a clear landing, no air powerups along a slide; 1 in slide_chance 6 with survival_roll() (1 in 24 easy to 120 chaos), joining at 300 ms, never in practice; debug choice slides; slides_ridden and slide_items_caught with 12 achievements (104 in all).
- Combinations ([[project_combined_obstacles_plan]]): globals/combo.nvgt; 16 pairs (combo_firsts/combo_seconds in tuning.nvgt, each also reversed), never three, never real doors; a pair replaces difficulty_combo_percents 5/10/15/20/25 of obstacle spawns (debug at 25, practice only by choice), once both types have joined and exist in the current environment; the second part after combo_gap_jump 1200 / crouch 600 / quick 500 / hands 1000 ms; a pair's barrier single in your lane; every obstacle has a pair field, cleared or hit reported through pair_part_cleared()/pair_part_hit() beside its own statistic; combinations_cleared and six achievements (92 in all); the clap fix (a hand that switched off a field doesn't count toward a clap while held, forcefield.nvgt); debug choices combinations, combinations reversed, combinations mixed (with 2 debug shields); practice: combinations last, barriers' goal dodge past, practice_combos_check() for saves with barriers open, practice_env_ok(). Two entries.
- Hazards practice has no steel shield (shields can't stop hazards): practice_shield_count() in shield.nvgt (0 for hazards, else practice_shields), used by give_debug_shield() and practice_death()'s top-up; the readme's practice paragraph.
- Environments ([[project_environments_plan]]): globals/env.nvgt; current_env picked at random by pick_start_env() (practice only where its obstacle is; the debug option first in the debug flow, each environment then random); every obstacle stores env at spawn and plays from trap_folder(env, type), play_countdown() takes it; surfaces, footsteps, landings, falls, tracks_folder() and ambiences_folder() follow current_env; env_check() switches every env_switch_min_time to env_switch_max_time (60 to 120 s of runtimer) to a random different eligible one: "You've entered the <name> environment." (misc buffer, interrupting at the start), a new surface, begin_ambience_fade(), the song finishing before track_env draws from the new tracks; the old ambience timer only without switching. custom is the second environment: the removed surfaces (81 folders), 100 ambiences and 7 tracks restored from history, plus a copy of default's traps and its own ledge.
- Learn sounds' top level is environments, items and weapons, built ahead of the rest of [[project_environments_plan]] at the dev's request: learn_environment_category() in learn_sounds_menu.nvgt makes a category per folder in environments/, named by it ("default"), each with countdowns (learn_countdown(env_root, type), types with cues only) and traps (<type>/general lists). Its own entry.
- The sound reorganization, the first step of [[project_environments_plan]]: sounds/objects moved to sounds/environments/default (audio, platforms, traps), every path repointed; then the dev moved misc/trap/<type> into traps/<type>/countdown and each type's themes into traps/<type>/general, and the code was repointed again; its entry, reworded at the dev's request: "Made it so the game's music, ambiences, ground surfaces, obstacle sounds and obstacle countdowns now live together in a default environment, ...".
- Fixed: a practice death left the worn shield on (shield_worn, shield_hp_left) as well as topping up the inventory; practice_death() in endrun.nvgt now calls reset_shield() first.
- The second keys back (dev, 2026-11-10: playing with letters only "got very challanging"): keyboard.ini has the arrows for jump, crouch and lanes, Shift+Tab and Tab for the inventory, RETURN for item use (ENTER isn't a registered key name), Page Up and Page Down for the music and Home and End for the ambience, as before 1.8, alongside the single defaults; hands stay A and D only. Docks only, no code change; the dev's tests passed (2026-11-10). A rebuild of a deleted keyboard.ini was discussed and not taken up.

## 1.9: tagged V1.90 at 5ed3664 (10 of 10)
- The item balance ([[project_item_balance_plan]], after a player ran an hour taking every hit): difficulty_item_percents 25/20/15/10/5 (tuning.nvgt) through item_percent() in difficulty.nvgt and survival_roll() in spawner.nvgt for life capsules, steel shields and health potions, pairs' second items too, debug at 100; barrier_weight 2 in the obstacle pick.
- The startup update check (auto_check_updates in dec.nvgt) off by default, also after a settings reset.
- The learn sounds counts (a player's report): learn_count_text() in learn_sounds_menu.nvgt, "This category has 9 individual sounds, 85 in total." from entries() and count(), "This category has a total of 6 sounds." when equal.
- The footsteps volume ([[project_footstep_volume_plan]]): footstep_volume in surface.nvgt for play_step()'s steps only, the Game tab's "Game footsteps volume," between ambience and heartbeat, saved in settings.srf, no keys.
- The heartbeat's F7/F8 volume keys removed (slider only; change_heartbeat_volume() gone).
- Ctrl+Tab and Ctrl+Shift+Tab switch a form's tab panel from anywhere, wrapping: switch_tab_panel() in deps/form.nvgt, checked in monitor() after a subform's turn, with Tab read once into tab_hit; "Category Tab panel" and the tab when coming from another control, only the tab when already on it.
- Practice locks ([[project_practice_locks_plan]]): globals/practice.nvgt; each practice obstacle opens after practice_unlock_count 5 clean passes of the one before, counted through stat_add()'s practice_pass() in a practice run of that obstacle; endless run opens with spikes; lines and locked dialogs in choose_game_mode() and choose_practice(), last_practice_choice remembered; pracunlock and the unlock lines in the misc buffer, the mode's first; saved in saves/game.srf and kept by clearing; a one-time returning player check opens everything for saves with endless play.
- Practice and debug runs' quit and restart questions drop the lost progress sentence (leave_run_question() in pause_menu.nvgt); endless runs keep it.
- Every run starts with the fist drawn (reset_weapons() in weapons.nvgt).
- Also in 1.9, no entry: the trap sound reshuffle (chasm3, electricity fall1/fall2, barriers/powerline, force_fields/electric3).

## 1.8: tagged V1.80 at aa6d164 (10 of 10; re-released with the ledge sounds restored)
- The key binder ([[project_rebinding_plan]]): kc_capture_combo() reads keys itself so Tab and Shift plus Tab bind; both sides held captures SHIFT/CTRL/ALT, one side LSHIFT and so on; the replace and trigger questions in bindings_menu.nvgt; get_keyboard_action_string() writes the compact hand-written form; empty actions saved as "fire=" and still loaded.
- Add binding uses the selected action, like edit and remove.
- keyboard.ini trimmed by the dev to one default key per action (W, S, Q, E, A, D, F3 to F8; the arrows, Tab, Enter, Home, End, Page Up and Page Down unbound).
- A weapon draw cuts off the last one (draw_sound in weapons.nvgt).
- Practice offers fake doors, real doors (key then door, spawn_only real_doors) and mixed doors (practice_doors).
- Practice deaths ([[project_practice_deaths_plan]]): a practice run's last life or a hazard fall goes to practice_death() in endrun.nvgt, "You died.", set down past what caught you with full health, practice_lives 1 and practice_shields 1 back; pause_pools(keep_player).
- Difficulty scaling ([[project_difficulty_scaling_plan]]): difficulty_damage_percents 60/70/80/90/100 through level_percent() in difficulty.nvgt for take_damage() and wall_spawn_hp(); difficulty_top_step_times 200/150/100/75/50 through run_top_step_time() for speedup_check() and the door and key marks; Rush Hour may pass the cap; practice and debug at full.
- The ambience cleanup.
- Reset settings restarts the game (restart_game() after "Settings reset.").
- The menu music, music and ambience volumes start at 80 percent, -20 dB, also after a settings reset (music_start_volume, ambience_start_volume, menu_music_start_volume in tuning.nvgt).

## 1.7: tagged V1.70 at 6fc021c (10 of 10)
- The sound device menu marks each device active or inactive.
- The startup update check moved to the General tab (main menu only).
- The practice speed menu in steps a second (C reads milliseconds in a debug run only).
- A "Getting started." readme section after the welcome, after CookieCraze's.
- A heartbeat ([[project_heartbeat_plan]]): globals/heartbeat.nvgt, heartpool in all_pools, 5 bpm at 500 ms to 155 at 150 ms in a straight line and held there, powerups included, gap 2000 - 10 x bpm, silent in a door carry, every kind of run, B readout, heartbeat_volume with a Game tab slider (its F7/F8 keys removed in 1.9); the breath sounds were dropped.
- The pause menu opens on resume run and remembers your place, saying the focused item.
- Escape and P pause every sound but the ambience (pause_pools() skips ambpool).
- The Game tab's "Show session results after dying" and "Show copy and export options after dying" ([[project_death_settings_plan]]): show_death_results and show_death_copy_export; after_death_menu() says "You have died. " first when it opens without the results.
- Volume sliders ([[project_volume_sliders_plan]]): Game tab ambience and music, Sound tab menu music and master via sound_master_volume, 0 to 100 percent = -100 to 0 dB, applied on save, min_volume -100.
- Alt+F4's exit_program key removed.

## 1.6: tagged V1.60 at a561a2d (10 of 10)
- Session results ([[project_session_results_plan]]): menus/results_menu.nvgt, endless runs only; the pause menu's view, copy and export; the after death results and menu (after_death_menu(): copy, export, replay run or return to game menu) replacing the replay question; "death outcome" second in the session lines; stats/player_results.txt.
- Game achievements in the game menu ([[project_achievements_plan]]): 86 in data/config/achievements.ini, globals/achievements.nvgt and menus/achievements_menu.nvgt, earned once and announced mid-run, achievement statistics first in the statistics menu.
- The game menu's clear game progresses and copy or export of all progress (player_progresses.txt).
- Game statistics in the game menu ([[project_statistics_plan]]): globals/stats.nvgt counts endless runs only, menus/stats_menu.nvgt shows session and lifetime lists, clear, copy and export, saved in saves/game.srf.
- C says steps a second to one decimal place, not ms; Z says steps, not tiles.
- I and O move back and forward through the inventory (a user's suggestion, replacing I and Shift+I).
- Music and ambience ([[project_music_ambience_plan]]): a fresh shuffle of objects/audio/tracks every run, and objects/audio/ambiences crossfading every 1 to 2 min; F3/F4 and F5/F6 as second volume keys.

## 1.5: tagged V1.50 at adcd14d (10 of 10)
- The game menu refactor ([[project_game_menu_refactor_plan]], 2026-11-06): the mode menu (choose_game_mode(): debug run from source, endless run, practice run), five difficulty levels with a schedule and run-count locks in saves/game.srf.
- The weapon lineup ([[project_weapon_lineup_plan]]): a sword replaces the laser.
- Speech buffers per system ([[project_buffers_plan]]), created in sdr.nvgt alphabetically after all (achievements, doors, items, misc, powerups, status, weapons), each speak_buffer() naming its buffer.
- The auto updater ([[project_updater_plan]]): globals/updater.nvgt on the dev's deps/downloader.nvgt and functions/downloaderfuncts.nvgt, nvgt_curl; a startup check setting auto_check_updates; extracts the portable copy to sdr\sdr; guards on the download and the extract; the GitHub repo must stay PUBLIC or downloads 404. Change game version too, both in the main menu.
- Walls 50 to 500 hp, fake doors their own 100 to 1000.
- Test speakers in the main menu (test_speakers() in menu.nvgt).
- The learn sounds menu in the game menu ([[project_learn_sounds_plan]]): menus/learn_sounds_menu.nvgt, built from the sound folders, with the loop_previews (Sound tab) and variant_descriptions (Menu tab) settings.
- Scoring was dropped from the todo list (2026-11-05).

## 1.4: tagged V1.40 at cb11eb8 (10 of 10)
- Lanes ([[project_lanes_plan]], undone in 1.3 so it stayed the last side-scroller): lane.nvgt holds three lanes on Q and E (Left and Right too until 2026-11-09), turning from the lane moved into, a bump at an edge, the L readout, footsteps centred; place_lane_sound() places one-lane sounds by lane relative to yours (a fixed angle under HRTF).
- Barriers: barrier.nvgt, the one-lane trap, 80 damage, random lanes, pairs half the time, countdown only in its lane.
- The forward belt on sound_pool's y axis (x across lanes, listener at x 0 and y me.x; retune_belt_falloff() keeps the fade per time), with the behind_pitch and hrtf settings, on by default. The six inventory items sit in random lanes and pair half the time (spawn_items()); powerups and every other obstacle span the belt. Same-sound pairs either side of you blend into a phantom centre (not a bug; the readme explains it; the dev declined staggering pairs).
- shield_hp 400; damages raised (force fields 30, projectiles 40, walls 50, mines 60, doors 70).
- Life capsules give 1 or 2 lives up to max_lives 20; life potions renamed life capsules (globals/capsule.nvgt).
- Doors count down (misc/trap/doors, four layers).
- Health potions healing 5 to 10 percent (globals/potion.nvgt, [[project_health_potion_plan]]).
- Birds ([[project_birds_plan]]): a belt-wide trap cleared only by a clap (both hand keys), 10 damage, globals/animal.nvgt (the "animals" type; dogs came later).
- A lone empty hand whooshes to its side.

## 1.3: tagged V1.30 at 09e3573 (the last side-scroller version)
- Settings ([[project_settings_plan]]): one encrypted APPDATA_DIR/preffs/settings.srf read by readpreffs() and written by writepreffs(); fadepool.nvgt fades every pool through leave_run() on quit and restart; "settings menu" in the main menu and F2 mid-run (Game, Menu, Speech only); F1 the read-only bindings screen; dlgmessage_return() from CookieCraze.
- Powerups ([[project_powerups_plan]]): ground ones run onto, flight ones jumped into, 14 timed effects in 7 pairs through current_step_time(), current_jump_tick(), current_duck_time(), current_fire_gap() and powerup_damage() in powerup.nvgt; step_time stays the normal speed for door marks.
- The menus ([[project_menus_plan]]): the main menu is documentation menu (changelog, credits, readme, todo list in a read-only window), game menu, settings menu, change game version and check for updates (1.5), test speakers (1.5), restart game and exit game; the pause menu (P) is resume run, restart run, quit run, restart and quit confirmed.
- The life capsule rename was re-released into 1.3's tag with no 1.3 entry, at the dev's word.

## 1.2: tagged V1.20 at d6df5a9 (10 of 10)
- Keys ([[project_keys_plan]]) come once before each real door; U unlocks a real door from up to 2 s away and a hand then opens it; a hand or key on a fake door plays jam.
- Steel shields ([[project_shields_plan]]) worn with U take damage from everything but hazards before your health (200 then, 400 since 2026-11-04); H reads health and lives, M the shield.
- Life potions gave 1 life; player teleporters throw you a random 2 to 5 s forward or back, never onto an obstacle ([[project_potion_teleporter_plan]]); I and U are off while a door carries you.
- Player health ([[project_player_health_plan]]): 200 health and 1 life to start; every blow but a hazard does its obstacle's damage through take_damage() in lives.nvgt; a life goes at 0 health and the next starts full; hazards end the run outright.

## 1.1: tagged V1.10 at abcb495 (10 of 10)
- Real doors and fake doors ([[project_doors_plan]]): a real door marks each 50 ms speed section and carries you through when opened by hand; fake doors at odd pitches appear any time and are broken with weapons, like walls.
- Walls ([[project_walls_plan]]), broken with weapons, hp climbing with speed; bullets ([[project_bullets_plan]]) fly ahead from the guns.
- Weapons break ammo packs; a force field's countdown stops once it's switched off.
- Over a hundred new ground surfaces, changing every 10 to 20 seconds at any speed; crouch again after half a second; every trap plays its full five-step countdown at any speed.

## 1.0: tagged V1.00 at ca6f256 (20 of 20)
- The first build ([[project_first_build_plan]]; game in 69dedf8, docks in 0f0ccff): an endless run on a step timer (500 ms down to 50 ms), footsteps on random platform surfaces, jump and a silent crouch, hazards with ledges, a warning countdown per obstacle, deaths that sound different by obstacle.
- Lives (1 to start; health came in 1.2), a pause menu, speech buffers, the volume and readout keys.
- Spikes, mines, force fields ([[project_force_fields_plan]]: switched off with either hand during their countdown, or they hurt and throw you 5 steps forward), projectiles ([[project_projectiles_plan]]: twice the belt's speed, ducked under).
- Ten weapons ([[project_weapons_plan]]) on Space with per-gun ammo and a 2 s reach; ammo packs picked up by hand into an inventory and opened to refill the guns.
