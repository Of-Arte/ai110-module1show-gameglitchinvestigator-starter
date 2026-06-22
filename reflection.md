# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - The game initially started with inaccurate "Lower/Higher" hints, making it more difficult to win.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - The higher/lower hints were incorrect, causing the user to guess in the wrong direction.
  - Changing the difficulty did not reset the game state under the expected conditions.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                                  | Expected Behavior                                  | Actual Behavior                                           | Console Output / Error                      |
| -------------------------------------- | -------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------- |
| Guess of 60 when secret is 50          | Returns "Too High" and hints "Go LOWER"            | Returned "Too High" but hinted "Go HIGHER"                | none                                        |
| Even attempt number (e.g. 2nd attempt) | Hints compare integer values                       | Secret is cast to string, causing TypeError in comparison | TypeError (caught internally by try-except) |
| Change difficulty setting in dropdown  | Resets game state with new range and secret number | Secret number is kept or remains out of new range         | none                                        |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude Code, Gemini 3.1 Flash.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - The AI correctly identified the cause of the "wrong hints" bug and fixed it by swapping the conditional logic in check_guess(). I verified this by testing the function with values above, below, and equal to the secret number.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - When I asked Claude to help me debug the check_guess function, I noticed an unsually lengthy response time. After checking the thinking process, I noticed there was a hiccup in the tool execution flow which required me to manually end the request and restart it. Once restarted it worked properly and Claude picked up where it left off and was able to complete the task.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - By using pytest to assert the outcomes of various inputs and using dev tools to monitor for errors and console logs.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - Ran pytest for test_winning_guess, test_guess_too_high, and test_guess_too_low from tests/test_game_logic.py. These tests verified that for a secret of 50, a guess of 50 correctly returns "Win", 60 returns "Too High", and 40 returns "Too Low".
- Did AI help you design or understand any tests? How?
  - Yes. The AI suggested adding `test_parse_guess_float` to test decimal inputs to catch floating point errors if the player enters a decimal.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Every interaction with a widget in streamlit causes the entire app.py to re-execute from the first line. This means that if you define a variable as a plain python variable outside of a function, it will reset to the initial value on every attempt. To prevent this, we use st.session_state, which stays persistent across reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.
  - Using AI assistance to quickly gain context of a new project and identify bugs while reserving human judgment for the final refactoring design.

- What is one thing you would do differently next time you work with AI on a coding task?
  - I would provide the model with direct access to documentation of any libraries or frameworks it uses to avoid adding additional bugs.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - In this exercise I learned that while AI is excellent at quickly providing context and refactoring existing code, it can make errors in its own execution flow and should always be used with human oversight.
