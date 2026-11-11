---
name: project_combined_obstacles_plan
description: STARTED, NO QUESTIONS YET (2026-11-10, for 2.0) - combined obstacles, two (three on chaos) at once needing actions in a row; background, the explained design and the questions to ask; Q&A log
metadata:
  type: project
---

Status: STARTED (2026-11-10), questions not asked yet. The dev (2026-11-10): "Pleast start this plan, Do not ask me any questions yet. I still want to look at your other suggestions". Ask the open questions below one per turn once the dev says to go on.

Background:
- One of Claude's 2.0 suggestions ([[project_suggestions]]), liked by the dev ("es. Deffenatly") and copied to the todo list's open section: "Add combined obstacles, two at once that need two actions in a row, such as crouching under a projectile and then jumping a spike."
- The dev asked whether it's already a thing: not really. next_gap() in spawner.nvgt leaves room for a hazard's ledge, a random floor stretch and the next obstacle's full countdown, so every countdown starts after the last obstacle is passed, with floor between. At high speed obstacles come quickly, but always one finished before the next is heard. The nearest things today: barrier pairs (two at once, one action), items beside obstacles (a choice), a force field's throw. Combined obstacles overlap on purpose: the second part's countdown runs while the first arrives.

The design as explained to the dev (2026-11-10), not yet confirmed point by point:
- In play: one obstacle with two parts, such as a projectile reaching you, then a spike a step later: crouch, then jump straight after. The skill is sequencing.
- Pairs that fit: projectile then spike (crouch, jump); force field then wall (hand, weapon); mine then barrier (jump, lane switch); animal then hazard (clap, jump).
- Fairness: each part keeps its own countdown, layered or one after the other, perhaps a short combined cue as a chain starts; the gap between parts, in steps, never below what the actions need, even at top speed; only obstacles already met that run.
- Gaps by action: hands, lane switches and weapon swings are instant, so the next part can follow almost at once; a jump keeps you in the air a few steps, so the next part comes after landing; a crouch lasts while held, so the next part can follow just after the projectile passes.
- Damage: each part hurts on its own with its normal damage, so a half-right attempt costs only the part missed.
- By level: rare with a comfortable gap on easy; commoner and tighter on harder levels.
- Three-part chains (dev asked, 2026-11-10: "it can be up to 3 at a time right? If so, how does that work?"; answered "Perfect."): chaos only as suggested. Examples: force field, wall, hazard (hand, weapon, jump); projectile, spike, barrier (crouch, jump, lane switch after landing); animal, mine, projectile (clap, jump, crouch after landing); wall, barrier, spike (weapon, lane switch, jump). Never the same action twice in a row (that's two ordinary obstacles), nothing impossible given a jump's air time (a hazard landing straight into a spike), never two barriers in one chain, so a lane stays open.
- Elsewhere: a "combinations" practice choice at the end of the practice chain; a statistic for combinations cleared in full; achievements, perhaps for clearing a number in one run without a hit.

Open questions, to ask one per turn later:
1. Which obstacle combinations are allowed: the listed pairs only, or any pair that's physically possible?
2. How often per level (easy to chaos), and whether they replace an ordinary spawn or come on top.
3. The minimum gap between parts, per action, at top speed.
4. Three-part chains: chaos only, insane too, or none.
5. A combined cue at the start of a chain: yes or no, and its sound (sounds must exist first, [[feedback_sounds_before_features]]).
6. When they join on easy to insane: from the start, or once both parts' types have joined the schedule.
7. Practice: a "combinations" choice, where it sits in the unlock chain, and its goal.
8. Statistics and achievements: which ones.
9. Learn sounds: does the combined cue get an entry.
10. Debug options: a combinations spawn choice.

Q&A log:
