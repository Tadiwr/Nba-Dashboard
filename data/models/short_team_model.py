class ShortTeamModel:
    id = 0
    abbr = ""
    name = ""

    def __init__(self, i:int, a:str, n:str) -> None:
        self.id = i
        self.abbr = a
        self.name = n