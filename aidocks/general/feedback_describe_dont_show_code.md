---
name: feedback_describe_dont_show_code
description: For a multi-section build, present all section plans up front (classes/functions + prose), then code each section on go-ahead without re-presenting it; never paste code into chat
metadata:
  type: feedback
---

When a feature takes several sections, give the whole plan in one message: how many sections, and for each one the classes and functions it adds with a one-line explanation. Don't show the actual code. Then build one section per go-ahead, without recapping its plan.

**Why:** the dev reviews the real files after each section. Code pasted into chat is redundant and clutters the screen-reader read-through. Carried over from SimpleFighter.

**How to apply:** save the plan in aidocks/plans/ ([[feedback_memory_folder_layout]]). Each section still waits for a go-ahead ([[feedback_confirm_before_implementing]]) and ends with [[feedback_list_modified_files]].
