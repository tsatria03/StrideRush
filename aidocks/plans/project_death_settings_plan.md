---
name: project_death_settings_plan
description: SETTLED, not built (2026-11-08, for 1.7; 2 sections) - settings to turn off the results menu after a death, and the copy and export items in the after death menu; Q&A log
metadata:
  type: project
---

Status: SETTLED, nothing built. Started 2026-11-08, with 1.6 closed (V1.60) and 1.7 not yet opened.

Background:
- The dev (2026-11-08): "I had some ides for 1.7, and they all have to do with dying in the game. You know how after you dye, it shows the results menu every single time? I wish there were settings to disable that, including the copy/export options found in the replay menu."
- Now ([[project_session_results_plan]]): after a death ends an endless run, after_death_menu() in menus/results_menu.nvgt shows the results menu ("You have died. Here are your current results for this session.", the 50 lines, back), then the question menu (copy session results to clipboard, export session results to file, replay run, return to game menu). A debug death already skips the results and drops copy and export, with the intro "What would you like to do now? You can replay the current run, or return to the game menu."
- Settings live in menus/settings_menu.nvgt's tabs (general, game, keyboard, menu, sound, speech), saved in preffs/settings.srf by readpreffs() and writepreffs() ([[project_settings_plan]]). The Game tab holds "Enable behind pitch decrease", "Enable checking for game updates at startup" and "Ask to quit the run when pressing escape"; F2 mid-run shows the Game, Menu and Speech tabs. ToyMania's gamcopy checkbox, "Enable post-game copy and export prompts.", was left out of 1.6.

Q&A log:
- Q (2026-11-08): two Game tab checkboxes after "Ask to quit the run when pressing escape", both on by default: "Show session results after dying" (off: a death skips the results menu and goes straight to the question menu) and "Show copy and export options after dying" (off: the question menu is only replay run and return to game menu, with the intro "What would you like to do now? You can replay the current run, or return to the game menu.", as a debug death has now); independent of each other, changeable mid-run through F2. A (dev, 2026-11-08): "Yes please. That's exactly right." SETTLED as proposed. The pause menu's view, copy and export session results are untouched.
- SETTLED (2026-11-08). Build sections (one per go-ahead): 1. the two settings (saved in settings.srf, on by default, in the Game tab and the reset to defaults) and after_death_menu() reading them; 2. docks (a 1.7 changelog entry opening the block with build/version.txt at 1.7, the readme's settings and death flow, the todo item to finished, this plan COMPLETE, MEMORY.md and CLAUDE.md).
