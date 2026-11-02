---
name: reference_cavedefender_buffer
description: Stride Rush's speech-buffer system comes from CaveDefender's client deps/buffer.nvgt (newer and less buggy than ToyMania's); what it does, its keys, and the CaveDefender-only parts to adapt
metadata:
  type: reference
---

Source: the dev's CaveDefender game, in Stride Rush's user/ folder at user/CaveDefender-main/src/client/includes/main/deps/buffer.nvgt (423 lines). The file is gitignored here. Treat it as read only, like the other reference games ([[reference_simplefighter_readonly]]). The dev chose it over ToyMania's 243-line buffer.nvgt on 2026-11-01, because ToyMania's has bugs and CaveDefender's is more up to date.

STATUS 2026-11-01: the dev copied it unchanged into Stride Rush as src/includes/main/deps/buffer.nvgt. deps/ is glob-included, so it compiles with the game, and as-is it references things Stride Rush doesn't have:
- the spool pool and the logfile global
- net_keepalive_cb
- alt_is_down, shift_is_down, control_is_down and convert_to_pitch
- the CaveDefender logs path
- sounds/ui/misc and sounds/ui/buffer clips that don't exist yet
ADAPTED the same day (dev go-ahead):
- Removed: net_keepalive_cb, ensure_buffer and remove_buffer (rank-gated chats), and format_number. Counts are plain numbers now.
- Logs go to tsatria03/StrideRush/logs through buffer_log_dir().
- Sounds come through get_pack_sound: ui/buffer/*switch* and *choose*, and ui/other/*toggleon* and *toggleoff*.
- buffer_menu() uses setupmenu() and item ids instead of numeric indexes.
- The four item-nav functions share a new announce_buffer_item().
- The local "temp" in add_buffer_item was renamed to "item", so it no longer shadows the global temp pool.
- buffercheck() reads the keyboard.ini [buffer] actions with controls.action_triggered(), so each binding's own trigger applies. It checks review before copy (the Alt+Shift+C caveat).
- buffercheck() isn't called anywhere yet; the game loop will call it.
- Later the same day: categories "all" and "misc" are created at startup. The class's interrupt default was flipped to true (CookieCraze-style), and lines arrive through speak_buffer() in speech.nvgt ([[project_first_build_plan]] question 4).

What it does:
- Named buffers (categories) of spoken messages. An "all" buffer is created automatically and collects every message. "alerts" and "all" can't be muted.
- add_buffer_item(buffer, text, speak) logs a message and speaks it unless that buffer is muted.
- Empty categories are hidden from navigation, except all and alerts.
- Navigation has hard stops at the ends (no wrap), and a single item re-announces itself.
- Item and category cues are panned and pitched by position. The cue sounds are sounds/ui/buffer/choose.ogg and switch.ogg, plus ui/misc/toggleon and toggleoff for muting.
- Copy an item or the whole buffer, review in a read-only box (vd.info_box), and export to an AppData logs folder. Exporting a buffer also clears it.
- A Shift+B buffer menu covers all of these actions.

Keys, in buffercheck(), which reads raw key_repeating:
- Comma and period: previous and next item.
- Shift+comma and Shift+period: first and last item.
- Left and right bracket: previous and next category.
- Shift+brackets: first and last category.
- Shift+M: mute the buffer.
- Shift+C: copy the item.
- Alt+Shift+C: review the item.
- Shift+B: buffer menu.
- Shift+backslash: export, then clear.

CaveDefender-specific parts to adapt when porting:
- the logs path, tsatria03/CaveDefender/logs
- remove the net_keepalive_cb background callback in buffer_menu. Stride Rush is offline with no networking ([[project_tech_decisions]]).
- remove ensure_buffer and remove_buffer (rank-gated staff chats) and all of CaveDefender's multiplayer buffer names (chats, connections, staff and private chats, leaderboards). Stride Rush's own categories are still to be decided.
- the spool pool and the logfile global
- helpers from its extrafuncts: shift_is_down, alt_is_down, control_is_down and convert_to_pitch
- the sound paths, which must fit Stride Rush's tree ([[project_sound_layout]])
- the raw key_repeating input, which should probably route through key_config ([[project_controls_plan]])
- writepreffs() saving the mute state

**How to apply:** port it when the buffer system is built, after the plan discussion ([[feedback_plans_record_qna]]).
