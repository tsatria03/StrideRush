---
name: project_menu_counts_plan
description: COMPLETE (2026-11-12, 2.1 at 5 of 10) - the practice and difficulty menus say how many choices are unlocked, as the achievements menu does; Q&A log
metadata:
  type: project
---

Status: COMPLETE (2026-11-12, 2.1 at 5 of 10). From suggestion 16 in [[project_suggestions]] (practice progress).

Q&A log:
- The dev asked what practice progress would look like; Claude offered a count, a count with the next goal, and an all-open line. The dev: "What if it read like the achievements menu? I forgot what that looked like" (achievements: "Achievements menu. 40 of 130 unlocked in total.", "Lifetime achievements. 25 of 90 unlocked."). Claude proposed "Choose an obstacle to practice. 6 of 16 unlocked."
- The dev: "What about, Choose a practice level." Claude: "level" means easy to chaos; offered "Practice menu. 6 of 16 obstacles unlocked." (recommended), the old line with a count, or "Practice obstacles." The dev: "What about, Choose what to practice. x of x obsticals unlocked" (agreed).
- The dev added (2026-11-12): "The difficulty menu should also have a similar treatment. Something like, Choose a difficulty leve. x of x unlocked."
- Q: Both intros, "Choose what to practice. 6 of 16 obstacles unlocked." and "Choose a difficulty level. 3 of 5 unlocked.", with one entry "Made it so the practice and difficulty menus now tell you how many choices you've unlocked."? A: "Yes please. Then I'll test" (dev, 2026-11-12).

Built (2026-11-12): menus/menu.nvgt's choose_difficulty() and choose_practice() count difficulty_unlocked() and practice_unlocked() into their intros; the choices themselves unchanged; the 2.1 entry (5 of 10).
- Tested (dev, 2026-11-12): the test passed (both intros with matching counts).
