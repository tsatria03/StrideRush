---
name: feedback_shop_prices
description: every player shop price is unique, and new shop things are priced in steps of 250 gold coins (2,250, 2,500, 2,750)
metadata:
  type: feedback
---

No two things in the player shop share a price, and new shop things are priced in steps of 250 gold coins.

**Why:** the dev (2026-11-27, pricing the pack helpers): "I don't like things in the shop having the same price." (Claude had proposed 2,000 for both helpers, which also clashed with the steel shield's 2,000), then "Also, in the future, make new shop things 250 gold a part."

**How to apply:** before proposing a price, list every price in tuning.nvgt's shop_character_prices, shop_item_prices and shop_special_prices, and pick a free multiple of 250 near where the thing belongs. Existing prices that aren't multiples of 250 (the character points, 25 to 200; the power crystal's 750 is one) stay as they are. See [[project_shop_plan]].
