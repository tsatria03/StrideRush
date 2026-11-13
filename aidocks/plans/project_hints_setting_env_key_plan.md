---
name: project_hints_setting_env_key_plan
description: COMPLETE (2026-11-12, 2.1 at 4 of 10) - a status key, V, that says which environment you're in, and saved mutes for every speech buffer (a practice hints setting was dropped for them); Q&A log
metadata:
  type: project
---

Status: COMPLETE (2026-11-12, 2.1 at 4 of 10).

Background:
- Suggestions 13 and 14 in [[project_suggestions]] (2026-11-12): the dev: "Let's do these 2 next. WHat key would be good for env status?"
  - A practice hints setting: a Game tab checkbox to turn the practice buffer's hints off (on by default), for players who know the obstacles.
  - An environment readout key: a status key saying which environment you're in, as L says your lane; today it's only announced on entering one (env.nvgt: "You've entered the X environment." in misc).
- Free letters in keyboard.ini (2026-11-12): F (info_score removed 2026-11-06), G, J, K, N, V, Y. The readouts today: H health, Z distance, C speed, T time, M shield, L lane, B heart rate, all in [info] and the status buffer.

Q&A log:
- Q: The environment readout key: N (in "environment", by the bottom-row readouts), G or V? (Asked 2026-11-12; Claude recommended N.) A: "I'd say V would be a better choice here." (dev, 2026-11-12). V, info_environment in keyboard.ini's [info].
- Q: V's words: short like L ("custom environment.") or a sentence ("You're in the custom environment.")? (Asked 2026-11-12; Claude recommended short.) A: "It should speak like the L key" (dev, 2026-11-12): "custom environment." in the status buffer.
- Q: The practice hints setting: "Speak hints during practice runs", on by default, last among the Game tab's checkboxes; off silences hints and the closing line, the death dialog unchanged? The dev: "Yes, but what about the practice buffer though?" Claude: a muted buffer still collects its messages silently; offered silent hints (still in the buffer, a remembered mute) or no hints at all (the buffer never appears), recommending silent. The dev: "isn't this setting already tecknicly possible, by muting the practice buffer?" Claude: yes, except mutes aren't saved between launches; offered dropping the setting, saving every buffer's mute, or keeping the setting; recommended saving mutes. A: "I think a saved mute state would be better, instead of a seprat hints setting. And this would apply to all buffers. Look at cookie craze to see how it handled saving mute states." (dev, 2026-11-12). The hints setting is DROPPED.
- CookieCraze's way (read only, games/CookieCraze/src/includes/main/functions/savefuncts.nvgt): in its prefs save, one bool per buffer, "buffer_muted_" + the buffer's name, skipping the buffers that can't be muted (all, alerts, critical); read if it exists after the buffers are made, written with the other prefs. Stride Rush's mute toggle already calls writepreffs() (settings.srf), so the same keys go there.

- Q: The plan: V as L does, saved mutes for every buffer in settings.srf (reset to defaults unmutes all), built together; entries "Added the V key, which tells you which environment you're in." and "Made it so a muted speech buffer now stays muted the next time you play."? The dev: "because the buffer mute saving is a feature on it's own, that practice entry should be reworded since it now applies to every buffer." Claude asked which entry; the dev: the mute one. Reworded as an Added entry: "Added saved buffer mutes, so any speech buffer you mute, such as practice, powerups or items, stays muted the next time you play." A: "Yes. That works." (dev, 2026-11-12).

Settled design (2026-11-12): info_environment=V in keyboard.ini's [info], speaking "<environment> environment." in the status buffer; every buffer's mute but all and alerts saved as buffer_muted_<name> in settings.srf, restored at startup, cleared by reset to defaults; the readme's V line and Shift plus M line; the two entries above.

Sections (built together, small):
1. The V readout and saved mutes: keyboard.ini, run.nvgt, savefuncts.nvgt (writepreffs(), load_buffer_mutes()), sdr.nvgt, settings_menu.nvgt's reset_settings(). Done.
2. Docks: the readme, the two 2.1 entries (4 of 10), CLAUDE.md, the version history, the index. Done. Plan COMPLETE.
- Tested (dev, 2026-11-12): both tests passed (V says the environment as L does, into status; a muted buffer stays muted after relaunching, and an unmute stays too).
