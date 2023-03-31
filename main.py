import sys
sys.path.append("./data")
import streamlit as st
import pandas as pd
from data.repo import Repo as rp
import utils.utils as ut
import plotly.figure_factory as ff

# config

st.set_page_config(
    page_title="NBA STATS",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("NBA Statistics 🏀")
st.write("Powered by a secret api ⚡")
"----------------------------------------------------------"

# Statistics and Data
points = rp.static.get_team_points()
points = points.sort_values(by="Points Scored")
ave = int(points.mean()["Points Scored"])
leastPoints = 0
mostPoints = 0

# Views
"# Points Breakdown 😃✨"
col1, col2, col3 = st.columns(3)

st.sidebar.markdown("Overview of the league")


def mostPoints():
    
    mostPoints = points.iloc[-1]
    offAverage = int(mostPoints["Points Scored"]) - ave

    col1.markdown("### Most Points Scored")
    col1.metric(
        mostPoints["Team"],
        str(mostPoints["Points Scored"]),
        delta=offAverage
    )


def leastPoints():
    leastPoints = points.iloc[0]
    offAverage = -(ave - int(leastPoints["Points Scored"]))

    col2.markdown("### Least Points Scored")
    col2.metric(
        label = leastPoints["Team"],
        value = int(leastPoints["Points Scored"]),
        delta=offAverage,
    )

def avePoints():
    col3.markdown("### Average Points Scored")
    col3.metric(
        "Rounded Average",
        int(ave),
    )



leastPoints()
mostPoints()
avePoints()

"----------------------------------------------------------"

"# Team Points 📊"
order_points = points
st.bar_chart(
    points,
    x="Team",
    y="Points Scored",
)

