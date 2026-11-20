---
name: feedback_no_sed_i
description: never run sed -i (or any in-place shell rewrite) on this repo's files, and never send a "draft" command to Bash: every Bash call runs
metadata:
  type: feedback
---

Never use sed -i, or any other in-place shell rewrite, on this repo's text files. In Git Bash, sed -i turns CRLF files into LF, and sed -i.bak also leaves backup files behind. Make text changes with the Edit tool (it keeps CRLF), or byte-level Python for many files, then check with eol.py.

Never send a command to Bash as a "draft" or "placeholder": every Bash call runs. On 2026-11-19, Claude sent a sed -i.bak path rewrite across five .nvgt files labeled "Placeholder, not executed", and it ran: all five went LF and five .bak files appeared. Claude owned it, restored CRLF with to_crlf.py, confirmed against the backups that only the intended path lines changed, then deleted the backups. It had already happened once the day before (sed -i on CLAUDE.md and the version history while recording the V2.50 hash).

It slipped in twice more on 2026-11-19, both pointed at /dev/null and touching no file: a stray sed -i inside a grep command while counting "6 sections", and a sed -i.x '' /dev/null at the start of a grep for "for 9 of 10". Harmless, but the habit is the problem: never write sed in a Bash command at all, not even as a no-op.

**Why:** CRLF is a load-bearing rule here ([[feedback_no_crlf_normalization]]), and a mislabeled command misleads the dev about what changed.

**How to apply:** for path or text replacements, use Edit per occurrence, or a Python script that reads and writes bytes, then eol.py. If unsure about a command, describe it in text instead of calling Bash. Related: [[feedback_log_without_bash]].
