import random
import streamlit as st
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

# FIX: Refactored logic into logic_utils.py using agent mode
st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

# Rounded outer container + subtle card shadow
st.markdown(
    """
    <style>
    .main .block-container {
        border-radius: 1.5rem;
        border: 1px solid rgba(128, 128, 128, 0.15);
        padding: 2rem 2.5rem;
        max-width: 680px !important;
        margin-left: auto !important;
        margin-right: auto !important;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.07);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 style='text-align:center;'>🎮 Game Glitch Investigator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>An AI-generated guessing game. Something is off.</p>", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────
st.sidebar.header("Settings")

with st.sidebar.container(border=True):
    st.markdown("##### 🎯 Difficulty")
    difficulty = st.selectbox(
        "Difficulty level",
        ["Easy", "Normal", "Hard"],
        index=1,
        label_visibility="collapsed",
    )
    attempt_limit_map = {
        "Easy": 6,
        "Normal": 8,
        "Hard": 5,
    }
    attempt_limit = attempt_limit_map[difficulty]
    low, high = get_range_for_difficulty(difficulty)
    st.caption(f"Range: {low} – {high}")
    st.caption(f"Max attempts: {attempt_limit}")

# Track difficulty in session state to detect changes and reset the game state if needed
# FIX: Reset the game state (secret number, attempts, history, status) when difficulty is changed to ensure the secret is within the new difficulty range, implemented in agent mode.
if "difficulty" not in st.session_state:
    st.session_state.difficulty = difficulty

if st.session_state.difficulty != difficulty:
    st.session_state.difficulty = difficulty
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.history = []
    st.session_state.status = "playing"

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

# FIX: Initialized attempts to 0 so the user receives the full number of allowed attempts, implemented in agent mode.
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar.expander("🔧 Developer Debug"):
    st.write("Secret:", st.session_state.get("secret", "—"))
    st.write("Attempts:", st.session_state.get("attempts", 0))
    st.write("Score:", st.session_state.get("score", 0))
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.get("history", []))

with st.container(border=True):
    st.subheader("Make a guess")

    # FIX: Dynamically displays the current difficulty range (low to high) instead of a hardcoded 1 to 100, implemented in agent mode.
    st.info(
        f"Guess a number between {low} and {high}. "
        f"Attempts left: {attempt_limit - st.session_state.attempts}"
    )

    raw_guess = st.text_input(
        "Enter your guess:",
        key=f"guess_input_{difficulty}"
    )

    show_hint = st.checkbox("Show hint", value=True)

    col1, col2 = st.columns(2)
    with col1:
        submit = st.button("Submit Guess 🚀", use_container_width=True)
    with col2:
        new_game = st.button("New Game 🔁", use_container_width=True)

if new_game:
    # FIX: Reset all game states (including status, attempts, and history) on new game and use correct difficulty range for secret number, implemented in agent mode.
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.history = []
    st.session_state.status = "playing"
    st.session_state.score = 0
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        # FIX: Removed the type conversion bug on even attempts where secret was cast to str, ensuring the secret number remains an int, implemented in agent mode.
        outcome, message = check_guess(guess_int, st.session_state.secret)

        if show_hint:
            st.warning(message)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

st.divider()
st.markdown("<small style='display:block; text-align:center; color:gray;'>Built by an AI that claims this code is production-ready.</small>", unsafe_allow_html=True)
