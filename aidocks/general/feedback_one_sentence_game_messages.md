---
name: feedback_one_sentence_game_messages
description: In-game spoken feedback messages are exactly one sentence; no trailing advice sentence
metadata:
  type: feedback
---

Anything the game speaks to the player during play is exactly one sentence. Don't append a second sentence of advice or instruction.

**Why:** the game is played by ear, and a runner especially can't afford speech talking over the next obstacle cue.

**How to apply:** state the result and stop. Guidance belongs in the readme. Related: [[feedback_menus_say_canceled]].

EXCEPTION (dev, 2026-11-06: "Yes. Achievements are the exception."): an achievement announcement is the name and then its full description, as CookieCraze's are ("Achievement unlocked: Lane Changer. Change lanes 50 times over all your runs."), so it can run to two sentences or more. Related: [[project_achievements_plan]].

EXCEPTION (dev, 2026-11-12: "Yes agreed. Another multi centince exception."): a practice death's dialog is "You died.", then what caught you, then how to get past it ("You died. A spike hit you. Jump as its last countdown cue plays to sail over it."), since it's a dialog dismissed with Enter, not speech over play. Related: [[project_practice_guidance_plan]].

EXCEPTION (dev, 2026-11-12, agreeing to the hint lines): a practice hint, in the practice buffer, is what appeared, then what to do ("A key has appeared in the left lane. Move into its lane and use a hand to grab it."), at most 5 per kind in a practice run. Related: [[project_practice_guidance_plan]].
