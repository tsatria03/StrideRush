# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This file is a **lean dispatcher**: the orientation you need first, plus a trigger for every load-bearing rule. The detail lives in `aidocks/` (indexed in `aidocks/MEMORY.md`): `aidocks/general/` for topics and conventions, `aidocks/plans/` for feature plans. They aren't auto-loaded, so treat every double-bracketed trigger as "there is a rule here; read it before you touch this." "Memory" always means `aidocks/`.

## What this is

**Stride Rush** is an audio-only lane runner written in **NVGT** (an AngelScript-based engine): no visuals, only screen-reader speech and HRTF spatial audio through sound_pool. The player rides a one-way belt forward across three lanes, a step timer moves them with a footstep each tick and speeds up over time, and they jump, crouch, switch lanes, use their hands and weapons past obstacles, collecting items into an inventory. Endless runs come in five difficulties; practice runs drill one obstacle. It is **offline, single player**, a simple core meant to be easy to expand. See **[[project_runner_overview]]** and **[[project_game_design]]**.

Current state: **1.9 is the latest release** (tagged V1.90 at 5ed3664). **2.0 is open** (build/version.txt 2.0, 2 of 20; after x.9 always comes (x+1).0). Open plans, started with questions not asked yet: [[project_combined_obstacles_plan]] and [[project_environments_plan]]. Every version's contents, tags and plans are in **[[project_version_history]]**: read it before changing a feature, to see what was decided and why. New gameplay is designed through discussed plans first ([[feedback_plans_record_qna]]).

Gameplay code lives in `src/includes/main/globals/`: `tuning.nvgt` (every tunable number), `run.nvgt` (the run loop, step order, readouts), `surface.nvgt` and `player.nvgt` (footsteps, jump, crouch), `spawner.nvgt` (picks and places everything), one file per obstacle or item type, `lane.nvgt`, `lives.nvgt` and `endrun.nvgt` (health, lives, how a run ends), `difficulty.nvgt`, `practice.nvgt`, `decpool.nvgt` (the pool registry). A new obstacle type touches its own file, `spawner.nvgt` (`obstacle_types`, `place_obstacle()`), `clear_run_objects()` in `endrun.nvgt`, `all_pools`, and `step_check()`, with warning cues in `sounds/misc/trap/<type>/` ([[project_entity_pattern]]).

The **debug options** ([[feedback_call_them_debug_options]]; never "testing menus") follow debug run in the mode menu: spawn, speed, footsteps and lives, in `menus/menu.nvgt`. They're source only (`SCRIPT_COMPILED` hides them); keep them out of the docks.

## Layout: code and assets are split

- **`src/`**: code only. Entry `src/sdr.nvgt`; `src/includes/includes.nvgt` glob-includes `main/deps`, `main/functions`, `main/globals`, `main/menus`.
- **`sdr/`**: runtime assets plus the launcher: `sdr.py`, `data/`, `docks/`, `sounds/`, `lib/`.
- **`build/`**: release pipeline (`tools.py`, `tools.bat`, `tools.ini`, `site_updater.ps1`, `version.txt`). **`releases/`**: compiled output (gitignored).
- **`aidocks/`**: this project's memory folder (committed).
- **`user/`**: gitignored. Only read inside it where the dev points.

**The cwd trick:** `sdr/sdr.py` runs `../src/sdr.nvgt` with **cwd = `sdr/`**, so cwd-relative paths in code (`sounds/...`, `data/...`, `docks/...`) resolve under `sdr/`, while `#include` paths resolve relative to `src/`.

**Engine is pinned to the legacy fork at `C:\nvgt`** (BASS audio). `C:\nvgt2` is only for testing other people's games; never target it or treat upstream NVGT as authoritative ([[project_engine_pinned_nvgt]]).

## Running

No test suite or linter. **The dev runs and builds the game, never Claude**: don't launch `sdr/sdr.py`, run `build/tools.py` or `nvgt -c` ([[feedback_dont_run_or_build_the_game]]). A failed launch writes compile errors to `sdr/errors.txt`. `build/version.txt` is the single version source; `src/includes/version.nvgt` mirrors it and is never hand-edited ([[feedback_update_build_version_txt]], [[project_build_pipeline]]).

## Memory dispatch: where the detail lives

| Topic | Open before you... |
|---|---|
| **[[project_version_history]]** | change an existing feature, or close a version (add its section there, not here) |
| **[[project_tech_decisions]]** | pick a library, menu class, sound lookup, or port anything from another game |
| NVGT / AngelScript gotchas | write any .nvgt: **[[project_angelscript_braceless_if]]**, **[[project_angelscript_reserved_words]]**, **[[project_angelscript_while_true_return]]**, **[[project_angelscript_block_comment_star_slash]]**, **[[project_nvgt_key_pressed_oneshot]]** (key_repeating() too), **[[project_nvgt_sound_preload_cache]]**, **[[project_nvgt_hrtf_dummy_sound]]** |
| **[[project_sound_layout]]** | add a sound path or folder |
| **[[project_audio_model]]** | add a sound_pool or keep a sound handle |
| **[[project_entity_pattern]]** | add an object type |
| **[[project_controls_plan]]** | add or change any key binding |
| **[[project_build_pipeline]]** | touch `build/`, the version, or a release |
| `aidocks/plans/` | start any feature: check for an existing plan and its Q&A log first |
| Reference games (read only) | borrow code: see the reference memories in `aidocks/MEMORY.md` |

## Load-bearing rules (triggers)

- **Reference repos are read only.** Read them, then write the adapted code here. Never name the dev's other games in code, data or build files ([[feedback_no_game_names_in_code]]).
- **CRLF line endings** on `*.nvgt/.py/.txt/.bat/.ps1/.md/.ini`. Create new files with CRLF, preserve endings on edit, never run a tree-wide normalizer ([[feedback_no_crlf_normalization]]).
- **No sound packs or themes.** `get_pack_sound(path)` looks in `sounds/` + path ([[project_sound_layout]]).
- **Nothing gets built until its sounds exist.** Rescan `sdr/sounds/` before a build section ([[feedback_sounds_before_features]]).
- **`dummy.load("dummy")` must run before `sound_global_hrtf` is set.** It isn't dead code ([[project_nvgt_hrtf_dummy_sound]]).
- **Offline only**, except the updater's download ([[project_tech_decisions]]); the GitHub repo must stay public.
- **Keys are never rebindable during a run.** Mid-run, F1 views bindings and F2 opens settings with only Game, Menu and Speech tabs ([[project_controls_plan]]).
- **Docks are live.** Player-facing changes get an `sdr/docks/changelog.txt` entry, newest on top; 20 entries for a major version, 10 for a minor; no version numbers inside entries, the readme or the todo list ([[feedback_changelog_rules]]). Finished todo items move to its finished section, newest first ([[feedback_docks_later]]). Dock lines stay at or under 1024 characters ([[feedback_dock_line_length_1024]]).

## Working style (triggers)

- **Confirm before implementing.** A design discussion or question is a request for a plan, not a go-ahead ([[feedback_confirm_before_implementing]]).
- **One question per turn**, with a recommendation ([[feedback_ask_one_question_at_a_time]]).
- **Gameplay is planned before it's built.** Log every Q&A in the plan file ([[feedback_plans_record_qna]]); say when a plan is settled and wait for the dev to commit it ([[feedback_tell_when_to_commit_plans]]).
- **Multi-section builds:** all section plans up front, one section per go-ahead, never paste code into chat ([[feedback_describe_dont_show_code]]).
- **Check the latest commit before every section**; never commit or push unless asked ([[feedback_check_git_log_for_commits]]).
- **End file-editing turns with a "Files changed:" list** plus a relaunch note ([[feedback_list_modified_files]]).
- **Test steps one at a time**: ask if the dev is ready first, then one step per message, then "Did it pass?" ([[feedback_test_steps_one_at_a_time]]).
- **Player-facing speech:** one sentence ([[feedback_one_sentence_game_messages]]); cancel paths say "canceled", nested menus step back silently ([[feedback_menus_say_canceled]]); yes/no menus are Yes then No ([[feedback_yes_no_menu_labels]]).
- **Code style:** multi-line comments are one `/* */` block ([[feedback_multiline_comment_style]]); don't flag or fix indentation ([[feedback_dont_flag_indentation]]).
- **Keep this file under 10,000 characters.** Move detail into memory, don't expand it here ([[feedback_claudemd_length]]).
