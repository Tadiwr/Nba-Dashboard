import streamlit as st
import sys
sys.path.append("../data")
from data.repo import Repo as rp
import pandas as pd


teama_stats = []
teamb_stats = []
statisitcs = ["Wins", "Loses", "Win Percentage","Points Scored", "Streak"]


def get_team_stats(abbr):
    id = rp.static.get_team_id_by_abbr(abbr)
    team = rp.teams_api.getTeamData(id)
    team_stats = [
        team.stats.wins, team.stats.loses,
        team.stats.win_percentage, 
        team.stats.points_scored,team.stats.streak
    ]

    return team_stats


# UI
st.write("# Head To Head 🥊")
col1, col2 = st.columns(2)

# Select team 1
teamNames = rp.static.get_team_names()
options1 = col1.selectbox(options = teamNames, label="", key=1)
teama_stats = get_team_stats(options1)
teama_name = options1

# Select team 2
teamNames = rp.static.get_team_names()
options2 = col2.selectbox(options = teamNames, label="", key=2)
teamb_stats = get_team_stats(options2)
teamb_name = options2


df = pd.DataFrame({
    "Statistic": statisitcs,
    teama_name: teama_stats,
    teamb_name: teamb_stats
})

st.table(df)