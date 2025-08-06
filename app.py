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

import numpy as np
import matplotlib.pyplot as plt
from love_data import get_love_dataframe

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
