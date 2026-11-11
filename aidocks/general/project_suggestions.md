---
name: project_suggestions
description: Claude's gameplay suggestions waiting on the dev's decision (not the player-facing todo list): the 2.0 run mechanics ideas, lane-changing barriers in detail; also the suggestions the dev declined, never to re-suggest
metadata:
  type: project
---

Kept here, not in sdr/docks/todo list.txt, at the dev's request (2026-11-10: "Put this in a suggestions memmory ... Not my personal todo list file."). When the dev says they like a suggestion, copy it to sdr/docks/todo list.txt as a player-facing line in its open section (dev, 2026-11-10: "If I like a suggestion, it should get coppied to my personal todo list file. I'll let you know when you'll need to do this"); only when the dev says so, never on Claude's own call. It stays here too, marked liked, until a plan starts (then it moves into aidocks/plans/). Turned down, it moves to the declined list below. The review routine (dev, 2026-11-10): Claude explains one suggestion in play, then asks whether the dev wants it for later. Yes: copy it to the todo list and mark it liked here. No: move it to the declined list. Maybe or "I'll think about it": mark it not certain here.

## Waiting on the dev (suggested 2026-11-10, for 2.0)
The dev asked for 2.0 ideas "related to the run modes itself. Example, new macanics." Claude's top picks were the pursuer and zones.
1. Lane-changing barriers. NOT CERTAIN (dev, 2026-11-10: "I'll think about that one."). See the detail below.
2. Combined obstacles. LIKED (dev, 2026-11-10: "es. Deffenatly"), copied to the todo list's open section; its plan is started, [[project_combined_obstacles_plan]], so the detail lives there now. Explained in play: two cues together needing two actions in sequence, the second part's countdown running while the first arrives, on purpose (today next_gap() keeps every countdown after the last obstacle is passed, with floor between); each part keeps its own warning and damage, the gap in steps never below what's possible, only obstacles already met that run; rarer and looser on easy, tighter on harder levels, maybe three-part chains on chaos; a practice choice at the end of the chain, a statistic and achievements. Examples: such as a projectile over a spike (crouch, then jump) or a wall behind a force field (hand, then weapon).
3. (Declined, see below.)
4. A pursuer. NOT CERTAIN (dev, 2026-11-10: "I recommend it being more of a chase thing, but I'll think about this one too"). Something heard behind you (a dog, a boulder, a storm) that gains while you're hit and falls back while you run clean; caught costs a life. Explained: no new action as first described (the dev asked whether you kill, jump, duck or dodge it: no, you keep it back by passing obstacles cleanly), so on its own it mostly repeats the damage penalty. The dev leans to a chase: an escape run (start close, lose it by running clean until it fades out of hearing) or a door race (reach each real door before it catches you). Optional actions offered: a clap to scare it back when close (fits a dog), swinging behind you (no turning exists), a lunge you dodge by switching lanes.
5. Zones. FOLDED INTO the dev's environments idea, [[project_environments_plan]] (started 2026-11-10), as its automatic mode; the detail lives there now. Was: NOT CERTAIN (dev: "I'll also think about this, as I did have an idea independent of this that could tie into it."). The belt passes through places (city, cave, forest, factory), each with its own ambience (replacing the random crossfade), surfaces, a favoured obstacle mix, entered perhaps at a real door; landmarks for long runs, a furthest zone statistic and achievements; easy reaches only the first few; none in practice; more content than code.
6. Jump pads and slides: a pad launches you over the next few obstacles; a slide speeds you up for a stretch; risky shortcuts.
7. A hardcore endless option: one life, no survival items, its own statistics and achievements.
8. Daily run: one seeded endless run a day from the date, offline, with a best distance for the day.

## Lane-changing barriers in detail (as explained to the dev, 2026-11-10)
- In play: a barrier (a car, say) is heard coming in one lane, then plays a swerve cue (tyre squeal, horn) and its sound slides into a neighbouring lane; you track where it ends up and dodge that. The skill is listening for where it lands, not where it started.
- Fairness: the drift is always announced by its own cue; it moves once, one lane, never at the last moment, finishing while there's still time to react; at least one lane always stays open, as with pairs today. Its countdown (which plays only in its own lane) picks up as it drifts into yours.
- By speed and level: early and slow at low speeds (a listening test), little time between swerve and arrival at high speeds. Easy: few drifters, drifting away from you or into an empty lane; chaos: drifting towards you, or one of a pair crossing the other.
- Situations: the fake-out (it starts in your lane, you dodge left, it drifts left too); a pair where one drifts, so the open lane moves and you switch twice; an item in the lane you'd dodge into.
- Elsewhere: a drifting option in barriers practice (or part of barriers once unlocked); the swerve cue in learn sounds; a "drifting barriers dodged" statistic and maybe an achievement for one that swerved into your lane.
- Uses place_lane_sound() and the existing barrier lane rules; the sounds (a swerve cue per barrier kind) would have to exist first ([[feedback_sounds_before_features]]).

## Declined: never suggest these again
- From the end of 1.8 (dev, 2026-11-09: "Please close those suggestions ... I no longer want them."): a personal best callout, a low health warning, a heartbeat that reacts to danger, player sounds in learn sounds, a stretch announcement, a heartbeat on and off setting.
- Wide hazards with a long jump (dev, 2026-11-10: "No thanks. I'm perfectly fine with 1 tiled hazards. They are already hard enough at high speeds."). Explained: a 2 to 3 tile gap, a held long jump or a run-up, width in time; it changes the jump itself.
- Alt keys as hand keys (asked 2026-11-10; Claude advised against: Alt plus Tab with Tab on the inventory, Alt combos, AltGr, the binder skipping modifiers).
- A rebuild of a deleted keyboard.ini (2026-11-10): discussed, not taken up for now.
