---
name: project_angelscript_reserved_words
description: Never name a variable out (or in, inout, shared, final, from, override, explicit, property), nor after a type such as sound, any or joystick; both are compile errors
metadata:
  type: project
---

out reads like a natural variable name but is a reserved AngelScript keyword, so using it breaks the compile. The same goes for in, inout, shared, final, from, override, explicit and property.

**Why:** a compile error means the game won't launch.

**How to apply:** pick another name such as output or result. Related: [[project_angelscript_braceless_if]].

Type names are illegal too (2026-11-18, the free run powerups build: "Illegal variable name 'sound'" and "'any'"): a variable can't share a name with a registered type, such as sound (NVGT's sound class), any (AngelScript's any type), joystick, timer or string. Earlier, a parameter named joystick clashed the same way. Use names such as get_path, running_one or for_joystick.
