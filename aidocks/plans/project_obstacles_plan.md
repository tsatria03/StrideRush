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
  - Ledges (dev, 2026-11-01): the ground turns to the "ledge" platform tile just before and after each hazard, like SimpleFighter's hazard auto-ledges. The change in footstep sound is itself a warning that a hazard is next. Its sounds exist, so it's allowed under the sounds-first rule. The ledge tile is excluded from the random surface stretches in [[project_run_plan]]. Width: ledges are at least 2 tiles wide on either side of a hazard (dev, 2026-11-01), a tunable minimum. The ledge before a hazard first widened as the run sped up (dev agreed, 2026-11-01). FINAL RULE (dev, 2026-11-02), replacing both earlier versions: the ledge BEFORE a hazard has one step per 100 ms of step time, rounded up. That's 5 steps at 500 ms, 4 at 400, 3 at 300, 2 at 200 and 1 at 100 (the new speed cap). The ledge AFTER stays 2 tiles.
    - Purpose: the ledge will carry the hazard countdown, one cue per ledge step, using the friend's template's hazcount1 to hazcount5 sounds once the dev copies them into Stride Rush.
    - Countdown design: with L ledge steps, play the LAST L of the 5 cues, so the final ledge step always plays hazcount5, the "jump now" cue. At 500 ms you hear hazcount1 to 5; at 300 ms hazcount3 to 5; at 100 ms only hazcount5.
    - BUILT 2026-11-02: the sounds are in sr/sounds/misc/game/. They play in 2d, never stationary (dev), at the ledge tile you've just stepped onto. They were first placed at the hazard's tile; the dev changed that the same day.
    - Timing consequence (the dev accepted it): at 500 ms and 400 ms, jumping on the early ledge steps lands before the hazard, so you jump on the last 2. At 300 ms and below, any ledge step works.
  - The earlier version, a fixed 2 tiles on each side at every speed (dev, 2026-11-02), was also superseded. The dev didn't like ledges growing with speed. Jumping on either ledge step always clears a hazard (the check happens on arrival, and a jump lasts about 1 s), and the hazard's loop gives the main warning about 3 s ahead.
- Spikes (objects/traps/spikes: electric_ray, large_spike): cost 1 life. Running into one plays hit. The loop plays while ahead (dev, "exactly right", 2026-11-01).
  - UPDATE, same day: the dev trimmed the spike folders to loop and hit only. Their death1-2 and hurt clips are gone, so spikes are NOT destroyable by weapons, unlike SimpleFighter's. Under the sounds-first rule there's nothing to play for smashing one. The dev confirmed: "Spikes are non destroyable."
- Mines (objects/traps/mines: mine, mine2, mine3): cost 2 lives. Jump over them like spikes and hazards (dev, 2026-11-01).
  1. spawn plays quietly when the mine appears ahead.
  2. light plays when the player gets within a few tiles (tunable), and the mine arms. It's a built-in warning that's allowed now because the sounds exist.
  3. loop is the armed ticking, positioned ahead.
  4. Running into it plays explode, then hit, and costs 2 lives.
  5. Jumped over, it stays behind and goes quiet.
- Force fields (objects/traps/force_fields: electric, electric2; clips on, off, hit): NOT in the first build. Recorded as a POTENTIAL hand-interaction obstacle for when interact hands are designed (dev, 2026-11-01).
  - Idea: a full-height field that stays on, switched off with an interact hand at a switch placed before it. The switch sound now exists: objects/interaction/switches/switch/press (dev added it, 2026-11-01). Hitting it while it's on plays hit and costs lives (amount to decide then).
  - Rejected as a plain on/off timing gate: the belt controls speed and the player can't wait, so arriving while it's on or off would be luck, not skill.

Doors (full height, hands; PARKED for later, the dev said they aren't needed now; dev, 2026-11-01). Sounds are objects/transitions/doors/door to door4, picked at random per door; all doors can be randomized.
- Real door: plays at pitch 100. It can be opened with an interact hand, as long as you don't run into it.
- Fake door: plays at exactly one of four pitches, 80, 90, 110 or 120, picked at random. Never anything in between, and never near 100, so it's always at least 10% off and audibly different (dev, 2026-11-01). It can't be opened with a hand. It must be destroyed with a weapon (hurt on each hit, death when destroyed), or you smash right into it.
  - Reason for the gap: the dev first gave 80 to 120, but that includes 100, and 99 or 101 can't be told apart from a real door by ear.
  - Door type: SimpleFighter's normal doors, not passages. The dev put the move sounds in for a reason (dev, 2026-11-01). In SimpleFighter a door carries you through to its destination, playing move as you go, while a passage just opens a corridor and has no move clip ([[reference_simplefighter_builder_objects]]).
  - Door sound flow (dev, 2026-11-01): the loop plays on the field for a door while it's present. Opening a real door plays open, then the door's move sound, then close, in that order. grant, deny and jam are never played. Claude's proposals to use grant on opening and deny on a fake door were declined.
  - Fake doors still use hurt (each weapon hit) and death (destroyed), since the dev added the doors partly for those sounds.
- So there are five door pitches in total: 100 is the real door, and 80, 90, 110 and 120 are fakes. Combined with the four door folders, players learn a small, fixed set of door sounds.

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
- Q: Is the ledge platform for hazards, or just a favorite surface? A: For hazards (dev, 2026-11-01).
- Q: How many ledge tiles before and after a hazard? A: At least 2 tiles wide on either side (dev, 2026-11-01).
- Q: Should the ledge before a hazard widen with speed so it stays audible, with 2 tiles as the floor? A: Yes (dev, 2026-11-01). REVERSED after testing (dev, 2026-11-02): "It should have been 2 tiles on either side regardless." Ledges were then fixed at 2 before and 2 after.
- Q: (dev, 2026-11-02) New ledge rule: 500 ms gives 5 ledge steps, 400 gives 4, 300 gives 3, 200 gives 2, 100 gives 1, with speed capped at 100 ms? A: Built. Claude warned that at 500 and 400 ms the early ledge steps are too soon to jump, since a jump lasts 1 s. The dev explained the ledge will carry the friend's countdown sounds, one per step. Rounding is up for in-between speeds (450 gives 5, 350 gives 4), and the ledge after stays 2.
- Q: (dev note) Doors? A: A door at pitch 100 can be opened with a hand, assuming you don't run into it. A door pitched between 80 and 120 must be destroyed with a weapon or you smash into it; it isn't hand-interactable, like a fake door. All doors can be randomized; there are 4 door folders (dev, 2026-11-01).
- Q: 80 to 120 includes 100. Use a gap: fake doors from 80 to 90 or 110 to 120? A: "I like that 80, 90, 110, 120" (dev, 2026-11-01).
- Q: Ranges or exact values? A: Four exact pitches. 100 is the normal door; 80, 90, 110 and 120 are the fake door (dev, 2026-11-01).
- Q: (dev) Which door type: SimpleFighter's doors or passages? A: Normal doors, not passages, because of the move sounds (dev, 2026-11-01).
- Q: Door sounds: grant and open on the hand, move while passing, close behind, and deny on a fake door? A: Open plays, followed by move, then close. The other clips aren't played. The loop plays on the field for a door (dev, 2026-11-01).
- Concern (dev, 2026-11-01): playing move and close makes it sound as if the game is ending, not continuing. The open-move-close flow is under reconsideration.
- Q: How to keep a door from sounding like an ending? Claude's options: 1, open only; 2, open and move with no close; 3, all three, with close placed behind the player and fading. A: Not decided. The dev parked doors: "we can talk about doors later; right now we don't need them" (2026-11-01). Resume with this question when doors come up again.
