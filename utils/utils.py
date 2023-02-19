from data.apis.teams_api import TeamsAPI as tp
import pandas as pd

api = tp()
team_points = []
team_names = []

def getAllTeamsPoints(x=int):

        if x != 31:
            team = api.getTeamData(id=x)
            team_points.append(team.stats.points_scored)
            team_names.append(team.name)
            getAllTeamsPoints(x + 1)
        
        df = pd.DataFrame({
        "Team":team_names,
        "Points Scored":team_points
        })

        return df