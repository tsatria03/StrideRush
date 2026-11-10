---
name: project_footstep_volume_plan
description: COMPLETE (2026-11-10, 1.9 at 6 of 10; 3 sections) - a footstep volume slider in the Game tab (steps only), and the heartbeat's F7/F8 volume keys removed; Q&A log
metadata:
  type: project
---

Status: COMPLETE (2026-11-10, 1.9 at 6 of 10). Started 2026-11-10, with 1.9 at 4 of 10.

Background:
- The dev (2026-11-10): "I want to be able to adjust the footstep volume in the game tab."
- Now: play_step() in surface.nvgt plays objects/platforms/<tile>/*step* through the shared player pool p with play_stationary(), at full volume, on every grounded step (ledge tiles included). A landing plays objects/platforms/<tile>/*land* and, with with_player_sound, misc/player/*land* (player.nvgt), also through p. A hazard fall plays the tile's *fall* (endrun.nvgt).
- The pattern to follow: the heartbeat volume ([[project_heartbeat_plan]], heartbeat.nvgt): heartbeat_volume in dB (-100 to 0), played with play_stationary_extended() at that volume, a Game tab slider "Game heartbeat volume," (0 to 100 percent = -100 to 0 dB, applied on save, [[project_volume_sliders_plan]]), saved in settings.srf, and in-run keys (Shift+Home/F8, Shift+End/F7). The Game tab's sliders now: ambience, heartbeat, music.

Q&A log:
- Q: Which sounds should the footstep volume cover: steps only (ledges included), steps and landings, or steps, landings and falls? (Asked 2026-11-10; Claude recommended steps and landings.) A: "I only want to turn down step sounds only, not fall/land sounds" (dev, 2026-11-10). Only play_step()'s *step* sounds.
- Q: Should footsteps get their own in-run volume keys (F9 lower, F10 raise), or just the Game tab slider? (Asked 2026-11-10; Claude recommended the slider only.) A: "I have a better idea. The heart/step volumes should only belong in the game tab." (dev, 2026-11-10). Footsteps: a Game tab slider only. The heartbeat's in-run keys (heartbeat_up F8, heartbeat_down F7 in keyboard.ini; run.nvgt) to go, leaving its slider; confirmation asked next.
- Q: Remove the heartbeat volume keys (heartbeat_up F8 and heartbeat_down F7 from keyboard.ini, their checks in run.nvgt, change_heartbeat_volume() in heartbeat.nvgt; the readme's F8 and F7 lines and mention), keeping the Game tab slider and B, with its own changelog entry ("Removed the F7 and F8 keys for the heartbeat volume, ...")? (Asked 2026-11-10.) A: "Yes. Make the step slider a seprat entry" (dev, 2026-11-10). Two 1.9 entries: the footstep slider (Added) and the heartbeat keys (Removed).
- Q: Where should "Game footstep volume," go among the Game tab's sliders (ambience, heartbeat, music)? (Asked 2026-11-10; Claude recommended after the heartbeat, starting at 100 percent, 0 dB, as now, and back to 100 on a settings reset.) A: "footsteps should go before heartbeat" (dev, 2026-11-10). Order: ambience, footstep, heartbeat, music. The 100 percent default and reset weren't objected to.

Settled design:
- footstep_volume, in dB (-100 to 0), default 0 (full, as now), saved in settings.srf as "footstep_volume", back to 0 on a settings reset. Only play_step()'s objects/platforms/<tile>/*step* sounds use it (ledges included), through play_stationary_extended() on p; landings and falls stay at full volume.
- "Game footstep volume," in the Game tab, 0 to 100 percent = -100 to 0 dB, applied on save, between the ambience and the heartbeat sliders. In both the main menu's settings and mid-run F2. No in-run keys.
- The heartbeat's in-run volume keys go: heartbeat_up (F8) and heartbeat_down (F7) out of keyboard.ini, their checks out of run.nvgt, change_heartbeat_volume() out of heartbeat.nvgt. Its slider and B stay.
- Two 1.9 changelog entries: an "Added" for the footstep slider, a "Removed" for the heartbeat keys.

Sections:
1. The footstep slider: footstep_volume (in surface.nvgt, with play_step()); readpreffs() and writepreffs() in savefuncts.nvgt; settings_menu.nvgt's new_step_vol, the slider before the heartbeat's, its read on save, reset_settings() and apply_volume_settings() taking it.
2. The heartbeat keys removed: keyboard.ini (LF), run.nvgt, heartbeat.nvgt (the function and heartbeat_volume's comment).
3. Docks: the readme (the settings section's Game tab, the key list's F8 and F7 lines, the heartbeat paragraph), both changelog entries, CLAUDE.md, this plan COMPLETE.
- Section 1 built (2026-11-10): footstep_volume in surface.nvgt, play_step() through play_stationary_extended() at it; readpreffs()/writepreffs() "footstep_volume"; settings_menu.nvgt's new_step_vol and step_vol_slider between ambience and heartbeat, read on save, reset to the current value on cancel, 0 on reset_settings(); apply_volume_settings() takes it last (step).
- Section 1 tested (dev, 2026-11-10): "It should be footsteps volume, not, footstep volume. Also it works." The slider is now "Game footsteps volume,". Section 1 COMPLETE.
- Section 2 built (2026-11-10): heartbeat_up and heartbeat_down out of keyboard.ini (found CRLF now, kept as is), their checks out of run_input() in run.nvgt, change_heartbeat_volume() out of heartbeat.nvgt, heartbeat_volume's comment updated.
- Section 2 COMPLETE (dev, 2026-11-10): both tests passed (F7 and F8 do nothing and are gone from F1; the heartbeat slider still works, B too).
- Section 3 (docks) done (2026-11-10): the readme's F8 and F7 lines removed, the heartbeat paragraph points to its slider, the settings section's Game tab and starting volumes name the footsteps; two changelog entries (Added, Removed); CLAUDE.md. Plan COMPLETE.
