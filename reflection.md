# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

The game is a Streamlit number guessing game with difficulty settings, a score, and a developer panel that displays the secret number. Baseline testing showed that the hint could be wrong, an incorrect guess could increase the score, and the New Game button did not reset a completed game. The starter tests also failed because the functions in `logic_utils.py` were placeholders.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| In Normal mode, secret shown as 55; enter 40 on the first submission | Since 40 is below 55, show “Go HIGHER!” | The game showed “Go LOWER!” | none |
| In Normal mode, enter 9999 as an incorrect guess | An incorrect guess should not increase the score | On the first submitted guess, the score increased by 5 | none |
| Submit incorrect guesses until “Out of attempts!” appears, then click “New Game” | Start a new playable game with status `playing` | Attempts changed to 0, but status remained `lost` and “Game over” stayed on screen | none |

## 2. How did you use AI as a teammate?

I used ChatGPT/Codex to inspect the starter code, plan the refactor, implement the logic changes, and add pytest coverage. A useful suggestion was to keep the game rules in `logic_utils.py` and have the Streamlit app call those functions; the tests then verified each outcome and the UI test verified the repaired hint and reset behavior. One early diagnosis from the assistant treated a guess of 101 against a secret of 55 as proof of a wrong visible hint, but the observed “Go LOWER!” direction was actually correct for that high guess, so I rejected that example and verified the bug with 40 against 55 instead. That check produced the incorrect “Go LOWER!” hint for a low guess, which identified the real user-visible failure.

## 3. Debugging and testing your fixes

I treated a bug as fixed only after checking the relevant helper with pytest and exercising the related behavior in the Streamlit test interface. The final suite has 10 passing tests for ranges, parsing, high/low/win outcomes, and scoring; it also checks blank input, whitespace, decimals, and non-numeric text. I tested the game flow separately: a low guess produced “Go HIGHER!”, and clicking New Game after losing restored `playing` status, zero attempts, zero score, and empty history. The baseline test run had three failures because `logic_utils.py` had unimplemented functions; all passed after the refactor.

## 4. What did you learn about Streamlit and state?

Streamlit reruns the Python script when a user interacts with a widget. Ordinary variables are recreated during each rerun, so values that must persist, such as the secret number, score, and attempt count, belong in `st.session_state`. A New Game action must update all related session state together; resetting only the attempt count can leave the app stuck in a previous win or loss.

## 5. Looking ahead: your developer habits

I want to keep separating pure game logic from UI code so small rules can be tested quickly. Next time I work with AI, I will verify its diagnosis against an exact input and observed output before changing code. This project reinforced that AI-generated code and even AI-generated diagnoses can sound plausible while still being wrong, so tests and direct checks need to guide the final decision.
