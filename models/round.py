from datetime import datetime
from models.match import Match


class Round:
    def __init__(self, name=None, start_time=None, end_time=None):
        self.name = name
        self.start_time = start_time if start_time else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.end_time = end_time
        self.matches = []

    def set_name(self, name):
        self.name = name

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def add_match(self, match):
        if isinstance(match, Match):
            self.matches.append(match)

    def generate_results(self):
        for match in self.matches:
            match.generate_random_result()

    def to_dict(self):
        return {
            'name': self.name,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'matches': [match.to_dict() for match in self.matches]
        }

    @classmethod
    def from_dict(cls, data):
        round_ = cls(name=data['name'], start_time=data['start_time'], end_time=data['end_time'])
        round_.matches = [Match.from_dict(match_data) for match_data in data['matches']]
        return round_

    def __str__(self):
        return f"{self.name} - Start: {self.start_time}, End: {self.end_time}, Matches: {len(self.matches)}"
