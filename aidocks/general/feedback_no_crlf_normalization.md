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
REPEATED (dev, 2026-11-04, during the lanes rebuild tests: "It's asking me to approve the logging command again."): Claude slipped back into printf appends for test logs. Every test pass, Q&A answer and plan note goes through Read plus Edit, always; the Edit tool keeps CRLF on its own, so no shell check is needed after a plain Edit either.
REPEATED, and the check was broken too (2026-11-16, joystick work): Claude used sed -i again on 15 files (code, docks, joystick.ini, CLAUDE.md, plans, MEMORY.md), turning them LF, and reported "CRLF kept" from a Git Bash count of lines matching a carriage return (grep -c with a dollar-quoted backslash r) against all lines, which reports every line as having a CR even in an LF file, so it can never catch this. Found by git's "LF will be replaced by CRLF" warning; all 15 were converted back with a byte-level Python script, no content changed (core.autocrlf is true, so the repo copies were never affected). From now on: no sed -i on these file types (use the Edit tool, or Python reading and writing bytes); verify endings only with Python counting CRLF pairs against bare LFs in the raw bytes, or git ls-files --eol (w/crlf); never with grep in Git Bash.
