from datetime import datetime
import time
from models.match import Match


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

    def __repr__(self):
        return f"{self.name}:Match: {self.matches}, Start Time: {self.start_round()}, End Time: {self.finish_round()}"


if __name__ == "__main__":
    match0 = Match("Aylan", "Mouloud")
    match0.award_points()

    match1 = Match("Mily", "Rose")
    match1.award_points()

    round_1 = Round("Round 1")
    round_1.add_match(match0)
    round_1.add_match(match1)

    print(round_1)
