import streamlit as st
import random
import time
from PIL import Image

# Set Page Config
st.set_page_config(page_title="Mind Growth Kids", page_icon="🧠", layout="centered")
# Load and Resize Image
image = Image.open("images/kid.png")  # Image path ensure karein
resized_image = image.resize((300, 200))  # Width: 300, Height: 300

# Display Image with Proper Size
st.image(resized_image, caption="🧠 Fun Mind Growth Game for Kids!", use_container_width=True)
# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #FFDDC1;
            color: #333;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .stApp {
            background-color: #FFDDC1;
        }
        .stButton>button {
            background-color: #FF4500;
            color: white;
            font-size: 26px;
            border-radius: 15px;
            padding: 20px;
            width: 100%;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #FF6347;
        }
        .stTextInput>div>div>input, .stNumberInput>div>div>input {
            font-size: 24px;
            padding: 10px;
            border: 3px solid #FF4500;
            border-radius: 10px;
        }
        .stSelectbox>div>div>select {
            font-size: 24px;
            padding: 10px;
            border: 3px solid #FF4500;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🧠🎈 Mind Growth Kids Challenge 🎈🧠")
st.subheader("🌈 Fun & Exciting Brain Games for Smart Kids! 🚀")

# Select Challenge
st.write("🎮 Choose a fun challenge to play:")
options = ["🃏 Memory Game", "➕ Math Quiz", "🔠 Word Puzzle"]
choice = st.selectbox("🎯 Select a Challenge", options)

# Score Tracking
if "score" not in st.session_state:
    st.session_state.score = 0

st.write(f"🌟 Your Current Score: **{st.session_state.score}** 🎯")

# ---------------------- MEMORY GAME ----------------------
if choice == "🃏 Memory Game":
    st.subheader("🃏 Memory Game: Remember the Sequence")
    numbers = [random.randint(1, 100) for _ in range(5)]
    sequence = ", ".join(map(str, numbers))
    st.write("👀 Remember this sequence:")
    st.write(f"**🎲 {sequence} 🎲**")

    time.sleep(10)  # Increased Time for Kids
    st.write("✍️ Now enter the numbers in correct order!")
    user_input = st.text_input("🔢 Enter numbers separated by commas:")

    if st.button("Check 🧐", use_container_width=True):
        user_numbers = list(map(int, user_input.replace(" ", "").split(",")))
        if user_numbers == numbers:
            st.success("🎉🎊 Correct! Well Done! 🎊🎉")
            st.session_state.score += 1
        else:
            st.error(f"❌ Oops! The correct sequence was {sequence}")

# ---------------------- MATH QUIZ ----------------------
elif choice == "➕ Math Quiz":
    st.subheader("➕ Math Quiz Challenge")
    num1, num2 = random.randint(1, 20), random.randint(1, 20)
    correct_answer = num1 + num2

    user_answer = st.number_input(f"🤔 What is {num1} + {num2}?", min_value=0)
    if st.button("Submit ✅", use_container_width=True):
        if user_answer == correct_answer:
            st.success("🎉 Yay! You got it right! 🌟")
            st.session_state.score += 1
        else:
            st.error(f"❌ Oops! The correct answer was {correct_answer}")

# ---------------------- WORD PUZZLE ----------------------
elif choice == "🔠 Word Puzzle":
    st.subheader("🔠 Word Puzzle Challenge")
    words = ["python", "streamlit", "challenge", "brain", "puzzle"]
    word = random.choice(words)
    jumbled_word = "".join(random.sample(word, len(word)))

    st.write(f"🤹 Unscramble the word: **✨ {jumbled_word} ✨**")
    user_word = st.text_input("🔤 Your answer:")

    if st.button("Check Answer 🧐", use_container_width=True):
        if user_word.lower() == word:
            st.success("🎉 Correct! You're a genius! 🏆")
            st.session_state.score += 1
        else:
            st.error(f"❌ Try Again! The correct word was: {word}")

# Show Final Score
st.write(f"🏆 Your Final Score: **{st.session_state.score}** 🏅")








# import streamlit as st
# import random
# import time


# #app.title
# st.title("🧩 Cognitive Skills Trainer")
# st.subheader("Train your brain with fun and interactive challenges!")
# st.write("Choose a challenge:")
# options = ["Memory Game", "Math Quiz", "Word Puzzle"]
# choice = st.selectbox("Select a Challenge", options)

# #score tracking
# if "score" not in st.session_state:
#     st.session_state.score = 0
#     st.write(f"Your Current Score: **{st.session_state.score}** 🎯")

#     #memeory game:
#     if choice == "Memory Game":
#         st.subheader("🃏 Memory Game: Remember the Sequence")
#     numbers = [random.randint (1 , 100) for _ in range (5)]
#     st.write("Remember this sequence:")
#     st.write(numbers)

#     time.sleep(5)
#     st.write("Now enter the numbers in correct order!")
#     user_input = st.text_input("Enter numbers separated by space:")
#     if st.button ("check"):
#         user_numbers = list(map(int, user_input.split()))
#         if user_numbers == numbers:
#             st.success = ("Correct! 🎉")
#             st.session_state.score += 1
#     else:
#         st.error(f"Wrong! The correct sequence was {numbers}")

#         #math quiz
    
# elif choice == "Math Quaiz":
#     st.subheader("➕ Math Quiz Challenge")
#     num1, num2 = random.randint(1, 20), random.randint(1, 20)
#     correct_answer = num1 + num2

#     user_answer = st.number_input(f"What is {num1} + {num2}?", min_value=0)
#     if st.button("submitted"):
#         if user_answer == correct_answer:
#             st.status("Correct! 🎉")
#             st.session_state.score += 1

#         else:
#             st.error(f"Wrong! The correct answer was {correct_answer}")

#             # WORD PUZZLE 
        
#     elif choice ==  "Word Puzzle":
#         st.subheader("🔠 Word Puzzle Challenge")
#         words =  ["python", "streamlit", "challenge", "brain"]
#         word = random.choice(words)
#         jumbled_word = "".join(random.sample(word, len(word)))

#         st.write(f"Unscramble the word: **{jumbled_word}**")
#         user_word = st.text_input("Your answer:")

#         if st.button("Check Answer"):
#               if user_word.lower() == word:
#                 st.success("Correct! 🎉")
#                 st.session_state.score += 1
#         else:
#             st.error(f"Wrong! Try Again! ❌ The correct word was: {word}")

# # Show Final Score
# st.write(f"🏆 Your Final Score: **{st.session_state.score}**")

