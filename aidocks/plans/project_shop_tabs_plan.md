---
name: project_shop_tabs_plan
description: SETTLED (2026-11-26, for 2.9, 2 sections): the player shop's categories become form_menu tabs, SimpleFighter style, instead of a category menu leading to each list; Q&A log
metadata:
  type: project
---

# Shop tabs plan

Goal: the player shop (menus/shop_menu.nvgt) uses form_menu.nvgt's own tabbed mode (add_tab, add_item_to_tab, active_tab, set_active_tab_silent, selected_tab), the way SimpleFighter's shopmenu() does, instead of a category menu (character, items, specials, back) that opens a separate list for each.

The dev's rule (2026-11-26): form_menu tabs are for menus of things you choose; windows of things you check or change (checkboxes, sliders, the settings window) keep the form's own tab panel, as SimpleFighter's settingsmenu() and Stride Rush's settings window do.

## Findings

- form_menu's tabbed mode was never used in Stride Rush; only settings_menu.nvgt builds a tab panel, through audio_form directly.
- form_menu tabs hold one menu list each, so they can't host checkboxes, sliders or buttons; the settings window stays as it is.
- SimpleFighter uses form_menu tabs in shopmenu() (menu.nvgt, five tabs of point upgrades), weaponsmenu() (menu_callbacks.nvgt, disabled items for locked weapons), buildmenu() (map_menu.nvgt) and gallery_browse() (builder/misc/gallery.nvgt); all set tab_caption "Category" and remember the last tab with set_active_tab_silent. Its shop has no back items: escape leaves.
- Today's Stride Rush shop: shop_menu() lists character, items, specials and back; shop_category_menu() lists a category's things with price and how many you can buy, plus back; shop_open_character() hides the shield stats without a shield; shop_pack_menu() offers buy 1, 5, 10, 25, 50, 100 and all.

## Open questions

1. The shape: one tabbed menu replacing the category menu and the three category lists, with the pack menu kept.
2. Back items in each tab, or escape only.
3. The pack menu's back item.
4. Remembering the tab and position.
5. The intro and the tab caption.
6. Changelog wording and docks.
7. Sections.

## Q&A log

- Q1, the shape. Claude recommended one tabbed menu replacing the category menu and the three category lists: tabs character, items and specials, each listing its goods as the category lists do today ("health potion, costs 50 gold coins. You can buy 12."); Enter opens the pack menu, unchanged; the character tab still hides the shield stats without a shield; categories switched with left and right on the tab panel or Ctrl+Tab from the list. Dev: "that works." Settled.
- Q2, back items. Claude first recommended a back item at the bottom of each tab to match the game's other menus; the dev asked where it would even be (the last line of each tab's list, three times over, never on the tab panel), and Claude then leaned to escape only. Dev: "I highly recomment not having a back button at all, and let escape do the job of going out of the store." Settled: no back items in the tabs; escape anywhere in the tabbed menu leaves the shop with "You're now exiting the player shop." and the close sound. Whether the pack menu keeps its back item is question 3.
- Q3, the pack menu's back item. Claude recommended dropping it too: escape returns silently to the tab and good you came from, as nested menus step back, so the whole shop works one way (escape goes up one level, and from the tabs leaves the shop). Dev: "I agree with no back button there." Settled.
- Q4, remembering. Claude recommended SimpleFighter's way: within one visit, leaving a pack menu lands you on the same tab and good, the list rebuilt so "You can buy" is current (saved tab and position restored with set_active_tab_silent and run()'s start position); each new visit opens on the character tab, the first, with nothing remembered between visits. Dev: "agreed". Settled.
- Q5, the intro and caption. Claude recommended today's opening unchanged ("You're now entering the player shop.", the open sound, "Welcome to the player shop. What would you like to buy?"), then SimpleFighter's run(pos, true, false): "character menu List" spoken, the cursor in the character tab's list; tab_caption "Category" as in the settings window, so Shift+Tab says "Category Tab panel, character tab" and Ctrl+Tab switches from anywhere; each list named after its tab by add_tab() ("items menu", "specials menu"), which the language files will need. Dev: "I like that. agreed". Settled.
- Q6, changelog and docks. Changelog, 2.9's second entry, on top: "Made it so the player shop now shows its character, items and specials categories as tabs in one menu, and escape takes you back a step or out of the shop instead of a back item." Docks: player_shop.txt's Buying something says the shop opens on three tabs (left and right on the tab panel, or control plus tab from anywhere), each listing what it sells with its price and how many you can afford; the pack menu line adds that escape takes you back to the tab you came from; "Every tab always lists what it sells, even with no gold coins"; escape leaves the shop. player_stats.txt: "character category" becomes "character tab". The readme and older changelog entries unchanged. Dev: "agreed". Settled.
- Q7, sections. Claude recommended two: Section 1, the tabbed shop (shop_menu() as one tabbed form_menu, tab_caption "Category", tabs character, items and specials with the shield stats still hidden without a shield, no back items, escape leaves, saved tab and position after a pack menu; shop_category_menu() folded into that loop with its errors kept; shop_pack_menu() loses back; template.lng refreshed and english.lng synced), with tests; Section 2, the docks from Q6, no tests. Dev: "agreed. 2 sections". Settled.

PLAN SETTLED (2026-11-26): all 7 questions answered; ready to commit, then build Section 1 on the go-ahead.

## Sections

1. The tabbed shop (shop_menu.nvgt, template.lng, english.lng). Tests.
2. The docks (changelog.txt, player_shop.txt, player_stats.txt). No tests.
