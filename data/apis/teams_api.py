import requests as req
import json
from data.models.team_model import TeamModel 

class TeamsAPI:

    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/"
    starting_id = 1

    def getTeamData(self, id:int):
        team_json = req.get(self.url + str(id)).text
        team_dict = json.loads(team_json)
        team_dict = team_dict["team"]
        team_model = TeamModel(team_dict)
        return team_model
        return team_dict
