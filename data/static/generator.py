import json
from os import path
import pandas as pd
import datetime as dt
import requests as req
from pathlib import Path
from data.apis.teams_api import TeamsAPI as tapi

# I cant import the repo class due
# to circular imports
team_api = tapi()

class Static:
    
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams"

    team_ids_path = "./data/static/team_ids.csv"
    team_points_path = "./data/static/team_points.csv"
    team_percentages_path = "./data/static/win_percentages.csv"
    last_updated_path = "last_updated.txt"
    win_perc_path = "./data/static/win_percentages.csv"
    wins_and_loses_path = "./data/static/wins_and_loses.csv"

    def __init__(self) -> None:
        self.generate_team_stats()
        self.genarate_team_ids()
  

    def genarate_team_ids(self):
        exists = path.exists(self.team_ids_path)
        if(exists == False):
            data = req.get(self.url).text
            data = json.loads(data)["sports"]
            teams = data[0]["leagues"][0]["teams"]

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

            result = result.sort_values('Id')
            result.to_csv(self.team_ids_path)

    def get_team_ids(self):
        return pd.read_csv(self.team_ids_path)

    def get_team_id_by_abbr(self, abbr:str) -> int:
        df = self.get_team_ids()
        team = df.loc[df["Abbreviation"] == abbr]
        id = int(team["Id"])
        return id
        
    
    def get_team_id_by_name(self,display_name):
        df = self.get_team_ids()
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

    def generate_team_stats(self):
        today = str(dt.date.today())
        last_update = self.read_date_last_updated()
        team_points = []
        team_names = []
        percentages = []
        wins = []
        loses = []

        if today != last_update:
            for x in range(1, 31):
                team = team_api.getTeamData(x)
                team_names.append(team.display_name)
                team_points.append(team.stats.points_scored)
                percentages.append(team.stats.win_percentage)
                wins.append(team.stats.wins)
                loses.append(team.stats.loses)

            percentages_df = pd.DataFrame({
                "Team":team_names,
                "Win Percentage":percentages
            })

            points_df = pd.DataFrame({
                "Team":team_names,
                "Points Scored":team_points
            })

            wins_df = pd.DataFrame({
                "Team":team_names,
                "Wins":wins,
                "Loses":loses
            })

            percentages_df.to_csv(self.team_percentages_path)
            points_df.to_csv(self.team_points_path)
            wins_df.to_csv(self.wins_and_loses_path)
            self.write_date_last_updated(today)

    def get_team_points(self):
        self.generate_team_stats()
        return pd.read_csv(self.team_points_path)

    def get_win_percentages(self):
        self.generate_team_stats()
        return pd.read_csv(self.win_perc_path)

    def write_date_last_updated(self, string:str):
        file = open(self.last_updated_path, "w")
        file.write(string)
        file.close()
    
    def read_date_last_updated(self) -> list[str]:
        file = open(self.last_updated_path, "r")
        date = file.read()
        file.close()
        return date
    
    def get_team_wins_and_loses(self) -> pd.DataFrame:
        self.generate_team_stats()
        return pd.read_csv(self.wins_and_loses_path)