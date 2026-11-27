---
name: project_weapon_practice_plan
description: COMPLETE (2026-11-27, 3.0's second entry, 2 sections): a practice choice, fake doors and walls, after mixed doors (aircrafts and vehicles dropped); Q&A log
metadata:
  type: project
---

# Weapon practice plan

Goal (the dev, 2026-11-27): "I want to add a practice obstical that lets you test out fake doors andwalls, but I'm not sure what to call it."

## Findings

- practice_choices (practice.nvgt) runs hazards, spikes, mines, projectiles, force fields, animals, insects, walls (fake walls), real walls, mixed walls, fake doors, real doors, mixed doors, floor breakers, barriers, winds, vehicles, aircrafts, trampolines, combinations, mixed obstacles. Each opens the next after 5 clean passes (practice_goal_verbs, practice_goal_singulars, practice_passes saved per choice).
- Names in the menu: single kinds plainly; "mixed" means fake and real of one family (mixed walls, mixed doors); mixed obstacles is everything.
- What weapons destroy: fake walls and fake doors (wall_spawn_hp()), vehicles and aircrafts (hit from your jumps), insects (shot or ducked).

## Open questions

1. The name.
2. What it holds.
3. Its place in the unlock chain and its goal.
4. Weapons, hints and the death line.
5. Changelog wording and docks.
6. Sections.

## Q&A log

- Q1, the name. Claude listed the menu's naming (plain kinds, "mixed" for fake and real of one family) and recommended "fake doors and walls" over "breakables" and "weapon targets". Dev: "I like that. fake doors and walls. I also suggest aircrafts and vehicles, as you can destroy those too." So the choice holds more than doors and walls, and the name is reopened once what it holds is settled (Q2).
- Q2, what it holds. Claude recommended fake doors, fake walls, vehicles and aircrafts, leaving insects out on the claim that ducking gets you past one. Dev: "You are wrong. If you duck for too long, they sting you." Checked insect.nvgt: crouched, an insect hovers for insect_dive_time and then stings, and standing up first stings at once, so the only way past is to kill it with weapons while crouched. Claude's corrected recommendation: insects belong in it too, making five.
 Dev: "I have a better idea. 2 practice options. aircrafts and vehicles, fake doors and walls." Settled: two new practice choices, "fake doors and walls" (fake doors and fake walls, Q1's name) and "aircrafts and vehicles"; insects keep their own choice. The plan now covers both.
- Q3, the chain. Claude recommended fake doors and walls after mixed doors (open after 5 mixed doors; floor breakers then open "after you break 5 fake doors and walls"), and aircrafts and vehicles after aircrafts, before trampolines (open after 5 aircrafts; trampolines then "after you get past 5 aircrafts and vehicles"); a one-time check like practice_aircrafts_check() opens both for anyone already past their places, so nothing locks again (passes are saved by name, practice_passes_<choice>). Dev: "exactly right." Settled.
- Q4, how a run plays. Claude recommended following the existing choices: each spawn one kind or the other, half and half (as mixed walls); both in practice_weapon_choices, so weapons stay drawn; 1 life and 1 steel shield; each obstacle's own hint and death line; a run only goes where both kinds have sounds (practice_env_ok(), as mixed walls needs walls and ladders). Dev: "exactly right". Settled.
- Q5, changelog and docks. Changelog, on top of 3.0's block: "Added fake doors and walls, and aircrafts and vehicles, to practice runs, each mixing two obstacles you destroy with your weapons, half and half." Docks: practice_runs.txt's choice list (after mixed doors, and after aircrafts), a sentence beside mixed walls and mixed doors on what each mixes, the "You only have weapons when practicing" list; floor_breakers.txt opens "after you break 5 fake doors and walls", trampolines.txt "after you get past 5 aircrafts and vehicles"; fake_doors.txt, fake_walls.txt, vehicles.txt and aircrafts.txt checked for what they open next. Dev: "Yes. That works." Settled.
- Q6, sections. Claude noted that vehicles and aircrafts count as passed when destroyed or dodged (practice_goal_stats2), so "aircrafts and vehicles" would need four goal keys and the changelog's "you destroy" would be untrue, and recommended two sections. Dev: "I just realized. Because you can dodge the aircraft and vehicles by not shooting, I much rather favor the fake doors/walls instead." Settled: aircrafts and vehicles is DROPPED; the plan is now one new choice, fake doors and walls, after mixed doors (Q3), as Q4 plays it. Revised changelog: "Added fake doors and walls to practice runs, mixing fake doors and fake walls half and half, which you break with your weapons." Docks: practice_runs.txt (list, mix sentence, weapons list) and floor_breakers.txt ("after you break 5 fake doors and walls"); trampolines.txt unchanged. Two sections, the choice with tests, then the docks. Goals: a fake wall or a fake door broken (walls_broken, fake_doors_broken), within today's two goal keys. Dev: "Yes. that works". Settled.

PLAN SETTLED (2026-11-27): ready to commit, then build Section 1 on the go-ahead.

## Sections

1. The choice (tests). practice.nvgt: "fake_doors_and_walls" after mixed_doors in practice_choices, practice_goal_stats walls_broken and practice_goal_stats2 fake_doors_broken, verb "break", singular "fake door or wall" with the plural "fake doors and walls", practice_passes, practice_weapon_choices, practice_env_ok() needing walls and doors, a one-time check opening it for anyone past mixed doors; its own shield as fake doors; the spawner and menu.nvgt pick fake walls and fake doors half and half (as mixed walls); the practice hint and death line of each kind; template.lng refreshed and english.lng synced.
   BUILT (2026-11-27, after f529198): practice.nvgt's arrays (22 entries each), practice_fake_mix_check() saved as practice_fake_mix_checked, available_obstacles()'s fake_mix pick, practice_goal_kind(), the debug spawn choice and debug shields list. A temporary unlock (choices up to fake doors and walls open, floor breakers on) was used for the tests and removed. Tests: 1 (the menu, floor breakers' lock line and dialog) PASSED; 2a (a weapon drawn, both kinds mixed, each kind's hint) PASSED; 2b (the death line and retry) PASSED; 3 (5 clean breaks open floor breakers) PASSED. Section 1 COMPLETE.
2. The docks (no tests): the changelog entry on top of 3.0's block, practice_runs.txt (list, mix sentence, weapons list), floor_breakers.txt ("after you break 5 fake doors and walls"). WRITTEN (2026-11-27, after efd18af): those, plus fake_doors.txt (what it mixes, what opens it, what it opens, the weapons line) and fake_walls.txt (a pointer to fake doors, the weapons line). PLAN COMPLETE.
