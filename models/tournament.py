from pathlib import Path
import json


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
        self.save_folder = Path.cwd().parent / "data" / "tournament"

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
        self.registered_players.append(player)

    def add_round(self, round):
        self.rounds[self.current_round - 1].append(round)

    def start_next_round(self):
        if self.current_round < self.number_rounds:
            self.current_round += 1
            self.rounds[self.current_round - 1] = []

    def get_tournament(self):
        return {
            "name": self.name,
            "location": self.location,
            "date": f"{self.start_date} - {self.end_date}",
            "list_of_players": self.registered_players,
            "rounds": self.rounds,
            "current_round": self.current_round,
            "description": self.description
        }

    def save_tournament(self):
        self.save_folder.mkdir(parents=True, exist_ok=True)
        save_file = self.save_folder / "tournament.json"

        # Load the existing player list if there is one
        if save_file.exists():
            with open(save_file, "r") as file:
                tournament_list = json.load(file)
        else:
            tournament_list = []

        new_tournament = self.get_tournament()
        exiting_tournament = any(new_tournament["name"] == player["name"] for player in tournament_list)

        # Add new player
        if not exiting_tournament:
            tournament_list.append(new_tournament)

            # Save updated player list
            with open(save_file, "w") as file:
                json.dump(tournament_list, file,  ensure_ascii=False, indent=2)
        else:
            print(f"The tournament '{new_tournament['name']}' already existed in the database")


if __name__ == "__main__":
    tournament = Tournament()
    tournament.set_name("Tournoi d'échecs")
    tournament.set_location("Paris")
    tournament.set_date("30/09/2024", "15/10/2024")
    tournament.save_tournament()
