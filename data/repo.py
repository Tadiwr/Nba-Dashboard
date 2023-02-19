from data.apis.teams_api import TeamsAPI
from data.static.generate_static_team_ids import Static
from data.database.db import Database

class Repo:

    teams_api = TeamsAPI()
    static = Static()
    db = Database()