---
name: project_helpers_plan
description: SETTLED (2026-11-20, 2.7's tenth entry): animal, floor, force field and ladder helpers in the player shop's specials, doing the rest of your hands' jobs; 4 sections; Q&A log
metadata:
  type: project
---

# Helpers plan

The dev's idea: expand the player shop's helpers, which so far cover only two of the six jobs your hands do. Follows [[project_shop_plan]]. Nothing gets built until this plan is settled and committed.

## Where things stand

What hands do now:
- Picking up items: covered by the item helper (your lane only).
- Opening real doors: covered by the door helper (it also uses your first key).
- Switching off force fields: no helper.
- Scaring away animals with a clap: no helper.
- Climbing real walls (grab, then alternate hands on each rung): no helper.
- Repairing floor breakers (open the corridor, then alternate hands on each piece): no helper.

How the two existing helpers work, as the starting point: bought in the player shop's specials through a pack menu, used from the inventory to toggle on or off, last the whole run unless you fully die, extra copies add no strength, and every shop price is different. Code: game/specials.nvgt, menus/shop_menu.nvgt, prices in tuning.nvgt.

Versioning: 2.7 has 1 changelog entry left, so this plan either shares that entry or opens 2.8.

## Open questions

1. SETTLED: hand jobs only, so animal, floor, ladder and force field helpers join the item and door helpers.
1b. SETTLED: helpers are never permanent. They work like the item and door helpers: bought per run through a pack menu, and gone when you fully die or the run ends.
2. SETTLED: the ladder helper grabs the ladder as soon as a hand could, then climbs at the fastest pace the level allows.
3. SETTLED: the floor helper opens the corridor as soon as a hand could, then repairs at the same fastest pace.
4 and 5. SETTLED: the animal and force field helpers act as soon as a hand could, with the normal clap and switch sounds.
6. SETTLED: animal helper 3,000, floor helper 5,500, force field helper 2,500, ladder helper 4,500 gold coins, listed alphabetically among the specials (animal, door, floor, force field, item, ladder, slide, trampoline).
7. SETTLED: what the new helpers do counts toward statistics and achievements, as the item and door helpers' work already does.
7b. Where the new helpers are available: bought in endless and debug runs, given, set or taken in a free run's modify player inventory, and absent from timed and practice runs, as the existing helpers are. SETTLED (dev: "yes").
8. SETTLED by a rescan: no new sounds are needed. The helpers reuse the clap, switch press, force field off, ladder grab and step, and floor open and fix clips.
9. SETTLED: one entry as 2.7's tenth, the dev's wording with "an" dropped: "Added animal, floor, force field and ladder helpers to the player shop's specials, which do the work of your hands for you as the belt speeds up."

## Sections

1. The four new specials: prices, the player shop's specials list in alphabetical order, pack menus, inventory toggling, reset when you fully die or the run ends, and give, set or take in a free run. They switch on and off but do nothing yet. All six helpers' toggle in specials.nvgt moves from the generic main/ui/other toggleon and toggleoff to the dev's main/misc/game/helperon.ogg and helperoff.ogg.
2. Force field and animal helpers: each acts as soon as a hand could, with the normal switch and clap sounds.
3. Ladder and floor helpers: each grabs or opens as soon as a hand could, then climbs or repairs with alternating hands at the level's fastest allowed pace.
4. Docks: the changelog entry, the player shop document and any others naming the helpers, then template.lng and english.lng.

## Q&A log

- Q (dev, 2026-11-20): what do you have to use your hands for right now? A: the six jobs listed above.
- Dev (2026-11-20): start a helper plan to talk this over, thinking of an animal helper, floor helper, ladder helper, force field helper, etc.
- Q1: only the jobs your hands do? Dev: "Yes. This is the reason why I wanted hand helpers."
- The reason (a player's post the dev shared): needing a hand to pick up items, and a key plus a hand for doors, becomes too much finger work once the belt speeds up; they'd rather run onto items and have a key both unlock and open a door. They otherwise love the game.
- Q1b raised by Claude: helpers are lost at the end of a run, and the item and door helpers together cost 7,500 gold coins, about 38 gold packs on easy at an average of 200 each, so the player who needs them most can't keep them. Making them permanent would change the dev's earlier rule that a helper goes when you fully die, and would replace their pack menus with a single purchase.
- Q1b answer, dev: "I do not want helpers to be permenent items. That's not how my runner is supposed to work." Do not suggest this again.
- Q2 and Q3, dev: "for floor/ladders, it will open/grab it, then climb/repare it, but it needs to go based on the fastest the game allowes. I mean the climb/repare time." The pace is ladder_rung_min_times, which rungs and repair pieces share: easy 200 ms, medium 250, hard 300, insane 350, chaos 400. Build note: pressing exactly at that time is allowed (the check is less than), and the helper must alternate hands so it never trips the same-hand failure.
- Q4 and Q5: the animal and force field helpers act as soon as a hand could, with the normal clap and switch sounds? Dev: "yes".
- Q6: the names, prices and alphabetical order above? Dev: "that works".
- Q7: should the new helpers' work count toward statistics and achievements? Dev: "I want them to count like the item/door helpers already do."
- Sounds (dev, 2026-11-21): added main/misc/game/helperon.ogg and helperoff.ogg, to use instead of the generic toggle sounds. The generic ones stay in place for whatever else uses them.
- Section 1 BUILT (2026-11-21, after 2e5bc36): specials.nvgt holds all six helpers in helper_items and helpers_on, with helperon and helperoff; the four new ones are in tuning.nvgt's specials and freebelt.nvgt's give, set and take lists. Tests: 1 of 3 (shop list and prices), 2 of 3 (free run give and the new toggle sounds), 3 of 3 (item and door helpers still work) all PASSED.
- Build note: helpers_update() in specials.nvgt returns early while climbing or repairing, so the ladder and floor helpers need their own path there. The existing helpers call the normal pickup and door functions, which is why their work already counts in statistics and achievements.
