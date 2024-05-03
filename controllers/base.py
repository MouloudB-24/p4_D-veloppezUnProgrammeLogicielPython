import random


class Controller:
    def __init__(self, tournament):
        self.tournament = tournament

    def shuffle_players(self):
        return random.shuffle(self.tournament.registered_players)
