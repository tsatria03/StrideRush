---
name: feedback_dont_flag_indentation
description: AngelScript ignores indentation; don't flag uneven whitespace or reformat it
metadata:
  type: feedback
---

NVGT and AngelScript ignore indentation. Don't call out uneven indentation after edits and don't spend turns reformatting it. The dev's code is often flush-left on purpose.

**Why:** it's cosmetic noise; a reformat pass is unwanted churn.

**How to apply:** keep new code readable, match surrounding style loosely, and move on unless the dev asks for a formatting pass.
