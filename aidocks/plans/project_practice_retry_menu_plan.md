---
name: project_practice_retry_menu_plan
description: SETTLED (2026-11-19), not built: a game settings option to hide the menu after a practice death, setting you straight down past what caught you as before 2.0; first plan for 2.6; Q&A log
metadata:
  type: project
---

Started 2026-11-19 (dev: "I'd say the retry menu because recall that in earlier versions of the game, it took you passt the obstical if you died. Look in my git history."), on top of the released 2.5 (V2.50). The first 2.6 item; the todo list also holds translations, a shop and helicopters. Built on [[project_practice_guidance_plan]], which added the menu.

## Findings (2026-11-19)
- The todo item: "Add an option to hide the retry menu for a practice run in the game settings menu."
- Before 2.0: a practice death showed "You died." in a dialog, then on Enter set you down just past what caught you, with full health, the life and the practice shield ([[project_practice_deaths_plan]]).
- The practice guidance plan (2026-11-12, 2.0 entries 13 to 17) added the per-obstacle death line in that dialog, then the menu "What would you like to do now?" with retry practice and return to game menu (escape "canceled", back to the game menu). Changelog: "Added a menu after a practice death, so you can retry practice or return to the game menu."
- endrun.nvgt's practice_death(): the death sound, then, unless a free run is on no deaths, dlgmessage_return(practice_death_text()) and the menu ("retry free run" in a free run on practice deaths); retry waits for the keys' release and sets you down past it (me.x = past_x, spawner_catch_up(), health, lives, shield). A free run on no deaths already skips both the dialog and the menu.

## Q&A log
- Q1 (Claude, 2026-11-19): what hiding it does. Proposed: a checkbox in the settings' game tab; when the menu is hidden, a practice death still plays its sound and shows the death dialog with its line (what caught you and how to get past it), and Enter on the dialog sets you straight down past it, as before 2.0, with no menu; a free run on practice deaths follows the same setting; leaving early stays with quit run in the pause menu; shown by default, so nothing changes until you turn it off. Recommended: as proposed, keeping the dialog since its line is the practice's teaching.
- A1 (dev, 2026-11-19): "Yes it does." As proposed. The dev asked what the setting would be called, recalling that the results menu can be hidden too.
- Found: the game tab's two death checkboxes, after "Ask to quit the run when pressing escape", both on by default: "Show session results after dying" (show_death_results) and "Show copy and export options after dying" (show_death_copy_export).
- Q2 (Claude, 2026-11-19): the name and place. Proposed: "Show retry options after a practice death", a third checkbox right after those two, on by default, worded like them ("Show ... after ...") and naming practice deaths, which covers both a practice run and a free run on practice deaths. Recommended: as proposed.
- A2 (dev, 2026-11-19): "yes."
- Q3 (Claude, 2026-11-19): the sections. No sounds needed. Proposed: 1. The option: a saved setting beside show_death_results (on by default, saved and loaded with the other settings, and set back on with them where the settings reset), the game tab checkbox after "Show copy and export options after dying", and endrun.nvgt's practice_death() skipping the menu when it's off, so Enter on the death dialog sets you down past what caught you. Tests. 2. Docks: opens 2.6 ("New in 2.6." on top of the changelog, build/version.txt to 2.6), one entry, the readme's settings list and practice death paragraph, the todo item to finished, the version history and CLAUDE.md. Recommended: as proposed.
- A3 (dev, 2026-11-19): "Because this is very small. Please do the docks after section 1." The two sections stand, but the docks follow straight on once section 1's tests pass, with no separate go-ahead.
- Q4 (Claude, 2026-11-19, per [[feedback_changelog_wording_in_plan]]): the entry, opening 2.6 (1 of 10): "Added a setting to the game tab to hide the retry options after a practice death, so closing the death message sets you down just past what caught you." Recommended: as worded.
- A4 (dev, 2026-11-19): "yes".

## THE PLAN IS SETTLED (2026-11-19)
1. The option: a saved setting beside show_death_results, on by default (saved, loaded, and set back on where the settings reset); the game tab checkbox "Show retry options after a practice death" right after "Show copy and export options after dying"; with it off, endrun.nvgt's practice_death() still plays the death and shows the death dialog with its line, then skips the "What would you like to do now?" menu, so Enter on the dialog sets you straight down past what caught you (health, life and shield back, as retry does); it covers a practice run and a free run on practice deaths; leaving early stays with quit run. Tests.
2. Docks, straight after section 1's tests pass (dev's request): "New in 2.6." on top of the changelog with the entry "Added a setting to the game tab to hide the retry options after a practice death, so closing the death message sets you down just past what caught you."; build/version.txt to 2.6; the readme's settings list and practice death paragraph; the todo item to finished; the version history and CLAUDE.md.

## Build log
- Not started.
