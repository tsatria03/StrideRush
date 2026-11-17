---
name: project_readout_formats_plan
description: SETTLED (2026-11-17), not built: settings to choose how health and shield readouts are spoken (percentage, amount or both); 2.4's ninth entry; Q&A log
metadata:
  type: project
---

Started 2026-11-17 (dev: "I figured a ninth change we can do for 2.4. Is it possible to configure the health/shield formats in the game settings?"), on a2f831f. 2.4 holds 8 of 10. Not built; no sections yet.

## Findings (2026-11-17)
- H, speak_health() in lives.nvgt: "70 percent health remaining, 2 lives."; in a free run "60 percent, 300 of 500 health remaining, 3 lives."
- M, speak_shield_strength() in shield.nvgt: "Shield strength, 80 percent."; in a free run "Shield strength, 80 percent, 320 of 400 endurance remaining."; "You're not wearing a shield." without one.
- The pause menu's session statuses (session_status_lines() in stats_menu.nvgt) repeat both formats as "health, 70 percent, 2 lives" and "shield, 80 percent" (with the amounts in a free run).
- A health potion: "Healed to 85 percent health." (potion.nvgt).
- So both formats exist already; the kind of run picks one. The settings' Game tab (also shown mid-run through F2) has sliders, then checkboxes.

## Q&A log
- Q1 (Claude, 2026-11-17): what can players choose? Proposed: two settings on the Game tab, health format and shield format, each a list of percentage (as today, the default), amount ("300 of 500 health", "320 of 400 endurance") and percentage and amount ("60 percent, 300 of 500"). Recommended: as proposed, two separate settings, since you might want amounts for health but a percentage for the shield.
- A1 (dev, 2026-11-17): "Agreed. Also it would be 2 list controls, before the checkboxes." Two lists on the Game tab, health format then shield format, after the volume sliders and before the checkboxes, each with percentage (default), amount, and percentage and amount.
- Q2 (Claude, 2026-11-17): free runs. Today they always give both, since you can set your health and shield there. Proposed: free runs follow the two settings like every other run, so there's one place to choose and the readouts never disagree between kinds of run; anyone wanting the amounts in a free run picks amount, or percentage and amount. The potion's "Healed to ..." and the pause menu's session statuses follow the health and shield settings too. Recommended: as proposed.
- A2 (dev, 2026-11-17): "I want free runs to follow the global formats." Free runs follow the two settings; their always-both readout goes.
- Q3 (Claude, 2026-11-17): the wording. Lists "Health format," and "Shield format," (captions ending in a comma, like the sliders), items "percentage", "amount", "percentage and amount". H: "70 percent health remaining, 2 lives." / "350 of 500 health remaining, 2 lives." / "70 percent, 350 of 500 health remaining, 2 lives." M: "Shield strength, 80 percent." / "Shield strength, 320 of 400 endurance remaining." / "Shield strength, 80 percent, 320 of 400 endurance remaining." Session statuses: "health, 70 percent, 2 lives" / "health, 350 of 500, 2 lives" / "health, 70 percent, 350 of 500, 2 lives", and "shield, 80 percent" / "shield, 320 of 400 endurance" / "shield, 80 percent, 320 of 400 endurance". The potion: "Healed to 85 percent health." / "Healed to 425 of 500 health." / "Healed to 85 percent, 425 of 500 health." Recommended: as worded.
- The dev asked how CookieCraze words its number format setting (2026-11-17). Its settings_menu.nvgt has a list "Number format" with items "Raw. Example, 5,230.", "Suffix short. Example, 5.23 K.", "Suffix long. Example, 5.23 million.", "Scientific. Example, 5.23 e plus 3." Q3 revised (Claude): the list items in that style: health "Percentage. Example, 70 percent.", "Amount. Example, 350 of 500.", "Percentage and amount. Example, 70 percent, 350 of 500."; shield "Percentage. Example, 80 percent.", "Amount. Example, 320 of 400 endurance.", "Percentage and amount. Example, 80 percent, 320 of 400 endurance."; the readouts as in Q3. Recommended: yes.
- A3 (dev, 2026-11-17, after a recap): "yes." The revised list items and the Q3 readouts.
- Q4 (Claude, 2026-11-17): the sections. No new sounds. Proposed: 1. Formats: health_format and shield_format in dec.nvgt (0 percentage, the default, 1 amount, 2 percentage and amount), saved and read with the settings and put back to percentage by reset settings; the two lists on the Game tab after the sliders and before the checkboxes, kept across the window's rebuilds and applied on save settings, from the main menu or F2; one text helper each for health and shield, used by H, M, the session statuses and the potion, replacing the free-run-only wording. Tests. 2. Docks: one changelog entry on top of 2.4 (9 of 10, wording proposed then); the readme's H and M lines, the Game tab line and anything describing free run's readouts; the version history and CLAUDE.md. Recommended: as proposed.
- A4 (dev, 2026-11-17): "they are good". The two sections as proposed.

## THE PLAN IS SETTLED (2026-11-17)
1. Formats: dec.nvgt's health_format and shield_format (0 percentage default, 1 amount, 2 percentage and amount), saved and read with the settings, put back to 0 by reset settings; "Health format," and "Shield format," lists on the Game tab after the sliders, before the checkboxes, items in CookieCraze's example style (A3), kept across rebuilds, applied on save settings from the main menu or F2; a text helper each for health and shield, used by H, M, the session statuses and the potion, free runs included (A2). Tests.
2. Docks: one changelog entry on top of 2.4 (9 of 10, wording proposed then); the readme's H and M lines, the Game tab line, and free run's readout mentions; the version history and CLAUDE.md.

## Build log
- Not started.
