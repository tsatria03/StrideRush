---
name: project_joystick_ini_names_plan
description: COMPLETE (2026-11-17, 2.4 FULL at 10 of 10): joystick.ini writes buttons by name (jump=DPAD_UP) like keyboard.ini's key names, instead of SDL numbers; 2.4's tenth entry; Q&A log
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
- Section 1 BUILT (2026-11-17, on c9102b9; the dev also asked: "rewrite joystick.ini with the new button names."): key_config.nvgt's _kc_button_names, kc_button_name(button) (BUTTON_<n> past 14) and kc_button_from_name(name) (any case, a name, BUTTON_<n>, or a plain number; -1 otherwise); bind_joystick_string() reads through it and skips an unknown name, as an unknown key is skipped; get_joystick_action_string() writes names, so the rebind screen saves names; the old ini-section example comment in names. joystick.nvgt's joystick_names() (the bindings screens and F1) reads through kc_button_from_name() too, which it had to, since it parsed numbers. sdr/data/config/joystick.ini rewritten by a byte-level script: the 17 bound actions in names (jump=DPAD_UP ... quit_run=BACK), triggers kept, the 39 empty actions untouched. Braces balanced, CRLF checked by bytes. All 3 tests PASSED (dev, 2026-11-17): the new file loaded with no warning, the buttons worked, F1 spoke friendly names; a rebind of weapon_1 to the right stick click saved "weapon_1=RIGHT_STICK" (the dev put the file back); "jump=11" and "fire=a" still worked and showed as d-pad up and A button (put back too). joystick.ini checked after: names, CRLF. SECTION 1 COMPLETE; section 2 (docks) is next.
- Section 2 WRITTEN (2026-11-17, on d17491a; the dev: "write the change log entry, then tell me what it says after"): changelog.txt's entry on top of 2.4 ("Made it so joystick.ini now names each button, such as DPAD_UP or LEFT_SHOULDER, the way keyboard.ini names its keys, instead of using numbers, and a file that still has the old numbers keeps working."), so 2.4 is FULL at 10 of 10; readme.txt's joystick.ini paragraph in the joystick commands: names instead of the number list (A, B, X, Y, BACK, GUIDE, START, LEFT_STICK, RIGHT_STICK, LEFT_SHOULDER, RIGHT_SHOULDER, the four DPAD_ names, BUTTON_<n> for others), duck_held=DPAD_DOWN:down, old numbers still working. Version history, CLAUDE.md, the changelog rules. Edit tool only, CRLF checked by bytes. THE PLAN IS COMPLETE.
