---
name: feedback_no_game_names_in_code
description: Never name the dev's other games (ToyMania, SimpleFighter, CookieCraze, CaveDefender, the HeartbeatSimulator tool) in code comments, data files or build files; where something came from belongs only in aidocks
metadata:
  type: feedback
---

The dev (2026-11-09): "I noticed that you talk about my other games a lot in the code comments. Please remove my game mentions from them. If you are going to talk about my other games, only do it in your aidocks folder."

On 2026-11-09 every mention was stripped from src/ and build/ (95 comment edits in 34 files): "ported from X's ...", "X-style", "like X", "as X does", "unlike X's". The comments now say what the code does, with the dev's dated quotes kept.

**Why:** the code is the game's own; which game a pattern was borrowed from is design history, and that history lives in the plans and reference memories.

**How to apply:**
- In .nvgt, .ini, .py, .iss and other repo files outside aidocks/, describe the behavior only; never write a reference game's name, its function names as provenance ("SimpleFighter's restart()"), or its file names.
- Keep provenance in the plan's Background or Q&A log and the reference memories ([[reference_toymania_readonly]], [[reference_simplefighter_readonly]], [[reference_cavedefender_buffer]]).
- Third-party library names that aren't the dev's games (m_pro, BGT, the virtual_dialogs license note) can stay.
- Grep for the names before finishing any section that ports code.
