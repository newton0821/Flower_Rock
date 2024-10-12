import streamlit as st

st.title('Newtons first apply')
st.image('Flower.gif')
import random
import streamlit as st

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Streamlit UI
st.title("Rock, Paper, Scissors Game")

# Options for the game
options = ["Rock", "Paper", "Scissors"]

# Ask the user to pick an option
user_choice = st.selectbox("Choose your option:", options)

# Button to play
if st.button("Play"):
    # Randomly select the computer's choice
    computer_choice = random.choice(options)

    # Display choices
    st.write(f"You chose: {user_choice}")
    st.write(f"Computer chose: {computer_choice}")

    # Determine the winner and display the result
    result = determine_winner(user_choice, computer_choice)
    st.write(result)

# Instructions
st.write("Click 'Play' to see if you can beat the computer!")
