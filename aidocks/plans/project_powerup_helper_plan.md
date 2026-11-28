---
name: project_powerup_helper_plan
description: SETTLED (2026-11-27, for 3.0, 2 sections, 3,250 gold coins): a powerup helper in the player shop collecting every powerup, ground or air, as the master helper deluxe does; Q&A log
metadata:
  type: project
---

# Powerup helper plan

Goal (the dev, 2026-11-27): "One more helper we forgot to add is the powerup helper. This one will collect any powerup for you, ground or air, just like the master helper deluxe already does."

## Findings

- Powerups (powerup.nvgt): belt-wide, half ground and half flight; powerup_check() collects one when pu.flight != is_grounded(), or while the master helper deluxe is on (helper_active()), and otherwise breaks it. The event is picked on contact, good or bad.
- Helpers (specials.nvgt): helper_items has ammo pack, animal, door, floor, force field, gold pack, item, ladder, master and master helper deluxe; helper_working() is the helper, the master helper or the deluxe. The master helper has done every single-job helper's job so far.
- Shop prices in use ([[feedback_shop_prices]]): 25, 50, 100, 150, 200, 500, 750, 1,000, 1,250, 1,500, 1,750, 2,000, 2,250, 2,500, 2,750, 3,000, 3,500, 4,000, 4,500, 5,000, 5,500, 10,000, 15,000, 20,000.

## Open questions

1. Whether the master helper takes the job too.
2. The price and its place in the specials.
3. Changelog wording and docks.
4. Sections.

## Q&A log

- Q1, the master helper. Claude recommended the master helper collect powerups too, keeping its rule (it does every single-job helper's job) without an exception; the deluxe then differs only in taking items from every lane; powerup_check() would use helper_working("powerup_helper"). Dev: "I agree. The regular master helper should also collect those." Settled.
- Q2, price and place. Claude recommended 3,250 (just above the animal helper; it can't choose good powerups, so below the always-helpful helpers), listed after the master helper deluxe, the last helper before the power crystal; the master helper stays 15,000, saving 16,250 against the nine single helpers' 31,250. Dev: "agreed". Settled.
- Q3, changelog and docks. Changelog, on top of 3.0's block: "Added a powerup helper to the player shop's specials, which collects every powerup for you whether you're on the ground or in the air, and the master helper now does this too." Docks: new powerup_helpers.txt (item_helpers.txt's format: price, either kind either way so none breaks, bad ones too, using one, in a run, practice and free runs); master_helpers.txt (all nine, 16,250 less, a powerups job line, the flight sentence); master_helpers_deluxe.txt (the powerups line as the powerup helper's job, items from every lane its only extra); powerups.txt (the pointer names the powerup helper, then the master helpers); player_shop.txt ("Powerup helper: 3,250 gold coins. Collects every powerup, on the ground or in the air." after the deluxe; the master line all nine). Dev: "that works." Settled.
- Q4, sections. Claude recommended two: the helper (specials.nvgt's helper_items with "powerup_helper" after the deluxe and helpers_on 11; powerup_check() collecting while helper_working("powerup_helper"); tuning.nvgt 3,250; freebelt.nvgt; the language files), with tests; then the docks. Dev: "yes that works". Settled.

PLAN SETTLED (2026-11-27): ready to commit, then build Section 1 on the go-ahead.

## Sections

1. The helper (tests): as Q4.
   BUILT (2026-11-27, after 1aca020): helper_items with "powerup_helper" after the deluxe (helpers_on 11); powerup_check() through helper_working("powerup_helper"), so the deluxe's own check is gone; tuning.nvgt 3,250; freebelt.nvgt's lists (15 entries each). Also fixed, at the dev's go-ahead: the mode menu's free run line said "with no difficulty", out of date since 2.9, now "with nothing counted toward your progress." (menu.nvgt; no changelog entry). A temporary free run unlock was used for the tests and removed. Tests, in a free run: 1 (the price and place, "Powerup helper on.", the mode menu line) PASSED; 2 (flight run under and ground jumped are collected; off, both break) PASSED; 3 (the regular master helper collects both; off, they break) PASSED. Section 1 COMPLETE.
2. The docks (no tests): as Q3. Added (dev, 2026-11-27): the dev's own change to the default keyboard.ini (jump, both lane changes, both hands, ammo check and reload, the nine readouts and the buffer's copy and export all :repeat) gets its own changelog entry, "Made it so holding the jump, lane change, hand, ammo, reload, readout and speech buffer copy and export keys now repeats them at your keyboard's repeat rate.", and keyboard_and_joystick.txt a sentence near the top of the keyboard list: "Most keys repeat while you hold them, at your keyboard's repeat rate, and you can change any key's trigger in the keyboard tab of the settings menu." Dev: "Yes. save that for the docks."
