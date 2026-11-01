---
name: feedback_plans_record_qna
description: Gameplay is designed through several discussed plans before any game code; record the Q&A from each discussion in the plan file
metadata:
  type: feedback
---

Before any gameplay code is built, the game needs several plans discussed with the dev, with question-and-answer rounds along the way. Each plan file in aidocks/plans/ keeps a Q&A log: the question asked, the dev's answer and the date.

**Why:** the dev said on 2026-11-01 that the Q&As are for recording purposes. They're the durable record of why each design choice was made.

**How to apply:**
- Ask one question per turn ([[feedback_ask_one_question_at_a_time]]).
- After each answer, append the Q and A to that plan's log and update the plan's settled sections.
- Don't start building a gameplay plan until the dev gives the go-ahead after the discussion ([[feedback_confirm_before_implementing]]).
