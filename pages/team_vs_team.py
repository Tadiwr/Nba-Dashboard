import streamlit as st
import sys
sys.path.append("../data")
from data.repo import Repo as rp

def teamWidget():
    def showStats(abbr):

        id = rp.static.get_team_id_by_abbr(abbr)
        team1 = rp.teams_api.getTeamData(id)
        f"# {team1.display_name} "
        col1, col2, col3, col4, col5 = st.columns(5)


        col1.metric(
            label="Wins",
            value=team1.stats.wins
        )

        col2.metric(
            label="Loses",
            value=team1.stats.loses
        )

        col3.metric(
            label="Win Percentage",
            value=round(team1.stats.win_percentage,2)
        )

        col4.metric(
            label="Points Scored",
            value=team1.stats.points_scored
        )

        col5.metric(
            label="Streak",
            value=team1.stats.streak,
        )

    teamNames = rp.static.get_team_names()

    options = st.selectbox(options = teamNames, label="")
    showStats(options)

def team2Widget():
    def showStats(abbr):

        id = rp.static.get_team_id_by_abbr(abbr)
        team2 = rp.teams_api.getTeamData(id)
        f"# {team2.display_name} "
        col6, col7, col8, col9, col10 = st.columns(5)


        col6.metric(
            label="Wins",
            value=team2.stats.wins
        )

        col7.metric(
            label="Loses",
            value=team2.stats.loses
        )

        col8.metric(
            label="Win Percentage",
            value=round(team2.stats.win_percentage,2)
        )

        col9.metric(
            label="Points Scored",
            value=team2.stats.points_scored
        )

        col10.metric(
            label="Streak",
            value=team2.stats.streak,
        )

    teamNames = rp.static.get_team_names()

    options2 = st.selectbox(options = teamNames, label="", key=2)
    showStats(options2)

con1 = st.container()
con2 = st.container()

con1.write(teamWidget())
con2.write(team2Widget())


