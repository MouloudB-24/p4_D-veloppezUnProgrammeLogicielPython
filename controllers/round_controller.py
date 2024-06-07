from models.round import Round
from models.match import Match


class RoundController:
    def create_round(self, name):
        round_ = Round(name)
        return round_

    def add_match_to_round(self, round_, player1, player2):
        match = Match(player1, player2)
        round_.add_match(match)

    def generate_results_for_round(self, round_):
        round_.generate_results()
