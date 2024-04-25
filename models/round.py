from datetime import datetime
import time


class Round:
    def __init__(self, name, start_time=None, end_time=None):
        self.name = name
        self.matches = []
        self.start_time = start_time if start_time else datetime.now()
        self.end_time = end_time

    def started_round(self):
        return self.start_time

    def add_match(self, match):
        self.matches.append(match)

    def finish_round(self):
        self.end_time = datetime.now()
        return self.end_time

    def __repr__(self):
        return f"{self.name}:Match: {self.matches}, Start Time: {self.started_round()}, End Time: {self.finish_round()}"


if __name__ == "__main__":
    round_1 = Round("Round 1")
    time.sleep(4)
    print(round_1)
