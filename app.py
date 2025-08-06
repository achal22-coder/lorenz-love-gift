import streamlit as st
st.set_page_config(page_title="Strangely Attracted 💘", layout="centered")

from PIL import Image
import random
import numpy as np
import matplotlib.pyplot as plt
from love_data import get_love_dataframe, show_love_story



# Session state to track access
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

# Funny password screen
def password_screen():
    st.title("Who dares to enter the Scientific Love world?")
    st.write("This love story is **highly confidential**. This app can only be run by a certain **Jiggly-loving user**. Please identify yourself 🧐")
    st.write("_Hint: The cartoon character you call me ..._ ")

    password = st.text_input("Enter the Secret Nickname:", type="password")

    if password == "doraemon":
        st.success("Access granted! Welcome to the birthday love simulation 💘")
        st.session_state.unlocked = True
        st.rerun()
    elif password:
        wrong_responses = [
           
            "Try again, Sexy Brain. I believe in you 🧠❤️",
        
            "404: Love not found. Try again, babe."
        ]
        st.error(random.choice(wrong_responses))

# Main app after unlocking

def show_main_app():
    st.title("🦋 Strangely Attracted — A Chaotic Love Story")
    st.subheader("Built with SciML, Love, and Efforts")

    st.markdown("""
    This isn’t just a birthday gift.  
    It’s a simulation of us in equations, in chaos, in code.

    Welcome to the butterfly effect of our love 🦋💜
    """)

    # Display the Lorenz attractor plot
    image = Image.open("assets/lorenz.png")
    st.image(image, caption="We may swirl and twist, but we always come back together.", use_container_width=True)

    show_love_story()

    st.markdown("---")
    st.subheader("📈 Our Love Regression")

    df = get_love_dataframe()

   # Fit a simple polynomial regression model
    X = df["Days"].values.reshape(-1, 1)
    y = df["Love Score"].values
    z = np.polyfit(df["Days"], df["Love Score"], 3)
    p = np.poly1d(z)

    # Plot the regression
    fig, ax = plt.subplots()
    ax.scatter(df["Days"], df["Love Score"], color='purple', label='Actual Points')
    ax.plot(df["Days"], p(df["Days"]), color='hotpink', linewidth=2, label='Love Curve')

    # Annotate the events
    for _, row in df.iterrows():
        ax.annotate(row["Event"], (row["Days"], row["Love Score"] + 2), fontsize=8)

    ax.set_title("Love Over Time 💗")
    ax.set_xlabel("Days Since First Text")
    ax.set_ylabel("Love Score")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    st.caption("Every point on this curve is a memory, a smile, a moment we chose each other.")

  

    st.markdown("---")
    st.subheader("🎁 The Final Surprise")

    st.markdown("---")
st.subheader("🎁 The Final Surprise")

with st.expander("🔐 Click to unlock your final surprise..."):
    password = st.text_input("Enter the secret code (hint: my sexy wala nickname):", type="password")

    if password == "koala":  
        st.success("Access granted! 💘")
        st.markdown("""
        **You unlocked the final layer of this chaos and love.**  
        And behind it... is just something simple.
        
         Just a reminder that you are one of the most precious part of my entire simulation (my life).  
                    
        *Now check the gift below.* 🎁
        """)
        st.image("assets/letter.jpg", caption="A little something I made with all my heart 💌", use_container_width=True)


    elif password:
        st.error("Oops! That's not it. Love doesn't respond to random inputs 😛")
        
    if st.button("👀 One last thing?"):
        st.image("assets/silly_you.jpg", caption="Even this version of you is adorable")

    st.markdown("""
    ---

    **Final Model Output:**  
    Accuracy = 100%  
    Confidence = Absolute  
    Conclusion = *She loves you in every known dimension*
    """)

    st.markdown("""
    **\"Among all the strange equations of life, you are my one true solution.\"**  
    *May your curiosity always stay wild and you never forget how deeply you are cared for.*

    **HAPPY BIRTHDAY LIL HONEY BEE!!**  
    **A Little Gift From Your Jiggly Baby**  
    *I hope you like it.*
    """)

# App control logic
if not st.session_state.unlocked:
    password_screen()
else:
    show_main_app()
