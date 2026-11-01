---
name: feedback_no_crlf_normalization
description: Create new files with CRLF; preserve each file's ending on edit; never run a tree-wide normalizer
metadata:
  type: feedback
---

.gitattributes pins *.nvgt, .py, .txt, .bat, .ps1, .md and .ini to CRLF. Create new files of those types with CRLF, and keep a file's existing ending when editing it. Never run a normalizer over the whole tree.

**Why:** a blind normalizer pass flips endings on files you didn't mean to touch and makes huge noisy diffs. Once this is a repo, git add --renormalize is the dev's call.

**How to apply:** after writing a new file, convert only that file to CRLF and confirm it. Related: [[feedback_memory_folder_layout]].
