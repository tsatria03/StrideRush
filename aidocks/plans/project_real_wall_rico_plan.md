---
name: project_real_wall_rico_plan
description: SETTLED (2026-11-27, for 3.0, 2 sections): weapons ricochet off real walls with the new rico sounds (melee rico.ogg, guns rico1-12), after CaveDefender's ricochets; Q&A log
metadata:
  type: project
---

# Real wall ricochet plan

Goal (the dev, 2026-11-27): "I added rico sounds to all weapons. These will play for real walls if you try to hit it. Look at cave defender for how ricos work."

## Findings

- Sounds (rescanned 2026-11-27, untracked until the dev commits): game/equipments/weapons/melee/<weapon>/rico.ogg for all eight melee weapons; artillery/pistol and artillery/machine_gun each rico1.ogg to rico12.ogg. get_pack_sound(weapon_folder(w) + "*rico*") picks a random variant, and "*hit*" doesn't match them.
- CaveDefender (read only): play_wall_rico() plays a melee weapon's rico.ogg at the wall when a swing connects but does no damage; play_bullet_rico() plays a gun's random rico1-12 (plus a shell) where a bullet lands on a wall it can't hurt. No damage, no wall reaction.
- Stride Rush today: a real wall (ladder.nvgt, at l.wall_x, ladder_wall_gap past its ladder) is never a weapon target. weapon_strike() (weapons.nvgt) picks the nearest of walls (fake), fake doors, vehicles, items, insects and aircrafts and plays the weapon's hit at it; bullet_hits() (bullet.nvgt) does the same for a bullet's tile, adding the gun's shell. So a swing or shot at a real wall does nothing, and a bullet flies straight through it.

## Open questions

1. What a hit on a real wall does.
2. Changelog wording and docks.
3. Sections.

## Q&A log

- Q1, what a hit does. Claude recommended CaveDefender's way: a swing whose nearest target in reach is a real wall plays the weapon's rico.ogg at the wall in place of its hit, no damage; a bullet reaching a real wall's tile stops there with one of the gun's rico1 to rico12 and its shell in place of the hit, the round spent; a real wall blocks what's behind it (a swing or bullet can't pass it); no statistic, and the climb is untouched (only the ladder gets you past). Dev: "That's perfect. agreed". Settled.
- Q2, changelog, docks and learn sounds. Changelog, on top of 3.0's block: "Added ricochets for every weapon, so swinging at or shooting a real wall now plays a ricochet off it instead of doing nothing, and a bullet stops there instead of flying through." Docks: real_walls.txt (after "tall walls you can't break": a swing or shot ricochets off with your weapon's ricochet sound, no damage, nothing behind it hit until you're past), weapons.txt (after "Real doors and real walls can't be harmed.": a real wall answers with a ricochet and stops bullets). Learn sounds: learn_sound_name() lists "rico" as "ricochet"; the guns' rico1 to rico12 are one entry with 12 versions. Dev: "that works". Settled.
- Q3, sections. Claude recommended two: the ricochets (ladder.nvgt's real_wall_in_reach() and real_wall_at(), weapon_strike() and bullet_hits(), learn sounds' "ricochet", the language files), with tests; then the docks. Dev: "yes". Settled.

PLAN SETTLED (2026-11-27): ready to commit with the 32 rico sounds, then build Section 1 on the go-ahead.

## Sections

1. The ricochets (tests): ladder.nvgt's real_wall_in_reach(reach) and real_wall_at(x) (a ladder whose real wall still stands ahead); weapon_strike() counts a real wall as the nearest target, blocking anything behind it, and the swing plays the weapon's *rico* at it instead of its hit; bullet_hits() stops a bullet on a real wall's tile with *rico* and *shell*; learn_sound_name() "rico" as "ricochet"; template.lng refreshed and english.lng synced.
2. The docks (no tests): the changelog entry, real_walls.txt, weapons.txt.
