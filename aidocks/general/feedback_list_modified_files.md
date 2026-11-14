---
name: feedback_list_modified_files
description: End every file-editing turn with an explicit "Files changed:" list of repo-relative paths, plus the total git change count since the last commit
metadata:
  type: feedback
---

End every turn that edited files with a "Files changed:" list, one repo-relative path per line. Then note whether the game needs a relaunch to see the change.

**Why:** the dev reviews by screen reader and uses the list to know what to re-read, commit and relaunch. Silent edits are easy to miss.

**How to apply:** .nvgt edits need a relaunch; sdr/data or sdr/docks edits usually don't. Related: [[feedback_dont_run_or_build_the_game]].

Also (dev, 2026-11-13: "Remember to always show how many changes were made in git. I see 42 changes, but forgot what they were."): with the Files changed list, give the total count of git changes since the last commit (git status --short), so the number matches what the dev sees in git, and when asked, what each one is, grouped by why it changed. Check git status before writing the list.
