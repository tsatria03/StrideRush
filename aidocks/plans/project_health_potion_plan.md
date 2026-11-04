---
name: project_health_potion_plan
description: SETTLED, not built (2026-11-04, 1.4) - health potions, a new inventory item that restores some of your health, using the health_potion sounds left over from the life potion; ToyMania's heals a random 5 to 10 percent of max HP; Q&A log
metadata:
  type: project
---

Status: SETTLED, not built, started 2026-11-04 on top of 09e3573 (V1.30), in 1.4 (1 of 10 changelog entries used). No code until the plan is settled and the dev gives a go-ahead ([[feedback_plans_record_qna]]). The dev: "we need to implement health potions. Look at how much it healed in toy mania."

What exists already:
- Sounds: equipments/items/common/health_potion has spawn, loop, get, break1-6 and use (the old life potion set, kept when the life potion became the life capsule, [[project_potion_teleporter_plan]]). There's no misc/player heal sound.
- Health: player_health out of player_hp 200; take_damage() in lives.nvgt; H speaks "P percent health remaining, N lives." ([[project_player_health_plan]]). Damage: spikes, force fields, projectiles and walls 20, mines 40, doors 60, barriers 80 (barriers return in 1.4 with lanes).
- The life capsule (globals/capsule.nvgt) is the item pattern to copy: spawned on the belt with spawn and loop, picked up with either hand into the inventory, broken by running or landing on it or by a weapon, used with U.

ToyMania (read only, src/includes/main/globals/inventory.nvgt, the "health_potion" branch of item use):
- Refused at full health: "You don't need to use this!", and the potion is kept.
- Otherwise it plays the item's use sound and misc/player's heal sound, takes one potion, heals a random 5 to 10 percent of max health (health is 1000 there, so 50 to 100), capped at the maximum, and speaks "Healed to P percent HP."

Q&A log:
- Q: How much should a health potion heal? ToyMania's 5 to 10 percent would be 10 to 20 of Stride Rush's 200 health, less than one spike hit. (Asked 2026-11-04; Claude recommended a random 20 to 40 percent, 40 to 80 health, about one or two hits' worth, capped at full health.)
- The dev (2026-11-04): "What about 1 to 5 percent of your health? What would that be. Also I added the healing sounds." Claude: 1 to 5 percent of 200 is 2 to 10 health, at most half of a spike's 20; ten potions at the top roll would undo one door. SOUNDS ADDED: misc/player/heal1 to heal3 (a *heal* wildcard picks one at random), so the use can play the potion's use and the player's heal together, as ToyMania does. Still open: the amount (1 to 5 percent, or Claude's 20 to 40).
- A (dev, 2026-11-04): "What about 5 to 10? Would that be good? I don't want those to be too strong. I want you to be able to collect a few of them." Claude agreed: 5 to 10 percent is 10 to 20 health, at most one spike hit, so a few potions together undo a mine or a door; it's also exactly ToyMania's range. SETTLED: a random 5 to 10 percent of player_hp, capped at full health.
- Q: How often do they turn up? Item chances now (one spawn in N): ammo packs 8, powerups 10, shields 16, teleporters 16, life capsules 20. (Asked 2026-11-04; Claude recommended 1 in 10, as often as powerups and more often than capsules, so a run gathers a few as the dev wants.)
- A: "I like that. 1 in 10." (dev, 2026-11-04). SETTLED: health_potion_chance 10.
- Q: Are Claude's proposed defaults for the rest OK (asked 2026-11-04)? 1. On the belt it works exactly like a life capsule: spawn and loop at its tile, either hand picks it up into the inventory (get, the player's give, "health potion"), running or landing onto it or a weapon hit breaks it, a clean jump misses it. 2. U plays the potion's use and a player heal together and says "Healed to 85 percent health." 3. At full health U refuses with "You don't need to use this.", and you keep the potion. 4. Not usable while a door carries you (the inventory rule). 5. A "health potions" debug spawn choice, whose run starts at half health so there's something to heal. 6. The code goes in globals/potion.nvgt, after the dev's short names (capsule.nvgt, ammo.nvgt). 7. Docks: a 1.4 changelog entry, "Added health potions, ...", and the readme's items paragraph and U line.
- A: "agreed with all 7" (dev, 2026-11-04). THE PLAN IS SETTLED; build one section per go-ahead.

Build sections (written 2026-11-04; [[feedback_describe_dont_show_code]]):
Section 1: health potions. New globals/potion.nvgt copied from capsule.nvgt's pattern (potionpool, class healthpotion, potion_folder equipments/items/common/health_potion/; spawn, pickup, break, landing, weapon hits, destroy_all), with use_potion(): refuse at full health, otherwise heal a random health_potion_min_percent 5 to health_potion_max_percent 10 of player_hp capped at player_hp, play use and misc/player *heal*, speak "Healed to P percent health.". Hooks: all_pools, clear_run_objects(), step_check(), player_land(), hand_check(), bullet and melee strikes, the inventory's U, the spawner (item_types "health_potions", health_potion_chance 10), tuning values, and the debug run starting at half health.
Section 2: docks (1.4 changelog entry, readme).
