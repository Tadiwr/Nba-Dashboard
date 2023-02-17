from data.models.team_model import TeamModel
import pandas as pd
from data.repo import Repo
from matplotlib import pyplot as plt

def Summarize(team_data:TeamModel):
    columns = [
        "Full Name", "Abbreviation", "Division", "Location",
         "Games Played", "Win-Lose Record", "Win Percentage", 
         "Points Scored", "Points Conceded"
    ]

    
    # type: ignore
    
    data = [
        team_data.display_name, team_data.abbr,
        team_data.division, team_data.location, 
        team_data.stats.games_played,
        team_data.stats.summary,
        team_data.stats.win_percentage,
        team_data.stats.points_scored,
        team_data.stats.points_conceded
    ]

    return pd.DataFrame({
        'columns':columns,
        'data':data
    })

def SummarizeAllTeamsWinPercentage():

    column = "leagueWinPercent"

    win_percentages : list[float] = [

    ]

    teams_abbriviations = Repo.static.read_team_ids()["Abbreviation"].values
    team_ids = Repo.static.read_team_ids()["Id"].values


    for team in team_ids:
        n_team_data = Repo.teams.getTeamData(id=team)
        win_percentage = n_team_data.stats.win_percentage
        win_percentages.append(win_percentage)

    table = pd.DataFrame({
        "Team": teams_abbriviations,
        "Win Percentage": win_percentages
    })

    return table
    
