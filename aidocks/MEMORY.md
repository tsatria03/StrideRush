# Stride Rush memory index

The [[name]] links across these memories resolve to aidocks/general/<name>.md or aidocks/plans/<name>.md. Add a one-line pointer here for every new memory. "Memory" always means this folder.

## Project
- [Runner overview](general/project_runner_overview.md) — audio runner in legacy NVGT, launchable skeleton (main menu, no gameplay), git repo tsatria03/StrideRush on main, assets in sr/, CLAUDE.md written 2026-11-01 as a dispatcher
- [Game design](general/project_game_design.md) — basic 2d side-scroller, no lane switching (later expansion), jump or duck on cue or die, weapons/hands later, speed-up step timer with oneshot footsteps, ToyMania sound layout
- [Engine pinned to legacy nvgt](general/project_engine_pinned_nvgt.md) — target C:\nvgt (BASS), source in misc/Legacy-NVGT; C:\nvgt2 only for testing others' games
- [Tech decisions](general/project_tech_decisions.md) — offline single player, no networking (updater HTTP excepted); form_menu not custom_menu; no map files for now; SimpleFighter sound glob functions; SimpleFighter updater later; no JAWS keyhook; deps copied from SimpleFighter
- [Build pipeline](general/project_build_pipeline.md) — build/ tools adapted from SimpleFighter (StrideRush, password StrideSprinter, v1.0, sounds bundled); V<version>0 tag format; site page not created yet
- [Entity pattern](general/project_entity_pattern.md) — one file per object: pool, handle array, class, spawn/check/remove/destroy_all, sentinel-null removal, one clear registry
- [Audio model](general/project_audio_model.md) — pool per category, listener every frame, HRTF pref; kept handles must be looping or persistent
- [Sound layout](general/project_sound_layout.md) — NO top-level sound packs (sounds/ is the root); objects/ grouped by SimpleFighter builder categories (audio, construction, interaction, kombat, transitions, traps); current clip inventory; NO menu or dialog themes (flat ui/menu, ui/dialog, ui/buffer, ui/other; ui/other's "coppied" spelling and the missing menu music noted); one theme folder per object type (e.g. traps/hazards/pit); weapons add a category level (weapons/melee/<name>, weapons/artillery/<name>); keys sit under interaction/items/other; wildcard random-variant lookup; all folders and code paths lowercase (misc/player)
- [Memory folder layout](general/feedback_memory_folder_layout.md) — memories go in aidocks/: general/ for topics, plans/ for completed or in-progress plans; CRLF files

## Reference repos (read only)
- [SimpleFighter reference](general/reference_simplefighter_readonly.md) — games/SimpleFighter is object/entity reference material; strictly read only, never modify
- [ToyMania reference](general/reference_toymania_readonly.md) — games/ToyMania is the sound-layout, scoring and difficulty reference; read only; scoring/difficulty only when the dev asks
- [ToyMania architecture](general/reference_toymania_architecture.md) — launcher, glob includes, build pipeline, game loop, menus, keybinds; closest template for the skeleton
- [ToyMania scoring and difficulty](general/reference_toymania_scoring_difficulty.md) — session/lifetime stats, savedata, achievements, 5-tier difficulty ladder, bugs not to copy
- [Friend's runner template](general/reference_friend_runner_template.md) — a friend's BGT runner in user/: auto-step with a shrinking interval, 5-step hazard countdown cues, jump arc, 10 level tracks; its bugs; don't name it in committed files
- [CaveDefender buffer](general/reference_cavedefender_buffer.md) — the speech-buffer system to port (user/CaveDefender-main client deps/buffer.nvgt, read only), its keys, and the CaveDefender-only parts to adapt
- [SimpleFighter architecture](general/reference_simplefighter_architecture.md) — launcher, map format and dispatcher, menus, dialogs, settings, key_config
- [SimpleFighter builder objects](general/reference_simplefighter_builder_objects.md) — the 81 builder object docs as an obstacle/pickup reference: jump/duck/destroy/hand/collect/zone roles, clips (turbulence template not used)
- [SimpleFighter movement and jump](general/reference_simplefighter_movement_jump.md) — 2d step, footstep, jump state machine, gravity, hazard death and pause paths

## NVGT / AngelScript gotchas
- [Braceless if](general/project_angelscript_braceless_if.md) — a braceless branch holds one statement; a second orphans the else and breaks the compile
- [Reserved words](general/project_angelscript_reserved_words.md) — never name a variable out, in, inout, shared, final, from
- [while(true) return](general/project_angelscript_while_true_return.md) — a non-void function returning only inside while(true) still needs a trailing return
- [Block comment star-slash](general/project_angelscript_block_comment_star_slash.md) — an asterisk followed by a slash inside /* */ closes the comment early
- [key_pressed one-shot](general/project_nvgt_key_pressed_oneshot.md) — read a key once per frame and branch inside
- [Sound preload cache](general/project_nvgt_sound_preload_cache.md) — reloading changed audio under the same filename replays the old clip
- [HRTF dummy sound](general/project_nvgt_hrtf_dummy_sound.md) — dummy.load("dummy") must run before sound_global_hrtf is set; looks like dead code, never remove it
- [Not built-ins](general/project_nvgt_not_builtins.md) — min, max (extrafuncts) and vd (dec.nvgt) are game-defined, not engine built-ins; verify ported names, don't assume
- [Sound device indexing](general/project_sound_device_indexing.md) — device list is 0 No sound, 1 Default, 2+ named; no synthetic Default
- [Transient flags per-frame reset](general/project_transient_flags_per_frame_reset.md) — a timed lockout must be re-held each frame after any per-frame flag reset

## Feedback: how the dev wants me to work
- [Confirm before implementing](general/feedback_confirm_before_implementing.md) — a design discussion is a request for a plan; wait for go-ahead; one step at a time
- [Plans record Q&A](general/feedback_plans_record_qna.md) — several gameplay plans get discussed before any game code; log every Q&A in the plan file
- [Tell when to commit plans](general/feedback_tell_when_to_commit_plans.md) — flag when a plan is settled with all Q&A recorded so the dev can commit it
- [Ask one question at a time](general/feedback_ask_one_question_at_a_time.md) — one question per turn, with a recommendation
- [Describe, don't show code](general/feedback_describe_dont_show_code.md) — give all section plans up front, build per go-ahead, never paste code in chat
- [List modified files](general/feedback_list_modified_files.md) — end editing turns with "Files changed:" plus a relaunch note
- [Don't run or build the game](general/feedback_dont_run_or_build_the_game.md) — never launch or compile; the dev verifies
- [Verify code while fixing](general/feedback_verify_code_while_fixing.md) — locate by symbol, confirm the finding, flag adjacent bugs
- [Check git log](general/feedback_check_git_log_for_commits.md) — always check the latest commit before each section; the dev commits between turns; never commit unless asked
- [Stage commits before big changes](general/feedback_stage_commits_before_big_changes.md) — flag a commit break point before a risky stage
- [CLAUDE.md length](general/feedback_claudemd_length.md) — lean dispatcher under 40,000 chars when one is written
- [Changelog rules](general/feedback_changelog_rules.md) — player-facing prose, newest on top, bump build/version.txt per block
- [Update build/version.txt](general/feedback_update_build_version_txt.md) — version.txt is the source of truth; version.nvgt is generated
- [Sounds before features](general/feedback_sounds_before_features.md) — nothing gets built until its sounds exist in sr/sounds; design it and defer
- [Docks later](general/feedback_docks_later.md) — don't update sr/docks/ yet; readme at first playable, changelog at first release; todo list is player-facing entries only
- [Dock line length 1024](general/feedback_dock_line_length_1024.md) — lines in sr/docks/ stay at or under 1024 chars
- [One-sentence game messages](general/feedback_one_sentence_game_messages.md) — in-game speech is one sentence, no trailing advice
- [Menus say canceled](general/feedback_menus_say_canceled.md) — every escape, Back or No path speaks "canceled"
- [Yes/No menu labels](general/feedback_yes_no_menu_labels.md) — items exactly Yes then No; context in the prompt
- [Multiline comment style](general/feedback_multiline_comment_style.md) — multi-line comments are one /* */ block
- [Don't flag indentation](general/feedback_dont_flag_indentation.md) — AngelScript ignores whitespace; don't reformat
- [No CRLF normalization](general/feedback_no_crlf_normalization.md) — new files CRLF, preserve endings on edit, never a tree-wide normalizer
- [Don't name others' games](general/feedback_dont_name_others_games.md) — in committed files, name only the dev's own games
- [Presets need a driving need](general/feedback_presets_need_driving_need.md) — no presets or type abstractions without a real pain point

## Plans
- [End-of-run plan](plans/project_end_of_run_plan.md) — SETTLED FOR BASIC BUILD: hazards play their own fall; spikes and mines play hit sounds, then player death, then the tile's fall on the last life; then straight to the main menu (results dialog deferred); Q&A log
- [Obstacles plan](plans/project_obstacles_plan.md) — SETTLED FOR FIRST BUILD (hazards end the game, spikes cost 1 life, mines 2; random spacing with a speed-aware minimum gap; force fields later with hands): which obstacles are jumped, ducked, or need a weapon/hand/lane change; agreed three-height model (low jump, high duck, full = hands); feet vs hands; first build is jump-over only from the hazard, spike and mine sounds (duck-under when its sounds exist); 1 starting life; tunable life cost per type; duck and jump timing limits
- [Run plan](plans/project_run_plan.md) — SETTLED, NOT BUILT: endless run; timer speed-up 500 ms minus 10 ms every 10 s to a 50 ms floor; footstep every step; random platform stretches of 50-200 tiles; random music and ambience; warning cues deferred; Q&A log
- [Controls plan](plans/project_controls_plan.md) — SETTLED, NOT BUILT: dev-set keys (Up/W jump, Down/S duck, lanes reserved, Tab/Z and Enter/C hands, Space-only fire, X ammo, R reload, 1-0 weapons, readouts L lives/Q distance/E speed/T time/F score (H unused), Esc/P pause, Home/End ambience, PgUp/PgDn music), rebindable via key_config; status readouts on letters, not F keys; CaveDefender buffer keys kept as-is; in-game F1 opens the view-bindings screen and F2 opens settings (SimpleFighter-style tabs), both pausing; mid-run F2 shows only Game/Menu/Speech tabs (General, Keyboard, Sound hidden), no rebinding mid-run; no settings in the pause menu, no Alt shortcuts; unlisted keys pending; Q&A log
- [Skeleton plan](plans/project_skeleton_plan.md) — COMPLETE: launcher, sr.nvgt + includes, dep shims and main menu built, launch-tested and committed (d0e340f); 4 sections (sr.py launcher; sr.nvgt + glob includes; shims and trims for the SimpleFighter-copied deps; form_menu main menu); all decisions settled (flat sound root, no keyhook, Escape exits right away, version.nvgt tracked, sr/errors.txt ignored); ready to build
