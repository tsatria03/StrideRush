---
name: project_npc_folder_plan
description: SETTLED (2026-11-17), not built: repoint animals (and later insects) to each environment's new traps/npc/<kind> folder after the dev's sound reorg; learn sounds lists npc's kinds; groundwork for 2.5's insects; Q&A log
metadata:
  type: project
---

Started 2026-11-17 (dev: "Please rescan the sounds. I did a reorg of it.", then "Yes. You'll need to repoint the paths again. Also check the change log to see if it has any entries related to path moves."), on 1c0f79b (V2.40). Not built; no sections yet.

## Findings (2026-11-17)
- The reorg, uncommitted: all 153 files of default's traps/animals moved, unchanged (checked against HEAD byte for byte), to traps/npc/animals (countdown, general/birds, general/dogs). New: traps/npc/insects, 23 files: countdown warn1-1 to warn3-5, general/bees/bee and bee2, each death, hit, hurt, loop. The start of 2.5's insects todo item.
- What breaks: animal.nvgt's animal_folder() is trap_folder(env, "animals"), environments.nvgt's type_path() gives traps/animals/, now missing, so animals don't spawn anywhere (endless, timed, combinations with animals), practicing animals finds no environment, free run's add list drops them; learn_sounds_menu.nvgt's learn_environment_category() lists every folder in traps/* as a type, so "npc" shows as a type with no general folder, and the animals' countdown and themes vanish from it. No crash anywhere.
- Changelog: no entry has ever covered a sound path move (the misc/trap to environments move, the countdown moves went in without one); the only related entry is a removal, "Removed a bunch of ambiences and platforms that were no longer needed in the game." This reorg was never released, so it needs no entry ([[feedback_changelog_rules]]: a never-shipped change in source needs none).

## Q&A log
- Q1 (Claude, 2026-11-17): the npc rule and learn sounds. Proposed: in every environment, traps/npc/<kind> holds the npc kinds, animals now and insects later; type_path() sends those kinds there, so everything that finds a type's themes and countdown follows (spawning, environment checks, practice, free run, combinations, countdowns). Learn sounds gets an npc category beside traps and transitions, with a list per kind (animals split into birds and dogs as now), mirroring the folders, and npc's kinds join the countdowns list; "npc" itself is no longer listed as a trap. Recommended: as proposed.
- A1 (dev, 2026-11-17): "yes that works."
- Q2 (Claude, 2026-11-17): the sections. No new sounds needed. Proposed: 1. Paths: a list of npc kinds in environments.nvgt holding only kinds the game has (animals; insects join it when they're built in 2.5), type_path() sending them to traps/npc/<kind>/; learn sounds' npc category built from that list, so a folder the game doesn't know yet, like insects today, isn't listed, as the readme says unknown kinds are ignored; "npc" skipped as a trap. Tests: animals spawn again, practice animals works, learn sounds shows npc with animals. 2. Docks: the readme's customizing section (traps/npc for the npc kinds such as animals) and learn sounds section (animals under npc); no changelog entry, since the reorg was never released and the game plays the same; the version history and CLAUDE.md. Recommended: as proposed.
- A2 (dev, 2026-11-17): "it's good."

## THE PLAN IS SETTLED (2026-11-17)
1. Paths: environments.nvgt's list of npc kinds (animals; insects added when built), type_path() sending them to traps/npc/<kind>/; learn sounds' npc category from that list, beside traps and transitions, with npc kinds in the countdowns and "npc" no longer a trap; unknown npc folders (insects today) not listed. Tests.
2. Docks: the readme's customizing and learn sounds sections; no changelog entry (unreleased reorg, same play); the version history and CLAUDE.md.

## Build log
- Not started.
