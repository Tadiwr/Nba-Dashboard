from data.models.short_team_model import ShortTeamModel
import mysql.connector as mysql
from pandas import DataFrame

class Database:

    host = "localhost"
    user = "root"
    password = "password"
    cursor = None
    db = None

    def __init__(self) -> None:
        self.connect()

    def connect(self):
        self.db = mysql.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )

        self.cursor = self.db.cursor()

    def getTeamIDS(self) -> DataFrame:
        sql =   """
                    select * from nba.team_ids
                    order by team_id;
                """
        self.cursor.execute(sql)
        result = DataFrame(self.cursor.fetchall())
        ids = result[0]
        abbr = result[1]
        names = result[2]

        # assembling dataframe
        result = DataFrame({
            "Id":ids,
            "Abbriviation":abbr,
            "Name":names
        })

        return result

    def getTeamByID(self, id:int):
        sql = f"""Select * from nba.team_ids 
                where team_id={id} 
              """

        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        id = result[0][0]
        abbr = result[0][1]
        name = result[0][2]

        result_model = ShortTeamModel(
            i = id,
            a = abbr,
            n = name
        )

        return result_model
        



