import random

import streamlit as st

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def start_game(low: int, high: int, difficulty: str) -> None:
    """Reset all per-game state and choose a secret within the selected range."""
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.game_difficulty = difficulty


st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")
difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)
attempt_limit_map = {"Easy": 6, "Normal": 8, "Hard": 5}
attempt_limit = attempt_limit_map[difficulty]
low, high = get_range_for_difficulty(difficulty)

if (
    "secret" not in st.session_state
    or st.session_state.get("game_difficulty") != difficulty
):
    start_game(low, high, difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

st.subheader("Make a guess")
st.info(
    f"Guess a whole number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input("Enter your guess:", key="guess_input")

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    # FIX: reset status, score, attempts, and history together for a clean game.
    start_game(low, high, difficulty)
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
else:
    if submit:
        ok, guess_int, err = parse_guess(raw_guess)

        if not ok:
            st.error(err)
        elif guess_int < low or guess_int > high:
            st.error(f"Enter a number from {low} to {high}.")
        else:
            st.session_state.attempts += 1
            st.session_state.history.append(guess_int)

            # FIX: compare integers consistently; do not stringify the secret on
            # alternating attempts, which caused incorrect outcomes and hints.
            outcome, message = check_guess(guess_int, st.session_state.secret)

            if show_hint:
                st.warning(message)

            st.session_state.score = update_score(
                current_score=st.session_state.score,
                outcome=outcome,
                attempt_number=st.session_state.attempts,
            )

            if outcome == "Win":
                st.session_state.status = "won"
                st.balloons()
                st.success(
                    f"You won! The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score}"
                )
            elif st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
