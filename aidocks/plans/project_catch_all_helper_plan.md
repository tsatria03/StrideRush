---
name: project_catch_all_helper_plan
description: SETTLED (2026-11-21, 2.8's first entry): the master helper, a seventh, premium helper at 15,000 gold coins that does all six helpers' jobs, sold alongside them; 2 sections; Q&A log
metadata:
  type: project
---

# Catch-all helper plan

The dev's idea for 2.8: one helper that does every job the six helpers do. Follows [[project_helpers_plan]]. Nothing gets built until this plan is settled and committed.

## What it does

While it's on, it does all six jobs, by the same rules: claps at animals, unlocks and opens real doors with your first key, opens and repairs floor breakers, switches off force fields, picks up items in your lane, and grabs and climbs ladders. Its limits are theirs too: no protection from damage, a lane key still knocks you off a ladder, it uses no items but keys, and it's gone when the run ends or you fully die.

## Open questions

1. SETTLED: master helper, listed after ladder helper in the specials.
2. SETTLED: 15,000 gold coins (the six together cost 23,000).
3. SETTLED: while it's on, all six jobs are done whatever the others are set to; each keeps its own on or off setting, which can still be changed and applies again when the master helper is switched off. Having both on never doubles a job.
4. SETTLED: the same as the other helpers: bought in endless and debug runs, given, set or taken in a free run, absent from timed and practice runs, its work counts in statistics and achievements, and it lasts through lost lives until the run ends or you fully die.
5. SETTLED: it shares helperon.ogg and helperoff.ogg with the other helpers, so no new sounds are needed.
6. SETTLED: the first entry of 2.8: "Added a master helper to the player shop's specials, which does the jobs of all six other helpers at once."

## Sections

1. The master helper: its price and place in the specials, free run give, set and take, and all six jobs done while it's on, with each helper keeping its own setting.
2. Docks: open "New in 2.8." with the changelog entry and bump build/version.txt to 2.8, update the player shop and inventory documents, then template.lng and english.lng. Its own document, master_helpers.txt, goes into game/ in this section; the draft is held in the session scratchpad until then.

## Q&A log

- Dev (2026-11-21): what if, instead of 6 individual helpers, one item called hand helper did all their jobs? What are the pros and cons?
- Claude recommended keeping the six and adding it as a seventh, premium item. Dev: "I didn't think about that option. A catch all sort of deal." Asked what it would do, and wants another name that keeps the helper suffix.
- Q1: the name? Claude recommended master helper. Dev: "I like that. Master helper sounds good."
- Q2 raised by Claude: 20,000 gold coins saves 3,000 over buying all six, is about 100 gold packs on easy or 20 on chaos at their average amounts, and reaches the top shop_coin_steps band, so a single purchase plays coin100000.
- Q2 answer, dev: "I think I want it to be 15k gold". At 15,000 a single purchase is in the coin50000 band, about 75 gold packs on easy or 15 on chaos at their average amounts.
- Q3, dev: "Oh yes." Then asked what happens with a master helper and a ladder helper both on. A: the job runs once, at the same pace, and the ladder helper carries on alone if the master helper is switched off.
- Q4: the same rules as the other helpers everywhere else? Dev: "Yes for the first one." The dev then asked to hear Q3 again, so it isn't settled yet.
- Q3 asked again in full. Dev: "yes. That works."
- Q5: the same sounds, or its own? Dev: "Use the same helper sounds."
- Q6: the changelog wording? Dev: "That's goood. Please create a master_helper dock file covering every helper job as a hole, and what each one covers." Drafted as master_helpers.txt (plural to match the other helpers at the dev's request), then moved out of the repo to the session scratchpad, as the dev wants it added in section 2 with the other dock changes. Plan SETTLED.
- Build note: helpers_update() and hand_check() need a "job is being done" check (the helper or the master helper on), while the inventory's on or off wording keeps reading each helper's own setting.
