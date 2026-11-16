---
name: project_free_run_touches_plan
description: SETTLED, NOT BUILT (2026-11-15), three sections: two small free run changes for 2.3's last two entries: modify heartbeat (heard or silent, like footsteps), and the modify options saying what they're currently set to; Q&A log
metadata:
  type: project
---

Started 2026-11-15 (dev: "Oh yes. 2 small changes for 2.3. 1. I wish you were able to turn off your heartbeat in the free run mode, like the footsteps. 2. The modify options should say something like, currently set to x. You can make one short plan for both things."). 2.3 holds 8 of 10, so these are its last two entries. Built on [[project_free_run_plan]] and [[project_free_run_tools_plan]].

## Today (2026-11-15)
- Footsteps: freerun.nvgt's free_footsteps_menu() ("Choose your footsteps.": heard footsteps, silent footsteps, back) sets footsteps_on (surface.nvgt), with "Your footsteps are now heard." or "... silent." in misc; view current setup shows "footsteps, heard" or "silent". play_game() (menu.nvgt) sets footsteps_on fresh for every run, and a free run's replay keeps it.
- Heartbeat: heartbeat.nvgt's heartbeat_check() already stays silent while a door carries you, on a slide, or standing in a free run (free_standing()); nothing turns it off otherwise.
- The modify menus' intros today: speed "Choose your running speed, in steps a second.", environment "Choose the environment you'd like to run in.", death mode "Choose what happens when you die.", footsteps "Choose your footsteps.", practice hints "Choose your practice hints.", ammo limits "Choose your <gun>'s ammo limits."; health, lives, shield strength and ammo reserves go through free_change_choice() ("Choose how you'd like to change your health." and so on, give, set, take); inventory already reads each item with its count.

## Proposed
1. Modify heartbeat: a console item between modify footsteps and modify player health (alphabetical), "Choose your heartbeat." with heard heartbeat, silent heartbeat, back; "Your heartbeat is now heard." or "... silent." in misc; heartbeat_check() stays silent while it's off; view current setup gains "heartbeat, heard" or "silent"; set fresh by play_game() like footsteps, kept through a free run's replay; the B readout still says your heart rate.
2. Currently set to: where it's said is the open question below.
3. Docks: two 2.3 changelog entries (10 of 10, so 2.3 is full), the readme's free run section.

## Q&A log
- Q1 (Claude, 2026-11-15): where should "currently set to" be said: at the end of each modify menu's intro (such as "Choose your footsteps. Currently set to heard footsteps."), or in the console's item names (such as "modify footsteps, heard footsteps")? Recommended: the intro, so the console list stays short to move through, and you hear the current value right where you'd change it; the focus can also start on the current choice.
- A1 (dev, 2026-11-15): "I agree with that." The current setting goes at the end of each modify menu's intro, and the choice menus open focused on the current choice.
- Q2 (Claude, 2026-11-15): the wording, one sentence added to each intro:
  - running speed: "Currently set to 5 steps a second." (or "normal", "rising")
  - environment: "Currently set to random." or the environment's name, as chosen
  - death mode: "Currently set to normal deaths." (no deaths, practice deaths)
  - footsteps: "Currently set to heard footsteps." (silent footsteps)
  - heartbeat: "Currently set to heard heartbeat." (silent heartbeat)
  - practice hints: "Currently set to silent hints." (spoken hints)
  - ammo limits: "Currently set to limited rounds." (unlimited rounds)
  - health: "You currently have 150 of 200 health." lives: "You currently have 3 lives." shield strength: "Your shield currently has 300 of 400 strength." ammo reserves: "You currently have 50 rounds in reserve."
  Recommended: as listed; the choice menus repeat the choice's own name, and the amounts say what you have now, since "set to" doesn't fit a number that changes as you play.
- The dev asked which items wouldn't have "Currently set to" (2026-11-15). Claude listed: the four amounts (health, lives, shield strength, ammo reserves) say "You currently have ..." instead; modify player inventory gets nothing new (its menus already read each item with its count); the add, clear, start running and view current setup items aren't settings. Asked whether the amounts should say "Currently set to" too; recommended keeping "You currently have".
- A2 (dev, 2026-11-15): "I like your idea better." The wording as listed in Q2, with "You currently have" for the amounts.
- Q3 (Claude, 2026-11-15): the two 2.3 changelog entries (9 and 10 of 10, so 2.3 is full): "Added a way to make your heartbeat heard or silent in a free run, the same way as your footsteps." and "Made it so a free run's modify options now say what each one is currently set to, or how much you currently have, as you open them." Recommended: as worded.
- A3 (dev, 2026-11-15): "Make the heartbeat change go first." The wording as proposed, with the heartbeat entry first: listed above the modify options entry in the changelog, and built first.

## THE PLAN IS SETTLED (2026-11-15)
Sections, one per go-ahead:
1. Modify heartbeat. A free_heartbeat_on flag (true for every new run, set by play_game() as footsteps_on is, kept through a free run's replay); "modify heartbeat" in the console between modify footsteps and modify player health, both standing and running; "Choose your heartbeat." with heard heartbeat, silent heartbeat, back; "Your heartbeat is now heard." or "... silent." in misc; heartbeat_check() silent while it's off; view current setup's "heartbeat, heard" or "silent". One test.
2. Currently set to. Each modify menu's intro gains the Q2 sentence (running speed, environment, death mode, footsteps, heartbeat, practice hints, ammo limits: "Currently set to ..."; health, lives, shield strength, ammo reserves: "You currently have ..."), and the choice menus open focused on the current choice. One test.
3. Docks: the two changelog entries on top of 2.3, the heartbeat entry above the modify options one (10 of 10, 2.3 full); the readme's free run section; the version history; CLAUDE.md.
