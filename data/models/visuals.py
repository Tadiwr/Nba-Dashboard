from data.models.team_model import TeamModel
import pandas as pd

def Summerize(team_data:TeamModel):
    columns = [
        "Full Name", "Abbreviation", "Division", "Location",
         "Win-Lose Record"
    ]
    data = [
        team_data.display_name, team_data.abbr,
        team_data.division, team_data.location, 
        team_data.record.summary
    ]

    return pd.DataFrame({
        'columns':columns,
        'data':data
    })
