# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

This file is a **lean dispatcher**. It carries the orientation you need before you know what you're doing, plus a trigger for every load-bearing rule. The detail lives in the `aidocks/` memory files, indexed in `aidocks/MEMORY.md`. Memories are split into `aidocks/general/` (topics, conventions, references) and `aidocks/plans/` (feature plans, finished or in progress). They are not auto-loaded, so treat every double-bracketed memory trigger below as "there is a rule here; go read it before you touch this." "Memory" / "memories" always means `aidocks/`.

## What this is

**Stride Rush** (v1.0, early development) is an audio-only 2d side-scrolling runner written in **NVGT** (Non-Visual Game Toolkit, an AngelScript-based engine). There is no visual rendering: output is screen-reader speech plus HRTF spatial audio through NVGT's sound_pool. The player rides a one-way belt to the right; a step timer moves them and plays a oneshot footstep each tick, the tick speeds up over time, and they must jump or duck on cue past obstacles or die. It is **offline, single player**, built to be a simple core that users can easily expand in code. See **[[project_runner_overview]]** and **[[project_game_design]]**.

Current state: **the first build is complete and v1.0 is playable** ([[project_first_build_plan]]; game in 69dedf8, docks in 0f0ccff). It has an endless run on a step timer (500 ms down to 50 ms) with footsteps on random platform surfaces, jump and a silent crouch, and hazards with ledges. Every obstacle has its own warning countdown. Spikes and mines cost lives, and deaths sound different by obstacle. Force fields ([[project_force_fields_plan]]) are switched off with either hand during their countdown, or they cost a life and throw you 5 steps forward. There's a pause menu, readouts, volume keys and the speech buffer. Lanes, weapons, doors, duck-under obstacles, scoring, settings (F1/F2) and the updater are still to come. New gameplay is designed through discussed plans first ([[feedback_plans_record_qna]]).

Gameplay code lives in `src/includes/main/globals/`:
- `tuning.nvgt`: every tunable number.
- `run.nvgt`: the run loop, step order and readouts.
- `surface.nvgt` and `player.nvgt`: surfaces, footsteps, jump and crouch.
- `spawner.nvgt`: picks and places obstacles.
- `hazard.nvgt`, `spike.nvgt`, `mine.nvgt`: one file per obstacle type.
- `lives.nvgt` and `endrun.nvgt`: lives and how a run ends.
- `decpool.nvgt`: the pool registry.

A new obstacle type touches its own file, `spawner.nvgt` (`obstacle_types` and `place_obstacle()`), `clear_run_objects()` in `endrun.nvgt`, `all_pools`, and check and countdown calls in `step_check()` (its warning cues live in `sounds/misc/trap/<type>/warn1-5`) ([[project_entity_pattern]]). The lives, speed, spawn and "end the run when out of lives?" menus in `menus/menu.nvgt` (shown in that order) are testing only (`SCRIPT_COMPILED` hides them in releases); keep them out of the docks.

## Layout: code and assets are split

- **`src/`**: code only. Entry `src/sr.nvgt`; `src/includes/includes.nvgt` glob-includes `main/deps`, `main/functions`, `main/globals`, `main/menus` (`main/parsers` is left out until it holds a file; there are no map files).
- **`sr/`**: runtime assets plus the launcher. `sr/sr.py`, `sr/data/`, `sr/docks/`, `sr/sounds/`, `sr/lib/`.
- **`build/`**: release pipeline (`tools.py`, `tools.bat`, `tools.ini`, `site_updater.ps1`, `version.txt`). **`releases/`**: compiled output (gitignored).
- **`aidocks/`**: this project's memory folder (committed).
- **`user/`**: gitignored. Only read inside it where the dev points (so far `user/CaveDefender-main`, for the buffer system).

**The cwd trick:** `sr/sr.py` runs `../src/sr.nvgt` with **cwd = `sr/`**, so every cwd-relative path in code (`sounds/...`, `data/...`, `docks/...`, `lib/...`) resolves under `sr/`, while `#include` paths resolve relative to the script under `src/`.

**Engine is pinned to the legacy fork at `C:\nvgt`** (BASS audio; source at `tsatria03/misc/Legacy-NVGT`). `C:\nvgt2` (stock miniaudio) is only for testing other people's games; never target it or treat upstream NVGT as authoritative. See **[[project_engine_pinned_nvgt]]**.

## Running

No test suite or linter. **The dev runs and builds the game, never Claude**: don't launch `sr/sr.py`, don't run `build/tools.py`, don't run `nvgt -c` ([[feedback_dont_run_or_build_the_game]]). A failed launch writes compile errors to `sr/errors.txt` (gitignored). `build/version.txt` is the single version source of truth; the launcher and `tools.py` mirror it into `src/includes/version.nvgt`, which is committed but never hand-edited ([[feedback_update_build_version_txt]], [[project_build_pipeline]]).

## Memory dispatch: where the detail lives

| Topic | Open before you... |
|---|---|
| **[[project_tech_decisions]]** | pick a library, menu class, sound lookup, or anything ported from another game (form_menu, no networking, no keyhook, no map files) |
| NVGT / AngelScript gotchas | write any .nvgt (a compile error means the game won't launch): **[[project_angelscript_braceless_if]]**, **[[project_angelscript_reserved_words]]**, **[[project_angelscript_while_true_return]]**, **[[project_angelscript_block_comment_star_slash]]**, **[[project_nvgt_key_pressed_oneshot]]**, **[[project_nvgt_sound_preload_cache]]**, **[[project_nvgt_hrtf_dummy_sound]]** |
| **[[project_sound_layout]]** | add a sound path or folder (flat `sounds/` root, no packs, no menu/dialog themes, per-type folders, all lowercase, underscores not spaces) |
| **[[project_audio_model]]** | add a sound_pool or keep a sound handle (looping/persistent rule) |
| **[[project_entity_pattern]]** | add an object type (one file per type, sentinel-null removal, one clear registry) |
| **[[project_controls_plan]]** | add or change any key binding |
| **[[project_build_pipeline]]** | touch `build/`, the version, or a release |
| `aidocks/plans/` | start any feature: check for an existing plan and its Q&A log first |
| Reference games (read only) | borrow code: **[[reference_simplefighter_readonly]]**, **[[reference_toymania_readonly]]**, **[[reference_cavedefender_buffer]]**, plus the architecture/scoring/movement reference memories indexed in `aidocks/MEMORY.md` |

## Load-bearing rules (triggers)

- **Reference repos are read only.** Never edit SimpleFighter, ToyMania, or CaveDefender; read them, then write the adapted code here.
- **CRLF line endings are enforced** on `*.nvgt/.py/.txt/.bat/.ps1/.md/.ini`. Create new files with CRLF and preserve endings on edit; never run a tree-wide normalizer ([[feedback_no_crlf_normalization]]).
- **No sound packs or themes.** `get_pack_sound(path)` looks in `sounds/` + path. Menu sounds are flat in `ui/menu/`, dialog sounds in `ui/dialog/`, buffer cues in `ui/buffer/`, and copy/export cues in `ui/other/`; there's no menu or dialog theme selector ([[project_sound_layout]]).
- **Nothing gets built until its sounds exist.** Rescan `sr/sounds/` before a build section ([[feedback_sounds_before_features]]).
- **`dummy.load("dummy")` must run before `sound_global_hrtf` is set.** It looks like dead code; it isn't ([[project_nvgt_hrtf_dummy_sound]]).
- **Offline only.** No networking systems; the future updater's HTTP download is the one exception ([[project_tech_decisions]]).
- **Keys are never rebindable during a run.** Mid-run, F1 views bindings and F2 opens settings with only Game, Menu, and Speech tabs ([[project_controls_plan]]).
- **Docks are live.** Player-facing changes get an `sr/docks/changelog.txt` entry. Newest goes on top, inside a block too; a block holds at most 20 entries with no intro line, and a new block pairs with a `build/version.txt` bump ([[feedback_changelog_rules]]). Finished `todo list.txt` items move to its finished section, newest first. The todo list holds only player-facing entries ([[feedback_docks_later]]). Dock lines stay at or under 1024 characters ([[feedback_dock_line_length_1024]]).

## Working style (triggers)

- **Confirm before implementing.** A design discussion or any question is a request for a plan, not a go-ahead to edit ([[feedback_confirm_before_implementing]]).
- **One question per turn**, with a recommendation ([[feedback_ask_one_question_at_a_time]]).
- **Gameplay is planned before it's built.** Log every Q&A in the plan file ([[feedback_plans_record_qna]]), and say when a plan is settled so the dev can commit it ([[feedback_tell_when_to_commit_plans]]).
- **Multi-section builds:** give all section plans up front, build one section per go-ahead, never paste code into chat ([[feedback_describe_dont_show_code]]).
- **Check the latest commit before every section**, and never commit or push unless asked ([[feedback_check_git_log_for_commits]]).
- **End file-editing turns with a "Files changed:" list** plus a relaunch note ([[feedback_list_modified_files]]).
- **Test steps one at a time**: never inside a build summary; ask whether the dev is ready for the test steps first, then one step per message with what to hear, then ask "Did it pass?" ([[feedback_test_steps_one_at_a_time]]).
- **Player-facing speech:** one sentence ([[feedback_one_sentence_game_messages]]); every cancel path says "canceled", except nested menus stepping back to their parent, which are silent ([[feedback_menus_say_canceled]]); yes/no menus are exactly Yes then No ([[feedback_yes_no_menu_labels]]).
- **Code style:** multi-line comments are one `/* */` block ([[feedback_multiline_comment_style]]); don't flag or fix indentation ([[feedback_dont_flag_indentation]]).
- **Keep this file under 40,000 characters.** Move detail into memory, don't expand it here ([[feedback_claudemd_length]]).
