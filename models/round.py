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
        self.start_time = datetime.now()
        return self.start_time

    def add_match(self, match):
        self.matches.append(match)

    def finish_round(self):
        self.end_time = datetime.now()
        return self.end_time


if __name__ == "__main__":
    round = Round()
