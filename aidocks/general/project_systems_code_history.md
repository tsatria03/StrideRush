---
name: project_systems_code_history
description: decision history moved out of the comments of the items and remaining systems in globals (weapons, bullet, ammo, keys, shield, capsule, potion, teleporter, powerup, inventory, heartbeat, stats, achievements, timerun, freerun, freebelt, updater, dec, fadepool) by the comment cleanup's Section 4 (2026-11-15); read before changing one of them
metadata:
  type: project
---

Moved here from the comments of nineteen files in src/includes/main/globals/ on 2026-11-15 ([[project_comment_cleanup_plan]], Section 4), so the code keeps only what it does and why. Dates are when the dev decided; quotes are the dev's own words. The plans named hold the full Q&A. The rest of globals is covered by [[project_tuning_history]], [[project_core_code_history]] and [[project_obstacle_code_history]].

## weapons.nvgt
- The weapons (2026-11-02, [[project_weapons_plan]]). weapon_strike() as the target hook for walls, fake doors and items (2026-11-03, for 1.1).
- The lineup, alphabetical with the guns last on 9 and 0 (the weapon lineup plan, 2026-11-06, [[project_weapon_lineup_plan]]): the boot and laser sounds went and the axe and sword came ("Keep it alphabetical, and remap the damages to it"); later that day the boot came back and the axe went. The feat became the dagger on 2026-11-15.
- The starting weapon: the bat from 2026-11-02, the axe for part of 2026-11-06, the fist since 2026-11-10.
- draw_sound as its own sound, so a new draw cuts the last one off and quick swaps never stack (2026-11-09).
- Guns fire traveling bullets (2026-11-03, [[project_bullets_plan]]); the shell plays at the target (the dev: "shell plays on hitting the object").
- A practice run's gun reserve never runs out (2026-11-05).

## bullet.nvgt
- Bullets (2026-11-03, for 1.1, [[project_bullets_plan]]). An item in a bullet's path breaks (2026-11-03). The shell plays at the target, at the dev's word.

## ammo.nvgt
- Ammo packs (2026-11-02, [[project_weapons_plan]]): the first item and the model for later ones. get plays centered, stationary and not panned (2026-11-02). Get and the player's give play together, and the pickup speaks just the item's name, at the dev's word.
- A random lane since the lanes plan's Section 4 (2026-11-05).
- Weapons break items too (2026-11-03).
- Break plays stationary, so its pitch never drops behind you (2026-11-05). The same for keys, shields, capsules and potions.
- A pack refills only the gun you're holding (2026-11-03).

## keys.nvgt
- Keys (2026-11-03, [[project_keys_plan]]). Any key opens any real door, at the dev's word. A random lane since the lanes plan's Section 4 (2026-11-05). Weapons break keys like packs (2026-11-03).

## shield.nvgt
- Shields (2026-11-03, for 1.2, [[project_shields_plan]]). The obstacle's hit layers with the shield's when one absorbs a blow (2026-11-03). An emptied shield plays death alone, with no speech (2026-11-03).
- Debug shields (2026-11-03): one until 2026-11-05, then two ("in debug, you'll have 2 shields in your inv"). "all" gets none, since it plays like the real game. The combination choices joined the list on 2026-11-11, and the slides debug choice gets them too (2026-11-11).
- Practice shields: every practice run had one from 2026-11-05. None for hazards since 2026-11-11 ("They should not come with a shield for hazards"), and none for floor breakers, a fall too (the floor breakers plan, 2026-11-13).
- The free run M readout with amounts (2026-11-13), worded "endurance remaining" (2026-11-14): "Shield strength, 50 percent, 400 of 800 endurance remaining."

## capsule.nvgt
- Life capsules began as life potions (2026-11-03, for 1.2, [[project_potion_teleporter_plan]]). They were renamed to life capsules with new sounds on 2026-11-04, and the old potion sounds became the health potion.
- A capsule gave exactly 1 life until 2026-11-04 ("between 1 to 2 lives"). The cap: "You can have unlimited life capsules, but limited lives". "Gained N lives." is the dev's wording (2026-11-04). Its use sound only, not the life sound, at the dev's word.

## potion.nvgt
- Health potions (2026-11-04, for 1.4, [[project_health_potion_plan]]), with the old life potion sounds. Small on purpose: "I don't want those to be too strong". "You're already at maximum health." is the dev's wording (2026-11-04).

## teleporter.nvgt
- Player teleporters (2026-11-03, for 1.2, [[project_potion_teleporter_plan]]). In a random lane since the lanes plan's Section 4 (2026-11-05).
- The break sound is stationary, so its pitch never drops behind you (2026-11-05).
- Never onto an obstacle (2026-11-03: "It can never land you exactly on the obstacle, like on top of a hazard.").
- The teleport's landing is the tile's only, like a force field's throw (2026-11-03).

## powerup.nvgt
- Powerups (designed 2026-11-03, built 2026-11-04 for 1.3, [[project_powerups_plan]]). A missed powerup breaks with powerbreak (2026-11-13); until then it kept sounding and faded behind you.
- One per kind, never stacking (dev: "I do not want the same type of powerup to stack up").
- Not looped, a one-shot on a timer (2026-11-04).
- The 14 names (2026-11-04): the shield pair was Shield Boost and Shield Crack, made timed and renamed; Tough Hide and Soft Hide added; Muffled Steps dropped.
- A slide doubles your current speed, powerups included (the slides plan, 2026-11-11); no air powerups along a slide (2026-11-11).

## inventory.nvgt
- The inventory (2026-11-02, [[project_weapons_plan]]), first on I, Shift+I and U.

## heartbeat.nvgt
- The heartbeat plan (2026-11-08, [[project_heartbeat_plan]]); the breathing was taken out (2026-11-08: "I didn't like them").
- The line: "5=500, and 150=200", then "Put the max heart rate to 155 at 150ms", one straight line (2026-11-08).
- heartbeat_volume's F7 and F8 keys were removed in the footstep volume plan (2026-11-10).
- Quiet on a slide (2026-11-11) and standing in a free run (2026-11-13). The B readout (2026-11-08).

## stats.nvgt
- Game statistics: the statistics plan (2026-11-05, built from 2026-11-06, [[project_statistics_plan]]); one set covers every difficulty (2026-11-06).
- What ended the run: Section 3. last_caught_kind: the practice guidance plan's Section 3. Clear game statistics: Section 5.
- practice_pass(): the practice locks plan (2026-11-10). Timed runs keep their own records (the timed run plan); the timed records clear with the lifetime (2026-11-13). Best runs clear with the lifetime (the achievements plan).

## achievements.nvgt
- Achievements: the achievements plan's Section 1 (2026-11-06, [[project_achievements_plan]]). The announcement includes how you got it (2026-11-06).

## timerun.nvgt
- Timed runs: the timed run plan (2026-11-13, Section 1; records, results and achievements in Section 2, [[project_timed_run_plan]]). Records kept separate from endless (2026-11-13: "I want them seprat if possible").
- The warning rearm (2026-11-13). T's wording with no "and" (2026-11-13). "on the clock" (2026-11-13), after "to the finish line" sounded like a deadline.

## updater.nvgt
- The updater (2026-11-05, [[project_updater_plan]]). The error-page check came from GitHub's "Not Found" for a private repository's release (2026-11-05). Extracting into the current folder (2026-11-05).

## dec.nvgt
- HRTF and behind pitch on by default (2026-11-05). The learn sounds settings (2026-11-05). auto_check_updates off by default since 2026-11-10 (on from 2026-11-05).
- APPDATA_DIR (2026-11-04). One settings file (2026-11-04: "I still want settings.srf, not split").
- game.srf: the game menu refactor plan's Section 6 (2026-11-06), with its own key (2026-11-06).
- fademode 1, the volume fade, the default (2026-11-04). show_death_results: the death settings plan (2026-11-08). master_volume: the volume sliders plan (2026-11-08).

## fadepool.nvgt
- Fading every pool on leaving a run (2026-11-04).

## freerun.nvgt
- Free run: the free run plan (2026-11-13, [[project_free_run_plan]]), standing still first so every key can be tried in place. Normal deaths and a normal run's 50-round reserve, not practice's unlimited, to start (2026-11-13).
- No deaths, modify footsteps, give, set and take, modify ammo limits and set items: the free run tools plan (2026-11-14, [[project_free_run_tools_plan]]).
- Modify ammo limits replaced a plain toggle (2026-11-14: "Can't unlimmited ammo be a toggle, like the other on/off choices?", then "It doesn't have to be simple on/off"); the dev named it "modify ammo limmits" (2026-11-14). It shows only with a gun drawn, and modify ammo reserves hides while the gun has unlimited rounds (2026-11-14).
- Practice hints use named choices, silent hints and spoken hints, not on and off (2026-11-14), and view current setup names them the same way.
- Specials are powerups and slides (2026-11-13). Lives go up to 1000 (2026-11-13).
- Every console change closes it with a line in the misc buffer, like CaveDefender's console (2026-11-13: "It should be consistent if possible"). The console's focus returns to where you were, never to start running (2026-11-13).
- A mid-run environment or speed choice is always announced (2026-11-13). Normal speed (speeds up like an endless run) sits before rising (2026-11-13).
- Clear belt also empties your inventory, takes off a worn shield and resets the weapons (2026-11-13).
- Give items (2026-11-13, Section 3B); keys get a color menu (2026-11-13: "I like the menu better."); take items (2026-11-13); "Your inventory is empty." is a dialog so the reopening inventory menu doesn't cut it off (2026-11-13). Modify player inventory as one menu (2026-11-13: "What about putting them in a menu called modify player inventory?").

## freebelt.nvgt
- Free run's belt: the free run plan's Section 2 (2026-11-13). A replay brings everything back (2026-11-13).
- Each add list remembers its focus (2026-11-13: "make it remember your focus on long list selections").
- The clear lists show what's coming, like take items' counts (2026-11-13: "It should say that for things you clear as well"), the all item with the whole group's count (2026-11-13).
- View current setup condenses several batches of one kind into one line (2026-11-14: "should be condensed into one item").
- On no deaths, what caught you comes again (2026-11-14: "you should land past it, then it will re-appear once or continiously based on the mode").

## src/sdr.nvgt, functions and deps (Section 5)
- The speech buffers (2026-11-05, [[project_buffers_plan]]). The quiet startup update check runs from source too, so it can be tested (2026-11-05).
- extrafuncts.nvgt's string_trim_sides(): missing, it stopped the launch (2026-11-05). strip_extension() and its partner for the updater (2026-11-05).
- savefuncts.nvgt: each setting is read only if the file holds it, so a newer setting keeps its default for older files (2026-11-04). Buffer mutes saved as buffer_muted_<name> (2026-11-12, after CookieCraze's prefs, [[project_hints_setting_env_key_plan]]).
- form.nvgt: the tab panel announced in full when coming from another control, and Control plus Tab switching tabs from anywhere (2026-11-10).
- form_menu.nvgt: menu music starts at 80 percent (2026-11-09).
- key_config.nvgt: the rebinding plan (2026-11-09, [[project_rebinding_plan]]): the replace question; the compact binding strings (Section 2); capturing combos, a modifier held on both sides captured side-agnostic ("only if they pressed both ... together").
- setupmenu.nvgt: menu music carries on through menus without their own (2026-11-07, [[project_menu_music_rule]]); the menu sound cache (2026-11-08: "You'll never know when I'll need it").
