---
name: project_free_run_powerups_plan
description: COMPLETE (2026-11-18, 2.5 at 8 of 10): giving yourself any powerup from a free run's console, starting it straight away; third of the todo list's free run items for 2.5; Q&A log
metadata:
  type: project
---

Started 2026-11-18 (dev: "Let's plan the powerups in the free run."), on 0fe1f38, with the spacing and lanes plans settled and committed but not built ([[project_free_run_spacing_plan]], [[project_free_run_lanes_plan]]). Built on [[project_powerups_plan]] and [[project_free_run_tools_plan]]. Not built; no sections yet.

## Findings (2026-11-18)
- The todo item: "Add a way to give yourself any powerup from a free run's console, starting it straight away, so you can try each one without waiting for it to turn up."
- powerup.nvgt: 14 powerups in 7 pairs, good first (powerup_names, powerup_name_kinds): Slow Motion and Rush Hour, Moon Jump and Short Hop, Long Crouch and Stiff Knees, Quick Swings and Clumsy Swings, Rapid Fire and Sticky Trigger, Sturdy Shield and Brittle Shield, Tough Hide and Soft Hide. One per kind; a new one of the same kind or its opposite replaces it and restarts powerup_time (15000 ms, on runtimer).
- Collecting one: collect_powerup() counts a stat, plays misc/game/powerget centered, then apply_powerup(pick_powerup_event()), which speaks the name in the powerups buffer and starts it. powerup_timers() says "<name> wore off." The shield pair is only picked with a shield worn, and a shield breaking ends its shield powerup quietly.
- The console (freerun.nvgt's free_console()): alphabetical items, the add, clear and player modify items only while running; every change closes the console and speaks in misc.

## Q&A log
- Q1 (Claude, 2026-11-18): the form. Proposed: a console item "give powerup", offered only while running (like add items and the player modify items), sitting alphabetically after clear specials and before modify ammo limits; its menu "Choose a powerup to start." lists the 14 by name, in their pairs, good first, then back (the shield pair only with a shield worn, as on the belt); choosing one closes the console, plays powerget, and starts it exactly as if collected: its name spoken in the powerups buffer, lasting the usual 15 seconds, replacing any running one of its kind, and wearing off as usual. No stat counts, since nothing was collected. Recommended: as proposed.
- A1 (dev, 2026-11-18): "that works." As proposed.
- Q2 (Claude, 2026-11-18): the details. Found: clear belt (free_clear_belt()) leaves running powerups going, since only reset_run() resets them, and view current setup says nothing about them. Proposed: no extra misc line, since the powerup's own name in the powerups buffer is the confirmation (as when collected); view current setup gains one line per running powerup, such as "powerup, Moon Jump, 12 seconds left", or "powerups, none"; clear belt also ends every running powerup, quietly, as it sets everything else back. Recommended: as proposed.
- A2 (dev, 2026-11-18): "Yes." As proposed.
- Q3 (Claude, 2026-11-18): the sections. No new sounds (powerget exists). Proposed: 1. Give powerup: freerun.nvgt's console item "give powerup" (running only, after clear specials) and its menu, "Choose a powerup to start." with the 14 in their pairs, good first (the shield pair only with a shield worn), then back; choosing closes the console, plays powerget centered and calls apply_powerup() with the chosen one (no stat); free_setup_lines() gains a line per running powerup with its seconds left, or "powerups, none"; free_clear_belt() calls reset_powerups(). Tests. 2. Docks: one changelog entry on top of 2.5 (wording proposed next, before the plan is committed); the readme's free run console; the todo item to finished; the version history and CLAUDE.md. Recommended: as proposed.
- A3 (dev, 2026-11-18): "yes".
- Q4 (Claude, 2026-11-18, per [[feedback_changelog_wording_in_plan]]): the entry, on top of 2.5 (8 of 10, after the spacing and lanes plans' 6th and 7th): "Added a way to give yourself any powerup from a free run's console, starting it straight away, and the current setup now says which powerups are running and how long they have left, while clearing the belt ends them." Recommended: as worded.
- A4 (dev, 2026-11-18): "yes".

## THE PLAN IS SETTLED (2026-11-18)
1. Give powerup: freerun.nvgt's console item "give powerup" (running only, after clear specials): "Choose a powerup to start." with the 14 in their pairs, good first (Sturdy Shield and Brittle Shield only with a shield worn), then back, escape or back stepping out; choosing closes the console, plays misc/game/powerget centered and calls apply_powerup() with the chosen one (its name in the powerups buffer, powerup_time, replacing its kind, wearing off as usual; no stat, no extra misc line); free_setup_lines() gains a line per running powerup, "powerup, Moon Jump, 12 seconds left", or "powerups, none"; free_clear_belt() ends every running powerup quietly (reset_powerups()). Tests.
2. Docks: the entry on top of 2.5 (8 of 10): "Added a way to give yourself any powerup from a free run's console, starting it straight away, and the current setup now says which powerups are running and how long they have left, while clearing the belt ends them."; the readme's free run console; the todo item to finished; the version history and CLAUDE.md.

## Build log
- Section 1 BUILT (2026-11-18, on fa6628d), awaiting tests: freerun.nvgt's free_give_powerup() (the console's "give powerup" after clear specials, running only; opens on its first item, Slow Motion; powerget if it exists, then apply_powerup()), free_powerup_lines() in free_setup_lines() just before what's coming ("powerup, Moon Jump, 12 seconds left", whole seconds rounded up, "1 second left"; "powerups, none"), and free_clear_belt() calling reset_powerups().
- CHANGED (dev, 2026-11-18, before testing: "Can you please put give powerups in a special category? Something like, modify player specials"): the console item is "modify player specials" (after modify player lives, running only), opening free_specials_menu(), "Choose what you'd like to do with your specials." with give powerup and back, as modify player inventory does; give powerup's back or escape steps back to it silently. The docks name it so. Also fixed before testing: two variables named after types (sound, any) broke the compile, renamed get_path and running_one.
- Section 1 tests: Test 1 of 4 (the menus: specials only while running, after modify player lives; 12 powerups without a shield; escape steps back) PASSED.
- Test 2 of 4 (Moon Jump given: powerget, its name, longer jumps, wore off after 15 seconds) PASSED.
- Test 3 of 4 (Rush Hour replacing Slow Motion; the shield pair listed with a shield worn; view current setup's powerup lines with seconds left) PASSED.
- Test 4 of 4 (clear belt ending Long Crouch quietly; "powerups, none") PASSED. Section 1 TESTED: all 4 passed.
- Section 2 DONE (2026-11-18): the entry on top of 2.5 (8 of 10), the readme (modify player specials in the running console list, a paragraph for it after the give, set and take paragraph, powerups in view current setup, clear belt ending powerups), the todo item to finished, the version history and CLAUDE.md. PLAN COMPLETE.
