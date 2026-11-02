---
name: project_obstacles_plan
description: IN DISCUSSION, NOT BUILT - which obstacles are jumped over, ducked under, or need another action (weapon, hand, later lane change); proposed three-height model; Q&A log
metadata:
  type: project
---

Status: in discussion, started 2026-11-01. The dev says they always get confused between duck and jump obstacles, and which obstacle fits which, and the same will be true of turning (lane changes) later. This plan settles that. No code until the go-ahead ([[feedback_plans_record_qna]]).

Model AGREED by the dev ("exactly right", 2026-11-01): every obstacle sits at one of three heights, and the height decides the action.
- Low: on the ground with open space above it. Jump over it with Up. Examples: pits and floor gaps, fire, spikes, mines, logs and low barriers.
- High: overhead with a gap underneath. Duck under it with Down, held. Examples: low beams, pipes, overhanging signs, swinging blades, projectiles at head height, a low ceiling (crawlspace).
- Full height: blocks from floor to top, so neither jump nor duck works. It needs another action:
  - walls or crates: smash them with a weapon
  - doors and gates: open them with an interact hand
  - later, with lanes: an obstacle filling the whole lane means changing lanes (the turn cue).

First playable build: jump-over (low) and duck-under (high) obstacles only. Each full-height type is added when the hand action that beats it is built: weapons for smashing, interact hands for doors, lanes for turning (dev, 2026-11-01).

The dev's shorthand for the five actions: feet versus hands. Feet means jump and duck. Hands means open (doors), hit (weapons) and turn (lane changes).

Duck timing (from the controls plan): ducking auto-unducks after about 1 to 2 seconds, and releasing early unducks sooner but risks smashing into the overhead obstacle. So a duck-under obstacle must be short enough to pass within the duck time at the current speed. At 500 ms per step, 2 seconds covers 4 tiles; at 50 ms it covers 40 tiles. Jump-over obstacles likewise must fit inside the jump's air time (in the friend's template about 1 second, so 2 tiles at 500 ms or about 18 tiles at 50 ms).

Sources for obstacle ideas: [[reference_simplefighter_builder_objects]] and [[reference_friend_runner_template]].

Q&A log:
- Q: (dev) Ducking is held, but not forever? A: It auto-unducks after about 1 to 2 seconds; releasing early unducks sooner but raises the chance of smashing into something (dev, 2026-11-01). Recorded in [[project_controls_plan]].
- Q: (dev) Help sorting which obstacles are jumped vs ducked (and turned, later). A: Claude proposed the three-height model above. The dev agreed: "Exactly right" (2026-11-01).
- Q: (dev) So there are three ways to avoid an obstacle, depending on its type? A (Claude): three heights, but five actions. Low means jump and high means duck, each a single action. Full height covers three actions depending on the obstacle: smash it (weapon), open it (hand), or change lanes (later). Since weapons, hands and lanes all come later, the first playable build only needs low and high obstacles.
- Q: (dev) So five ways: hands and feet? A: Yes, the dev's grouping (2026-11-01). Feet: jump and duck, for low and high obstacles. Hands: opening doors, hitting with a weapon, and turning (lane changes), for full-height obstacles.
- Q: First playable build with only jump-over and duck-under obstacles, full-height ones added later? A: Yes, "of course" (dev, 2026-11-01).
