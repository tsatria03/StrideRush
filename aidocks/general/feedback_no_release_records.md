---
name: feedback_no_release_records
description: Record version tags (and their commits) in memory, but never GitHub releases; git tags and build/version.txt stay the source for the current version
metadata:
  type: feedback
---

Record tags, not GitHub releases (dev, 2026-11-27, on tagging 2.9: "You can record tags, but not git releases."). This narrows the earlier rule (dev, 2026-11-23, on closing 2.8: "From now on, please do not record new releases in your memmories."), which had covered tags too.

**Why:** the dev publishes GitHub releases themselves, so a recorded release status goes stale; a tag and its commit are fixed history worth keeping.

**How to apply:** when the dev says a version is tagged, note the tag and its commit in [[project_version_history]]'s section for that version (check with `git tag` and `git rev-list -n1 <tag>`). Never write whether, when or where a version was released on GitHub, in aidocks or CLAUDE.md. For the current version, still read build/version.txt and `git tag`. Keep logging plans, their Q&A and what each change did, as [[feedback_plans_record_qna]] asks.
