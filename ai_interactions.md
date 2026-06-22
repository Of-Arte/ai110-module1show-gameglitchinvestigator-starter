# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**
I manually reviewed app.py and identified the bugs myself before asking the agent to fix them one by one. Example: "The hints 'Higher'/'Lower' within the check_guess function are inconsistent, help me find the issue and refactor the function"

**What did the agent do?**

1. Read app.py
2. Found 2 bugs:
   a. check_guess() — when guess > secret it says "Go HIGHER!" but should say "Go LOWER!", and vice versa
   b. TypeError (lines 158-161) - on even attempts secret is turned into a string causing comparison errors, producing incorrect hint results.
3. Fixed both bugs by swapping the conditional logic in check_guess() and ensuring that guess is always compared as an integer.

**What did you have to verify or fix manually?**

- To verify the hints were accurate after the agent's fix, I created tests to run through various inputs to ensure the function was returning the correct outputs for each case.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case                 | Prompt Used                                                                                                                                | AI-Suggested Test          | Did It Pass? | Your Reasoning                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- | ------------ | ------------------------------------------------------------------------------------ |
| Guess is 50, secret is 50 | "We need to create a test case where the player's guess is equal to the secret number, to make sure the function returns "Win" correctly." | test_guess_equals_secret() | No           | The existing test case was not properly constructed and failed to assert the correct |

---
