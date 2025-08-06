import streamlit as st

st.markdown("---")
st.subheader("📖 Our Scientific Love Story")

with st.expander("🧪 Click to expand the love..."):
    st.markdown("""
**14 August – The Beginning**  
Our first text.  
Like the starting point in a chaotic system small, but it changed everything.

---

**29 August – A Beautiful Disruption**  
You proposed.  
Two variables drifted apart from normal emotions began to swirl and dance.

---

**5 September – Orbit Locked**  
We got together.  
Even in chaos, we found each other constantly moving, yet always drawn back.

---

**15 November – First Touch of Stability**  
Our first kiss.  
The system found rhythm. A single moment settled into something unforgettable.

---

**27 January – Long Distance Begins**  
A disturbance.  
New forces entered, but our connection stayed strong steady through the storm.

---

**18 August – A Full Circle**  
Your birthday.  
The system loops not repeating, but growing. Our love, evolving with time.
    """)
import pandas as pd
from datetime import datetime

# Important dates in YYYY-MM-DD format
events = {
    "First Text": "2023-08-14",
    "Proposal": "2023-08-29",
    "Got Together": "2023-09-05",
    "First Kiss": "2023-11-15",
    "Long Distance": "2024-01-27",
    "Your Birthday": "2024-12-22"
}

# Assign a symbolic love score (totally subjective and cute)
love_scores = {
    "First Text": 10,
    "Proposal": 30,
    "Got Together": 60,
    "First Kiss": 80,
    "Long Distance": 95,
    "Your Birthday": 100
}

# Convert to DataFrame
def get_love_dataframe():
    base_date = datetime.strptime("2023-08-14", "%Y-%m-%d")
    data = []

    for event, date_str in events.items():
        date = datetime.strptime(date_str, "%Y-%m-%d")
        days_since_start = (date - base_date).days
        score = love_scores[event]
        data.append((days_since_start, score, event))

    df = pd.DataFrame(data, columns=["Days", "Love Score", "Event"])
    return df
