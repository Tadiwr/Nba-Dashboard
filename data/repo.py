from data.apis.teams_api import TeamsAPI
from data.static.generate_static_team_ids import Static

class Repo:

    teams = TeamsAPI()
    static = Static()