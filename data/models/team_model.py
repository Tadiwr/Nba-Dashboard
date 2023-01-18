from pandas import Series
import pandas as pd

class __RecordModel__:
    summary = ""
    stats = ""
    def __init__(self, record) -> None:
        self.stats = pd.DataFrame(pd.Series(record)["stats"])
        self.summary = record['summary']

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
    record = ""

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
         self.record = __RecordModel__(team["record"]["items"][0])
         self.division = standing_summary[2] + " " + standing_summary[3]
         self.dision_standing = standing_summary[0]

    
