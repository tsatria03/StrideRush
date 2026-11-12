---
name: feedback_commit_messages_from_changelog
description: The dev uses a feature's changelog entry as its commit message; when flagging a commit point for a player-facing change, suggest that entry as the message
metadata:
  type: feedback
---

The dev writes commit messages two ways. A feature's main commit uses its changelog entry word for word (for example 62a3ad0, d956876, b7b571c, ca6f256 and 77ad9ed). Other commits use a general message like "Major game enhancements." or "Major dock enhancements.". On 2026-11-03 the dev noticed they had forgotten the changelog descriptions on several commits. The 1.1 surfaces, crouch cooldown, walls, force field countdown, real doors and fake doors entries never got their own commit message.

The dev's fix (45573ec, 2026-11-03): a general subject line ("Major dock/game enhancements.") with every missed changelog entry in the commit BODY, newest first, one per line. That covered the seven 1.1 entries since 77ad9ed. A commit with several entries can follow that shape.

**Why:** the git log doubles as a readable history of what shipped. It's easy to forget the descriptive message when several features land between commits.

**How to apply:** when flagging a commit point that includes a new or changed changelog entry, quote the entry and suggest it as the commit message. If more than one entry lands, suggest the 45573ec shape: a general subject with the entries in the body. Never commit yourself ([[feedback_check_git_log_for_commits]]). Don't suggest rewriting old commits to add messages unless the dev asks; it needs a history rewrite, and a force push if they're already pushed. Related: [[feedback_changelog_rules]].

When one commit covers several changelog entries (dev, 2026-11-12, the practice guidance plan's four), the dev puts the entries in the commit description, under a short subject line. Suggest that shape for multi-entry commits.
