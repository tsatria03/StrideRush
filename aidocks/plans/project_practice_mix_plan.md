---
name: project_practice_mix_plan
description: SETTLED (2026-11-12, for 2.1; 2 sections) - a practice choice bringing every obstacle you've unlocked at random, at your chosen speed, with practice's deaths, hints and retry; Q&A log
metadata:
  type: project
---

Status: SETTLED (2026-11-12), waiting for the dev to commit it before Section 1. 2.1 at 5 of 10.

Background:
- Suggestion 20 in [[project_suggestions]] (2026-11-12): "A practice mix: a practice choice, once everything before it is open, bringing every obstacle you've unlocked at random, at the chosen speed, with the same deaths, hints and retry as other practice; a warm-up before an endless run." The dev: "I like this one the best. How would this work?" LIKED, copied to the todo list.
- Today's practice ([[project_practice_guidance_plan]], [[project_ladders_plan]]): 16 choices in an unlock chain, trampolines last with no goal; each run brings one obstacle (or its fixed mix: mixed doors, mixed walls, combinations, trampolines with obstacles between) at a fixed speed with chaos's spacing; 1 life and 1 shield, practice deaths with retry practice; hints 5 per kind per run in the practice buffer; weapons only where needed; no items but keys for real doors.

Q&A log:
- Claude described it (the last practice choice; a chosen speed; each spawn a random unlocked obstacle, combinations, trampolines and real doors with keys included; practice's lives, shield, spacing, weapons, hints, deaths and retry; no end and no goal). Q: when it opens: with trampolines, once everything else is open (all 16 kinds), or from the start bringing only what's unlocked? (Asked 2026-11-12; Claude recommended once everything else is open.) A: "I'd say once everything else in the set is unlocked." (dev, 2026-11-12). The dev asked for a good name.
- Q: The name: mixed obstacles (like mixed doors and walls), everything, warm up, or random mix? (Asked 2026-11-12; Claude recommended mixed obstacles.) A: "I like mixed obsticals the best. What's the unlock description" (dev, 2026-11-12). practice choice "mixed_obstacles", read "Mixed obstacles".
- Claude proposed its lock line as trampolines' (after 5 combinations) and a joint announcement. The dev: "Mixed obsticals should only unlock after trampolines." Claude restated: trampolines get a goal of their own; offered "take 5 trampoline flights" (good trampolines; trampoline_flights) or any kind (worn bounces too, a mistake rewarded), recommending flights; lock line "Mixed obstacles. Unlocked after you take 5 trampoline flights."; no saves have trampoline progress, so nobody needs a one-time check. A: "That's exactly what I meant. And yes, 5 trampoline flights works well" (dev, 2026-11-12).
- Q: Each spawn an equal pick among the kinds: hazards, spikes, mines, projectiles, force fields, animals, fake walls, fake doors, barriers, winds, real walls (with ladders), real doors (with keys before), combinations (a random pair), trampolines (any of the four); mixed doors and mixed walls covered by their parts; 14 kinds (Claude first said 15, corrected)? (Asked 2026-11-12; Claude recommended it.) A: "Yes. I agree with that." (dev, 2026-11-12).
- Q: Hints in mixed obstacles: one per kind (14 in all), the closing line once all 14 have been hinted, hits and missed keys starting them over until then; instead of 5 per kind (70)? (Asked 2026-11-12; Claude recommended one per kind.) The dev asked how 70 condensed into 5 would work; Claude walked through one per kind, and offered a total of 5 for the run. A: "I was confused for a second. I meant I want 1 per kind, not all 70 of them." (dev, 2026-11-12).

- Q: The rest as practice already works (1 life and 1 shield, practice deaths and retry; weapons drawn; the chosen speed with chaos's spacing; no items but keys before real doors; any environment, bringing the kinds it has; no goal of its own), the entry "Added mixed obstacles to practice runs, opened after you take 5 trampoline flights, bringing every kind of obstacle at random as a warm-up before an endless run.", and two sections? A: "Yes. This one needs testing, so I'll commit each section." (dev, 2026-11-12).

Settled design (2026-11-12):
- A new last practice choice, mixed_obstacles, read "Mixed obstacles". Trampolines get a goal: trampoline_flights, "take", singular "trampoline flight" (lock line "Mixed obstacles. Unlocked after you take 5 trampoline flights."). Mixed obstacles has no goal. The practice menu's count becomes "of 17".
- Each spawn an equal pick among 14 kinds, those the environment has themes for: hazards, spikes, mines, projectiles, force fields, animals, fake walls, fake doors, barriers, winds, real walls (with ladders), real doors (each with its key placed just before), combinations (a random pair, both orders), trampolines (any of the four).
- Hints: one per kind per run (14), the closing line once all 14 kinds have been hinted; hits and missed keys start them over until then.
- As other practice: 1 life and 1 shield, practice deaths with retry practice, weapons drawn, the chosen speed with chaos's spacing, no items but the keys before real doors, any environment.
- The 2.1 entry above (6 of 10).

Sections:
1. Mixed obstacles: the choice and the trampolines goal, the equal random pick, one hint per kind and its closing.
2. Docks: the readme's practice section, the entry, the todo item to finished, CLAUDE.md, the version history, this plan COMPLETE.
- Section 1 built (2026-11-12): practice.nvgt: mixed_obstacles last in practice_choices (17), trampolines' goal trampoline_flights with the verb take and the singular trampoline flight (practice_lock_reason() says "trampoline flights" for more than one), mixed obstacles keeping weapons, practice_env_ok() true for it; practice_spawn_id() to "practice_mixed"; spawner.nvgt: practice_mix_kinds() (the plain ten and trampolines if the environment has themes, ladders if ladders_ready(), real doors if doors and keys exist, combinations, choose_combo() finding a pair or the spawn skipped), an equal pick, a real door as its key then the door (practice_mix_door_next), keys one at a time in a random lane with no paired item; practice_hints.nvgt: one hint per kind, practice_mix_meet() marking kinds (trampolines as one, keys not a kind, a placed pair as combinations), the closing once all 14 are met and the last has passed you; restarts clear it too.
- Section 1 Tests 1 and 2 of 3 passed (dev, 2026-11-12): the menu, the trampolines goal and its unlock; the mix itself.
- Section 1 COMPLETE (dev, 2026-11-12): Test 3 of 3 passed too (one hint per kind, the closing line after all 14, restarts on a hit or missed key).
