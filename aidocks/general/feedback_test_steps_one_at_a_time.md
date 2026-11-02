---
name: feedback_test_steps_one_at_a_time
description: When the dev tests a built section, give ONE test step per message, with what they should hear, and ask whether it passed before giving the next
metadata:
  type: feedback
---

After a section is built, walk the dev through testing it one step at a time. Each message gives a single test: what to do, and what they should hear if it works. Then ask whether it passed, and wait. Give the next test only after the answer.

**Why:** the dev asked for this on 2026-11-01 after getting an 11-step Section 1 checklist in one message. They test by screen reader while the game is running, and a long list is hard to follow between the game and the chat. Their CookieCraze project has the same rule.

**How to apply:**
- Number the steps ("Test 3 of 11") so progress is clear.
- If a test fails, stop and fix it before moving on ([[feedback_verify_code_while_fixing]]).
- Record results in the build plan as the section's test outcome. Related: [[feedback_ask_one_question_at_a_time]], [[project_first_build_plan]].
