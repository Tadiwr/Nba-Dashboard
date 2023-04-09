import sys
sys.path.append("../data")

import streamlit as st
from data.repo import Repo as rp


st.title("Wins and Loses 🍻")

def wins_widget():
    data = rp.static.get_team_wins_and_loses()
    data = data.filter(items = ["Team", "Wins"])

    # Ordering the data set by wins from Z-A
    data = data.sort_values(by="Wins", ascending=False)

    "---------------------------------"
    ave = round(data["Wins"].mean(), 2)
    col1, col2, col3 = st.columns(3)

    def avepec():
        col1.write("### Average Number of Wins")
        col1.metric(
            label="",
            value=ave
        )

    def max():
        df = data.sort_values(by="Wins")
        max = df.iloc[-1]
        col2.write("### Highest Number of Wins")
        col2.metric(
            label=max["Team"],
            value=max["Wins"]
        )

    def min():
        df = data.sort_values(by="Wins")
        min = df.iloc[0]
        col3.write("### Lowest Number of Wins")
        col3.metric(
            label=min["Team"],
            value=min["Wins"]
        )

    max()
    avepec()
    min()
    "--------------------------------"
    st.bar_chart(data, x = "Team", y="Wins")
    "----------------------------------------------"
    st.table(data)


def loses_widgets():
    data = rp.static.get_team_wins_and_loses()
    data = data.filter(items=["Team", "Loses"])

    "---------------------------------"
    ave = round(data["Loses"].mean(), 2)
    col1, col2, col3 = st.columns(3)

    def average():
        col1.write("### Average Number of Loses")
        col1.metric(
            label="",
            value=ave
        )

    def max():
        df = data.sort_values(by="Loses")
        max = df.iloc[-1]
        col2.write("### Highest Number of Loses")
        col2.metric(
            label=max["Team"],
            value=max["Loses"]
        )

    def min():
        df = data.sort_values(by="Loses")
        min = df.iloc[0]
        col3.write("### Lowest Number of Loses")
        col3.metric(
            label=min["Team"],
            value=min["Loses"]
        )

    max()
    average()
    min()
    "--------------------------------"
    st.bar_chart(data, x = "Team", y="Loses")
    "----------------------------------------------"
    st.table(data)

def points_widgets():

    # Grabbing points data and sorting in ascending order
    points = rp.static.get_team_points().sort_values(by="Points Scored")
    ave_points_scored = int(points.mean()["Points Scored"])


    "# Points Breakdown 😃✨"
    most_points_col, least_points_col, ave_points_col = st.columns(3)

    def max():
        
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


    def min():

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

    def average():

        ave_points_col.markdown("### Average Points Scored")
        ave_points_col.metric(
            "Rounded Average",
            int(ave_points_scored),
        )

    max()
    average()
    min()

    "----------------------------------------------------------"

    # Bar chart for team points
    "# Team Points 📊"
    st.bar_chart(
        points,
        x="Team",
        y="Points Scored",
    )
