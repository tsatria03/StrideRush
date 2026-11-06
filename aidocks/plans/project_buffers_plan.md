---
name: project_buffers_plan
description: SETTLED, not built (2026-11-05, 1.5; alphabetical after all) - more speech buffers to spread the run's messages (today all 44 go to misc); items, weapons, powerups, doors, status, misc, plus achievements for later; buffer.nvgt's built-in "alerts" handling; Q&A log
metadata:
  type: project
---

Status: SETTLED 2026-11-05, nothing built (summary at the end of the Q&A log). Started 2026-11-05 on top of d0797ed (dev: "The next thing I was considering was more buffers to spread the messages.").

Today: sdr.nvgt calls create_buffer("misc") (which also makes "all"), and all 44 speak_buffer() calls in globals/ use the default, misc ([[reference_cavedefender_buffer]]).

References (read only):
- CookieCraze (cycrz.nvgt): achievements, boosts, combos, critical, events, general, misc, quests, ranks; misc still the busiest (about 25 calls).
- ToyMania (tm.nvgt): achievements, general, misc. general takes the gameplay notices (29 of 81: doors, keys, inventory, ammo); misc, the default, takes the volume keys ("track -5"), "canceled" and small notices; achievements has one message.

Stride Rush's messages by system (2026-11-05): items (pickups by name and using them: "You got 8 rounds of ammo.", "Gained 2 lives.", "Healed to 60 percent health.", "You put on the steel shield.", "You were moved forward 12 steps.", the "already at maximum" notices), inventory (browsing, "Your inventory is empty.", "You don't have anything to use."), weapons ("Pistol equipped.", reloading, loaded and reserve notices, the X readout), powerups (the name on collecting, "<name> wore off."), doors (locked, jammed, unlocked, no door nearby), status (the H, M, L, Z, C and T readouts), misc (the music and ambience volume messages).

Q&A log:
- Q: Buffers per game system? Claude's proposal: items (inventory folded in), weapons, powerups, doors, status and misc, each message naming its buffer. (Asked 2026-11-05; Claude recommended this over ToyMania's single general buffer.)
- A (dev, 2026-11-05): "I prefer your buffers, plus achievements for when they come. Also alerts, but idk what would go there. I think buffer.nvgt already has that one right?" SETTLED: items, weapons, powerups, doors, status, misc, and achievements (empty until achievements exist).
- Checked deps/buffer.nvgt: "alerts" is special-cased but never created. toggle_mute() refuses to mute it ("This buffer can not be muted.", like "all"), and buffer_visible() keeps it in the bracket-key rotation even when empty (other buffers are hidden until they hold a message). It came from CaveDefender, where it carried the server's important notices. achievements, being an ordinary buffer, stays hidden until its first message, so creating it now changes nothing players see.
- Q: Should alerts wait until something needs it? Nothing in Stride Rush today must be impossible to mute, and since alerts always shows in the rotation, creating it now would add an empty stop every time you cycle buffers. Claude's proposal: leave alerts out for now and add it with the first message that must never be missed. (Asked 2026-11-05; Claude recommended waiting.)
- A (dev, 2026-11-05): "I agree with this. Also, in cave defender, a buffer is invisible until something gets spoken right? If so, I want that." SETTLED: no alerts buffer yet. And yes, already there: Stride Rush's deps/buffer.nvgt has buffer_visible() (the same as CaveDefender's, buffer.nvgt line 152 there): a buffer joins the bracket-key rotation only once it holds a message, except "all" (and "alerts" if it's ever made); a new message still speaks live and lands in "all". It just never showed, because misc was the only buffer and gets messages from the start. No change needed.
- Q: The rotation order? "all" always first; Claude proposed alphabetical after it: achievements, doors, items, misc, powerups, status, weapons. (Asked 2026-11-05.)
- A (dev, 2026-11-05): "I want alphabetical buffers." SETTLED. THE PLAN IS SETTLED; not to be built without a go-ahead.

Settled summary:
- Buffers, created at startup in this order after "all": achievements, doors, items, misc, powerups, status, weapons (each hidden until its first message, by buffer.nvgt's buffer_visible()). No alerts yet.
- Messages: doors (locked, jammed, unlocked, already unlocked, no door nearby); items (pickups by name, using them, the "already" notices, the inventory's browsing, empty and nothing-to-use lines); powerups (collected, wore off); status (H, M, L, Z, C, T readouts); weapons (equipped, reloading, the load and reserve notices, the X readout, "doesn't take any ammo" from reloading or X); an ammo pack's own results ("You got 8 rounds of ammo.", and its "doesn't take any ammo" and "reserve is already full" when opened) stay with items, since they answer using an item; misc (music and ambience volumes, and the default for anything new).
- Build sections: 1, the buffers and each speak_buffer() call's buffer; 2, docks (a 1.5 changelog entry and the readme's speech buffer section).
- The dev (2026-11-05): "Do you think this section is small? If so, you can do the docks after the test steps." Yes: ONE build section, then test steps, then the docks right after the tests pass, in the same go.
- GO-AHEAD (dev, 2026-11-05: "yes. ready."). BUILT on top of d0797ed: sdr.nvgt creates achievements, doors, items, misc, powerups, status, weapons in that order (the first also makes "all"), replacing create_buffer("misc"). 42 speak_buffer() calls gained their buffer: doors (door.nvgt, 5); items (ammo.nvgt 4, capsule.nvgt 3, inventory.nvgt 3, key.nvgt 1, potion.nvgt 3, shield.nvgt's pickup, already wearing and put on, teleporter.nvgt 2); powerups (powerup.nvgt 2); status (lane.nvgt, lives.nvgt, run.nvgt's Z, C and T readouts, shield.nvgt's M readout and "You're not wearing a shield."); weapons (weapons.nvgt, 7). The two volume messages in run.nvgt stay on the default, misc. Awaiting test steps, then the docks.
