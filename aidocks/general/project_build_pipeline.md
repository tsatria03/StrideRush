---
name: project_build_pipeline
description: build/ holds tools.py, tools.bat, tools.ini, site_updater.ps1 and version.txt, copied from SimpleFighter and adapted to Stride Rush on 2026-11-01 (password StrideSprinter, version 1.0, sounds bundled)
metadata:
  type: project
---

The dev copied SimpleFighter's build tools into build/ on 2026-11-01.
- tools.py: the commit tools menu plus compile, package (password 7z), gh release and website stages.
- tools.bat runs it with Python 3.12.
- tools.ini holds the game name, password, nvgt_file and site paths.
- site_updater.ps1 does a regex version bump in the site HTML.
- version.txt is the single source of truth ([[feedback_update_build_version_txt]]).
- Machine paths for nvgt, 7z, gh and iscc come from ~/.game_tools/tools.ini, which is shared by all the dev's legacy-engine games.

Adapted to Stride Rush on 2026-11-01:
- tools.ini: name StrideRush, archive password StrideSprinter, nvgt_file sr.nvgt, site paths under projects/games/StrideRush.
- tools.py: ASSETS_DIR is "sr". ASSET_FOLDERS is data, docks, lib and sounds; sounds are bundled because there's no first-run sound downloader.
- site_updater.ps1: the regex now matches "StrideRush V".
- version.txt starts at 1.0, so the first tag is V1.00.

Not yet in place (as of 2026-11-01):
- the site page misc/tsatria03.github.io/projects/games/StrideRush/index.html, so the website stage would fail until the dev creates it
- src/sr.nvgt and the src/includes/version.nvgt mirror, so the compile stage has nothing to build
- a launcher in sr/

The release tag format is V<version>0 (for example V1.00), and the in-game updater depends on it.

**How to apply:** never run tools.py ([[feedback_dont_run_or_build_the_game]]). Keep the tag format in sync with the future updater ([[project_tech_decisions]]).
