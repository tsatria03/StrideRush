---
name: project_free_run_powerups_plan
description: SETTLED (2026-11-18), not built: giving yourself any powerup from a free run's console, starting it straight away; third of the todo list's free run items for 2.5; Q&A log
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
- Not started.
