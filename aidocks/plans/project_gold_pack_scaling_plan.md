---
name: project_gold_pack_scaling_plan
description: SETTLED (2026-11-21, 2.8's fourth entry): in endless runs, gold packs pay 10 percent at the start of a run and rise to the full amount at the level's top speed, decided on opening, so restarting isn't the best way to earn; 2 sections; Q&A log
metadata:
  type: project
---

# Gold pack scaling plan

A forum user reported that gold coins are saved as soon as a pack is opened, so you can collect a few packs early in a run, quit and repeat. The dev asked whether that's cheating. Nothing gets built until this plan is settled and committed.

## How things stand

- use_goldpack() in goldpack.nvgt pays a random amount from gold_pack_min_coins to gold_pack_max_coins by level, the same at any point in a run, and saves at once.
- Today's amounts: easy 100 to 300, medium 200 to 600, hard 300 to 900, insane 400 to 1,200, chaos 500 to 1,500.
- The belt starts at difficulty_start_times (500, 450, 400, 350, 300 ms) and drops 10 ms every 10 seconds to difficulty_top_step_times (200, 150, 100, 75, 50 ms). That takes 5 minutes on easy, medium and hard, about 4 minutes 40 seconds on insane, and about 4 minutes 10 seconds on chaos.
- Read step_time, not current_step_time(), so Slow Motion and Rush Hour don't change a pack's pay.

## Open questions

1. SETTLED: a pack pays 10 percent at the start of a run, rising steadily to 100 percent at the level's top speed.
2. SETTLED: the amount is decided when you open a pack, so saving packs for later is a real gamble, as unopened packs are lost when the run ends.
3. SETTLED: debug and free runs keep paying easy's full 100 to 300 with no scaling, as their coins are temporary and their speeds are chosen by hand. Only endless runs scale.
4. SETTLED: 2.8's fourth entry: "Made it so gold packs now pay less early in a run and more as the belt speeds up, reaching their full amount at your level's top speed."

## Sections

1. The payout: in an endless run, use_goldpack() scales its random amount from 10 percent at the level's start speed to 100 percent at its top speed, read from step_time when the pack is opened, with the percentages in tuning.nvgt. Debug and free runs are unchanged.
2. Docks: the changelog entry, gold packs, player shop and any other documents naming a pack's amounts, then template.lng and english.lng.

## Q&A log

- A forum user's report (2026-11-21): collecting gold packs, leaving and repeating keeps the coins. Dev: "Do you think this might be cheating?" Claude: not cheating or a bug, since saving is by design, but a loophole, as restarting is the safest way to earn. Claude advised against losing coins on quitting, since dying on purpose gets around it, and recommended paying more as a run goes on.
- Dev: "Let's plan that one."
- Q1, dev: "Do you think it could start at 5 or 10percent at the start?" Claude: 10, since 5 pays only 5 to 15 on easy, and the two are nearly the same after a minute or two (28 against 24 percent after one minute on easy). At 10 a start pays 10 to 30 on easy up to 50 to 150 on chaos. The cost is that players who die early earn very little. Dev: "Yes. I do."
- Q2, dev: "It should be decided upon opening it like you said".
- Q3: debug and free runs without scaling? Dev: "I agree with that."
- Q4: the changelog wording? Dev: "That's good." Plan SETTLED.
