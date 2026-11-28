---
name: project_master_helper_deluxe_plan
description: SETTLED (2026-11-27, for 3.0, 2 sections, 20,000 gold coins): the master helper deluxe, the master helper's eight hand jobs with items collected in every lane (never moving you); began as the item helper deluxe; Q&A log
metadata:
  type: project
---

# Master helper deluxe plan

Goal (the dev, 2026-11-27): "I have a new helper idea. What about, "item helper deluxe". WHat this does is collect any item in any lane. What do you think?"

## Findings

- The item helper (specials.nvgt's helpers_update()) calls each pickup function (pick_up_ammopack(), pick_up_goldpack(), pick_up_key(), pick_up_shield(), pick_up_capsule(), pick_up_potion(), pick_up_teleporter()), each skipping items with lane != current_lane; slides and the item helper share them.
- helper_items: ammo pack, animal, door, floor, force field, gold pack, item, ladder and master helpers; the master helper does the other eight jobs, its item job your lane only.
- Shop prices in use: 25, 50, 100, 150, 200, 500, 750, 1,000, 1,250, 1,500, 1,750, 2,000, 2,250, 2,500, 2,750, 3,000, 3,500, 4,000, 4,500, 5,000, 5,500, 10,000, 15,000; new prices on a free 250 step ([[feedback_shop_prices]]).

## Open questions

1. The price.
2. The master helper.
3. Pickup sounds from other lanes.
4. With the item helper on too.
5. Changelog wording and docks.
6. Sections.

## Q&A log

- Q0, the idea. Claude thought it a good premium special, as long as it stays a clear, expensive upgrade, since choosing a lane for an item is one of the game's small decisions; the name sorts right after the item helper. It suggested somewhere well above 4,000 on a free 250 step, such as 7,500 or 8,000. Dev: "I agree with the price. It should be way higher than the normal item helper." The exact figure is Q1.
- Q1, the price. Claude recommended 8,000 over 7,500: twice the item helper, well above the floor helper's 5,500, below the safety net's 10,000 and the master helper's 15,000. Dev: "I'd say 8k works well." Settled: 8,000 gold coins.
- Q2, the master helper. Claude recommended the master helper keep collecting in your lane only, the item helper deluxe its own upgrade outside the master's jobs. Dev: "Actually, on second thought, perhaps it might be a better idea to have a new item called master helper deluxe, instead of item helper deluxe. This one will cover any lane, not just your lane. It still will not play the game for you. It's just for hands, including lane changes." Claude asked whether "including lane changes" meant reaching items in every lane without moving you, or moving you to them. Dev: "I meant it collects all items in any lane. It does not switch lanes for you." Settled: the item helper deluxe is DROPPED; a new master helper deluxe does the master helper's eight hand jobs, its item job collecting every item in every lane without ever moving you, and never jumps, crouches, fires or dodges; the master helper stays your lane only. Q1's 8,000 no longer applies; the price is reopened.
- Q1 (reopened), the price. Claude recommended 19,000 (the master helper's 15,000 plus the 4,000 the dev valued every-lane collecting at), or 20,000 for a rounder top price. Dev: "I want it to be 20thousand". Settled: 20,000 gold coins, the shop's top price.
- Q2, other-lane pickup sounds. Claude recommended an item taken from another lane plays its get sound in that lane, held there with keep_lane_clip() (lane.nvgt) so it can't drift as you change lanes, your give sound centred as now, the same spoken name, the inventory and its focus as any pickup; your own lane's pickups unchanged. Dev: "I agree". Settled.
- Q3, with the other helpers. Claude recommended the master helper's way: while the deluxe is on, all eight jobs get done whatever the others are set to, its item job in every lane; the others keep their own settings underneath, so switching the deluxe off leaves the item and master helpers at your lane; nothing is done twice or faster; "master helper deluxe" sits right after the master helper in the shop and inventory, the last helper before the power crystal. In code, helper_working() becomes the helper, the master helper or the deluxe, and only the item pickups check for every lane. Dev: "agreed". Settled.
- Q4 (added), the plural. A plain "s" would make "master helper deluxes" (the inventory's count line, shop_item_words() in the pack menus, the free run lists). Claude recommended "master helpers deluxe" ("master helpers deluxe, 2", "Buy 5 master helpers deluxe for 100,000 gold coins", the document master helpers deluxe) through a small plural rule in those places. Dev: "agreed". Settled.
- Q5, changelog and docks. Changelog, on top of 3.0's block: "Added a master helper deluxe to the player shop's specials, which does every job the master helper does and picks up items in every lane, not just yours, without ever moving you." Docks: new master_helpers_deluxe.txt ("Master helpers deluxe.", in master_helpers.txt's format: price, jobs with every lane's items and their lane sound, what it doesn't do, using one, with your other helpers, practice and free runs); master_helpers.txt and item_helpers.txt each a sentence pointing to it; player_shop.txt "Master helper deluxe: 20,000 gold coins. Does the master helper's jobs, picking up items in every lane." after the master helper. Dev: "That works." Settled.
- Q6, sections. Claude recommended two: the helper (specials.nvgt's helper_items, helpers_on 10 and helper_working(); the seven pickup functions' every-lane option, used by the helpers only while the deluxe is on, with keep_lane_clip() for another lane's get sound; the plural in the inventory, shop_item_words() and the free run lists; tuning.nvgt's 20,000; freebelt.nvgt; the language files), with tests; then the docks. Dev: "agreed". Settled.
- Correction (dev, after the plan was committed): "One correction to the master helper deluxe. It will also help you collect powerups in the air." Powerups (powerup.nvgt) are belt-wide, half ground (collected arriving on the ground) and half flight (arriving in the air), and arriving the wrong way breaks one (powerup_check()'s pu.flight != is_grounded()). Claude recommended the deluxe collect both kinds whichever way you arrive, so none breaks while it's on, noting it collects bad powerups too, since the event is picked on contact. Dev: "Oh good idea. both kinds". Settled: while the deluxe is on, every powerup you reach is collected, on the ground or in the air. Section 1 adds it to powerup_check(); Section 2's docks add a powerups line to master_helpers_deluxe.txt and powerups.txt, and the changelog entry becomes: "Added a master helper deluxe to the player shop's specials, which does every job the master helper does, picks up items in every lane, not just yours, and collects every powerup whether you're on the ground or in the air, without ever moving you."

PLAN SETTLED (2026-11-27): ready to commit, then build Section 1 on the go-ahead.

## Sections

1. The helper (tests): as Q6, plus powerup_check() collecting both kinds while the deluxe is on.
   BUILT (2026-11-27, after c9a042f): specials.nvgt's helper_items (helpers_on 10) and helper_working() with the deluxe; the seven pick_up_ functions' any_lane, passed by the helpers while the deluxe is on; lane.nvgt's play_pickup_sound() (centred from your lane, else in the item's lane through keep_lane_clip()); powerup_check() collecting either kind either way; inventory.nvgt's item_plural() in the inventory, shop_item_words() and the free run's given, taken and now-have lines; tuning.nvgt 20,000; freebelt.nvgt (internal id master_helper_deluxes, so dropping the last letter maps to the item). Fixes during the build: the variable "any" is a reserved type name (errors.txt; renamed every_lane, per [[project_angelscript_reserved_words]]); the dev found slides didn't catch other lanes with the deluxe on, since slide_update() does its own catching, so it now passes the every-lane option too (the docks must say slides catch every lane with the deluxe on). The dev's save was wiped, so a temporary free run unlock was used for the tests and removed. Tests, in a free run: 1 (the price, the plural in the pack menu and inventory) PASSED; 2 (items in both other lanes, sounds from their lanes; off, they pass) PASSED; 3 (force fields, animals, a key from any lane and its real door, both packs) PASSED; 4 (a flight powerup run under and a ground one jumped are collected; off, both break) PASSED; 5 (a slide catches every lane, and a flight powerup; off, your lane only) PASSED. Section 1 COMPLETE.
2. The docks (no tests): as Q5, plus the powerups line in master_helpers_deluxe.txt and powerups.txt, and the corrected changelog entry.
