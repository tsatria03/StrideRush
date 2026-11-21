---
name: project_keyboard_joystick_plan
description: SETTLED (2026-11-20, 2.7, before the shop, two entries for 2 and 3 of 10, 4 sections): keyboard and joystick bindings: fire and duck each become one action (fire_held, duck_held and duck_release removed, older ini files merged), clashes that respect triggers, Control bindable on its own for firing; Q&A log
metadata:
  type: project
---

# Keyboard and joystick plan

The dev's suggestions (2026-11-20, before building the shop): "Fix key binding issues in the keyboard tab. You are not able to rebind the same key to another action. Example, the firing weapon actions. Make both control keys bindable."

## Findings

- keyboard.ini gives some actions the same key with different triggers: fire=SPACE and fire_held=SPACE:down; duck=DOWN,S, duck_held=Down:down,S:down and duck_release=DOWN:release,S:release.
- bindings_menu.nvgt's rebind_replace_question() and rebind_take_over() use key_config.nvgt's actions_using() and overlap_count(), which match the keys whatever the trigger. So binding a key to fire_held that fire already has asks to replace it and takes it off fire: the pair can never share a new key, and rebinding fire to Control leaves fire_held on Space with no way to follow.
- key_config.nvgt's kc_capture_combo() skips every modifier-only press (both shifts, controls, alts and GUI keys) and waits for a real key, so Control alone can't be captured; LCTRL and RCTRL are registered names, so a binding to them would load.

- The joystick has the same shape: joystick.ini's fire=A and fire_held=A:down, the duck trio on DPAD_DOWN, and actions_using_button() and button_overlap_count() ignoring triggers too.
- kc_save_preserving() writes back any line whose action isn't loaded, so an old fire_held line would survive saving unless the merge removes it from the file.

## Settled design

- One action each: fire (press for melee and the pistol, down for the machine gun) and duck (press starts it, down crouches on landing, release ends it), read through action_pressed(), action_down() and action_released(), on the keyboard and the joystick. fire_held, duck_held and duck_release leave the code, both ini files and the rebind lists.
- An older keyboard.ini or joystick.ini is merged on load: keys or buttons on the three old lines that fire or duck lack are added to them, and the old lines removed.
- The trigger question is skipped for fire and duck.
- Otherwise a key clashes only when the keys and the trigger both match, the rebind flow asking for the trigger first.
- fire's and duck's keys and buttons clash with any other action whatever its trigger, so the replace question always comes up for them.
- Control alone (released with no other key) binds as CTRL, either side; Control plus a key is still a combo; Shift, Alt and the Windows key stay combo-only. Space stays fire's default, since tapping Control silences NVDA and JAWS by default.

- Changelog, on top in this order: "Made it so either control key can now be bound on its own, such as for firing your weapons, and actions can now share a key when they use different triggers." / "Fixed a bug where rebinding your fire or crouch keys only moved part of the action, so each is now a single binding on the keyboard and joystick, and your current keys are kept."
- Docks: keyboard_and_joystick.txt's trigger example (duck_held=DPAD_DOWN:down) swapped for an action that still exists, with a short note that fire and duck handle their own triggers.

## Sections

1. One action each: weapons.nvgt and player.nvgt read fire and duck by press, down and release; the three old actions out of keyboard.ini and joystick.ini; older files merged on load and the old lines removed.
2. The rebind rules, on both devices: clashes by keys and trigger, fire and duck clashing with any trigger, the trigger asked before the replace question, and skipped for fire and duck.
3. Control on its own: the capture screen binds CTRL when Control is released with no other key; combos unchanged.
4. Docks: keyboard_and_joystick.txt, the two entries (2.7 at 3 of 10), the template script rerun (english.lng by hand if lines change), version history.

## Q&A log

- Claude laid out both causes (above).
- Q (Claude): the sharing rule: a key only clashes with another action's binding when the trigger is the same too, so fire (press) and fire_held (down), or duck, duck_held and duck_release, can share a key as the defaults do, and the replace question only comes up for the same key with the same trigger? Recommended.
- A (dev): yes. Settled: a key only clashes with another action's binding when the keys and the trigger both match; the rebind flow asks for the trigger first, then the replace question.
- Q (Claude): Control on its own: pressing and releasing either Control with no other key binds "CTRL", so left and right Control both do that action, while holding Control and pressing another key still makes a combo such as CTRL+A; Shift, Alt and the Windows key stay combo-only? Recommended (the alternative: left and right Control bound separately, as LCTRL and RCTRL).
- Dev: the Control request came from a player who wants to fire weapons with it. Claude's reading, settled by that: Control alone binds as CTRL, so either side fires; Shift, Alt and the Windows key stay combo-only.
- Finding: a one-key binding ignores other held modifiers (action_triggered() only checks a combo's own modifiers), so holding Control to fire doesn't block jumping, ducking or changing lanes, unless a CTRL+<key> combo is bound to that key. weapons.nvgt reads fire for the pistol and melee and fire_held for the machine gun, so a player who rebinds only fire finds the machine gun still on Space. Tapping Control also silences NVDA and JAWS by default, so firing with it can cut off screen reader speech; a reason to leave Space as the default and make Control the player's choice.
- Q (Claude): keep the firing pair together: adding, editing or removing a key on fire does the same on fire_held (with its held trigger), and the reverse, so one rebind moves all weapons, without asking for a trigger on the pair? Space stays the default. Recommended.
- Dev asked whether fire is for melee and fire_held for machine guns, and the same for ducking. Claude: fire (press) is one swing or one pistol shot; fire_held (down) is the machine gun's continuous fire. duck (press) starts a crouch; duck_held (down) is only read on landing, so holding the key through a jump crouches as you land; duck_release (release) ends the crouch early, otherwise it ends on its timer. A duck key moved without the other two loses both of those.
- Q (Claude, widened): keep each family together: fire with fire_held, and duck with duck_held and duck_release: adding, editing or removing a key on any one does the same on the others, each with its own trigger, and the trigger question is skipped for them? Recommended.
- Dev: could fire handle both press and down, and duck all three jobs, removing fire_held, duck_held and duck_release?
- Finding: yes. key_config.nvgt's action_pressed(), action_down() and action_released() ask any action for a given trigger whatever its binding says, on the keyboard and the joystick, so weapons.nvgt and player.nvgt can read one action each. keyboard.ini and joystick.ini live in data/config/main, so a player's existing file can still hold the three old lines, which would otherwise stay listed in the rebind menu.
- Q (Claude): replaces the families idea: fire and duck each become one action read by press, down and release as needed; the three old actions go from both ini files, code and the rebind lists; the trigger question is skipped for fire and duck, since each uses all its triggers; when the game loads an older ini, any extra keys on the old lines are merged into fire or duck and the old lines removed, so nobody loses a binding? Recommended.
- A (dev): yes, and this needs an actual keyboard and joystick plan. The plan file was renamed from the rebind fixes plan, and covers both devices.
- Finding: fire and duck now use every trigger, so a trigger-only difference can't let another action share their key: another action on Space with a held trigger would still run whenever you fire.
- Q (Claude): fire's and duck's keys and buttons clash with any other action whatever its trigger (the replace question always comes up), while other actions follow the same-keys-and-trigger rule, on both devices? Recommended.
- A (dev): yes. Settled.
- Q (Claude): two entries on top (2.7 to 3 of 10, the shop's three then 4 to 6), newest first: "Made it so either control key can now be bound on its own, such as for firing your weapons, and actions can now share a key when they use different triggers."; "Fixed a bug where rebinding your fire or crouch keys only moved part of the action, so each is now a single binding on the keyboard and joystick, and your current keys are kept." Recommended.
- A (dev): yes. Plan SETTLED; waiting for the dev to commit it. It builds before the shop, whose three entries become 4 to 6 of 10.
