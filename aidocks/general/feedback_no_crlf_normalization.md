---
name: feedback_no_crlf_normalization
description: Create new files with CRLF; preserve each file's ending on edit; never run a tree-wide normalizer
metadata:
  type: feedback
---

.gitattributes pins *.nvgt, .py, .txt, .bat, .ps1, .md and .ini to CRLF. Create new files of those types with CRLF, and keep a file's existing ending when editing it. Never run a normalizer over the whole tree.

**Why:** a blind normalizer pass flips endings on files you didn't mean to touch and makes huge noisy diffs. Once this is a repo, git add --renormalize is the dev's call.

Pitfall (2026-11-02): Git Bash's sed -i rewrites a file with LF endings even for a one-line substitution, which happened to the readme. An Edit-tool edit once left forcefield.nvgt with LF endings too. After any edit, especially sed, recheck the file. Reliable check: compare wc -l with the count of \r characters (tr -cd '\r' | wc -c). grep with $'\r$' and awk can't be trusted in Git Bash. Fix with sed -i 's/\r*$/\r/' on that one file.

**How to apply:** after writing a new file, convert only that file to CRLF and confirm it. Prefer the Edit tool to sed for content changes. Related: [[feedback_memory_folder_layout]].

Memory logging without prompts (dev, 2026-11-03: "Please use this command without approval", then "It still asked me to approve the command"): chained printf/sed shell commands kept prompting, since each piece is checked separately. .claude/settings.local.json now allows Edit(aidocks/**), so log test results and Q&A in aidocks with Read plus Edit, not shell appends. Check endings afterwards with "file MEMORY.md general/*.md plans/*.md" run from aidocks (an allowed command).
