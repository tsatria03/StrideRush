---
name: reference_friend_runner_template
description: A friend's small BGT runner template in user/ (gitignored) - auto-step loop with a shrinking interval, 5-step hazard countdown cues, jump arc, level layouts, plus its bugs; the closest model for Stride Rush's core run
metadata:
  type: reference
---

Source: a BGT (NVGT's predecessor) runner template written by a friend of the dev, in the gitignored user/ folder. Its readme is left over from a different game. The dev gave it as a runner template on 2026-11-01. Read only. Per [[feedback_dont_name_others_games]], don't name it in committed files. About 1,300 lines of game code: game.bgt, plus includes/ hazard, bomb, projectile, item, teleporter, src (ambience sources) and levels, with stock libraries.

Core run loop (game.bgt game()):
- Each frame: update the listener, then run the object loops.
- When movetimer >= ballspd: play a footstep oneshot (ball.wav) only if on the ground (y == 0), do ballspd -= 1, do me.x += 1, and restart the timer.
- ballspd is clamped from below by maxballspd, the fastest interval allowed.
- Starts at 500 ms per step.
- Jump: Space starts it (not while jumping or in the air). y rises 1 per jumptime (100 ms) up to jumpheight 5, then falls 1 per tick, and a land sound plays at y 0.
- So a jump lasts about 1 second whatever the run speed. As steps speed up, each jump clears more tiles.
- Readouts: C speaks coordinates, H speaks health.

Hazard warning (hazard.bgt), the useful pattern:
- Each hazard is a looping positioned sound.
- At 5, 4, 3, 2 and 1 tiles before it, at the same height, it plays escalating cues hazcount1 to hazcount5, one per step.
- Reaching its tile while on the ground means game over.
- Jumping changes your y, so the hazard's tile no longer matches and you're safe.
- This is a simple, step-synced "warn, then act" countdown, comparable to SimpleFighter's turbulence warning ([[reference_simplefighter_builder_objects]]).

Levels (levels.bgt): lvl1 to lvl10.
- Each level puts a random hazard type (hazard1 to hazard5) every 20 tiles.
- maxx grows by 200 per level (220 up to 2020).
- maxballspd drops by 50 per level (500 down to 50).
- So a level is a fixed-length track with a faster speed floor.

Other objects:
- bomb: a falling sound that homes toward the player's height and hurts on contact.
- projectile: moves along x and hurts on contact.
- teleporter: can move, and sends you to a destination.
- item: a beeping pickup, unused.
- source: an ambience loop that can be paused and resumed.

Bugs and gaps to NOT copy:
- Level 1 never speeds up, because its speed floor (maxballspd 500) equals the starting speed.
- Only lvl1 is ever called. Nothing completes a level, and lvlcomplete.ogg is never played. At maxx the player is clamped and runs in place.
- Health (ballhp) is reduced by bombs and projectiles but never checked, so they can't kill you. Only hazards can.
- Arrays are trimmed with remove_at inside loops with an early return, so only one object is processed per frame. Use sentinel-null removal instead ([[project_entity_pattern]]).
- Projectiles and teleporters step twice per tick (a move inside the timer branch, then another move after it).
- Death, Escape and every menu choice re-call mainmenu() recursively.
- Everything shares one sound_pool, p.

**How to apply:** use it as the model for the run plan's step loop, speed curve and countdown cues, fixing the bugs above ([[project_run_plan]]).
