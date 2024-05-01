from datetime import datetime


class Round:
    def __init__(self):
        self.name = None
        self.start_time = None
        self.end_time = None
        self.matches = []

    def set_name(self, name):
        self.name = name

    def start_round(self):
        self.start_time = str(datetime.now())

    def add_match(self, match):
        self.matches.append(match)

    def finish_round(self):
        self.end_time = str(datetime.now())

    def get_round(self):
        return {
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": self.matches
        }


if __name__ == "__main__":
    round = Round()
