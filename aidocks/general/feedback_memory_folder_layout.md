---
name: feedback_memory_folder_layout
description: Memories for this game live in aidocks/, split into general/ (topics) and plans/ (completed or in-progress plans)
metadata:
  type: feedback
---

Save every memory for this project in the project's own aidocks/ folder, not the harness's auto-memory directory. Generalized topics (conventions, engine notes, feedback, project facts) go in aidocks/general/. Feature plans, finished or not, go in aidocks/plans/. aidocks/MEMORY.md is the index for both.

**Why:** the dev set this layout up on 2026-11-01 when starting the project, matching how their other NVGT games keep memory in a committed aidocks/ folder.

**How to apply:** write the file into the right subfolder, add a pointer line to aidocks/MEMORY.md, and generate files with CRLF line endings (.gitattributes enforces CRLF on .md). See [[project_runner_overview]].
