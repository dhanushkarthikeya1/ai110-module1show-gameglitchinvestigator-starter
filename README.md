# 🎮 Game Glitch Investigator

Game Glitch Investigator is a Streamlit number guessing game. Choose Easy, Normal, or Hard, guess the hidden whole number in the displayed range, and use the hints to find it before the attempt limit runs out. The Developer Debug Info panel displays the secret number for investigation and testing.

## Run the game

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

Run the automated tests with:

```bash
python -m pytest -q
```

## Demo Walkthrough

Example Normal game with a secret number of 57:

1. The game starts with 8 attempts and a score of 0.
2. Enter `40`; the game says “Go HIGHER!” and keeps the score at 0.
3. Enter `80`; the game says “Go LOWER!” and keeps the score at 0.
4. Enter `57`; the game announces the win and awards 80 points for solving it on the third attempt.
5. Click **New Game** to start a fresh game with a new secret and reset attempts, score, and guess history.

## Document Your Experience

Baseline testing exposed three concrete bugs: a low guess could receive a “Go LOWER!” hint, an incorrect guess could add points, and New Game did not leave a lost state. The baseline `pytest` run also failed because the logic module contained placeholder functions.

The fixes were:

- Moved the game rules into `logic_utils.py` so they can be tested without running the UI.
- Corrected high and low outcomes and their direction hints.
- Kept guesses and the secret as integers on every attempt, preventing alternating attempts from comparing numbers to strings.
- Made invalid input and decimals fail clearly instead of consuming an attempt or silently truncating a decimal.
- Made incorrect guesses apply a consistent five-point penalty without allowing a negative score; faster wins earn more points.
- Reset the status, score, attempts, and history when starting a new game. Changing difficulty starts a game in the selected range.

## Test Results

The suite covers the game outcomes, scoring, difficulty ranges, and edge cases for blank input, whitespace, decimals, and non-numeric text.

```text
..........                                                               [100%]
10 passed in 0.02s
```

## Edge-case testing

Challenge 1 completed: tests verify that empty input, whitespace, decimal input, and non-numeric text are handled without crashing or being silently converted into a guess.
