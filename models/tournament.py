class Tournament:
    def __init__(self, name, location, start_date, end_date, number_of_rounds=4, current_round=1, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.rounds = [[] for _ in range(number_of_rounds)]
        self.registered_players = []
        self.description = description

    def add_player(self, player):
        self.registered_players.append(player)

    def add_round(self, round):
        self.rounds[self.current_round - 1].append(round)

    def start_next_round(self):
        if self.current_round < self.number_of_rounds:
            self.current_round += 1
            self.rounds[self.current_round - 1] = []

    def show_tournament_info(self):
        return {
            "name": self.name,
            "location": self.location,
            "date": f"{self.start_date} - {self.end_date}",
            "rounds": self.rounds,
            "current_round": self.current_round,
            "description": self.description
        }

    def __str__(self):
        return f"{self.show_tournament_info()})"


if __name__ == "__main__":
    tournament = Tournament("Tournoi d'échecs", "Paris", "30/09/2024", "15/10/2024", number_of_rounds=4)
    print(tournament.registered_players)
