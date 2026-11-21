---
name: project_free_run_shop_plan
description: SETTLED (2026-11-21, 2.8's sixth entry): the player shop opens in free runs, spending the run's temporary gold, with a new modify player gold console item up to 1,000,000; 2 sections; Q&A log
metadata:
  type: project
---

# Free run shop plan

The dev's idea: the player shop should open in free runs, as it does in debug runs. Nothing gets built until this plan is settled and committed.

## How things stand

- shop_available() in shop_menu.nvgt leaves free runs out, and that's the only thing keeping the shop from them.
- A free run already uses run_coins: shown_coins() reads it, spend_coins() takes from it, reset_run() clears it, and nothing reaches saved coins or the statistics, as stats_counting is false.
- free_ask_number() in freebelt.nvgt reads at most 6 digits, so a number box tops out at 999,999.

## Settled

- The shop opens in free runs on slash or F8.
- A new modify player gold console item gives, sets or takes the run's gold.

## Open questions

1. SETTLED: modify player gold has give, set and take like the other modify items. Set takes 0 to 1,000,000, give and take 1 to 1,000,000, take stops at 0, and give can build the balance past that. It's listed first among the modify player items, once you've started running. Build note: free_ask_number() must read 7 digits instead of 6 for 1000000 to pass; its range check still rejects anything too big for the other boxes.
2. SETTLED: 2.8's sixth entry: "Added the player shop to free runs, with a modify player gold option in the console, so you can try anything it sells without touching your saved gold coins."

## Sections

1. The shop and the gold: shop_available() includes free runs, modify player gold joins the console with give, set and take, and free_ask_number() reads 7 digits.
2. Docks: the changelog entry, player shop, gold packs, free runs, keyboard and joystick and any other documents saying the shop isn't in free runs, then template.lng and english.lng.

## Q&A log

- Dev (2026-11-21): "You know how the debug runs have the shop enabled? I wish the free run also had it enabled. WOuld this work since your gold is not saved if you quit?" Claude: yes, it's safe, and recommended a modify player gold item too, since a free run starts with 0 gold.
- Dev: "Oh I forgot about that. I do want both if possible. We can start a small plan for this."
- Q1, dev: "Will it have give/set/take like the other modify options do?" (yes), then: "I want the input cap to be 1000000, not 999999".
- Q2: the changelog wording? Dev: "That works for me." Plan SETTLED.
- Section 1 BUILT (2026-11-21): shop_available() includes free runs, free_set_gold() and the modify player gold item in freerun.nvgt, free_ask_number() reads 7 digits. Tests: 1 of 3 (modify player gold), 2 of 3 (buying in a free run), 3 of 3 (the balance stays separate, and practice has no shop) all PASSED.
