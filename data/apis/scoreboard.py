import requests as req
from IPython.core.display import JSON
import json
import pandas as pd

def getScoreBoard():
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
    data = req.get(url).text
    data = json.loads(data)

    events = data["events"]

    shortNames = []
    dates = []
    times = []
    for event in events:
        game = event["shortName"]
        game_date = event["date"].split("T")[0]
        game_time = event["date"].split("T")[1]
        times.append(game_time)
        dates.append(game_date)
        shortNames.append(game)

    scoreboard = pd.DataFrame({
        "Games":shortNames,
        "Date": dates,
        "Time":times
    })

    return scoreboard