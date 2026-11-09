---
name: project_dlg_enter_only
description: dlgmessage_return() dialogs close with Enter only and say " Press enter to continue." (space removed by the dev, 2026-11-09); don't write "enter or space" in docs, speech or comments
metadata:
  type: project
---

The dev (2026-11-09): "I took the space key out of dlg.nvgt, and the space wording, so now it's just press enter to continue."

deps/dlg.nvgt's dlgmessage_return(msg) shows msg + " Press enter to continue." and closes on Enter (and the A key, as the hand key); space no longer closes it. Space was added in 1.3 (the 1.3 changelog's "space now also closes a dlg message" stays as history).

**How to apply:** readme, changelog and speech say "press enter", never "enter or space"; plans written before 2026-11-09 that say "Enter or space" describe the old behavior. Code that waits for keys to lift after a dialog may still list KEY_SPACE harmlessly. Related: [[project_settings_plan]], [[project_practice_deaths_plan]].
