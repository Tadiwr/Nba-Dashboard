import requests as req
import json
import pandas as pd
from data.models.team_model import TeamModel

class TeamsAPI:

    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/"

    def getTeamData(self, id:str):

        team_json = req.get(self.url + str(id)).text

        team_data = pd.Series(pd.Series(json.loads(pd.Series(team_json)[0]))[0])
        team_model = TeamModel(team_data)
        return team_model
