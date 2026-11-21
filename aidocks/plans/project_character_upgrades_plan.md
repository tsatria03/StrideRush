---
name: project_character_upgrades_plan
description: SETTLED (2026-11-21, 2.8's second entry): a character category first in the player shop selling attack, defence and shield defence, 1 for 1 at 100, 200 and 300 gold coins a point with no cap, lasting the run; 3 sections; Q&A log
metadata:
  type: project
---

# Character upgrades plan

The dev's idea: a third player shop category, character, selling attack (useful for weapons), defence (damage reduction against obstacles) and shield defence. Follows [[project_shop_plan]]. Nothing gets built until this plan is settled and committed.

## How SimpleFighter does it (read only reference)

- Attack: every hit is the weapon's damage plus attack times attmod, which is 2 (weapon.nvgt, game_handlers.nvgt).
- Defence: a blow is max(1, damage minus defence times defmod), and defmod is 3.
- Shield defence: a blow to the shield is max(1, damage minus shield defence times 3).
- All three start at 0, and a point costs 1.

## How Stride Rush stands

- A weapon hit is weapon_damage times weapon_damage_multiplier: 12 for the bat up to 120 for the pistol.
- take_damage() in lives.nvgt scales every blow by level first (60 percent on easy up to 100 on chaos), then a worn shield takes it (shield_absorb()) or your health does, each through its powerups.
- Blows before scaling: 5 for winds and shots, 10 animals, 20 spikes and insects, 30 force fields, 40 projectiles, rams and ladder falls, 50 walls, 60 mines and ladder collapses, 70 doors, 80 barriers. Hazards and floor breaker falls skip take_damage().

## Open questions

1. SETTLED: 1 for 1. Each point of attack adds 1 damage to a hit, and each point of defence or shield defence takes 1 off a blow, never below 1 damage.
2. SETTLED: attack 100, defence 200, shield defence 300 gold coins a point, with the usual pack sizes of 1, 5, 10, 25, 50 and 100 and buy all.
3. SETTLED: no maximum for attack, defence or shield defence.
4. SETTLED: the level's share first, then the powerups, then defence or shield defence, never below 1 damage. Hazards and floor breaker falls are unaffected.
5. SETTLED: the shop's usual lines with no current amount, as for the other items; "You bought 5 attack points for 500 gold coins." on buying; your points in the pause menu's view session statuses; no new key.
6. SETTLED: they take effect the moment you buy them, without going into your inventory, last through lost lives, and are gone when the run ends or you fully die. Shield defence belongs to you, so it carries over to the next shield.
7. SETTLED: bought in endless and debug runs, none in timed or practice runs, a new "modify player stats" console item for a free run with give, set and take for each, and no new statistics or achievements, as gold coins spent already counts them.
8. SETTLED: 2.8's second entry: "Added a character category to the player shop, where your gold coins buy attack, defence and shield defence points that help you hit harder and take less damage for the rest of your run."
8b. SETTLED: the player shop's menu lists character first, then items, then specials. The character category lists attack, then defence, then shield defence.
8c. SETTLED: shield defence appears in the shop and in modify player stats while you have a steel shield in your inventory or are wearing one, and is hidden only with no shield at all. Points already bought stay yours while it's hidden.

## Sections

1. The upgrades and the shop: the three stats, reset when the run ends or you fully die; attack added to every weapon hit; defence and shield defence taken off blows last, never below 1; the character category first in the shop, with its pack menus, purchase wording and shield defence's visibility rule.
2. Readouts and free run: your points in view session statuses, and the new modify player stats console item with give, set and take.
3. Docks: the changelog entry, a new game document named player_stats.txt for the three stats, and the player shop, weapons, health and lives, steel shields, free runs and any other documents they touch, then template.lng and english.lng.

## Q&A log

- Dev (2026-11-21): a character category with attack and defence, useful for weapons and damage reduction against obstacles. Claude recommended leaving out SimpleFighter's other categories, since packs, potions, capsules and shields already cover them.
- Dev: "Yes. We can plan this. Attack and deffence cannot go lower than 1. We can also talk about how many points it increases/reduces if you buy 1 or multiple. If you are confused. Look at how both attack and defence work in simple fighter. I also want shield defence as well."
- Taken to mean SimpleFighter's rule that a hit or blow never does less than 1 damage; the dev didn't object.
- Q1, dev: "What about 1 for 1? As in each one you buy adds 1 point, not 2 or 3. HOpe this make sence. This also applies to shields."
- Q2 raised by Claude: at 1 for 1 a point is small, so prices are low and all different from the shop's others. Defence costs most since it works on every blow to your health, shield defence less since it needs a worn shield, attack least since it only matters when you hit something.
- Q2 answer, dev: "I want the gold to be less, take the 0 off that, so it's 10, 15, etc".
- Q3 raised by Claude: at 20 a point, 47 defence (940 gold coins, about 5 gold packs on easy) turns every blow on easy into 1 damage, and 79 defence (1,580) does the same on chaos. Caps of 25 defence and 25 shield defence leave a door at 17 on easy and 45 on chaos.
- Q4, dev: "I like that, but what about the earlier difficulty scaling? How will that effect defence?" A: the level's share comes first and defence is a flat amount after it, so the same defence takes the same number off on every level, which is a bigger share of a blow on easy. 10 defence: a door does 32, 39, 46, 53 and 60 from easy to chaos, a spike 2, 4, 6, 8 and 10. Dev: "Yes. That works."
- Q5: how you hear your points? Dev: "I like that better. No extra keys."
- Q6: how long they last? Dev: "I like that too. If you die, you loose them."
- Q7: where they're available, with a new console item? Dev: "That's good. I was gonna suggest a new console menu."
- Q8b, dev: "The character category will appear first in the player shop menu. Also attack will appear first, followed by defence, and then shield defence. I do have one question about shields, but I'll ask after you record it"
- Q8c, dev asked when shield items appear in a free run (only while a shield is worn), then: "I was gonna say you need to have a shield in your inventory, but you do not need to wear it". Claude raised that wearing one takes it out of your inventory, so a worn shield should count too. Dev: "I agree with that."
- Q8: the changelog wording? Dev: "It's good to go". Plan SETTLED.
- Dev: "There should be a new game dock called player_stats, but save that for the dock section".
- Section 1 BUILT (2026-11-21, after d6d1ec6): game/playerstats.nvgt holds the three stats, after_defence(), weapon_hit_damage() and has_a_shield(); reset_run() clears them (not clear_inventory(), which a free run also calls to empty the inventory); take_damage() and shield_absorb() take defence off last; the four weapon hit paths use weapon_hit_damage(); the shop lists character first. Dev, after the build: "please make shield defence 300gold" (was 150). Tests: 1 of 3 (shop list and buying), 2 of 3 (shield defence's visibility), 3 of 3 (the new wear sound) all PASSED.
- Tests: 1 of 4 (shop list and buying) and 2 of 4 (shield defence's visibility) PASSED.
- Sounds (dev, 2026-11-21): the steel_shield folder lost use.ogg and break.ogg for wear.ogg, remove.ogg and break1 to break6. Wearing now plays wear; the *break* lookup picks the new variants by itself. remove.ogg has no use yet, as a worn shield can't be taken off. Asked the dev whether to add that. Dev: "Let's save that question for after this plan is complete." ASK AGAIN once this plan is complete: should a worn shield be removable, with which key, and does a damaged one keep its strength?
- Section 1's tests became 3: exact damage can't be checked until section 2 adds modify player stats and your points to the session statuses, so the attack, defence, shield defence and reset checks move to section 2's tests.
- Section 2 BUILT (2026-11-21, after 026f82a): attack, defence and shield defence lines in session_status_lines() for endless, debug and free runs; modify player stats in the free run console (free_stats_menu(), free_change_stat()), set 0 to 1000, give and take 1 to 1000, take stopping at 0, reset on a replay like the shop's points. Tests: 1 of 5 (console and statuses), 2 of 5 (defence, floor of 1), 3 of 5 (shield defence, separate from defence), 4 of 5 (attack), 5 of 5 (kept through a lost life, reset on restart) all PASSED.
- Q2 and Q3 revised, dev: "Actually I have a better idea, put the 0 back, and no max cap for the following stats. attack, defence, shield defence." At 200 a point, 47 defence costs 9,400 gold coins and 79 costs 15,800, so the price is now what limits them.
