---
name: project_pause_status_plan
description: BUILT (2026-11-13, 2.1 at 10 of 10) - the status readouts in the pause menu, 2.1's last entry; ToyMania's pause menu as reference; Q&A log
metadata:
  type: project
---

Status: COMPLETE (2026-11-13, 2.1 FULL at 10 of 10; released in V2.10).

Background:
- The dev (2026-11-13, "For 1.9" meaning 2.1's last entry): "I have my last idea. The statis readouts. I suggest they live in the pause menu. Does toy mania have something similar in the pause menu?" Close to suggestion 19 in [[project_suggestions]] (a status summary).
- ToyMania's pause menu (read only, src/includes/main/menus/menu.nvgt, pausemenu()): copy level and game mode to clipboard; read current game session statistics (a dialog of toys collected, keys, guards killed, cars destroyed, steps, time played, then copy or export); quit game; resume game; view detailed stats.
- Stride Rush today: the status keys H (health and lives), M (shield), L (lane), V (environment), Z (distance), C (speed), T (time), B (heart rate), each into the status buffer; the pause menu (pause_menu.nvgt) has resume run, restart run, then in an endless run view, copy and export session results, then quit run.

Q&A log:
- Claude described ToyMania's pause menu and proposed "view run status": a list of the status readouts (health and lives, shield, lane, environment, speed, distance, time, heart rate), in every kind of run, back to the pause menu. A: "What about view session statuses? And then a menu will show up with them, and a back button. There will not be a copy button. Session results are different from session statuses." (dev, 2026-11-13): the item "view session statuses", a menu of them and back, no copy or export.

Settled design: not yet.

Sections: not yet.
- Q: Lines in "label, value" style like session results (health, shield, lane, environment, speed, distance, time, heart rate), the menu "Session statuses." then back, the item right after resume run? A: "Yes. Also no plan required. I'll test it after." (dev, 2026-11-13). Built: session_status_lines() in stats_menu.nvgt (debug runs give speed in milliseconds per step, as C does), shown by show_stat_lines() from pause_menu(); the readme's P line and pause menu paragraph; the 2.1 entry "Added view session statuses to the pause menu, listing your health, shield, lane, environment, speed, distance, time and heart rate in one place." (10 of 10, 2.1 FULL).
