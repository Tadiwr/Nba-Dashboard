import requests as req
import json
from data.models.team_model import TeamModel
import pandas as pd 

class TeamsAPI:

    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/"

    def getTeamData(self, id:int):
        team_json = req.get(self.url + str(id)).text
        team_dict = json.loads(team_json)
        team_dict = team_dict["team"]
        team_model = TeamModel(team_dict)
        return team_model
    
    def getAllTeamsPoints(self):
        team_points = []
        team_names = []

        for id in range(1, 31):
            team = self.getTeamData(id=id)
            team_points.append(team.stats.points_scored)
            team_names.append(team.name)
        
        df = pd.DataFrame({
        "Team":team_names,
        "Points Scored":team_points
        })
        
        return df
