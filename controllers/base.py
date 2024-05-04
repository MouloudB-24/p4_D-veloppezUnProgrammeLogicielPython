import random


class Controller:
    def __init__(self, player):
        self.player = player
        self.played_pairs = []

    def shuffle_players(self):
        return random.shuffle(self.tournament.registered_players)

