---
name: project_engine_pinned_nvgt
description: Target the legacy NVGT fork at C:\nvgt (BASS audio, source in misc/Legacy-NVGT); C:\nvgt2 (stock miniaudio) is only for testing others' games
metadata:
  type: project
---

Stride Rush targets the dev's legacy NVGT fork at C:\nvgt (nvgt.exe console build, nvgtw.exe windowed, BASS audio). Its source is at tsatria03/misc/Legacy-NVGT, and its stdlib includes are under release/include there. A stock NVGT at C:\nvgt2 (miniaudio) exists only for testing other people's games.

**Why:** the dev's games depend on fork-specific behavior; upstream NVGT changed the audio backend and is incompatible. The dev pointed at both paths for context on 2026-11-01.

**How to apply:** don't target C:\nvgt2, don't treat upstream NVGT docs as authoritative, and don't suggest upgrading. Check API questions against Legacy-NVGT source or C:\nvgt\nvgt.chm.
