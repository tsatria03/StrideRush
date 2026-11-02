---
name: project_run_plan
description: SETTLED, NOT BUILT (warning cues deferred) - the core run of Stride Rush (Start game begins a run, a step timer moves the player right one tile per tick with a oneshot footstep, the tick speeds up over time); includes a Q&A log
metadata:
  type: project
---

Status: SETTLED 2026-11-01, with warning cues deferred until the dev finds sounds. The timing numbers are defaults to tune by playtest. No code until the dev gives a go-ahead ([[feedback_plans_record_qna]]).

Scope: what happens from Start game until a run ends. That covers the belt, the step timer, footsteps, the speed-up curve, and the run's overall shape. Out of scope for this plan: obstacles and jump/duck ([[project_game_design]]), death details, weapons, items and scoring.

Settled so far:
- Run shape: endless. A run goes until the player dies. Levels (fixed-length tracks, as in the friend's template) are a later addition, not part of this plan.
- SimpleFighter's aircraft turbulence warning is not used as a template.
- Speed-up: timer-based. Every so often (for example every 10 seconds) the step interval shrinks by a set amount, down to a minimum. This is the dev's original description, and it was chosen over the friend's template's per-step "minus 1 ms every footstep". The run keeps getting faster for the whole run, but the step interval never drops below 50 ms (dev, 2026-11-01). Default test values, all tunable: start at 500 ms per step, take 10 ms off every 10 seconds, floor at 50 ms. That reaches the floor after 7.5 minutes, and each 10 ms cut matters more near the end (about 2% at 500 ms, about 20% at 60 ms).
  - CHANGED (dev, 2026-11-02): the speed is now capped at 100 ms, not 50 (min_step_time = 100). The run reaches the cap after about 6.7 minutes.
- Warning cues: based on the friend's template, step-synced. Each obstacle has its own looping positioned sound, plus a short countdown, one cue per footstep, in the last few steps before it ([[reference_friend_runner_template]]).
  - Each action gets its own distinct cue set: jump, duck, and lane change. Lane change is for later, but its cue set is reserved now. The player must be able to tell from the warning alone which key to press (for example rising pitch for jump, falling for duck).
- Countdown timing, PROVISIONAL until playtested: the warning starts a fixed time before the obstacle (about 1.5 s), but never less than 5 steps out. Five cues are spaced evenly through that window, and the last one means "act now". At 500 ms per step the cues land about on footsteps; at 50 ms they spread over about 30 steps. Every number here is a tunable value.
- Still open on cues: confirming the distinct final "act now" cue.
- Music and ambience: each run picks a random music track from sounds/objects/audio/musics/ and a random ambience from sounds/objects/audio/sources/ (paths updated after the dev's 2026-11-01 sound reorganization), found at runtime like the platforms (dev, 2026-11-01). Page Up and Page Down set music volume; Home and End set ambience volume ([[project_controls_plan]]).
- WARNING CUES DEFERRED (dev, 2026-11-01): the game won't have any warning cues until the dev finds the proper sounds for them. The cue design above (per-action cue sets, timing, the act-now cue) is kept for then, but isn't built. Build obstacles without countdown cues for now.
- Footsteps: a oneshot footstep plays on EVERY step, at any speed, even 20 per second at 50 ms. Never thin them out (dev, 2026-11-01). Because they're oneshots, overlapping clips are fine: play-and-forget, never keep a handle ([[project_audio_model]]).
- Footstep sounds come from platform tile folders. The dev already has dozens: SimpleFighter's sounds/decompiled/builder/construction/platforms/ holds 396 tile folders (concrete, dirt, grass, metal, snow, water, wood and so on). Each holds step1-5, land, fall, hurt and death. In Stride Rush they go under sounds/objects/construction/platforms/<tile>/ ([[project_sound_layout]]), picked with a *step* wildcard so a random step1-5 plays each step.
- Ground surface: switches between random platforms during a run. Variety is the whole point of the game (dev, 2026-11-01).
  - The dev will copy only their favorite platforms into Stride Rush, not all 396. So code must discover whatever tile folders exist with get_pack_sound_folders("objects/construction/platforms/*") and pick at random from them. Never hard-code a tile list. Exception: the "ledge" tile is reserved for the edges around hazards, so the random picker must skip it ([[project_obstacles_plan]]).
  - Stretch length: a random length within a range, counted in tiles (distance), not time. About 50 to 200 tiles, tunable and settled after playtesting. Because it's counted in distance, surfaces switch more often at high speed.

Reference: the friend's runner template is the closest model, with its auto-step loop, shrinking interval, 5-step hazard countdown and level tracks ([[reference_friend_runner_template]]). Also SimpleFighter's conveyor belt (one tile per speed interval, never reverses; [[reference_simplefighter_builder_objects]]) and its step and footstep code ([[reference_simplefighter_movement_jump]]).

Q&A log:
- Q: Is a run endless, or a series of fixed-length levels? A: Endless for now; levels can come later (dev, 2026-11-01).
- Q: (dev note, same answer) Use SimpleFighter's aircraft turbulence warn-alarm-pass sequence as the obstacle-warning template? A: No, it isn't needed (dev, 2026-11-01).
- Q: Speed up on a timer (a steady pace) or per step (the template's minus 1 ms each footstep, which accelerates faster the quicker you run)? A: The timer (dev agreed with Claude's recommendation, 2026-11-01).
- Q: Should jump and duck obstacles have clearly different countdown cues? A: Yes, and lane changes too: different warning cues for jump, duck and lane changes (dev, 2026-11-01).
- Q: (dev) What's the top speed in the friend's template, or does it plateau? A (Claude, from the code): it plateaus at once. Only lvl1 loads, and its floor (500 ms) equals the start, so the whole run stays at 500 ms. The unloaded levels would cap at 450 down to 50 ms, reaching each cap within about 50 steps.
- Q: Fixed 5-step countdown with a top-speed cap around 200 ms, or a scaling countdown? A: The dev wants the run to get faster and faster, but never below 50 ms. Since the 200 ms cap is out, a fixed 5-step countdown would shrink to 0.25 s of warning at 50 ms, so the countdown must scale to keep the warning time long enough.
- Q: Five evenly spaced cues over a fixed warning time (about 1.5 s), never starting less than 5 steps out? A: Recorded as PROVISIONAL. The dev isn't sure and needs to playtest the mechanic before deciding (2026-11-01). Build it with the warning time, cue count and minimum steps as tunable values, and settle them after testing.
- Q: At top speed, should footsteps play every step, or thin out to every second or third step? A: Every step, regardless; they're oneshots (dev, 2026-11-01). The dev also pointed to the many platform tile folders in SimpleFighter's sounds (396 found).
- Q: One surface per run, or change in stretches? A: Switch between random platforms; variety is the whole point (dev, 2026-11-01). Only the dev's favorite platforms will be copied in.
- Q: How long does each stretch of ground last? A: A random length in a tunable range, about 50 to 200 tiles, counted in distance (dev agreed, 2026-11-01).
- Q: Default speed numbers to test with: start 500 ms, minus 10 ms every 10 s, floor 50 ms? A: Yes (dev, 2026-11-01).
- Q: Random music track and random ambience per run, from objects/sources/tracks and ambiences? A: Yes (dev, 2026-11-01). Those folders later moved to objects/audio/musics and objects/audio/sources.
- Q: Should the last countdown cue be a distinct "act now" sound? A: Not answered. The dev deferred all warning cues: there will be none until they find the proper sounds (2026-11-01).
