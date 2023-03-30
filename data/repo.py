from data.apis.teams_api import TeamsAPI
from data.static.generate_static_team_ids import Static
import data.apis.scoreboard as sb

class Repo:

    
    teams_api = TeamsAPI()
    static = Static()
    scoreboard = sb.getScoreBoard()