class Tournament:
    def __init__(self):
        self.name = None
        self.location = None
        self.start_date = None
        self.end_date = None
        self.description = None
        self.number_rounds = 4
        self.current_round = 1
        self.rounds = [[] for _ in range(self.number_rounds)]
        self.registered_players = []

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def set_date(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def set_number_rounds(self, number_rounds):
        self.number_rounds = number_rounds

    def set_description(self, description):
        self.description = description

    def register_player(self, player):
        self.registered_players.append(player.get_player())

    def add_round(self, round):
        self.rounds[self.current_round - 1].append(round.matches)

    def start_next_round(self):
        if self.current_round < self.number_rounds:
            self.current_round += 1
            self.rounds[self.current_round - 1] = []

    def get_tournament_info(self):
        return {
            "name": self.name,
            "location": self.location,
            "date": f"{self.start_date} - {self.end_date}",
            "list_of_players": self.registered_players,
            "rounds": self.rounds,
            "current_round": self.current_round,
            "description": self.description
        }

    def __str__(self):
        return f"{self.get_tournament_info()})"


if __name__ == "__main__":
    #tournament = Tournament("Tournoi d'échecs", "Paris", "30/09/2024", "15/10/2024", number_of_rounds=4)
    #print(tournament.registered_players)
    pass
