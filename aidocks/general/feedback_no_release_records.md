---
name: feedback_no_release_records
description: Don't record new releases, tags or closed versions in memory or CLAUDE.md; git tags and build/version.txt are the source for them
metadata:
  type: feedback
---

Don't record new releases in memory (dev, 2026-11-23, on closing 2.8: "From now on, please do not record new releases in your memmories."). That covers tags, tagged commits, GitHub releases and "closed" or "not tagged yet" status, in aidocks and in CLAUDE.md.

**Why:** the dev handles releases themselves, and a recorded release status goes stale as soon as a tag moves.

**How to apply:** when the current version or latest release matters, read build/version.txt and `git tag`. Keep logging plans, their Q&A and what each change did, as [[feedback_plans_record_qna]] and [[project_version_history]] ask. Entries for 2.7 and earlier keep their tags as history.
