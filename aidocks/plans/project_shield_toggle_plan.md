---
name: project_shield_toggle_plan
description: SETTLED (2026-11-21, 2.8's third entry): switching a steel shield on and off from the inventory with wear and remove sounds, saying shield on or off and keeping its strength until it breaks, after SimpleFighter; 3 sections; Q&A log
metadata:
  type: project
---

# Shield toggle plan

The dev's idea: a worn steel shield can be taken off and put back on. Nothing gets built until this plan is settled and committed.

## How things stand

- SimpleFighter (read only): a shield is drawn and then worn or lowered; its strength stays while it's lowered, and only resets when it breaks.
- Stride Rush: use_shield() in shield.nvgt wears one at full strength, and item_used() then removes it from the inventory, so a worn shield can't be selected. shield_worn and shield_hp_left hold the worn one.
- Sounds: steel_shield/wear.ogg is in use; remove.ogg is waiting for this.

## Settled

- It says "Shield on." and "Shield off.", with the wear and remove sounds.
- A shield taken off remembers its strength.

## Open questions

1. SETTLED: the shield stays in your inventory while it's on, like a helper, reading "steel shield, on" or "steel shield, off". U switches it, and it only leaves when it breaks.
2. SETTLED: the stack counts as one line, and U only ever switches your current shield, whose strength carries until it breaks. A spare can't be switched on until then. After a break, the next one waits, off, until you press U, and starts at 400.
3. SETTLED: a running Sturdy or Brittle Shield keeps its timer and does nothing while the shield is off, working again if you put it back on in time, and neither turns up while it's off.
4. SETTLED: M says "Your shield is off, with 63 percent strength." in your shield format, session statuses say "shield, off, 63 percent", modify shield strength stays available for a shield you've taken off, and shield defence shows whenever you carry any shield. With no shield, M and the statuses stay as they are.
5. SETTLED: a shield counts toward steel shields used once, the first time it goes on, so switching it off and on again adds nothing.
6. SETTLED: the toggle works in every run; a practice death gives back a fresh shield, switched off; in a free run, taking or setting your last shield away removes the current one, while taking some leaves it on; clear belt removes everything as it does now.
7. SETTLED: 2.8's third entry: "Made it so you can now switch a steel shield on and off from your inventory, and it keeps its strength until it breaks."

## Sections

1. The toggle: the shield stays in your inventory while it's on and reads on or off, U switches it with the wear and remove sounds and "Shield on." or "Shield off.", its strength carries until it breaks, a break takes one from the stack and leaves the next off, a shield counts as used once, and the shield powerups follow the settled rules.
2. Readouts and other runs: M and session statuses while it's off, shield defence's visibility, modify shield strength for a shield that's off, free run give, set and take, and practice deaths.
3. Docks: the changelog entry, steel shields, inventory, keyboard and joystick, powerups, free runs, player stats and any other documents it touches, then template.lng and english.lng.

## Q&A log

- Claude asked, after the character upgrades plan, whether a worn shield should be removable. Dev: "For shields yes. It will say shild on/off. Also in SF, if you have it on, it remembers the strength."
- Q1: keep it in the inventory while it's on, like a helper? Dev: "yes".
- Q2, dev: "The next shield cannot be toggled on and off untill the current one breaks I think."
- Q3: Sturdy and Brittle Shield while it's off? Dev: "I agree with that."
- Q4: the dev asked what SimpleFighter's shield key says: "shield strength, 63 percent" while on, and "Your shield must be razed or worn to view it's status." while off. Claude still preferred reading the strength while it's off. Dev: "I'll take your stile."
- Q5: count a shield as used once, the first time it goes on? Dev: "agreed".
- Q6: other runs, practice deaths, free run inventory and clear belt? Dev: "agreed."
- Q7: the changelog wording? Dev: "it works". Plan SETTLED.
- Section 2 BUILT (2026-11-21, after f734b73): speak_shield_strength() and session_status_lines() read a shield that's off; modify shield strength shows for shield_in_use; has_a_shield() is just the inventory count. Practice deaths needed no change, since reset_shield() already leaves the refilled shield fresh and off. Tests: 1 of 3 (M and statuses while off), 2 of 3 (the console and shield defence's visibility), 3 of 3 (a practice death gives a fresh shield, off) all PASSED.
- Section 1 BUILT (2026-11-21, after bcfb1b7): toggle_shield() replaces use_shield(); shield_in_use marks a current shield that has been put on; a break calls reset_shield() and takes one from the stack; the inventory line reads on or off; clear_inventory() and losing your last shield reset it, so a free run's take and set already follow the settled rule. Tests: 1 of 3 (toggle, sounds and inventory line), 2 of 3 (strength kept while off), 3 of 3 (a break, the spare at full strength, the last one leaving) all PASSED.
