---
name: project_pack_helpers_plan
description: SETTLED (2026-11-27, for 3.0, 2 sections): two new player shop helpers, the ammo pack helper and the gold pack helper, opening packs for you, with the master helper taking both jobs; Q&A log
metadata:
  type: project
---

# Pack helpers plan

Goal (the dev, 2026-11-27): "What do you call a special item that helps you open ammo and or gold packs automaticly as long as someone has one?"

## Findings

- Helpers (specials.nvgt): helper_items lists animal, door, floor, force field, item, ladder and master helpers, helpers_on one bool each; the use key toggles one (toggle_helper(), the helperon and helperoff sounds); helper_working() is true for a helper or the master helper; a helper lasts the whole run. Prices in tuning.nvgt's shop_special_ids and shop_special_prices (animal 3000, door 3500, floor 5500, force field 2500, item 4000, ladder 4500, master 15000).
- Packs: use_ammopacks() (ammo.nvgt) opens every ammo pack into the drawn gun's reserve until it's full; use_goldpacks() (goldpack.nvgt) opens every gold pack at once, each paying goldpack_percent() of its amount, 10 percent at an endless level's start speed up to 100 at its top.
- The safety net is the one special that works just by being carried; every helper works only while switched on.

## Open questions

1. Settled below: two helpers, the master helper taking both jobs.
2. When each one opens packs.
3. Prices and the specials order.
4. The free run console and learn sounds.
5. Changelog wording and docks.
6. Sections.

## Q&A log

- Q1, the name and shape. Claude recommended "pack helper", following the helpers' naming; the dev asked whether one combined helper or two would be better; Claude recommended two, since gold packs pay more the longer you wait (goldpack_percent()) and ammo packs don't, so a player may want ammo opened at once and gold held. Dev: "I like that. 2 items, plus the master helper adds 2 extra jobs." Settled: an ammo pack helper and a gold pack helper, each a toggled helper like the others; the master helper does both jobs too, eight in all.
- Q2, when they open packs. Claude recommended both work as opening a pack yourself, without the key: the ammo pack helper, while on, opens the ammo packs you carry into the drawn gun whenever its reserve has room (the use sound, "You got 23 rounds of ammo."), waiting quietly with a melee weapon drawn or a full reserve, so "This weapon's reserve is already full." never repeats; the gold pack helper, while on, opens any gold pack you carry at once ("You got 482 gold coins."); both pause where you can't use your inventory (a door's carry, a ladder, a floor breaker's repair, a slide) and catch up after; switching one on with packs already carried opens them at once (ammo once there's room). Dev: "I like that." Settled.
- Q3, prices and order. Claude first recommended 2,000 for both, below every helper. Dev: "I don't like things in the shop having the same price." (2,000 was also the steel shield's.) Revised: ammo pack helper 2,250, the cheapest helper, first in the specials; gold pack helper 2,750, between the force field and item helpers in the list; the master helper stays 15,000. Dev: "I like that. Also, in the future, make new shop things 250 gold a part." Settled; the rule is saved as [[feedback_shop_prices]].
- Q4, free runs and sounds. Claude recommended both join free_bought_ids (freebelt.nvgt), in the shop's order, so modify player inventory gives, sets and takes them; no new sounds (the shared helperon and helperoff, the packs' own use sounds), so learn sounds is unchanged; the inventory says "ammo pack helper, on" or "off" and the use key "Ammo pack helper on." like the others. Dev: "yes it works". Settled.
- Q5, changelog and docks. Changelog, on top of 3.0's block: "Added an ammo pack helper and a gold pack helper to the player shop's specials, which open your ammo and gold packs for you while they're on, and the master helper now does both of their jobs too." Docks: new ammo_pack_helpers.txt and gold_pack_helpers.txt in item_helpers.txt's format (the gold one noting endless packs pay less early, so it may be worth switching on later); master_helpers.txt (all eight, 13,000 less than the eight's 28,000, two job lines, keys and packs the only things it uses from your inventory); player_shop.txt's specials list (both with prices and jobs, the master helper's line all eight). Dev: "agreed". Settled.
- Q6, sections. Claude recommended two: the helpers (specials.nvgt, tuning.nvgt, freebelt.nvgt, the language files), with tests; then the docks. Dev: "that works." Settled.

PLAN SETTLED (2026-11-27): ready to commit, then build Section 1 on the go-ahead.

## Sections

1. The helpers (tests): specials.nvgt's helper_items gains "ammo_pack_helper" and "gold_pack_helper" (helpers_on 9), their jobs in helpers_update() through helper_working() (so the master helper does both), the ammo helper calling use_ammopacks() only while a gun is drawn with reserve room, the gold helper use_goldpacks(), each removing what opened as use_item() does (item_used()), and both waiting while the inventory is locked (a door's carry, a ladder, a repair, a slide); tuning.nvgt's shop_special_ids and shop_special_prices (ammo pack helper 2,250 first, gold pack helper 2,750 between the force field and item helpers); freebelt.nvgt's free_bought_ids; template.lng refreshed and english.lng synced.
   BUILT (2026-11-27, after 5d9ca58): helper_items in alphabetical order with helpers_on(9); pack_helpers_update() called from helpers_update() after the item helper (so a pack it picks up opens the same frame); tuning.nvgt's prices; freebelt.nvgt's three lists. Tests, in a debug run on all at 500: 1 (the specials order and prices) PASSED; 2 (the gold pack helper opens a picked-up pack, off keeps it) PASSED; 3 (the ammo pack helper waits with the fist drawn, opens on drawing the pistol, then on pickup) PASSED; 4 (the master helper doing both jobs) SKIPPED, the dev: "You can skip this test. I'll test it myself when I unlock free run", since it costs 15,000 and helper_working() is the same check every helper's job uses. Then the dev unlocked free run and ran it: "I unlocked free run, and tested it. passed". Test 4 PASSED. Section 1 COMPLETE.
2. The docks (no tests): the changelog entry, ammo_pack_helpers.txt, gold_pack_helpers.txt, master_helpers.txt, player_shop.txt.
