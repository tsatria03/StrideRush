---
name: project_obstacles_plan
description: SETTLED FOR THE FIRST BUILD, NOT BUILT (duck-under, force fields and full-height types later) - which obstacles are jumped over, ducked under, or need another action (weapon, hand, later lane change); proposed three-height model; Q&A log
metadata:
  type: project
---

Status: SETTLED for the first build on 2026-11-01: jump-over hazards, spikes and mines, with placement rules. Still to come: duck-under (once its sounds exist), force fields with hands, and full-height obstacles. Game-over flow belongs to a later death/end-of-run plan. Started 2026-11-01. The dev says they always get confused between duck and jump obstacles, and which obstacle fits which, and the same will be true of turning (lane changes) later. This plan settles that. No code until the go-ahead ([[feedback_plans_record_qna]]).

Model AGREED by the dev ("exactly right", 2026-11-01): every obstacle sits at one of three heights, and the height decides the action.
- Low: on the ground with open space above it. Jump over it with Up. Examples: pits and floor gaps, fire, spikes, mines, logs and low barriers.
- High: overhead with a gap underneath. Duck under it with Down, held. Examples: low beams, pipes, overhanging signs, swinging blades, projectiles at head height, a low ceiling (crawlspace).
- Full height: blocks from floor to top, so neither jump nor duck works. It needs another action:
  - walls or crates: smash them with a weapon
  - doors and gates: open them with an interact hand
  - later, with lanes: an obstacle filling the whole lane means changing lanes (the turn cue).

First build (narrowed by the dev, 2026-11-01): jump-over obstacles only, built from the existing sounds in objects/traps/hazards, spikes and mines ([[project_sound_layout]]). Duck-under obstacles are added once their sounds exist. The rule, the same as the warning cues: nothing gets built until its sounds exist.

Per-type behavior (settled one type at a time):
- Hazards (objects/traps/hazards, every theme: chasm, chasm2, electricity, electricity2, electricity4, fire, lava, pit, quicksand, water, water2): running into any of them ENDS THE GAME regardless of lives (dev, 2026-11-01). Jump over them. Clips: a positioned loop while ahead, and fall on contact.
- Spikes (objects/traps/spikes: electric_ray, large_spike): cost 1 life. Running into one plays hit. Its death1-2 clips are for smashing it with a weapon later, like SimpleFighter's destroyable spikes. The loop plays while ahead; hurt is spare (dev, "exactly right", 2026-11-01).
- Mines (objects/traps/mines: mine, mine2, mine3): cost 2 lives. Jump over them like spikes and hazards (dev, 2026-11-01).
  1. spawn plays quietly when the mine appears ahead.
  2. light plays when the player gets within a few tiles (tunable), and the mine arms. It's a built-in warning that's allowed now because the sounds exist.
  3. loop is the armed ticking, positioned ahead.
  4. Running into it plays explode, then hit, and costs 2 lives.
  5. Jumped over, it stays behind and goes quiet.
- Force fields (objects/traps/force_fields: electric, electric2; clips on, off, hit): NOT in the first build. Recorded as a POTENTIAL hand-interaction obstacle for when interact hands are designed (dev, 2026-11-01).
  - Idea: a full-height field that stays on, switched off with an interact hand at a switch placed before it. The switch sound now exists: objects/interaction/switches/switch/press (dev added it, 2026-11-01). Hitting it while it's on plays hit and costs lives (amount to decide then).
  - Rejected as a plain on/off timing gate: the belt controls speed and the player can't wait, so arriving while it's on or off would be luck, not skill.

Placement (dev agreed, 2026-11-01): obstacles spawn ahead at random gaps. Each picks a random type (hazard, spike or mine) and a random theme folder within it, found at runtime. The minimum gap grows with speed, so there's always room to land from one jump and react before the next. The gap values are tunable.

Earlier plan for the first playable build: jump-over (low) and duck-under (high) obstacles only. Each full-height type is added when the hand action that beats it is built: weapons for smashing, interact hands for doors, lanes for turning (dev, 2026-11-01).

Hitting an obstacle (dev, 2026-11-01):
- The player has lives. Losing a life plays misc/player/life, and the run keeps going as if the obstacle had been cleared. No bounce-back and no restart.
- Running out of lives ends the game.
- Obstacles don't all cost the same. For example, a blade chops you for 1 life and the run continues, while falling into a pit ends the game no matter how many lives are left.
- Each obstacle type's behavior is to be discussed one type at a time.
- Life cost: each obstacle type has a tunable number of lives it costs, so one obstacle can cost several, plus a special value meaning "ends the game regardless" (pits). Agreed by the dev, 2026-11-01.
- Basic game: the player starts with only 1 life, so any mishap loses the game (dev, 2026-11-01). The lives system and per-type costs are still built in, because more lives can come later (for example extra-life pickups or difficulty modes). Until then, misc/player/life won't be heard in the basic game, since there's never a life to spare.

The dev's shorthand for the five actions: feet versus hands. Feet means jump and duck. Hands means open (doors), hit (weapons) and turn (lane changes).

Duck timing (from the controls plan): ducking auto-unducks after about 1 to 2 seconds, and releasing early unducks sooner but risks smashing into the overhead obstacle. So a duck-under obstacle must be short enough to pass within the duck time at the current speed. At 500 ms per step, 2 seconds covers 4 tiles; at 50 ms it covers 40 tiles. Jump-over obstacles likewise must fit inside the jump's air time (in the friend's template about 1 second, so 2 tiles at 500 ms or about 18 tiles at 50 ms).

Sources for obstacle ideas: [[reference_simplefighter_builder_objects]] and [[reference_friend_runner_template]].

Q&A log:
- Q: (dev) Ducking is held, but not forever? A: It auto-unducks after about 1 to 2 seconds; releasing early unducks sooner but raises the chance of smashing into something (dev, 2026-11-01). Recorded in [[project_controls_plan]].
- Q: (dev) Help sorting which obstacles are jumped vs ducked (and turned, later). A: Claude proposed the three-height model above. The dev agreed: "Exactly right" (2026-11-01).
- Q: (dev) So there are three ways to avoid an obstacle, depending on its type? A (Claude): three heights, but five actions. Low means jump and high means duck, each a single action. Full height covers three actions depending on the obstacle: smash it (weapon), open it (hand), or change lanes (later). Since weapons, hands and lanes all come later, the first playable build only needs low and high obstacles.
- Q: (dev) So five ways: hands and feet? A: Yes, the dev's grouping (2026-11-01). Feet: jump and duck, for low and high obstacles. Hands: opening doors, hitting with a weapon, and turning (lane changes), for full-height obstacles.
- Q: First playable build with only jump-over and duck-under obstacles, full-height ones added later? A: Yes, "of course" (dev, 2026-11-01).
- Q: Hitting an obstacle: instant death or lives? A: Lives. The life sound means you lost one and the run continues as if you'd cleared the obstacle; at zero lives the game ends. Costs vary by obstacle: a blade costs 1 life, a pit ends the game regardless of lives (dev, 2026-11-01).
- Q: Is the cost only "1 life" or "ends the game", or can obstacles cost several lives? A: A tunable number per obstacle type, so some can cost multiple lives (dev agreed, 2026-11-01). Added: "For the basic game, there will only be 1 life".
- Q: Does "1 life" mean the player starts with 1 life, or that every obstacle costs 1? A: The player starts with only one life, so any mishap loses the game (dev, 2026-11-01).
- Q: "Should the first build start with jump-over obstacles only, built from these hazard, spike and mine sounds, and add duck-under once you have sounds for them? That matches how you handled the warning cues: nothing gets built until its sounds exist." A: Yes (dev, 2026-11-01).
- Q: Which hazards end the game regardless, and which only cost lives (Claude proposed falls end it, fire and electricity cost lives)? A: Everything in traps/hazards ends the game if you run into it (dev, 2026-11-01).
- Q: Spikes cost 1 life, hit on contact, death clips for weapon-smashing later? A: "Exactly right for spikes" (dev, 2026-11-01).
- Q: Mines: spawn on appearing, light arms them a few tiles out, a ticking loop, explode plus hit on contact, cost 2 lives? A: Yes. You can jump over them like spikes and hazards, but mines cost 2 lives (dev, 2026-11-01).
- Q: (dev) Would time-based obstacles like force fields add depth? A (Claude): not as plain timing gates, because in a forced-speed runner the player can't control when they arrive, so it's luck. Options with depth: a flickering jump obstacle, a hands obstacle switched off with an interact hand, or a rhythm-changing zone. Recommended leaving them out of the first build, with the hands version for later.
- Q: Record force fields as out of the first build, with the hands idea for later? A: Yes, add it as a potential obstacle with hand interaction (dev, 2026-11-01).
- Q: Random spacing with a speed-aware minimum gap, random type and theme? A: Yes (dev, 2026-11-01). The dev also added a switches folder for the future hand-operated force field, first under transitions, then moved to objects/interaction/switches/switch/press.
