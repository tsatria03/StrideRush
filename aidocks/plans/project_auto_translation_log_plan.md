---
name: project_auto_translation_log_plan
description: COMPLETE (2026-11-20, 2.7, first entry): remove the General tab's "Log untranslated language lines" checkbox, so untranslated lines are always logged for any language but fallback; Q&A log
metadata:
  type: project
---

# Automatic translation log plan

The dev's first 2.7 change (2026-11-20, after 2.6 was released at V2.60): "removing the logging checkbox for translations, as I want it logged automaticly."

## Findings

- translation.nvgt's log_untranslated (off by default, saved in settings.srf by savefuncts.nvgt) gates log_missing() in translate_line(); fallback returns before any lookup, so it never logs.
- settings_menu.nvgt's General tab has the checkbox after the update check (log_box, new_log), reset to off by the defaults.
- translations.txt's "Logging untranslated lines." section tells players to turn the checkbox on.

## Settled so far

- Logging is always on for any language but fallback; the checkbox goes, and the saved log_untranslated is no longer read or written (an old settings.srf key is just ignored).
- translations.txt's logging section says it happens on its own.
- One changelog entry opens "New in 2.7."; build/version.txt goes to 2.7.

## Section

One section: translation.nvgt logs whenever a language but fallback is chosen (log_untranslated removed); the checkbox out of settings_menu.nvgt (its variables, saving and defaults reset); savefuncts.nvgt stops reading and writing log_untranslated; translations.txt's logging section reworded; the changelog entry; build/version.txt to 2.7; template.lng rerun (the checkbox caption leaves english.lng by hand); version history.

## Q&A log

- Claude laid out the change (always on for any language but fallback, the checkbox and its saved setting gone, translations.txt reworded, one entry opening 2.7). Q (Claude): always on for every non-fallback language, english included? Recommended yes: a complete language logs nothing, and after an update english.txt lists exactly what english.lng is missing.
- A (dev): yes.
- Q (Claude): the entry, first under "New in 2.7.": "Made it so lines your language doesn't translate yet are now always logged to a file named after it in your own lang folder, so the setting to log untranslated language lines has been removed."; translations.txt's logging section drops the checkbox paragraph and starts "While a language other than fallback is chosen, ...". Recommended.
- A (dev): yes. Plan SETTLED; waiting for the dev to commit it.
- Section BUILT with its docks (2026-11-20, after e1d0b61): translation.nvgt's log_untranslated removed, translate() and translate_line() log whenever they run (fallback returns first, so never); savefuncts.nvgt no longer reads or writes it; settings_menu.nvgt's General tab is the language, the update check, then reset; translations.txt's logging section starts "While a language other than fallback is chosen, ..."; the entry opens "New in 2.7." (1 of 10); build/version.txt 2.7; english.lng's checkbox line removed by hand and template.lng regenerated (1443 lines, 0 missing).
- Tests: 1 of 2 (General tab: language, update check, reset, no checkbox) PASSED; 2 of 2 (english chosen, a vehicles practice hint logged to english.txt with no checkbox) PASSED. COMPLETE.
