from datetime import datetime
import time
from models.match import Match


class Round:
    def __init__(self, name, start_time=None, end_time=None):
        self.name = name
        self.start_time = start_time if start_time else datetime.now()
        self.end_time = end_time
        self.matches = []

    def started_round(self):
        return self.start_time

    def add_match(self, match):
        self.matches.append(match.get_match_score())

    def finish_round(self):
        self.end_time = datetime.now()
        return self.end_time

    def __repr__(self):
        return f"{self.name}:Match: {self.matches}, Start Time: {self.started_round()}, End Time: {self.finish_round()}"


if __name__ == "__main__":
    match0 = Match("Aylan", "Mouloud")
    match0.award_match_points()

    match1 = Match("Mily", "Rose")
    match1.award_match_points()

    round_1 = Round("Round 1")
    round_1.add_match(match0)
    round_1.add_match(match1)

    print(round_1)
