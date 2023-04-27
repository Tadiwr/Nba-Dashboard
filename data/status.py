import json

import datetime as dt


class Status:


    file_path = "status.json"


    def __init__(self):
        file = open(self.file_path, "r")

        self.json_str = file.read()
        file.close()

        self.status_dict = json.loads(self.json_str)


    def __commit_changes__(self):
        json_str = json.dumps(self.status_dict)
        file = open(self.file_path, "w")

        file.write(json_str)
        file.close()


    def get_last_updated(self):

        return self.status_dict["last_updated"]


    def get_requests_count(self):

        return self.status_dict["requests_count"]


    def update_last_updated(self):

        today = str(dt.date.today())

        self.status_dict["last_updated"] = today

        self.__commit_changes__()


    def update_req_counts(self):
        new_count = self.status_dict["requests_count"] + 1

        self.status_dict["requests_count"] = new_count

        self.__commit_changes__()

        