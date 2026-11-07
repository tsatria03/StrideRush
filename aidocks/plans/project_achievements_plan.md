---
name: project_achievements_plan
description: NOT STARTED, notes only (2026-11-06) - game achievements in the game menu, for a single run and for all your runs, with your progress on each one; read the statistics (48 stats per run, 54 lifetime values); then the game menu's three "all progress" items; Q&A log to come
metadata:
  type: project
---

Status: NOT STARTED. Notes gathered so far, before any questions (2026-11-06). The todo item: "Add game achievements in the game menu, for a single run and for all your runs, with your progress on each one."

Background:
- Built on the statistics ([[project_statistics_plan]], COMPLETE 2026-11-06), which were planned first because achievements read them (dev, 2026-11-05: "Before we even consider achievements. We have to start with statistics because achievements will link to them later.").
- Achievement style: Claude recommended text-based achievements like CookieCraze's (feats as well as counts, finishable goals, categories, hints and hidden entries, one line per achievement in a data file, threshold ladders through %threshold%) over ToyMania's generated number tiers ([[reference_toymania_scoring_difficulty]]); not settled.
- After achievements are built, and as this plan's last part before docks: the game menu's three "all progress" items, always shown (dev, 2026-11-06: "I want them always shown, but the achievements needs planning/building first before we add the last 3 global menu items."); see the statistics plan's last Q&A entry for ToyMania's versions and what not to copy.
- The "achievements" speech buffer already exists (sdr.nvgt), empty until achievements speak into it.

The stats there are to read (counted 2026-11-06, dev: "record the stat count for life and session in the achievements plan"):
- Tracked per run (stat_keys in globals/stats.nvgt): 48 (47 until caught_hazards joined, 2026-11-06), every one kept for the session and added into the lifetime: steps, time_running, top_speed (the lifetime keeps the highest), lane_changes; 10 obstacles got past (hazards, spikes and mines jumped, projectiles ducked, force fields switched off, animals scared, barriers dodged, walls broken, fake doors broken, real doors opened); damage_taken, lives_lost; 9 caught_<type> (hazards, spikes, mines, projectiles, force fields, animals, barriers, walls, doors); 18 item counts (picked up, broken and used for ammo packs, keys, steel shields, life capsules, health potions, player teleporters); ground and air powerups collected; melee swings, gunshots fired, gun reloads.
- Lifetime only: runs_played and runs_<level> for the five difficulties, so 54 saved lifetime values; plus the last played date and time, and the session's difficulty and how it ended (session_end_cause).
- On screen (checked by the dev, 2026-11-06): lifetime statistics shows 47 lines always (2 date and time, 1 runs played, 5 per difficulty, 4 running, 10 obstacles, 2 damage and lives, 18 items, 2 powerups, 3 weapons), plus the 9 "times hit by" and "fell into" lines (times fell into hazards added 2026-11-06), which always show since 2026-11-06 (dev: "always show them for consistency"), so 56; they show even with no save file (zeros and "never"). Session statistics shows 50 lines (difficulty, 4 running, 10 obstacles, 2 damage and lives, 9 "hit by", 18 items, 2 powerups, 3 weapons, run ended by), or just "You haven't played an endless run yet." with no session.

Q&A log:
- (none yet)
