import json
import datetime as dt
import pandas as pd
from os import path
import requests as req
import utils.utils as ut
from pathlib import Path
from data.apis.teams_api import TeamsAPI as tapi


api = tapi()

class Static:
    
    
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams"

    team_ids_path = "./data/static/team_ids.csv"
    team_points_path = "./team_points"

    def __init__(self) -> None:
        lastUpdated = self.reading_state()
        today = str(dt.date.today())
        if lastUpdated != today :
            self.generate_team_points()
            self.generate_team_percentages()
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
    
    def get_team_names(self):
        df = pd.read_csv("./data/static/team_ids.csv")
        df = df.sort_values("Abbreviation")
        df = df["Abbreviation"].values
        teams = []

        for x in range(0, 30):
            teams.append(df[x])

        return teams

    def generate_team_points(self):
        team_points = ut.getAllTeamsPoints(1)
        team_points = team_points.to_csv("./data/static/team_points.csv")
        today = str(dt.date.today())
        self.write_state(today)

    def get_team_points(self):
        team_points = pd.read_csv("./data/static/team_points.csv")
        return team_points

    def generate_team_percentages(self):
    
        percentages = []
        team = []

        for x in range(1, 31):
            data = api.getTeamData(x)
            team.append(data.display_name)
            percentages.append(round(data.stats.win_percentage, 2))

        df = pd.DataFrame({
            "Team":team,
            "Win Percentage":percentages
        })

        file = open("./data/static/win_percentages.csv", "w")
        string = df.to_csv()
        file.write(string)
        file.close()
        today = str(dt.date.today())
        self.write_state(today)

    def get_win_percentages(self):
        state = self.reading_state()
        today = str(dt.date.today())
        if state != today:
            self.generate_team_percentages()
        return pd.read_csv("./data/static/win_percentages.csv")

    def write_state(self, string:str):
        file = open("state.txt", "w")
        file.write(string)
        file.close()
    
    def reading_state(self) -> list[str]:
        file = open("state.txt", "r")
        data = file.read()
        file.close()
        return data