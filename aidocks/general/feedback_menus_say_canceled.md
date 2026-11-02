---
name: feedback_menus_say_canceled
description: Every menu or input escape, Back, or No path speaks "canceled", except a nested menu whose Escape just steps back to its parent menu (silent, including back to the main menu)
metadata:
  type: feedback
---

Every menu or input path that backs out (escape, a Back item, or a No answer) speaks "canceled".

**Why:** without a spoken cue a screen-reader player can't tell whether the escape registered or the game hung.

Exception for nested menus (dev, 2026-11-02, refined twice the same day): when Escape just steps back to the menu it came from, it says nothing, because that menu's intro is cue enough. That includes escaping the first menu of a chain back to the main menu. "canceled" is for a lone prompt or menu that cancels an action, such as the pause menu's quit confirm answering No, or a buffer-menu escape. Example: the testing menus (lives, speed, spawn) are all silent: spawn to speed, speed to lives, lives to the main menu.

**How to apply:** wire the speak call into the cancel, back and No branches of new menus, except where Escape just steps back to a parent menu. Related: [[feedback_yes_no_menu_labels]].
