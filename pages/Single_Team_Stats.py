import streamlit as st
import sys
sys.path.append("../data")
from data.repo import Repo as rp


def showStats(abbr):
    
    id = rp.static.get_team_id_by_abbr(abbr)
    data = rp.teams_api.getTeamData(id)
    f"# {data.display_name} "
    col1, col2, col3, col4, col5 = st.columns(5)


    col1.metric(
        label="Wins",
        value=data.stats.wins
    )

    col2.metric(
        label="Loses",
        value=data.stats.loses
    )

    col3.metric(
        label="Win Percentage",
        value=round(data.stats.win_percentage,2)
    )

    col4.metric(
        label="Points Scored",
        value=data.stats.points_scored
    )

    col5.metric(
        label="Streak",
        value=data.stats.streak,
    )

teamNames = rp.static.get_team_names()

single_options = st.selectbox(options = teamNames, label="")
showStats(single_options)
