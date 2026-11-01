---
name: reference_toymania_scoring_difficulty
description: Where ToyMania's session/lifetime stats, achievements, save data and difficulty ladder live, and the bugs to not copy; for when the dev asks to port them
metadata:
  type: reference
---

Not for porting until the dev asks ([[reference_toymania_readonly]]). Paths are under ToyMania/src/includes/main/, and the line numbers are from 2026-11-01, so find things by symbol.

Stats:
- Paired globals in globals/dec.nvgt: session counters such as collected_toys and moved_steps, with total_ lifetime twins. Every event bumps both, then calls update_achievements().
- Playtime is int64 session_playtime and total_playtime, in milliseconds.
- "Session" means the current or last run. It is saved too, and reset_game_state() clears it at the start of a new game. Lifetime counters are cleared only from the Clear menus.

Save data:
- deps/savedata.nvgt is class savedata: a dictionary serialized and string_encrypt'ed with a hard-coded key, with typed read_* helpers.
- The files are %APPDATA%/tsatria03/ToyMania/saves/game.tmg (progress) and settings.tmg (preferences).
- functions/savefuncts.nvgt: readdata() guards every key with exists(); writedata() saves.
- It autosaves every 5 seconds and on key events.

Achievements:
- globals/achievments.nvgt has class AchievementTracker (thresholds, currentTier, isSessionBased) and generate_achievement_thresholds(start, 50, 1.5).
- Seven lifetime and seven session trackers.
- Sounds misc/PLAYER achsession and achlife.

Display:
- menus/menu.nvgt statsmenu() leads to view_session_stats() and view_lifetime_stats().
- achesmenu() shows the achievements.
- Exports go to plain text under %APPDATA%/.../stats/.

Difficulty:
- int gamemod is 1-5: Easy, Medium, Hard, Insane, Chaos. It's picked every run and not saved.
- choose_difficulty() in menu.nvgt picks the tier.
- difficulty_unlocked(diff, max_completed): a tier unlocks after completing the tier below.
- Per-mode completion counts and the max difficulty completed are saved by record_game_completion(), which every real end state calls except an Escape quit. migrate_unlocks() runs once for older saves.
- Effects are pure scaling: HP base + bonus*(gamemod-1), enemy HP*gamemod, timings/gamemod. For a runner that maps naturally to starting speed, speed-up rate and hazard density.

Don't copy:
- reset logic copy-pasted in about 6 places (use one reset_game_state and one end_game)
- the difficulty-name ternary chain repeated in about 6 places (use one function)
- playtime added only at end states (known undercount)
- the menu-volume save written to the wrong file
- "clear both" not resetting session_playtime
- an inconsistent export path
- the pause-menu quit "No" still quitting (it reads mres instead of confirmres)
