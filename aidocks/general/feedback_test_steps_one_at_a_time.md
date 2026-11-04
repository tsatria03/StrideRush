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
