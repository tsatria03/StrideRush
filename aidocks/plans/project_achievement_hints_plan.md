---
name: project_achievement_hints_plan
description: COMPLETE (2026-11-12, 2.1 at 2 of 10) - from the achievement audit: four stale hints and seven hints naming rebindable keys, reworded; Q&A log
metadata:
  type: project
---

Status: COMPLETE (2026-11-12, 2.1 at 2 of 10).

Background:
- The achievement audit (suggestion 12 in [[project_suggestions]], 2026-11-12) found all 130 achievements earnable, with four stale hints (Endurance, Smash and Dash, Potion Lover, Punching Bag) and seven naming keys that can be rebound (Doorman, Key Holder, Locked and Loaded, Shielded: U; Reloader: R; Heavy Hitter, Trigger Happy: space). The dev (2026-11-12): "these need fixing first. Also the achivements that mention bindable keys also need fixning as well." The long shots (Speed Shopper, Ice Skater, Trampoline Artist) are left for now.
- Related: [[project_door_achievements_plan]] (the door fix that started the audit); the practice guidance plan's rule that no practice line names a key, now extended to achievement hints.

Q&A log:

- Q: The eleven new hints (At top speed the steps pile up fastest. Hold on there, and they take care of themselves.; Fake walls start turning up once the belt reaches 3.3 steps a second.; Potions come most often on easy and get rarer on each harder level. Drink them as you go.; Barriers hit hardest of anything you can run into. Not that you should go looking for them.; Every real door has its key somewhere before it. Grab the key, then use it from your inventory to unlock the door.; Use a key from your inventory once a real door is within about two seconds of you.; Hold the gun you want to fill, then use the pack from your inventory.; Put a shield on from your inventory before the trouble starts, not after.; Reload any time a gun isn't full, and wait for the ping.; Melee weapons swing up to five times a second. Keep swinging.; The machine gun keeps firing while you hold the fire key. It adds up fast.) and the 2.1 entry "Fixed a bug where some achievement hints were out of date, or named keys that may no longer be the ones you use."? (Asked 2026-11-12.) A: "These all work. Just like last time, try to do all of the sections, if they are small enough of course." (dev, 2026-11-12).

Settled design (2026-11-12): the eleven hints above in achievements.ini; achievement hints name no keys from now on; the entry above (2.1 at 2 of 10).

Sections (both built together, at the dev's word):
1. achievements.ini: the eleven hints. Done.
2. Docks: the 2.1 entry, CLAUDE.md, the version history, the index. Done. Plan COMPLETE.
- Tested (dev, 2026-11-12): the test passed (Endurance, Smash and Dash, Doorman, Reloader and Trigger Happy read their new hints).
