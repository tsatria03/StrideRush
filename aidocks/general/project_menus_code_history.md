---
name: project_menus_code_history
description: decision history moved out of the menu files' comments (menu, pause_menu, bindings_menu, results_menu; settings, stats, learn sounds and achievements with Section 6B) by the comment cleanup's Section 6 (2026-11-15); read before changing a menu
metadata:
  type: project
---

Moved here from the comments of src/includes/main/menus/ on 2026-11-15 ([[project_comment_cleanup_plan]], Sections 6A and 6B), so the code keeps only what it does and why. Dates are when the dev decided; quotes are the dev's own words. The plans named hold the full Q&A. The menu rules themselves live in the feedback memories ([[feedback_menus_say_canceled]], [[feedback_yes_no_menu_labels]], [[feedback_alphabetical_menus]], [[feedback_named_menu_choices]], [[project_menu_music_rule]]).

## menu.nvgt
- The main menu (2026-11-03, for 1.3, [[project_menus_plan]]). The settings menu was added 2026-11-04. Change game version, check for updates and test speakers were added 2026-11-05 ([[project_updater_plan]]).
- The menu music fades for the settings menu (from the main menu only), check for updates, change game version and test speakers (2026-11-07: "fade the music when I test my speakers", [[project_menu_music_rule]]).
- Change game version takes digits and periods only (2026-11-05). Its disallowed-character line uses input_box()'s own wording (2026-11-05).
- Learn sounds came into the game menu 2026-11-05, first named "learn sounds menu". Achievements sit before statistics, and statistics after learn sounds (2026-11-06).
- The game menu intro: "learn about important sounds" (2026-11-05), "check your stats" (2026-11-06) and "view achievements" (2026-11-06).
- The mode menu (the practice plan, 2026-11-06) replaced the 2026-11-03 "Do you want to play in debug mode?" question ([[project_game_menu_refactor_plan]]). Practice run moved last, after free run (2026-11-15).
- The debug options' order: the environment first (2026-11-10), spawn before speed since 2026-11-06 ("Please make the speed menu come after the obstical/item menu"), speed, footsteps (2026-11-04), then whether lives can run out. The lives menu was removed with player health.
- Every choice is set again for the real game, since escaping a debug option left its "escaped" value behind. A speed of -1 ran every step at once; the dev found this bug 2026-11-04.
- Replay and restart work in releases too (2026-11-03). A free run's replay is the same run (2026-11-13).
- A single-type debug run starts with debug_lives (2026-11-03).
- The mode menu's endless line gained "and more obstacles join as you go" with the difficulty schedule (Section 5, 2026-11-05). A locked mode reads only its requirement, with no "Available." (the practice locks plan's Section 2, 2026-11-10). Timed run sits after endless (the timed run plan, 2026-11-13).
- The difficulty menu: the game menu refactor plan's Section 4 (2026-11-05), in difficulty order ("this menu will not need it", meaning alphabetical order), with locks from Section 6. The unlocked count in the intro (2026-11-12, [[project_menu_counts_plan]]).
- The practice menus: Section 2 (2026-11-05). The last practice choice stays focused (2026-11-10). The unlocked count (2026-11-12). Three door choices (2026-11-09: "fake doors, real doors, mixed doors"). The lock lines come from the practice locks plan's Section 2 (2026-11-10). The speed menu's intro and its steps-a-second labels (2026-11-08). Rising (the rising practice plan, 2026-11-12).
- The debug speed menu dropped the 50 ms steps for door testing (2026-11-03).
- The debug spawn menu is alphabetical (2026-11-05: "Please make the debug options in alphabetical order"). Animals were listed by kind (2026-11-04). The three barrier choices (2026-11-04 and 5). Real doors spread (2026-11-03). The three lane choices for items (2026-11-05). Mixed walls (the ladders plan, 2026-11-12). The combinations choices, "reversed" (2026-11-11). Slides and trampolines (2026-11-11). Nothing, for the music and ambience (2026-11-06).
- The debug footsteps option (2026-11-04: "extremely useful for the new transformed belt tests").
- The debug environment option (the environments plan, 2026-11-10), with "random" last (2026-11-10: "rename this to random, and put it at the bottum").

## pause_menu.nvgt
- The pause menu (2026-11-03, for 1.3, [[project_menus_plan]]): resume run, restart run and quit run, about the run, while restart game and exit game are about the program. The Yes/No wording is the dev's (2026-11-03).
- Restart run sits right after resume run (2026-11-07). View session statuses, for every kind of run (2026-11-13, [[project_pause_status_plan]]). Session results in the pause menu: the session results plan (2026-11-07, [[project_session_results_plan]]).
- The menu remembers your place, and the focused item is always spoken after the intro (2026-11-08: "I want it to say it if it focuses on it").
- The quit and restart questions warn about the session only when there's one to lose (2026-11-10).
- Escape asks the quit question straight away (2026-11-03). At first only the timers paused while it was asked (2026-11-03: "the timers should pause, but not the sounds"); since 2026-11-08 every sound but the ambience pauses too. The Game tab's ask setting (ask_quit_on_escape) lets Escape leave at once (2026-11-04).
- Leaving a run fades its sounds the way fademode says (2026-11-04, [[project_settings_plan]]).

## bindings_menu.nvgt
- The key bindings screens (2026-11-04, for 1.3, [[project_settings_plan]]).
- Escape, not the close button, says "canceled" (2026-11-09).
- Add binding works on the action selected in the list (2026-11-09: no separate menu of every action, which only repeated the list).
- The replace question (the rebinding plan, 2026-11-09: "It should ask you if you want to replace that key.", [[project_rebinding_plan]]). The trigger question (2026-11-09: "it should ask them if they want to change the default key trigger"). The save confirmation wording (2026-11-09).

## results_menu.nvgt
- Session results (the session results plan, 2026-11-07, [[project_session_results_plan]]), in a menu, never a dialog (2026-11-07: "I'd much rather a menu, not a dlg with 50 lines"). Section 1 put view, copy and export in the pause menu. Section 2 put after_death_menu() in place of the old Yes/No replay question (2026-11-07: a menu that asks what you'd like to do), with replay run after export.
- The Game tab's two death settings (the death settings plan, 2026-11-08, [[project_death_settings_plan]]). Without the results menu first, the question menu says you died as it first opens (2026-11-08: "I want to know that I died.").
- A timed run's own results (the timed run plan's Section 2, 2026-11-13, [[project_timed_run_plan]]).
