---
name: project_nvgt_key_pressed_oneshot
description: key_pressed() is consumed on first read each frame; read a multi-purpose key once and branch inside
metadata:
  type: project
---

NVGT's key_pressed() returns true only on the first read of that key per frame. Two sibling if (key_pressed(KEY_X)) checks for the same key means the second never fires.

**Why:** it looks like two independent handlers but one is dead, giving "the key sometimes does nothing" bugs. Matters for the jump key in a runner.

**How to apply:** read the key once into a local bool and branch on it, or nest the logic in one if. Related: [[project_angelscript_braceless_if]].
