from data.apis.teams_api import TeamsAPI
from data.static.generator import Static
import data.apis.scoreboard as sb

class Repo:

    teams_api = TeamsAPI()
    static = Static()
    scoreboard = sb.getScoreBoard()