---
name: project_game_design
description: Stride Rush core design as stated by the dev - basic 2d side-scroller, no lane switching, jump on cue over approaching hazards or die
metadata:
  type: project
---

Settled by the dev on 2026-11-01:

- Style: a basic 2d side-scroller. The player rides a one-way belt to the right; movement is automatic.
- No lane switching. Lanes may come later as an expansion, so don't design them out, but don't build them now.
- Hazards: as an obstacle approaches, the player must jump on cue. Failing to jump means death.
- Running: a game-script timer advances the player and plays a oneshot footstep on each step. The step rate speeds up over time.
- Extensibility: a simple core that users can expand in code.
- Sounds follow ToyMania's layout ([[reference_toymania_readonly]]), not SimpleFighter's.
- Later, when the dev asks: ToyMania's session and lifetime scoring, and possibly its difficulty modes.

**Why:** the dev wants to build it one step at a time, not all at once.

**How to apply:** propose one small step, wait for the go-ahead ([[feedback_confirm_before_implementing]]), and record each feature plan in aidocks/plans/. Open questions (death handling, lives, map source, the jump model) are still undecided. Related: [[project_runner_overview]].
