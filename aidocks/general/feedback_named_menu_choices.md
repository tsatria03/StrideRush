---
name: feedback_named_menu_choices
description: menu choices name what you get (silent hints, spoken hints; limited rounds, unlimited rounds) instead of plain off and on
metadata:
  type: feedback
---

A setting's menu lists named choices that say what you get, never bare "off" and "on" (dev, 2026-11-14: "It doesn't have to be simple on/off", then "Please reword the on/off options in the other menus as well"). Examples: modify ammo limits has limited rounds and unlimited rounds; modify practice hints has silent hints and spoken hints; modify death mode has no deaths, normal deaths, practice deaths; modify footsteps (planned) has heard footsteps and silent footsteps.

**Why:** a name like "ammo limits" made "on" ambiguous (limits on, or unlimited on?); a named choice can be understood on its own, as with [[feedback_yes_no_menu_labels]].

**How to apply:** for any new toggle-style menu, write two named choices (alphabetical, then back) and keep the internal ids as they are. Yes/no questions still use Yes then No.
