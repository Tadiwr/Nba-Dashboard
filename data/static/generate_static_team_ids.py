import json
import pandas as pd
from os import path
import requests as req
from multipledispatch import dispatch
from IPython.core.display import JSON
from data.models.team_model import TeamModel

pd = pd

class Static:
    
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams"

    team_ids_path = "./data/static/team_ids.csv"

    def __init__(self) -> None:
        self.initialize_static_file()

    def genarate_team_ids(self):
        data = req.get(self.url).text

        # Serialize the JSON and only extract the Sports Atrribute
        data = json.loads(data)["sports"]

        # Extract Leagues attribute
        leagues = data[0]["leagues"]

        # Extract the NBA
        league = leagues[0]

        # Get teams
        teams = league["teams"]

        ids = []
        abbr = []
        display_names = []
            
        # Extract every teams name, initial, short name and display name
        for x in range(len(teams)):    
            ids.append(int(teams[x]["team"]["id"]))
            abbr.append(teams[x]["team"]["abbreviation"])
            display_names.append(teams[x]["team"]["displayName"])

        result = pd.DataFrame({
            'Id':ids,
            'Abbreviation':abbr,
            'Display Name':display_names
        })

        results = result.sort_values('Id')
        return results

    def team_ids_file_exist(self) -> bool:
        return path.exists(self.team_ids_path)

    def write_team_ids(self, data:str):
        with open(self.team_ids_path, 'w') as file:
            file.write(data)

    def initialize_static_file(self):

        exists = self.team_ids_file_exist()

        # Only if path doesn't exist

        if(exists == False):
            data = self.genarate_team_ids().to_csv()
            self.write_team_ids(data=data)

    def read_team_ids(self):
        return pd.read_csv(self.team_ids_path)

    def get_team_id_by_abbr(self, abbr:str) -> int:
        df = self.read_team_ids()
        team = df.loc[df["Abbreviation"] == abbr]
        id = int(team["Id"])
        return id
        
    
    def get_team_id_by_name(self,display_name):
        df = self.read_team_ids()
        team = df.loc[df["Display Name"] == display_name]
        return team["Id"][0]


