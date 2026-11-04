---
name: project_build_pipeline
description: build/ holds tools.py, tools.bat, tools.ini, site_updater.ps1 and version.txt, copied from SimpleFighter and adapted to Stride Rush on 2026-11-01 (password FluentSprinter since 2026-11-04, sounds bundled); readied for the first release 2026-11-04 (assets in sdr/, the exe is sdr.exe)
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
- tools.ini: name StrideRush, archive password StrideSprinter, nvgt_file sdr.nvgt, site paths under projects/games/StrideRush.
- tools.py: ASSETS_DIR was "sr" (now "sdr"). ASSET_FOLDERS is data, docks, lib and sounds; sounds are bundled because there's no first-run sound downloader.
- site_updater.ps1: the regex now matches "StrideRush V".
- version.txt starts at 1.0, so the first tag is V1.00.

Not yet in place (as of 2026-11-01):
- the site page misc/tsatria03.github.io/projects/games/StrideRush/index.html, so the website stage would fail until the dev creates it
- src/sdr.nvgt and the src/includes/version.nvgt mirror, so the compile stage has nothing to build
- a launcher in sdr/

Readied for the first release (2026-11-04, after 1.3 closed; dev: "look at how the simple fighter's build tools look like, and try to adapt it here"):
- Compared with SimpleFighter's build/ (read only): tools.py, tools.bat, tools.ini and site_updater.ps1 are SimpleFighter's with only the adaptations above, so nothing else needed porting. The one real difference stays: Stride Rush bundles its sounds (SimpleFighter downloads its 2.3 GB on first run).
- The dev renamed the asset folder sr/ to sdr/; tools.py's ASSETS_DIR, .gitignore's /sdr/errors.txt, sdr.py's comments, CLAUDE.md and the memories followed. Then the dev renamed the scripts too: src/sr.nvgt to src/sdr.nvgt and sr/sr.py to sdr/sdr.py; tools.ini's nvgt_file (sdr.nvgt), sdr.py's SCRIPT path, restart_game() (sdr.exe, ../src/sdr.nvgt), .gitignore (/src/sdr/, /src/sdr.exe), CLAUDE.md and the memories followed. The compile bundle is src/sdr/ (named after sdr.nvgt) and stays ignored; the anchored /src/sdr/ rule doesn't touch the top-level sdr/ assets folder.
- nvgt -c names the exe after the script, so the release is releases/windows/StrideRush_password_is_FluentSprinter/sdr/sdr.exe, like SimpleFighter's sf/sf.exe. restart_game() in menus/menu.nvgt ran "StrideRush.exe" when compiled, which would never exist; FIXED to run "sdr.exe", as SimpleFighter's restart("sf.exe").
- The archive password is FluentSprinter (dev, 2026-11-04), replacing StrideSprinter in tools.ini; it names the release folder and the 7z (StrideRush_password_is_FluentSprinter.7z), and the future updater's extract step must use it. Sounds stay bundled (dev: "since the sounds folder is only 23mb, it can easily be bundled with the game").
- INSTALLER (dev, 2026-11-04, after committing the rest as a8ed2d3: "All we're missing is the installer. This game will use it. Look at how toy mania does that one."): ported from ToyMania (read only). build/installer.iss is ToyMania's Inno Setup script with only the install folder changed ({autopf}\tsatria03\StrideRush\sdr): x64, admin, AppId from tools.ini, version read from build/version.txt, password-encrypted, desktop and Start Menu shortcut tasks (both offered), an unticked "Launch" at the end, output to releases/archives. tools.ini gains [installer]: iss, app_id (a NEW GUID, 0936E445-B428-4601-977F-BB39EB8F737E; never reuse another game's, Windows uses it to tell installs apart), app_url (the site page), exe_name sdr.exe. tools.py gains ISCC (from ~/.game_tools/tools.ini's iscc), INSTALLER, the iscc build right after the 7z in the package stage, and the installer as a second release asset. ToyMania's naming came with it: the 7z and release folder are now StrideRush_windows_portable_password_is_FluentSprinter, beside StrideRush_windows_installer_password_is_FluentSprinter.exe.
- SITE PAGE created (dev, 2026-11-04: "I need an index page for it, just like my other games."): misc/tsatria03.github.io/projects/games/StrideRush/index.html, ToyMania's page layout (title, the README's one-line description, "Download StrideRush V1.3" with the installer and portable 7z links under releases/download/V1.30, "View StrideRush V1.3" with the release and source links), plus version.txt (1.3, no newline) beside it, which tools.py's website stage keeps current. The text must keep "StrideRush V<version>" and the releases/download|tag/V<tag> links, since site_updater.ps1's regexes rewrite exactly those. StrideRush was also added to the site home page's Games list, between SimpleFighter and ToyMania. Site files are LF, matching the other pages. The website stage only adds the game page and its version.txt, so the home page's new Games line has to be committed in the site repo by hand.
- Still to check by the dev: ~/.game_tools/tools.ini (nvgt, sevenzip, gh) and the site page; the V1.30 tag already exists, so a release run warns and offers to move it to HEAD.

The release tag format is V<version>0 (for example V1.00), and the in-game updater depends on it.

**How to apply:** never run tools.py ([[feedback_dont_run_or_build_the_game]]). Keep the tag format in sync with the future updater ([[project_tech_decisions]]).
