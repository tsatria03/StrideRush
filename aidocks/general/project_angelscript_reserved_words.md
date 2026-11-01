---
name: project_angelscript_reserved_words
description: Never name a variable out (or in, inout, shared, final, from, override, explicit, property); reserved words are a compile error
metadata:
  type: project
---

out reads like a natural variable name but is a reserved AngelScript keyword, so using it breaks the compile. The same goes for in, inout, shared, final, from, override, explicit and property.

**Why:** a compile error means the game won't launch.

**How to apply:** pick another name such as output or result. Related: [[project_angelscript_braceless_if]].
