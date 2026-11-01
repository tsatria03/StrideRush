---
name: project_sound_device_indexing
description: NVGT's output device list is index 0 "No sound", 1 "Default", 2+ named devices; don't add a synthetic Default in a device picker
metadata:
  type: project
---

get_sound_output_devices() returns index 0 "No sound", index 1 "Default", and real devices from index 2. ToyMania's settings picker strips index 0.

**Why:** rebuilding the picker makes it easy to add a second Default or store an index that's off by one against the trimmed list.

**How to apply:** if Stride Rush borrows ToyMania's device picker, keep its index math as is and don't inject a Default item. Related: [[feedback_verify_code_while_fixing]].
