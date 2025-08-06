import streamlit as st
from PIL import Image

st.set_page_config(page_title="Strangely Attracted 💘", layout="centered")

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

