---
name: feedback_menus_say_canceled
description: Every menu or input escape, Back, or No path speaks "canceled"
metadata:
  type: feedback
---

Every menu or input path that backs out (escape, a Back item, or a No answer) speaks "canceled".

**Why:** without a spoken cue a screen-reader player can't tell whether the escape registered or the game hung.

**How to apply:** wire the speak call into every cancel, back and No branch of new menus. Related: [[feedback_yes_no_menu_labels]].
