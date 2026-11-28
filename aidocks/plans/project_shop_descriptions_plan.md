---
name: project_shop_descriptions_plan
description: SETTLED (2026-11-28, for 3.0, 2 sections, docks last): a description on every player shop line, after CookieCraze's "Description:" shop lines (ToyMania has none); draft descriptions under review
metadata:
  type: project
---

# Shop descriptions plan

The dev's suggestion (2026-11-28): item descriptions in the player shop for each thing it sells. ToyMania's shop has none; CookieCraze's store lines end ". Description: <text>" after "You can buy N." (menu.nvgt bakercategorymenu()), so that is the model.

## Proposed shape

- Each tab line becomes "health potion, costs 1,000 gold coins. You can buy 3. Description: Heals 5 to 10 percent of your full health."
- One whole-sentence description per id, in a shop_description() function beside the shop's lists, so the translation template picks each one up.
- Numbers in the descriptions match tuning.nvgt today (ammo_pack_min/max, health_potion_min/max_percent, life_capsule_min/max_lives, teleport_min/max_time, powerup_time 15000).
- No key names ([[feedback_no_key_names_in_hints]]).

## Draft descriptions (for the dev's review)

Character:
- Attack: Adds 1 damage to every hit from any weapon.
- Defence: Takes 1 off every blow to your health.
- Max health: Adds 1 to your full and current health.
- Max shield strength: Adds 1 to your shield's full and current strength, and to every new shield.
- Shield defence: Takes 1 off every blow to your shield.

Helpers:
- Ammo pack helper: Opens your ammo packs into the gun you're holding while it's on.
- Animal helper: Claps to scare away animals while it's on.
- Door helper: Unlocks and opens real doors while it's on.
- Floor helper: Opens and repairs floor breakers while it's on.
- Force field helper: Switches off force fields while it's on.
- Gold pack helper: Opens your gold packs while it's on.
- Item helper: Picks up items in your lane while it's on.
- Ladder helper: Grabs and climbs real walls' ladders while it's on.
- Master helper: Does the jobs of all nine other helpers at once while it's on.
- Master helper deluxe: Does every job the master helper does while it's on, and picks up items in every lane, not just yours.
- Powerup helper: Collects every powerup while it's on, whether you're on the ground or in the air.

Items:
- Ammo pack: Adds 5 to 10 bullets to the gun you're holding when you open it.
- Health potion: Heals 5 to 10 percent of your full health.
- Life capsule: Gives you 1 or 2 more lives.
- Player teleporter: Throws you 2 to 5 seconds along the belt, forward or back.
- Steel shield: Takes the blows in place of your health until it breaks, and switches on and off from your inventory.

Specials:
- Power crystal: Starts a random good powerup for 15 seconds.
- Safety net: Saves you once from falling into a hazard or a floor breaker, by itself.
- Slide: Puts you on a slide straight away, carrying you at double speed for 2 to 4 seconds.
- Trampoline: Launches you on a good trampoline's flight over everything, from where you are.

## Q&A log

Q1. Are the draft descriptions right? (Recommended: go through them by tab and name only the ones to change.)
A1 (dev): "I like all of them for the most part, but master helper deluxe does not say, while it's on." Fixed: "Does every job the master helper does while it's on, and picks up items in every lane, not just yours." All others kept as drafted.

Q2. Where is the description heard: on the tab line after "You can buy N." (CookieCraze), or in the pack menu's intro? (Recommended: the tab line.)
A2 (dev): "I highly recommend putting it after it says you can buy x." The tab line, as "... You can buy 3. Description: ...".

Q3. The changelog wording: "Added a description to everything in the player shop, which you hear after how many you can buy, such as "Description: Heals 5 to 10 percent of your full health."."
A3 (dev): "That works. it will be 2 sections right? docks is always the last section". Wording kept; two sections, docks last.

## Sections (PLAN SETTLED 2026-11-28)

1. Code: shop_description() in shop_menu.nvgt with the 25 sentences, added to each tab line after "You can buy N."; refresh template.lng.
   BUILT and tested 2026-11-28 (all 3 passed: every tab line ends with its description; the line after an error; the line after a purchase, with the count updated).
2. Docks: player_shop.txt's example line and a sentence on descriptions, then the changelog entry (3.0's 14th of 20).

