---
name: feedback_list_modified_files
description: End every file-editing turn with an explicit "Files changed:" list of repo-relative paths
metadata:
  type: feedback
---

End every turn that edited files with a "Files changed:" list, one repo-relative path per line. Then note whether the game needs a relaunch to see the change.

**Why:** the dev reviews by screen reader and uses the list to know what to re-read, commit and relaunch. Silent edits are easy to miss.

**How to apply:** .nvgt edits need a relaunch; sdr/data or sdr/docks edits usually don't. Related: [[feedback_dont_run_or_build_the_game]].
