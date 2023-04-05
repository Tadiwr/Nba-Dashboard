import sys
sys.path.append("./data")
import streamlit as st
import pandas as pd
from data.repo import Repo as rp

# Setting Page Layout and title
st.set_page_config(
    page_title="NBA STATS",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🏀📉"
)

st.title("NBA Statistics 🏀")
st.write("Made with 💚 by Tadiwa Shangwa")
"----------------------------------------------------------"

# Grabbing points data and sorting in ascending order
points = rp.static.get_team_points().sort_values(by="Points Scored")
ave_points_scored = int(points.mean()["Points Scored"])


"# Points Breakdown 😃✨"
most_points_col, least_points_col, ave_points_col = st.columns(3)

st.sidebar.markdown("Overview of the league")

def mostPoints():
    
    # Since the points are sorted from 
    # A-Z then the heights points are on the last row
    most_points = points.iloc[-1]

    off_average = int(most_points["Points Scored"]) - ave_points_scored

    most_points_col.markdown("### Most Points Scored")
    most_points_col.metric(
        most_points["Team"],
        str(most_points["Points Scored"]),
        delta=off_average
    )


def leastPoints():

    # Since the points are sorted from 
    # A-Z then the min points are on the first row
    least_points = points.iloc[0]

    offAverage = -(ave_points_scored - int(least_points["Points Scored"]))
    least_points_col.markdown("### Least Points Scored")
    least_points_col.metric(
        label = least_points["Team"],
        value = int(least_points["Points Scored"]),
        delta=offAverage,
    )

def avePoints():

    ave_points_col.markdown("### Average Points Scored")
    ave_points_col.metric(
        "Rounded Average",
        int(ave_points_scored),
    )

leastPoints()
mostPoints()
avePoints()

"----------------------------------------------------------"

# Bar chart for team points
"# Team Points 📊"
st.bar_chart(
    points,
    x="Team",
    y="Points Scored",
)

