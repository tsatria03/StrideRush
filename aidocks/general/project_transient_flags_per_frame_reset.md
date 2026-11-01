---
name: project_transient_flags_per_frame_reset
description: Lesson from SimpleFighter - if a per-frame function rewrites player capability flags, a transient change (stun, freeze) only lasts one frame unless re-asserted after it each frame
metadata:
  type: project
---

In SimpleFighter, update_character_settings() rewrote the whole capability-flag set every frame, before stuncheck(). So a stun that set a flag false once was undone the next frame, and stuns never really froze the player until 15.0 made stuncheck() hold the flags every frame.

**Why:** Stride Rush will have similar per-frame state (can jump, is running, paused). Any temporary lockout, such as a stumble after clipping a hazard, must be held each frame by a check that runs after any per-frame reset, not set once by the event that starts it.

**How to apply:** when designing the game loop, put the reset first and the timed-effect holds after it. Reference: [[reference_simplefighter_readonly]].
