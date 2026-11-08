---
name: project_menu_music_rule
description: The menu music plays through every menu reached from the main menu and fades only when a run starts, when a document, the settings menu, learn sounds, change game version, test speakers or check for updates is opened from the main menu, for a clear, copy or export dialog, and on exit or restart game; run menus never play it (dev, 2026-11-07)
metadata:
  type: project
---

The dev (2026-11-07): "make it so the menu music does not fade unless you start the actual game in debug/normal/practice runs. The menu music should not play if you are in the pause menu, and other menus that aren't accessed within the main menu." Then: "The music fading can happen in the docks when you read them."

The rule: m.fade_music() is called only in play_game() (a debug, endless or practice run starting), change_game_version() (dev, 2026-11-07: "fade the music when I click, Change game version"), test_speakers() (dev, 2026-11-07: "fade the music when I test my speakers"), the main menu's check for updates, for its whole flow, menus and alert boxes (dev, 2026-11-07: "Fade the music when I check for updates. The hole menu flows, and it's alert boxes."), docksmenu() before dockread(), mainmenu() before settingsmenu() (dev, 2026-11-07: "fade it when you open the settings from the main menu"), learn_sounds_menu() (dev, 2026-11-07: "fade the music when you open learn sounds"), the dialogs of the six clear, copy and export items, right before their sound and message, not on the press, so a canceled clear keeps the music: clear_stats_menu(), copy_all_stats(), export_all_stats(), clear_all_progress(), copy_all_progress(), export_all_progress(), the export failures included (dev, 2026-11-07: "When you press the clear/copy/export buttons, it should fade so I can here the dlg.", then "It should only fade for the clear/copy/export dlg messages"; then, 2026-11-07: "The music does not come back after clearing stats", so m.play_music() right after each of those dialogs starts it again from the top), exit game and restart_game(). deps/setupmenu.nvgt: setupmenu() without music leaves playing music alone and only closes it when it has stopped, so menus reached from the main menu (achievements, statistics, the mode and difficulty menus, debug options, Yes/No questions) carry it on without restarting, while a run's menus (pause, F1, F2, buffer menu, session results, after death) find it faded and stay silent.

**Why:** before this, every setupmenu() without music closed the music, so opening a submenu cut it off and the game menu restarted it from the top.

**How to apply:** a new menu reached from the main menu just calls setupmenu(); don't add m.fade_music() to a new main menu item unless the dev asks. Related: [[project_menus_plan]].

No changelog entry (dev, 2026-11-07: "these menu changes do not require any change log mentions"), so 1.6 stays full at 10 of 10 with no 1.7 block for them.

Deliberately left over the music (dev, 2026-11-07: "You can leave them. That does it all for the menus"): the achievement description or locked hint dialog in the achievements lists, and the locked difficulty dialog in the difficulty menu, since they are opened often and a fade would restart the music each time. The menu music work is finished.

Menu sounds are cached (dev, 2026-11-08): setupmenu.nvgt's menu_sound(name) searches sounds/ui/menu/*name* once per launch and keeps every match, picking one at random each time, so the music, click, close, edge, enter, open and wrap lookups no longer hit the disk on every menu. A new ui/menu file added while the game runs is only seen after a relaunch.
