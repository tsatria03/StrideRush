---
name: project_controls_plan
description: SETTLED, PARTLY BUILT (jump, crouch, L/Z/C/T readouts, volume, pause, Alt+F4, buffer keys, hands, weapons, X ammo, R reload and the I, Shift+I and U inventory keys work; lanes, F score, F1 and F2 not yet) - Stride Rush in-game key layout (dev-set 2026-11-01), rebindable via SimpleFighter's key_config; item keys and jump/duck overlap deferred to later plans; includes a Q&A log
metadata:
  type: project
---

Status: SETTLED 2026-11-01. PARTLY BUILT in the first build (2026-11-02): every binding is in keyboard.ini. The keys with code behind them are jump, crouch (held, with a 1.5 s auto-stand and a 1 s cooldown), the L, Z, C and T readouts, the volume keys, pause, Alt+F4 and the buffer keys. Lanes, hands, weapons, F (score), F1 and F2 are bound but unread until their features are built. UPDATE 2026-11-02: the hands now work (force fields), and so do the weapon keys (1 to 0, Space, X, R), with a new fire_held = SPACE:down for the machine gun ([[project_weapons_plan]]). Two things are deferred: the item keys go to the items plan (the brackets are taken by the buffer), and the jump/duck overlap rules go to the movement plan ([[feedback_plans_record_qna]]).

Keys set by the dev (2026-11-01). Every action is rebindable through SimpleFighter's key_config class (deps/key_config.nvgt, already in Stride Rush) and a keyboard.ini, like SimpleFighter's data/main/config/keyboard.ini ([[reference_simplefighter_architecture]]):
- Up or W: jump.
- Down or S: duck, held. duck.ogg plays on press. Ducking auto-unducks after about 1 to 2 seconds even if the key is still held (tunable), and releasing early unducks sooner; unduck.ogg plays either way. Unducking early raises the chance of smashing into what you were ducking under (dev, 2026-11-01). Slides under obstacles you can't jump.
- Left or Q: lane switch left ("turning"). Lanes are a later expansion, so these keys are reserved now (FINAL, dev, 2026-11-02).
- Right or E: lane switch right (reserved, as above).
- How hands work (dev, 2026-11-02): either hand opens doors and turns off force fields. REVISED (dev, 2026-11-02): every hand sound (switch press, item pickup, and door openings later) plays STATIONARY and centered, never panned to the hand. The dev first wanted panning, then dropped it because it "sounds too far to the left and or right". hand_pan was removed from tuning.nvgt ([[project_force_fields_plan]]).
- Items rule (dev, 2026-11-02, from ammo packs; applies to future items such as the keys too): an item is picked up with either hand. Its get sound plays STATIONARY, centered and not panned, like every hand sound (dev, 2026-11-02). The pickup speaks ONLY the item's name, such as "ammo pack", not "You picked up an ammo pack." (dev, 2026-11-03). misc/player/give plays together with get as the item goes into the inventory (dev, 2026-11-03, during testing; ToyMania's item, key and toy pickups do the same). The pickup window is the same as the force field switch: any step of the usual countdown before it, and always at least the last switch_min_time. Running right onto an item, or landing on it from a jump, breaks it, and it's lost. A clean jump over it just misses it ([[project_weapons_plan]]).
- Tab or A: left interact hand, for doors and similar objects (FINAL, dev, 2026-11-02).
- Enter or D: right interact hand, for doors and similar objects (FINAL, dev, 2026-11-02).
- Space: shoot with an ammo weapon, or swing a melee weapon (ToyMania-style). Space only; no left or right Control (settled 2026-11-01).
- X: ammo check, for non-melee weapons.
- R: reload an ammo weapon.
- 1 through 0: select a weapon (ten slots).
- Alt+F4 (during a run only): quit the whole program, no confirm (dev, 2026-11-02).
- Escape or P: pause, which opens a pause menu. The pause menu does NOT hold settings (changed 2026-11-01; see F2).
- Buffer keys (CaveDefender's, kept as-is): comma and period for messages, the brackets for categories, Shift with either pair for first and last, Shift+M mute, Shift+C copy, Alt+Shift+C review, Shift+B buffer menu, Shift+backslash export.
- F1 (during a game): open the view-key-bindings screen, the same one as the settings Keyboard tab's "View current keyboard bindings". It pauses the run while open (settled 2026-11-01).
- F2 (during a game): open the settings panel, SimpleFighter-style tabs. No Alt-letter shortcuts. During a run it shows only the Game, Menu and Speech tabs; General, Keyboard and Sound are hidden, exactly like SimpleFighter's settingsmenu(true). Viewing key bindings mid-run is F1's job (settled 2026-11-01).
- L: lives readout, how many lives you have (dev, 2026-11-01). H is UNUSED; it was the health/lives key, replaced by L. There's no separate health, only lives.
- Z: distance traveled readout (moved from Q, dev, 2026-11-02).
- C: current speed readout, spoken as the step time in ms (moved from E, dev, 2026-11-02).
- T: time in this run readout.
- F: score or money readout.
- Home and End: ambience volume (also F6 up and F5 down since 2026-11-06, dev: "f3/f4=music, and f5/f6=ambience").
- Page Up and Page Down: music volume (also F4 up and F3 down since 2026-11-06).

Later features named by these keys: ducking, weapons (number row plus fire, ammo check and reload), the two interact hands, lanes, a pause menu, and separate ambience and music volume.

keyboard.ini WRITTEN 2026-11-01 at sdr/data/config/keyboard.ini (CRLF, 46 bindings). It replaced the dev's copied SimpleFighter file entirely. Action names, by section:
- [movement]: jump, duck (press), duck_held (down), duck_release (release), lane_left, lane_right
- [interaction]: hand_left, hand_right
- [combat]: fire, ammo_check, reload, weapon_1 to weapon_10 (keys 1 to 0)
- [info]: info_lives, info_distance, info_speed, info_time, info_score
- [volume]: ambience_up and ambience_down (Home and End), music_up and music_down (Page Up and Page Down), all repeating
- [screens]: pause, view_bindings (F1), settings (F2)
- [buffer]: buffer_item_previous, buffer_item_next, buffer_item_first, buffer_item_last, buffer_previous, buffer_next, buffer_first, buffer_last, buffer_mute, buffer_copy_item, buffer_review_item, buffer_menu, buffer_export

Notes:
- The buffer keys are in keyboard.ini so key_config's consumed-key rule can work. A single-key binding (hand_right on C, or the bracket keys) is skipped in any frame where a held modifier combo on the same key fires (Shift+C copy). If the buffer read raw keys, as CaveDefender's buffercheck() does, Shift+C would also fire the right hand.
- Caveat for coding: the consumed rule only protects single-key bindings. Alt+Shift+C (review) also satisfies Shift+C (copy), because copy's only modifier, Shift, is down. The buffer code must check review first, or skip copy while Alt is held, the way CaveDefender reads C once and branches on Alt.
- Code should query actions with controls.action_triggered(name). It uses each binding's own trigger from the ini (press, :repeat, :down, :release), so the ini decides behavior. action_pressed and action_repeating override the ini's trigger. controls is loaded at startup by load_controls() (functions/contfuncts.nvgt, renamed from controlfuncts.nvgt by the dev, 2026-11-04).
- Letters and digits resolve through SDL key names (kc_name_to_code falls back to get_key_code), so 1 to 0 and the letter keys need no registration.

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
- Q: Overlap (flag 3): Up while crouched, and Down in mid-air? A: Up while crouched cancels the crouch and jumps right away, skipping unduck. Down in mid-air is ignored (dev agreed with Claude's recommendation, 2026-11-01).
- Q: Is ducking a crouch or a slide? A: More of a crouch (dev, 2026-11-01). Footsteps keep playing while ducked. REVISED after playtesting (dev, 2026-11-02): no footsteps while crouched; steps felt wrong, and similar runners go silent.
- Q: (dev, 2026-11-02) Why does a single tap of Down duck and then unduck at once? A (Claude): the crouch is held, so releasing ends it, and a tap is a press and release. The alternative, a tap giving a full 1.5 s crouch, would lose standing up early by releasing. The dev chose to keep the held crouch "for now".
- Q: Can you duck forever? A: No. It auto-unducks after about 1 to 2 seconds. You can unduck early by releasing, but that raises the chance of smashing into something (dev, 2026-11-01).
- Q: (dev note) Lives key? A: L shows how many lives you have. H is unused (dev, 2026-11-01).
- Q: Adapt the dev's copied SimpleFighter keyboard.ini to this plan, with the buffer keys included? A: Yes (dev, 2026-11-01). Written as listed above.
- Q: F1 and F2 in the first playable build? A: Leave both out for now (dev, 2026-11-01). The bindings stay in keyboard.ini for later.
- Q: (dev, 2026-11-02) Key switch: Q and E become the left and right hands instead of Z and C. Tab and Enter stay as the other hand keys. That frees Z and C. A: Z replaces Q for distance and C replaces E for speed (dev, 2026-11-02). keyboard.ini updated: hand_left=TAB,Q, hand_right=RETURN,E, info_distance=Z, info_speed=C. Plain C (speed) and Shift+C (buffer copy) don't clash thanks to the consumed-key rule.
- Q: (dev, 2026-11-02) Final keyset decision? A: A and D are the left and right hands (with Tab and Enter). Q and E are for turning, meaning switching lanes when lanes arrive (with Left and Right). This supersedes Q and E as hands and A and D as lanes. keyboard.ini: hand_left=TAB,A, hand_right=RETURN,D, lane_left=LEFT,Q, lane_right=RIGHT,E. Readouts stay on Z (distance) and C (speed).
- Q: (dev, 2026-11-02) Alt+F4? A: Quits the entire program, only within an actual run, with no confirm. It says "exiting" (the same word as the main menu's exit) and closes. keyboard.ini [screens]: exit_program=ALT+F4, read in run_input().
- Q: Does the no-networking rule remove the updater? A: No. The updater stays, because it isn't part of the game mechanics (dev, 2026-11-01).

CHANGED (dev, 2026-11-03, shields plan [[project_shields_plan]]): the lives readout moves from L to H, freeing L, and M becomes the shield readout ("Shield strength, x percent."), checked after Shift+M (buffer mute). To be built with shields. BUILT with shields.

CHANGED (dev, 2026-11-03, menus plan [[project_menus_plan]]): "P should be reserved for the pause menu", and Escape during a run asks "Are you sure you want to quit this run? ..." directly. keyboard.ini [screens]: pause=P (was ESCAPE,P) and a new quit_run=ESCAPE. BUILT.

ADDED (dev, 2026-11-04, outside the lanes plan, with new misc/player sounds clap1-3 and woosh): "The clap sounds are for pressing a/d at the same time, and or tab/enter. The woosh sound is for using your hands. You hear it after pressing a/d, and or tab/enter. a/tab at -50 pan, and d/enter for plus 50 pan. These sounds will not play if you grab/open stuff. The clapping, I'll discuss what that does later. You can put the sounds in the code, but it will not do anything except playing the sounds." BUILT 2026-11-04 on top of 921e85c: hand_check() in forcefield.nvgt reads both hands; when no field, door or item took the press, empty_hand_sound() claps (centred, *clap*) if both hands were pressed on the same frame or one was pressed while the other was held (action_down), and otherwise plays *woosh* at -50 for the left hand or +50 for the right. Sounds only. Pressing the second hand a moment after the first gives a woosh then a clap. Awaiting tests.
- Test 1 (A and Tab woosh at -50, D and Enter at +50, with nothing in reach) passed (2026-11-04).
- CHANGED (dev, 2026-11-04: "I don't like how it plays the clap and woosh at the same time upon pressing both your left and right hand together."): a lone empty hand's woosh now waits clap_window (100 ms, tuning.nvgt) before playing (woosh_pending_side and wooshtimer in forcefield.nvgt, flushed by play_pending_woosh() at the top of hand_check()); the other hand inside that window turns it into the clap instead. The same hand twice plays the first woosh at once. reset_player() clears a waiting woosh.
- Test 2 (A with D and Tab with Enter give only a centred clap; holding one then pressing the other claps; a lone A still wooshes left after the short wait) passed (dev, 2026-11-04: "That's much more realistic."). BUILT AND TESTED. Docks are still to write (a 1.4 changelog entry and the readme's hand keys) whenever the dev wants them; what a clap does comes later.
- Claps later scared animals and the docks were written with the animals plan ([[project_birds_plan]]).
- CHANGED (dev, 2026-11-04, during the lanes plan's Section 3: "Please make your hand woosh sounds play in the center again."): play_pending_woosh() plays the woosh centred for either hand; the -50/+50 pan is gone. woosh_pending_side still tells left from right for the clap check. The readme's clap line now says "a single hand makes a whoosh" ("to that side" dropped, 2026-11-04). The dev heard it centred and it passed; no changelog entry, since 1.4 isn't released and its animals entry only says "your hands now make a sound".
- CHANGED (dev, 2026-11-06: "A user suggested that I/O should be used for inventory nav. Instead of I/Shift I", then "I=prev, and o=next."): inventory_previous=I and inventory_next=O in keyboard.ini (Shift+I dropped; O was unbound); the readme's two key lines and a 1.6 changelog entry follow.
- REMOVED (dev, 2026-11-06: "Please remove that unused key"): info_score=F, the score or money readout reserved on 2026-11-01, which no code ever read; scoring was dropped from the todo list on 2026-11-05 and the statistics plan has no score. F is unbound now.
- REMOVED (dev, 2026-11-08, for 1.7: "Please remove alt f4 to completely quit the game ... Look in keyboard.ini"): exit_program=ALT+F4 is gone from keyboard.ini [screens], its check (end_run_stats(), "exiting", exit()) from run_input() in run.nvgt, and its line from the readme's keys.
