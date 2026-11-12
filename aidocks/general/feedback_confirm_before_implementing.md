---
name: feedback_confirm_before_implementing
description: Treat every design discussion as a question needing an explicit go-ahead, never a commission to start editing
metadata:
  type: feedback
---

Treat every design discussion as a question that needs an explicit go-ahead. "What if we did X", "I have an idea", or anything ending in a question mark is a request for a plan, not permission to edit. Lay out the design and tradeoffs, ask, then stop and wait. Don't fan out into adjacent files unprompted.

**Why:** the dev's workflow is to describe an idea first and then say "go ahead". Edits started off a discussion have to be unwound. Carried over from SimpleFighter and ToyMania.

**How to apply:** answer a proposal with a plan and one question ([[feedback_ask_one_question_at_a_time]]). Edit only after "yes", "do it" or "go ahead". The dev also said this game is built one step at a time, not all at once. Memory upkeep in aidocks/ is the exception and can be done freely.

Also during tests (dev, 2026-11-12, practice guidance plan: "Make sure to confirm with me first before you modify code. I mean questions that I'm not sure if it's clear."): when a change asked for mid-test could be read more than one way, restate it in plain words (before and after, what it covers) and wait for the dev to confirm before touching code. A clear request with an agreed answer can be built.
