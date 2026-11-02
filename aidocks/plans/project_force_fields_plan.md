---
name: project_force_fields_plan
description: IN DISCUSSION (started 2026-11-02) - force fields as the next obstacle type after the first build; how they're passed, warned, hit and placed; Q&A log
metadata:
  type: project
---

Status: IN DISCUSSION, started 2026-11-02 on top of a785be4. The dev chose force fields as the next feature because "they are sort of like hazards". No code until the plan is settled and the dev gives a go-ahead ([[feedback_plans_record_qna]]).

Already recorded elsewhere:
- Obstacles plan ([[project_obstacles_plan]]): force fields were parked as a potential hand-interaction obstacle. The idea was a full-height field that stays on, switched off with an interact hand at a switch placed before it. Hitting it while on plays hit and costs lives, with the amount decided later. A plain on/off timing gate was rejected, because the belt controls speed, so arriving while it's on or off would be luck.
- End-of-run plan ([[project_end_of_run_plan]]): a force field hit plays its hit with misc/player/hit (only when survived); a fatal one plays its hit through p with misc/player/death, then the tile's fall, the same as spikes and mines.
- Controls ([[project_controls_plan]]): the hands are Tab or A (left) and Enter or D (right), bound in keyboard.ini but unread so far.

Sounds (rescanned 2026-11-02):
- objects/traps/force_fields/electric and electric2: on, off, hit. CORRECTED by the dev (2026-11-02): on and off are both LOOPS, each a distinct sound for the field's state. on loops while the field is active, and off loops while it's inactive. So a field is always heard, positioned, and its loop tells you which state it's in. Claude had wrongly read them as oneshots because there's no file named loop.
- Code consequence: one kept looping handle per field. Changing state destroys one loop and starts the other at the same x, the way mine.nvgt starts its ticking loop ([[project_audio_model]]).
- objects/interaction/switches/switch: press.
- misc/player/hit and death exist for the hit and death.
- misc/trap/force_fields/warn1 to warn5 (added by the dev, 2026-11-02): the force field's own countdown cues, distinct from the hazard set.

Q&A log:
- Q: How does the player get past a force field: switch it off with a hand on cue, or jump over it like a hazard? (Asked 2026-11-02; Claude recommended the hand.) The dev's first reply corrected the sounds (on and off are state loops). A: a switch (dev, 2026-11-02). You click it off with a switch, and you hear the off loop as you pass it. So the field is ahead on its on loop; pressing a hand at the switch plays switch/press and swaps the field to its off loop; you then run past the inactive field hearing off. Not jumped.
- Q: Which hand works the switch: either hand, or one particular hand? (Asked 2026-11-02; Claude recommended either hand.) A: either hand (dev, 2026-11-02), as a game-wide rule for hands: either hand opens doors and turns off force fields. The switch press plays in 2d, panned to the hand used, so you hear which hand pressed it: left hand on the left, right hand on the right. Door openings do the same. Planned approach: play it a small offset from the player (me_x minus or plus an offset, tunable), so the pan comes from the 2d position.
- Q: When can the switch be pressed: only on a countdown's final cue, or any time within a short reach window before the field? (Asked 2026-11-02; Claude recommended a reach window matching the countdown steps.) A: pending.
