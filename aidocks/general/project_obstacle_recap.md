---
name: project_obstacle_recap
description: Every obstacle at 2.2 (2026-11-13) - what it is, how to get past it, what it does if it catches you (full chaos damage), plus combinations, slides, trampolines and the patterns that tie them together; the dev's approved player-level reference ("It's perfect!")
metadata:
  type: project
---

Written 2026-11-13 at 2.2 (5 of 10, after floor breakers, vehicles and timed runs), approved by the dev ("It's perfect! I love it. Please save this as a memmory file."). A player-level reference: what each obstacle is and how it's beaten. The numbers are the full amounts (chaos); easier levels take less (difficulty_damage_percents). The code and readme are the authority if they drift: check tuning.nvgt and sdr/docks/readme.txt before quoting a figure. Related: [[project_difficulty_comparison]] (the levels side by side), [[project_version_history]] (when each came in), [[project_sound_layout]] (where their sounds live).

Obstacles, roughly in the order they join an endless run (chaos brings them all at once):

Hazards: pits, fire, lava, water, quicksand and electricity, across the whole belt.
- Get past: jump. A five-step ledge counts down to it, and at slow speeds you jump on the last cues.
- If it catches you: falling in ends the run outright, whatever your health or shield.

Spikes: blades swinging on their own rhythm, across the belt.
- Get past: jump over them.
- If it catches you: 20 health.

Mines: they appear, then light up and tick as you get close.
- Get past: jump over them.
- If it catches you: 60 health.

Projectiles: missiles flying at head height, twice your speed.
- Get past: crouch so you're down as it arrives. Jumping won't help.
- If it catches you: 40 health.

Force fields: a humming barrier across the belt.
- Get past: press either hand during its countdown to switch it off, up to the last half second at top speed.
- If it catches you: 30 health, and it throws you 5 steps forward.

Animals: birds and dogs, each with its own call.
- Get past: clap, both hands together, during its countdown.
- If it catches you: 10 health.

Fake walls: glass windows at an odd pitch.
- Get past: break them with your weapons. Your reach is about 2 seconds ahead, and they get tougher as you speed up.
- If it catches you: 50 health.

Fake doors: like a real door but at an odd pitch, and jammed shut.
- Get past: break them with your weapons; about twice as tough as a fake wall.
- If it catches you: 70 health.

Real doors: locked doors marking each faster stretch. A key always comes earlier in the stretch.
- Get past: unlock it with a key from your inventory once it's close, then open it with a hand in the last few steps, and it carries you through.
- If it catches you: 70 health.

Real walls: unbreakable walls at normal pitch, with a ladder 5 steps before each.
- Get past: grab the ladder with a hand during its countdown, then climb hand over hand, alternating hands at a steady pace, until you're over.
- If it catches you: missing the grab, the same hand twice or stalling collapses the ladder (60); a lane switch or climbing too fast drops you off it (40); either way you then crash into the wall for 50 more.

Floor breakers: a hole of air across every lane.
- Get past: press a hand during its countdown to open the corridor, then at the edge rebuild the hole with alternating hands at the ladder's pace, 3 to 4 pieces on easy up to 7 to 8 on chaos.
- If it catches you: reaching it unopened, or any repair mistake, drops you through and ends the run outright.

Barriers: boulders, firewalls and power lines, each in one lane, sometimes two side by side, never all three. (Cars were barriers once; they're vehicles now.)
- Get past: be in another lane when it arrives. Nothing else works.
- If it catches you: 80 health.

Winds: gusts in one lane that follow you a lane every three quarters of a second.
- Get past: switch lanes after its last move. Switching early just brings it after you.
- If it catches you: 5 health and a shove one lane over. Crouching as it hits braces you, so you aren't shoved.

Vehicles: cars, small and big, that drive at you in one lane and follow you a lane every second.
- Get past: shoot them down while they're in your lane, or switch lanes after their last move.
- If it catches you: half a second after lining up with you, a burst of 5 quick shots down its lane, 5 health each, then a 2 second wait (step out of its lane as it lines up and the burst misses); about 2 steps out it stops shooting and rams you for 40.

Things that come with the obstacles:
- Combinations: two obstacles close together that need two actions in a row, such as crouching then jumping. More common on harder levels; never real doors, real walls, winds, slides or trampolines.
- Slides: belt-wide, carrying you at double speed for 2 to 4 seconds. You pass harmlessly through everything and catch any item in your lane, but can only switch lanes while on one.
- Trampolines: lane or belt-wide; a good one launches you on a long flight over everything ahead, a worn one (odd pitch) only gives a normal jump; you avoid a lane one by being in another lane.

Patterns worth knowing:
- Odd pitch means break it: fake walls and fake doors, and worn trampolines warn you the same way.
- Lane obstacles (barriers, winds, vehicles) only play their countdown while they're in your lane.
- Barriers are the lane obstacles that stay put; winds and vehicles follow you, and vehicles are the only ones you can also destroy.
- Hands work things: force fields, doors, ladders, floor breakers. Weapons break things: fake walls, fake doors, vehicles.
- Only hazards and floor breakers end a run outright. Everything else takes health, and your shield takes it first.
