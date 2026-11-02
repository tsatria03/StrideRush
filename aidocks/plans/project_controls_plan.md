---
name: project_controls_plan
description: SETTLED, NOT BUILT - Stride Rush in-game key layout (dev-set 2026-11-01), rebindable via SimpleFighter's key_config; item keys and jump/duck overlap deferred to later plans; includes a Q&A log
metadata:
  type: project
---

Status: SETTLED 2026-11-01. Not built; the keys get written into keyboard.ini when input is built. Two things are deferred: the item keys go to the items plan (the brackets are taken by the buffer), and the jump/duck overlap rules go to the movement plan ([[feedback_plans_record_qna]]).

Keys set by the dev (2026-11-01). Every action is rebindable through SimpleFighter's key_config class (deps/key_config.nvgt, already in Stride Rush) and a keyboard.ini, like SimpleFighter's data/main/config/keyboard.ini ([[reference_simplefighter_architecture]]):
- Up or W: jump.
- Down or S: duck, held. duck.ogg plays on press. Ducking auto-unducks after about 1 to 2 seconds even if the key is still held (tunable), and releasing early unducks sooner; unduck.ogg plays either way. Unducking early raises the chance of smashing into what you were ducking under (dev, 2026-11-01). Slides under obstacles you can't jump.
- Left or A: lane switch left. Lanes are a later expansion, so these keys are reserved now.
- Right or D: lane switch right (reserved, as above).
- Tab or Z: left interact hand, for doors and similar objects.
- Enter or C: right interact hand, for doors and similar objects.
- Space: shoot with an ammo weapon, or swing a melee weapon (ToyMania-style). Space only; no left or right Control (settled 2026-11-01).
- X: ammo check, for non-melee weapons.
- R: reload an ammo weapon.
- 1 through 0: select a weapon (ten slots).
- Escape or P: pause, which opens a pause menu. The pause menu does NOT hold settings (changed 2026-11-01; see F2).
- Buffer keys (CaveDefender's, kept as-is): comma and period for messages, the brackets for categories, Shift with either pair for first and last, Shift+M mute, Shift+C copy, Alt+Shift+C review, Shift+B buffer menu, Shift+backslash export.
- F1 (during a game): open the view-key-bindings screen, the same one as the settings Keyboard tab's "View current keyboard bindings". It pauses the run while open (settled 2026-11-01).
- F2 (during a game): open the settings panel, SimpleFighter-style tabs. No Alt-letter shortcuts. During a run it shows only the Game, Menu and Speech tabs; General, Keyboard and Sound are hidden, exactly like SimpleFighter's settingsmenu(true). Viewing key bindings mid-run is F1's job (settled 2026-11-01).
- L: lives readout, how many lives you have (dev, 2026-11-01). H is UNUSED; it was the health/lives key, replaced by L. There's no separate health, only lives.
- Q: distance traveled readout.
- E: current speed readout.
- T: time in this run readout.
- F: score or money readout.
- Home and End: ambience volume.
- Page Up and Page Down: music volume.

Later features named by these keys: ducking, weapons (number row plus fire, ammo check and reload), the two interact hands, lanes, a pause menu, and separate ambience and music volume.

Rule: status readouts go on letter keys, never function keys (dev, 2026-11-01). Function keys are for screens: F1 key bindings, F2 settings.

Still unassigned: item keys (deferred). Record any new key here when it's settled.

Q&A log:
- Q: Is ducking in? A: Yes (dev, 2026-11-01). Down slides under obstacles that need it.
- Q: Weapons? A: Later, ToyMania-style. The number row selects, and Space or Control fires or swings.
- Q: Rebinding? A: Yes, via SimpleFighter's key_config.
- Q: (dev) What does Claude think of the keyset? A (Claude's review, 2026-11-01):
  - Strong overall. Arrows mirror WASD, jump and duck sit on the up/down axis, and the interact hands are physically mirrored (Tab/Z left, Enter/C right). PgUp/PgDn already means music volume in form_menu.
  - Flag 1: plain Control fires the weapon. Screen readers (NVDA, JAWS) stop speech on any Control press, so every shot would cut off game speech such as status readouts. Space doesn't have this problem.
  - Flag 2: key_config's in-game rebind capture (kc_capture_combo) skips modifier-only presses, so a player can't rebind fire to a lone Control from inside the game. Only a hand edit of keyboard.ini can do it.
  - Flag 3 (reworded after the dev pointed out you never jump and duck at the same time): the question is overlap, not both at once. What should Down do in mid-air, and what should Up do during a slide? Settle it in the movement plan.
- Q: Keep Control as a second fire key? A: No. Fire is Space only, with neither left nor right Control (dev, 2026-11-01). That resolves flags 1 and 2.
- Q: Health key? A: H, for later (dev, 2026-11-01).
- Q: Status readouts on letters or F keys? A: Letters, not function keys (dev, 2026-11-01). The dev clarified this applies to status keys only; function keys aren't banned game-wide, so the F1 (controls list) and F2 (version) proposals are still open.
- Q: Readout letters Q distance, E speed, T time, F score/money, H health? A: Yes (dev, 2026-11-01).
- Q: A reviewable speech history? A: Yes, a buffer system, taken from CaveDefender's buffer.nvgt, not ToyMania's, which has bugs (dev, 2026-11-01). See [[reference_cavedefender_buffer]]. Its keys use comma, period, the brackets, and Shift+M, C, B and backslash. The brackets are therefore taken, so Claude's earlier idea of brackets for inventory cycling is off; items need other keys later.
- Q: Keep CaveDefender's buffer keys exactly? A: Yes (dev, 2026-11-01). The keys are comma and period for previous and next message, Shift+comma and Shift+period for first and last, the brackets for previous and next category, Shift+brackets for first and last category, Shift+M mute, Shift+C copy, Alt+Shift+C review, Shift+B buffer menu, and Shift+backslash to export and clear.
- Q: Settings mid-run via Alt-letter shortcuts (ToyMania) or the pause menu? A: The pause menu (dev, 2026-11-01). No Alt-letter settings shortcuts. SUPERSEDED the same day: settings open with F2, not from the pause menu (see below).
- Q: Does SimpleFighter's pause menu have ToyMania's quit bug? A (Claude, from the code): no, but only because it has no Quit item. Its pausemenu() offers resume, save game (arena only) and view statistics. ToyMania's bug isn't about custom_menu: it reads m.get_item_id(mres), the pause menu's result, instead of confirmres, the Yes/No result. That's a typo that would break form_menu too. For Stride Rush's pause menu, borrow SimpleFighter's structure (a while(true) loop that returns on resume, rather than ToyMania's pausemenu() calling itself), and read the confirm menu's own result.
- Q: F1 for a controls list? A: The controls list lives in the Keyboard tab of the settings panel, modeled on SimpleFighter's (dev, 2026-11-01). Then, in a follow-up the same day: pressing F1 during an actual game also opens that same view-key-bindings screen directly. So F1 is in, as a shortcut to the screen, not a separate list. The run is paused while the screen is open and resumed on close (confirmed by the dev).
  - Reference: SimpleFighter's settingsmenu(bool ingame) in main/menus/menu.nvgt is one audio_form window, "preferences", with a "Category" tab panel. Its tabs are General, Game, Keyboard, Menu, Sound and Speech, with save settings and cancel buttons.
  - The Keyboard tab has "Rebind keyboard controls" and "View current keyboard bindings". The second one is view_keyboard_bindings(), which reads keyboard.ini so the list stays accurate after rebinding. That's the controls list.
  - Catch: when opened in-game, SimpleFighter hides the General, Keyboard and Sound tabs. Stride Rush opens settings in-game with F2, so it has to decide which tabs show in-game.
- Q: Where do settings open mid-run? A: F2, not the pause menu (dev, 2026-11-01). This replaces the earlier "settings live in the pause menu" answer. Also confirmed: F1 effectively pauses the game while the bindings screen is open.
- Q: Can keys be rebound mid-run? A: No. During a run, keys can only be viewed, never rebound (dev, 2026-11-01). When F2 opens settings mid-run, the Keyboard tab shows only "View current keyboard bindings" and hides "Rebind keyboard controls". Rebinding happens only from settings opened outside a run. Whether the General and Sound tabs show mid-run is still open.
- Q: Which settings tabs show mid-run? A: Hide General, Keyboard and Sound (dev, 2026-11-01). F2 mid-run shows only Game, Menu and Speech, matching SimpleFighter. This replaces the "Keyboard tab view-only" detail above: the Keyboard tab is hidden entirely mid-run, and F1 remains the in-run way to view bindings.
  - SimpleFighter reference: on a map it shows only Game, Menu and Speech, opened by the pf/preffs command, which calls pause_pools() then settingsmenu(true). The ingame flag hides General, Keyboard and Sound.
- Q: Is duck held or a timed slide? A: Held. duck.ogg means the player holds Down/S; unduck.ogg means they release it (dev, 2026-11-01). For the movement plan: Up while ducking, and Down in mid-air (flag 3) still need rules.
- Q: Can you duck forever? A: No. It auto-unducks after about 1 to 2 seconds. You can unduck early by releasing, but that raises the chance of smashing into something (dev, 2026-11-01).
- Q: (dev note) Lives key? A: L shows how many lives you have. H is unused (dev, 2026-11-01).
- Q: Does the no-networking rule remove the updater? A: No. The updater stays, because it isn't part of the game mechanics (dev, 2026-11-01).
