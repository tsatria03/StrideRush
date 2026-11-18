---
name: project_free_run_lanes_plan
description: SETTLED (2026-11-18), not built: choosing the lane for barriers, items, vehicles and lane trampolines added in a free run (your lane or a set lane) instead of a random one; second of the todo list's free run items for 2.5; Q&A log
metadata:
  type: project
---

Started 2026-11-18 (dev: "I want to plan the lain item next."), on 7ecc939, with the spacing plan settled and committed but not built ([[project_free_run_spacing_plan]]). Built on [[project_free_run_tools_plan]]. Not built; no sections yet.

## Findings (2026-11-18)
- The todo item: "Add a way to choose the lane for barriers, items, vehicles and lane trampolines in a free run, such as your own lane or a set lane, instead of a random one."
- Today in a free run: items come one at a time in a random lane (set_spawn_only() gives a free run item_lane_mode "random", spawner.nvgt's spawn_items()); barriers in a random lane, and barrier_pair_percent of the time a second in another lane (barrier.nvgt's spawn_barriers()); a vehicle starts in a random lane, then moves a lane toward yours every vehicle_beat_time (vehicle.nvgt); a trampoline is belt-wide trampoline_belt_percent (25) of the time, otherwise in a random lane (trampoline.nvgt).
- The debug options already have "your lane" forms for barriers and items (spawn_only "barriers", item_lane_mode "own": current_lane at the moment it spawns).
- The console's add flow (freebelt.nvgt's free_add()): kind, how many, a breakable kind's health, then continuous or not; each batch or rule is a free_entry (type, group, count, full, hp).

## Q&A log
- Q1 (Claude, 2026-11-18): where the lane is chosen. Proposed: in the add flow, as one more question for the kinds that sit in a lane (barriers, the six items, vehicles, trampolines), and for "all" of a group that holds them: "Choose the lane." with random lanes (today's, the default), your lane (wherever you are as each one appears), left lane, middle lane and right lane; kept on that batch or continuous rule, so barriers can come in your lane while items stay random. Recommended: per add, as proposed, rather than one console setting for everything.
- A1 (dev, 2026-11-18): "I want them to be per obstical, not global." Per add: the lane question in the add flow, kept on each batch or rule.
- Q2 (Claude, 2026-11-18): how each kind takes a chosen lane. Proposed: barriers in your lane or a set lane come one at a time, never with a second beside them (side-by-side pairs stay with random lanes); items likewise one at a time; a vehicle starts in the chosen lane and still moves a lane toward yours every beat, as vehicles do, so the choice is where it starts; a trampoline with a chosen lane is always a lane pad there, never belt-wide (random keeps today's quarter belt-wide); with "all" of a group, the lane applies to the lane kinds in the mix and the rest come as usual; your lane means the lane you're in as each one appears, not when you added it. Recommended: as proposed.
- A2 (dev, 2026-11-18): "yes. Also the spawning question should appear after the lain question. I mean this. \"Do you want these obstacles to spawn continuously?\". \"Do you want these items to spawn continuously?\"." As proposed, and the add flow's order is kind, how many, health (breakable kinds), lane, then the continuous question last.
- Q3 (Claude, 2026-11-18): the wording. The lane menu: "Choose the lane for these obstacles." (or items, specials), then random lanes, your lane, left lane, middle lane, right lane; escape says "canceled" like the add flow's other questions. The confirmations gain the lane when it isn't random: "Barriers will now keep coming in your lane." and "3 barriers added, in the left lane." (with health: "3 fake walls added, with 200 health each, in your lane."); random says nothing extra, as today. Recommended: as worded.
- A3 (dev, 2026-11-18): "yes".
- Q4 (Claude, 2026-11-18): the sections. No sounds needed. Proposed: 1. Lanes: free_entry gains a lane (random, your lane, left, middle, right), asked in free_add() after the health and before the continuous question, only for lane kinds or "all" of a group holding them; the chosen entry's lane rides to the spawner beside its health (as free_hp_next does), and spawn_items(), spawn_barriers(), the vehicle's start lane and the trampoline's lane take it (a set lane or your lane: one barrier or item, a lane pad never belt-wide); the confirmations name it; replays keep it with their batches. Tests. 2. Docks: one changelog entry on top of 2.5 (wording proposed next, before the plan is committed); the readme's free run add line; the todo item to finished; the version history and CLAUDE.md. Recommended: as proposed.
- A4 (dev, 2026-11-18): "yes".
- Q5 (Claude, 2026-11-18, per [[feedback_changelog_wording_in_plan]]): the entry, on top of 2.5 (7 of 10, after the spacing plan's 6th): "Added a lane choice when adding barriers, items, vehicles or trampolines in a free run, so they can come in random lanes, your own lane, or the left, middle or right lane." Recommended: as worded.
- A5 (dev, 2026-11-18): "yes. good".

## THE PLAN IS SETTLED (2026-11-18)
1. Lanes: free_entry gains a lane (random, your lane, left, middle, right); free_add() asks it after the health and before the continuous question, only for lane kinds (barriers, the six items, vehicles, trampolines) or "all" of a group holding them: "Choose the lane for these obstacles." (items, specials) with random lanes, your lane, left lane, middle lane, right lane, escape "canceled"; the entry's lane rides to the spawner beside its health, as free_hp_next does; spawn_items() and spawn_barriers() put one in the chosen lane (no side-by-side pair), a vehicle starts there and still moves toward yours each beat, a trampoline is a lane pad there, never belt-wide; your lane is the lane you're in as each appears; random keeps today's behaviour; confirmations name a chosen lane ("Barriers will now keep coming in your lane.", "3 barriers added, in the left lane.", "3 fake walls added, with 200 health each, in your lane."); replays keep each batch's lane. Tests.
2. Docks: the entry on top of 2.5: "Added a lane choice when adding barriers, items, vehicles or trampolines in a free run, so they can come in random lanes, your own lane, or the left, middle or right lane."; the readme's free run add line; the todo item to finished; the version history and CLAUDE.md.

## Build log
- Not started.
