---
name: feedback_test_steps_one_at_a_time
description: Never put tests in a build summary; ask if the dev is ready for the test steps first, then give ONE step per message with what they should hear, and ask whether it passed before the next
metadata:
  type: feedback
---

After a section is built, walk the dev through testing it one step at a time. Each message gives a single test: what to do, and what they should hear if it works. Then ask whether it passed, and wait. Give the next test only after the answer.

**Why:** the dev asked for this on 2026-11-01 after getting an 11-step Section 1 checklist in one message. They test by screen reader while the game is running, and a long list is hard to follow between the game and the chat. Their CookieCraze project has the same rule.

Never put a test step in a build summary (dev, 2026-11-02). End the summary by asking whether they're ready for the test steps, and give Test 1 only after they say yes. The dev was handed a test inside the summary for the spike and mine countdowns and asked for this.

**How to apply:**
- A build or fix turn ends with the summary, "Files changed:", the relaunch note, then "Are you ready for the test steps?" No test steps in that turn.
- Number the steps ("Test 3 of 11") so progress is clear.
- If a test fails, stop and fix it before moving on ([[feedback_verify_code_while_fixing]]).
- Record results in the build plan as the section's test outcome. Related: [[feedback_ask_one_question_at_a_time]], [[project_first_build_plan]].

Keep each test small (dev, 2026-11-03: "please split this test into parts. This seems like a lot"): one scenario per test, a few steps at most. A test that checks several behaviors (such as each of U's refusals) is split into parts like 4a, 4b, 4c, each asked "Did it pass?" on its own.

No test steps for sections that aren't gameplay (dev, 2026-11-03, for the menus plan's Section 1: "I do not want testing steps. It's not game play related."). Menus, docs and similar sections end with the build summary and the relaunch note; the dev checks them on their own. Gameplay sections still get the one-at-a-time test steps. Related: [[project_menus_plan]].

NUMBERED (dev, 2026-11-06: "when you show your tests. Tell me me how many. Like test x of x."): every test step is headed with its place and the section's total, such as "Test 3 of 3: ...", so the dev knows how many are left.

AN EXPLICIT RESULT IS REQUIRED (dev, 2026-11-15, after Claude took a commit and "ready for section 5" as a pass: "Next time, please make it so I'm required to tell you weather a test passed. example. passed/failed/yes/no. If I say failed/no, I'm required to explain what happened."): never assume a test passed. Accept passed or yes as a pass, failed or no as a fail. If the dev replies with anything else (a commit, a go-ahead, a new request), handle it, then ask for the test result before recording it or moving to the next test or section, and record nothing as passed until they answer. On failed or no, ask what happened before fixing anything, if they haven't already said.

USE THE DEBUG RUN (dev, 2026-11-08: "For tests in the future, please tell me to use the debug run feature, not any other run unless you want me to play the real game."): test steps start a debug run (play game, debug run, then the spawn, speed, footsteps and "end the run when out of lives?" debug options), naming the choices that set up the test, such as "nothing" for an empty belt, one obstacle type, or "real doors" and a speed. Ask for an endless or practice run only when the test is about that mode itself (difficulties, stats, achievements, session results, practice rules).

REPEATED (dev, 2026-11-18, starting the free run lanes tests: "when you show tests, make sure to say something like, test x of x"): open every test message with exactly "Test 1 of 5:" (not "Test step 1 of 5"), and keep it on every step.

Docks never get test steps (dev, 2026-11-20: "recall that docks do not require test steps. I'll read those on my own time."). When a section only changes documents, list what changed and say it's ready to commit; don't ask the dev to read them as a test.
