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
    status = []
    for event in events:
        game = event["shortName"]
        game_date = event["date"].split("T")[0]
        game_time = event["date"].split("T")[1]
        is_completed = event["status"]["type"]["completed"]

        if is_completed:
            is_completed = "Full Time"
        else:
            is_completed = "Upcoming/Live"

        times.append(game_time)
        dates.append(game_date)
        shortNames.append(game)
        status.append(is_completed)

    scoreboard = pd.DataFrame({
        "Games":shortNames,
        "Date": dates,
        "Time":times,
        "Game Status": status
    })

    return scoreboard