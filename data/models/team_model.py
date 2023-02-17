from pandas import Series
import pandas as pd

class __StatsModel__:
    summary = ""
    
    def __init__(self, stats:list[dict]) -> None:
        self.wins = int(stats[17]["value"])
        self.ties = int(stats[15]["value"])
        self.loses = int(stats[9]["value"])
        self.games_played = int(stats[7]["value"])
        self.streak = int(stats[14]["value"])
        self.points_scored = int(stats[13]["value"])
        self.points_conceded = int(stats[12]["value"])
        self.win_percentage = stats[16]["value"] * 100
        self.summary = str(self.wins) + " - " + str(self.loses)

class TeamModel:
    id = ""
    uid = 0
    slug = "",
    location = "",
    name = "",
    abbr = "",
    display_name = "",
    short_display_name = ""
    color = ""
    alternative_color = ""
    is_active = True
    logos = []
    division =  ""
    dision_standing = ""
    stats = ""

    def __init__(self, team:Series) -> None:

         standing_summary = team["standingSummary"].split(" ")
         self.id = int(str(team["id"]))
         self.uid = team["uid"]
         self.slug = team["slug"]
         self.location = team["location"]
         self.name = team["name"]
         self.abbr = team["abbreviation"]
         self.display_name = team["displayName"]
         self.short_display_name = team["shortDisplayName"]
         self.color = team["color"]
         self.alternative_color = team["alternateColor"]
         self.is_active = team["isActive"]
         self.logos = team["logos"]
         self.stats = __StatsModel__(team["record"]["items"][0]["stats"])
         self.division = standing_summary[2] + " " + standing_summary[3]
         self.dision_standing = standing_summary[0]

    
