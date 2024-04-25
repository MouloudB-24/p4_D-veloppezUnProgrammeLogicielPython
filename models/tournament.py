class Tournament:
    def __init__(self, name, location, start_date, end_date, rounds=4, current_round=1, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.current_round = current_round
        self.matches = [[] for _ in range(rounds)]
        self.registered_players = []
        self.description = description

    def add_player(self, player):
        self.registered_players.append(player)

    def add_match(self, match):
        self.matches[self.current_round - 1].append(match)

    def award_match_points(self, match_index, winner_index):
        match = self.matches[self.current_round - 1][match_index]
        winner, loser = match
        if winner_index == 0:
            winner.add_points()
        elif winner_index == 1:
            loser.add_points()
        else:
            winner.add_points(0.5)
            loser.add_points(0.5)

    def start_next_round(self):
        if self.current_round < self.rounds:
            self.current_round += 1
            self.matches[self.current_round - 1] = []

    def __str__(self):
        return f"{self.name} {self.registered_players})"


if __name__ == "__main__":
    tournament = Tournament("Tournoi d'échecs", "Paris", "30/09/2024", "15/10/2024", rounds=4)
    print(tournament.registered_players)
