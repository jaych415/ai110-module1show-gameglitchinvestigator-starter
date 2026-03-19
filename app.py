import streamlit as st
import random
from logic_utils import check_guess, parse_guess

st.title("🎯 Number Guessing Game")

# Initialize session state
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

guess_input = st.text_input("Enter your guess (1-100):")

if st.button("Submit Guess") and not st.session_state.game_over:
    guess = parse_guess(guess_input)

    if guess is None:
        st.error("❌ Invalid input. Enter a number.")
    else:
        st.session_state.attempts += 1
        result = check_guess(guess, st.session_state.secret)

        if result == "correct":
            st.success(f"🎉 Correct! You won in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True
        elif result == "high":
            st.warning("📉 Too high!")
        elif result == "low":
            st.warning("📈 Too low!")

# Reset button
if st.button("Restart Game"):
    st.session_state.secret = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False