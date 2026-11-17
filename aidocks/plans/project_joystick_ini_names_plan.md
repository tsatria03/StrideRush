---
name: project_joystick_ini_names_plan
description: SETTLED (2026-11-17), not built: joystick.ini writes buttons by name (jump=DPAD_UP) like keyboard.ini's key names, instead of SDL numbers; 2.4's tenth entry; Q&A log
metadata:
  type: project
---

Started 2026-11-17, on 113e481. Asked for 2.4's last change, Claude suggested a Test vibration button, PlayStation button names, or a no-joystick note; the dev: "Speaking of option 2. It's extremely confusing to see numbers in joystick.ini, wile keyboard.ini has actual keycode names." 2.4 holds 9 of 10. Built on [[project_joystick_plan]]. Not built; no sections yet.

## Findings (2026-11-17)
- keyboard.ini: "jump=UP,W", "duck_held=Down:down,S:down", names through key_config.nvgt's _kc_register() table (kc_name_to_code(), kc_code_to_name()), upper case with underscores (NUMPAD_ENTER, MEDIA_NEXT_TRACK).
- joystick.ini: "jump=11", "duck_held=12:down", SDL gamepad button numbers; key_config's bind_joystick_string() reads them with parse_int(), get_joystick_action_string() writes them; the readme's joystick commands list what each number is.
- The bindings screens already speak names (joystick.nvgt's button_names: A button, d-pad up, ...), through joystick_names().

## Q&A log
- Q1 (Claude, 2026-11-17): the names joystick.ini would use, in keyboard.ini's style (upper case, underscores): 0 A, 1 B, 2 X, 3 Y, 4 BACK, 5 GUIDE, 6 START, 7 LEFT_STICK, 8 RIGHT_STICK, 9 LEFT_SHOULDER, 10 RIGHT_SHOULDER, 11 DPAD_UP, 12 DPAD_DOWN, 13 DPAD_LEFT, 14 DPAD_RIGHT, and BUTTON_15 and on for any past those. So "jump=DPAD_UP", "duck_held=DPAD_DOWN:down", "fire=A", "hand_left=LEFT_SHOULDER". The file is read case-insensitively like keyboard.ini, and a plain number still works, so an older or hand-made file keeps working; saving always writes names. Recommended: as proposed.
- A1 (dev, 2026-11-17): "yes". The names as proposed, case-insensitive, numbers still read, names always written.
- Q2 (Claude, 2026-11-17): the sections. No new sounds. Proposed: 1. Names: a name table in key_config.nvgt beside the key names (keyboard.ini's names live there too), so bind_joystick_string() reads a name or a number and get_joystick_action_string() writes names; sdr/data/config/joystick.ini rewritten with names, same layout; the bindings screens keep speaking their friendly names (A button, d-pad up). Tests: a launch with the new file, a rebind writing a name, an old number still working. 2. Docks: one changelog entry on top of 2.4 (10 of 10, so 2.4 is full, wording proposed then); the readme's number list becomes the name list; the version history, CLAUDE.md. Recommended: as proposed.
- A2 (dev, 2026-11-17): "Yes, settled".

## THE PLAN IS SETTLED (2026-11-17)
1. Names: key_config.nvgt's joystick button name table (A, B, X, Y, BACK, GUIDE, START, LEFT_STICK, RIGHT_STICK, LEFT_SHOULDER, RIGHT_SHOULDER, DPAD_UP, DPAD_DOWN, DPAD_LEFT, DPAD_RIGHT, BUTTON_<n> past those); bind_joystick_string() reads a name (any case) or a number; get_joystick_action_string() writes names; sdr/data/config/joystick.ini rewritten with names; the bindings screens' friendly names unchanged. Tests.
2. Docks: one changelog entry on top of 2.4 (10 of 10, 2.4 full; wording proposed then); the readme's number list becomes the name list; the version history and CLAUDE.md.

## Build log
- Not started.
