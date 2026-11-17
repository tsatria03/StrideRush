---
name: user_dualsense_controller
description: The dev's game controller is a PS5 DualSense; joystick features are tested on it
metadata:
  type: user
---

The dev owns and tests with a PlayStation 5 DualSense controller (dev, 2026-11-16: "That's the controler I currently own."). Joystick part 1 ([[project_joystick_plan]]) and vibration ([[project_joystick_vibration_plan]]) were tested on it. It's connected by USB (dev, 2026-11-16: "I'm using a USB connect. Usually I never go for bluetooth."), so anything Bluetooth-only goes untested unless the dev says otherwise.

**Why:** test steps and button names should match what's in the dev's hands; SDL maps it like an Xbox pad (cross is the game's A button, circle B, square X, triangle Y, L1 and R1 the shoulders, create is back, options is start).

**How to apply:** when writing joystick test steps, it's fine to add the PlayStation name after the game's name (A button, cross). Its rumble is SDL's emulation of the voice-coil haptics; over Bluetooth it needs SDL's PS5 rumble hint.
