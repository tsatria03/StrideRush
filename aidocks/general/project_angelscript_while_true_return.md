---
name: project_angelscript_while_true_return
description: A non-void function whose returns are all inside while(true) still needs a trailing unreachable return, or it fails with "Not all paths return a value"
metadata:
  type: project
---

AngelScript's flow analysis doesn't know while(true) or for(;;) never falls through. A non-void function that only returns from inside such a loop fails to compile with "Not all paths return a value".

**Why:** menu functions in the dev's games are often built this way (ToyMania's choose_difficulty hit it).

**How to apply:** add a dummy return after the loop, such as return -1. Related: [[project_angelscript_braceless_if]].
