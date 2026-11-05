---
name: project_game_design
description: Stride Rush core design as stated by the dev - a lane runner (the dev's term) with three lanes, heard from behind the runner, since 1.4 (a basic 2d side-scroller through 1.3), jump, duck or turn on cue past obstacles or die; weapons and interact hands
metadata:
  type: project
---

Settled by the dev on 2026-11-01:

- Style: a basic 2d side-scroller through 1.3. The player rides a one-way belt; movement is automatic. CHANGED in 1.4 (dev, 2026-11-04, [[project_lanes_plan]]): a behind-the-runner three-lane runner. NAME (dev, 2026-11-05: "I'd call this a lane runner, not a side scroller runner"): call it a lane runner wherever the game's style is described, never a side-scroller (except when describing 1.3 and earlier). The belt carries you forward, things ahead are heard in front and passed things behind (lower in pitch), and left and right mean only lanes.
- Lanes (first "no lane switching, don't design them out"): BUILT in 1.4. Three lanes, starting in the middle, switched with Left/Q and Right/E ("turning"). Every obstacle but barriers spans all three lanes and sounds straight ahead in any lane; barriers and the six inventory items sit in one lane; powerups span the belt.
- Hazards: as an obstacle approaches, the player must jump on cue. Failing to jump means death.
- Ducking (added 2026-11-01): Down or S, held, ducks under obstacles that need it. So obstacles come in jump-over and duck-under kinds. It was built as a crouch, not a slide, with no footsteps while crouched; no duck-under obstacles exist yet (their sounds don't).
- Later features: weapons (ToyMania-style, number row plus Space to fire, X ammo check and R reload) and left and right interact hands for doors and similar objects. The pause menu and the separate ambience and music volume keys were built in the first build. Full key list: [[project_controls_plan]].
- Running: a game-script timer advances the player and plays a oneshot footstep on each step. The step rate speeds up over time.
- Extensibility: a simple core that users can expand in code.
- Sounds follow ToyMania's layout ([[reference_toymania_readonly]]), not SimpleFighter's.
- Later, when the dev asks: ToyMania's session and lifetime scoring, and possibly its difficulty modes.

**Why:** the dev wants to build it one step at a time, not all at once.

**How to apply:** propose one small step, wait for the go-ahead ([[feedback_confirm_before_implementing]]), and record each feature plan in aidocks/plans/. The early open questions were settled and built in the first build (2026-11-02): death handling ([[project_end_of_run_plan]]), lives ([[project_obstacles_plan]]), no map source (obstacles are placed at random by the spawner), and the jump model (about 1 s in the air, contact checked only on arriving at a tile). Related: [[project_runner_overview]].
