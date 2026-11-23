---
name: project_shop_items_plan
description: SETTLED (2026-11-23, 2.8's last three entries, 8 to 10 of 10): max health and max shield strength in the character category, and a safety net and power crystal in specials; 4 sections; Q&A log
metadata:
  type: project
---

# Shop items plan

New items for the player shop. Follows [[project_shop_plan]]. Nothing gets built until this plan is settled and committed.

## Rules for this plan

- It's a living list: more items can be added as we go (dev, 2026-11-21).
- The dev may change their mind about any item. When they do, remove that item from this plan.
- Every shop price is different. Taken: 25, 50, 100, 150, 200, 500, 1,000, 1,250, 1,500, 1,750, 2,000, 2,500, 3,000, 3,500, 4,000, 4,500, 5,000, 5,500, 10,000, 15,000.
- Nothing is permanent: what you buy lasts the run at most.
- No gold multipliers, as they'd undo the gold pack balance ([[project_gold_pack_scaling_plan]]), and keys stay out of the shop.
- 2.8 is at 7 of 10 with the floor breaker ledges, so this plan has at most 3 changelog entries.
- Nothing gets built until its sounds exist ([[feedback_sounds_before_features]]).

## Candidate items

Prices and details are placeholders until settled.

1. Safety net, 10,000 (SETTLED), in specials: if you'd fall into a hazard or a floor breaker, including a repair mistake, it's used up automatically and moves you just past it, running on, with main/misc/player move1 or move2 at random and "Your safety net caught you." Your health and lives aren't touched. Carrying several means each saves you once. How it works is SETTLED (dev: "Exactly right.").
2. Power crystal, 750 (SETTLED), in specials, inventory based: pressing the use key on it starts one of the 7 good powerups at random (Slow Motion, Moon Jump, Long Crouch, Quick Swings, Rapid Fire, Sturdy Shield, Tough Hide) for its 15 seconds, and it's used up. Replaces the idea of one token per powerup. (being discussed)
3. Maximum health upgrade, in the character category (from the dev's todo list), not an inventory item: each point adds 1 to your full health and 1 to your current health, works at once, lasts through lost lives (each new life refills to the raised maximum), and is gone when the run ends or you fully die. How it works and its price of 50 gold coins a point are SETTLED; it's called max health, with no limit.
4. Maximum shield strength upgrade, in the character category (from the dev's todo list), not an inventory item: each point adds 1 to your shield's full strength and 1 to its current strength if one is in use, and every new shield you start gets the bonus. It lasts the same way. How it works and its price of 25 gold coins a point are SETTLED; it's called max shield strength, with no limit, and is listed only while you have a steel shield, on or off, as shield defence is. Points already bought stay yours while it's hidden.

## Sections

1. Max health and max shield strength: the two stats at 50 and 25 gold coins a point, listed before shield defence, max shield strength only while you have a steel shield; adding to your bars at once, carrying through lost lives and to new shields; session statuses and modify player stats.
2. The power crystal: 750 gold coins in specials, a random good powerup on use, the still active message, and free run give, set and take.
3. The safety net: 10,000 gold coins in specials, catching a hazard or floor breaker fall automatically with move1 or move2, its use key line, and free run give, set and take.
4. Docks: the three changelog entries (2.8 at 10 of 10), a document for the safety net and the power crystal, player stats, player shop, hazards, floor breakers, free runs and any others they touch, the finished todo item, then template.lng and english.lng.

## Q&A log

- Dev (2026-11-21), with 2.8 at 6 of 10: "We have room for 4 more changes, but I'm not sure what else to add. Have any ideas? No new obsticals." Claude suggested a shield repair kit, shop achievements, records by difficulty and a quick start guide. Dev: "Oh good idea. New shop items. What do you suggest for those?" Claude suggested the four candidates above.
- Dev: "Let's make this as a propper shop items plan. We can add more items as we go along. Note that I may change my mind about certain items. If I do, you can remove that particular item from the plan."
- Q1: the shield repair kit (100 strength, 750 gold coins)? Dev: "I don't think I want this one, as I need new sounds for it". REMOVED from the plan.
- Q2 (asked): should this plan only hold items that can use sounds already in the game? Claude recommends yes.
- Dev: "For the safety net, how would that work? I recommend making you go passed the hazard slash floor breaker if you get too close. I mean on it. Also I forgot to tell you that the ledge sound should of also been used for floor breakers as well. The platform."
- Separate from this plan, to build first as its own small change: floor breakers get the ledge platform like hazards, on their countdown steps and the 2 steps after the hole (on_ledge() in hazard.nvgt covers only hazards today). It takes one changelog entry, 2.8's seventh, leaving this plan 3.
- Dev on the safety net as described: "Exactly right. Please do the quick ledge fix first, then change log it. Also try to make a seprat commit if possible." The ledge fix passed its test and Claude committed it alone as a709a75, with no attribution lines ([[feedback_no_coauthor_lines]]).
- The dev rescanned the sounds (2026-11-23), then: "update the code/docks first, then I'll talk about the new sounds. Also add the new character items to the shop plan." Paths updated; items 4 and 5 added from the todo list entry "Add some upgrades to increase your maximum health and shield strength in the character shop." The dev will explain money, move1 and move2 next; Q2 (existing sounds only) is on hold until then.
- Dev: "I was think the new move sounds would be used for the hazard/floor breaker item, but I forgot what that item was called." That's the safety net, so it plays move1 or move2 at random in place of the teleporter's sound.
- Q3: the safety net's price, 10,000 gold coins? Dev: "I agree with the new price. Let's talk about the character items".
- Q4 (asked): how the maximum health and maximum shield strength upgrades work. Claude recommends 1 for 1 like the other stats: each point adds 1 to the maximum and 1 to what you have now, lasts through lost lives, and is gone when the run ends. Maximum shield strength belongs to you, so every shield you start also gets it. Dev: "Yes. These are not inventory based. It addes to your helth bars for the player and shield."
- Q5: their prices a point, maximum health 50 and maximum shield strength 25 gold coins? Dev: "Agreed. The 2 max items should appear before shield defence. What would you call them?" SETTLED: the character category lists attack, defence, the maximum health upgrade, the maximum shield strength upgrade, then shield defence.
- Q6: their names, max health and max shield strength? Dev: "Agreed. Also, lower the following prices. defence=150, shield defence=200". Both prices changed in tuning.nvgt and the player shop and player stats documents, with no new changelog entry, as 2.8 isn't released.
- Q7: a limit on max health and max shield strength? Dev: "No max cap. I mean no limmit".
- Q8: when max shield strength is listed? Dev: "Use the same shield rule for that item too".
- Q9 (asked): free runs. Claude recommends both also join modify player stats with give, set and take, 0 to 1000, as bonuses on top of the full amounts that modify player health and modify shield strength set. Dev: "agreed." SETTLED.
- Q10 (asked): the full heal kit: 2,250 gold coins, in the items category, restoring all your health up to your maximum with the health potion's use sound, refused and kept at full health? Dev: "I do not want this item." REMOVED from the plan.
- Q11 (asked): powerup tokens: a new powerups category with the 7 good powerups, each its own price, kept in your inventory and used for its 15 seconds? Claude recommends yes. Dev: "I like the idea, but I want an item that lets you use a random good powerup if you press the use key. WHat are some good names for this item? This will be inventory based."
- Q12: its name? Claude recommended lucky charm. Dev: "I think I like, - Power crystal".
- Q13 (asked): the power crystal: 750 gold coins, in the specials category after master helper, with the existing powerup sound? Sturdy Shield only comes up while your shield is on. Dev: "What happens if you press a use key when one is active? I want it to say something. Like slides and trampolines."
- Q14 (asked): while a crystal's powerup is running, the use key says "Your power crystal is still active." and keeps the crystal, which also stops a held use key spending them all. It can be used again once that powerup ends, or if a powerup from the belt replaces it. Dev: "Yes." SETTLED.
- Q13 again (asked): the power crystal at 750 gold coins, and both it and the safety net in the specials category, alphabetically: animal, door, floor, force field, item, ladder and master helpers, power crystal, safety net, slide, trampoline? Dev: "That works for me. Also re-explain the safety net again, and what it would do." SETTLED.
- Q15 (asked): what the use key does on a safety net, since it works by itself. Claude recommends it says "Your safety net is ready." and keeps it. The dev asked what a door key says ("There is no door nearby." with none in reach). Dev: "I'll take your wording". SETTLED.
- Q16 (asked): where the safety net and power crystal work. Claude recommends the same as other specials: bought in endless, debug and free runs, given, set or taken in a free run's modify player inventory, absent from timed and practice runs; a net also catches you on a free run's no or practice deaths; no new statistics or achievements, and a caught fall doesn't count as caught or as cleared. Dev: "Agreed. Also, when it says your safety net is ready, that makes me think I need to engage it." Q16 SETTLED; Q15's wording reopened.
- Q15 again (asked): the use key's line on a safety net; Claude recommends "Your safety net will catch you if you fall." Dev: "I would say the first one, but when it says fall, that's fine for the most part, but you can also fall off of ladders." The net doesn't cover ladders. Claude now recommends "Your safety net will save you from a hazard or floor breaker." Dev: "yes. much better." SETTLED.
- Q2 closed by the choices since: the safety net uses move1 and move2, and the power crystal the existing powerget sound, so nothing new is needed.
- Q17 (asked): the changelog. Claude recommends two entries, leaving 2.8 at 9 of 10: "Added max health and max shield strength to the player shop's character category, which raise your health and shield bars for the rest of your run." and "Added a safety net that saves you from a hazard or floor breaker, and a power crystal that starts a random good powerup, to the player shop's specials." Dev: "Actually, I recommend 3 because I'm not going to add anything else."
- Q17 again (asked): three entries, filling 2.8 at 10 of 10: "Added max health and max shield strength to the player shop's character category, which raise your health and shield bars for the rest of your run.", "Added a safety net to the player shop's specials, which saves you once from a hazard or floor breaker." and "Added a power crystal to the player shop's specials, which starts a random good powerup when you use it." Dev: "Those are good." Plan SETTLED.
