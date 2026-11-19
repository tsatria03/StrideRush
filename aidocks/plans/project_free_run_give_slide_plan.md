---
name: project_free_run_give_slide_plan
description: SETTLED (2026-11-18), not built: giving yourself a slide from a free run's console (modify player specials), starting it straight away; 2.5's tenth and last entry; Q&A log
metadata:
  type: project
---

Started 2026-11-18 (dev: "Please add giving slides to the todo list." then "It will appear in the modify special option"), on 8e92d2e, with 2.5 at 9 of 10, so this is its last entry. Built on [[project_free_run_powerups_plan]] (modify player specials, free_specials_menu()) and the slides code (slide.nvgt).

## Findings (2026-11-18)
- The todo item: "Add a way to give yourself a slide from a free run's console, starting it straight away, so you can try sliding without waiting for one to turn up."
- slide.nvgt: a slide_obj sits on the belt at x with its ride_ms (slide_min_time 2000 to slide_max_time 4000, on runtimer), a theme from the environment's transitions/slides/general, and a clear landing (land_from to land_to: a countdown and the minimum floor past where the ride ends). Reaching it calls start_slide(): start plays, the move loop runs, sliding is true; your step is halved (twice as fast), no footsteps or heartbeat, jumping, crouching, hands, inventory and weapons blocked, lane switches allowed; obstacles pass harmlessly, items in your lane are caught; slide_update() ends it on time with stop. A slide reached while riding one stops the old move loop and starts the new ride (back to back already works in a free run).
- slides_available(): the environment has slide themes. The spawner keeps new things out of the landing (slide_landing_push()) and holds real doors and keys while a slide holds (slide_holds()).
- Modify player specials (running only) holds give powerup today.

## Q&A log
- Q1 (Claude, 2026-11-18): the form. Proposed: modify player specials gains "give slide" after give powerup; choosing it closes the console and puts you on a slide where you stand, straight away, as if you'd just reached one: its start sound, the move loop, twice your speed, for the usual random 2 to 4 seconds, then its stop, with the usual clear landing after; a theme at random from the current environment; giving one while already sliding starts a fresh ride, as back-to-back slides do. Give slide is always listed; in an environment with no slides, choosing it says "This environment has no slides." and stays in the specials menu. No statistic, as nothing in a free run counts. Recommended: as proposed.
- The dev (2026-11-18) asked: "It will work like powerups where it only gives you 1 at a time right? I mean no typing numbers." Claude: yes, one slide per choice, no number box and no further menu; choosing give slide starts it at once. Q1 stands.
- A1 (dev, 2026-11-18): "yes". As proposed.
- Q2 (Claude, 2026-11-18): the details. Found: clear belt already ends a ride quietly (clear_run_objects() calls reset_slides()), and so does clearing slides in clear specials. Proposed: no misc line, since the slide's start sound is the confirmation (as a powerup's name is); view current setup gains "slide, 2 seconds left" while you're on one, beside the powerup lines, and says nothing about slides otherwise; clear belt and clear specials keep ending a ride as they do. Recommended: as proposed.
- A2 (dev, 2026-11-18): "yes." As proposed.
- Q3 (Claude, 2026-11-18): the sections. No new sounds (the environments' slide themes). Proposed: 1. Give slide: slide.nvgt gains a way to start a slide where you are (a slide_obj at your tile, already reached, its ride_ms, theme and clear landing worked out as spawn_slide() does, then start_slide()); freerun.nvgt's free_specials_menu() lists give slide after give powerup, closing the console and starting it, or saying "This environment has no slides." and staying in the menu when slides_available() is false; free_powerup_lines() (or beside it) adds "slide, 2 seconds left" while sliding. Tests. 2. Docks: one changelog entry on top of 2.5 (10 of 10, wording proposed next, before the plan is committed), the readme's modify player specials paragraph, the todo item to finished (bringing back the empty line), the version history and CLAUDE.md. Recommended: as proposed.
- A3 (dev, 2026-11-18): "all good. Review the change log, then I'll commit".
- Q4 (Claude, 2026-11-18, per [[feedback_changelog_wording_in_plan]]): the entry, on top of 2.5 (10 of 10, closing it): "Added a way to give yourself a slide from a free run's console, putting you on one straight away, and the current setup now says how long your slide has left." Recommended: as worded.
- A4 (dev, 2026-11-18): "yes".

## THE PLAN IS SETTLED (2026-11-18)
1. Give slide: slide.nvgt gains a way to start a slide at your tile (a slide_obj already reached, its ride_ms slide_min_time to slide_max_time, a random theme from the current environment and its clear landing worked out as spawn_slide() does, then start_slide(), which already handles riding into a new slide while on one); freerun.nvgt's free_specials_menu() lists "give slide" after give powerup: one slide per choice, no number, closing the console and starting it at once, or, when slides_available() is false, saying "This environment has no slides." and staying in the menu; no misc line (the start sound is the confirmation) and no statistic; view current setup shows "slide, 2 seconds left" while riding, nothing about slides otherwise; clear belt and clear specials keep ending a ride. Tests.
2. Docks: the entry on top of 2.5 (10 of 10): "Added a way to give yourself a slide from a free run's console, putting you on one straight away, and the current setup now says how long your slide has left."; the readme's modify player specials paragraph; the todo item to finished, bringing back the "Nothing is waiting here right now." line; the version history and CLAUDE.md.

## Build log
- Not started.
