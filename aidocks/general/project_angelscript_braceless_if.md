---
name: project_angelscript_braceless_if
description: A braceless if/else governs only ONE statement; adding a second orphans the else and breaks the compile
metadata:
  type: project
---

In AngelScript a braceless if or else covers exactly one statement. Adding a second statement to a braceless branch orphans the following else and the file fails to compile. The game runs from source, so a compile error means it won't launch.

**Why:** the dev's code uses braceless dispatch chains heavily, so this is easy to hit when extending a menu or handler.

**How to apply:** wrap the branch in braces before adding a statement. Sibling gotchas: [[project_angelscript_reserved_words]], [[project_angelscript_while_true_return]], [[project_angelscript_block_comment_star_slash]], [[project_nvgt_key_pressed_oneshot]].
