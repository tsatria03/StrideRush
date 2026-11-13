---
name: feedback_no_key_names_in_hints
description: Practice lines and achievement hints never name a keyboard key, only the action, since keys can be rebound
metadata:
  type: feedback
---

Practice lines (hints, the closing line, death dialogs) and achievement hints never name a keyboard key such as U, R, Enter, Escape or space. Name the action instead: "use it from your inventory", "a hand", "reload", "the fire key", "quit the run".

**Why:** the dev (2026-11-12, the practice guidance plan): "Never mention actual keyboard keys in practice lines, as that can change." Then, after the achievement audit: "the achivements that mention bindable keys also need fixning as well." Every action is rebindable, and the bindings string is keyboard.ini's format, not speech.

**How to apply:** check any new practice line or achievement hint for key names before showing it to the dev. The readme still names default keys, since it documents them. Related: [[project_practice_guidance_plan]], [[project_achievement_hints_plan]].
