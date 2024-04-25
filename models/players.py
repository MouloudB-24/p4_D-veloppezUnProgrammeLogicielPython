import json
from pathlib import Path
from pprint import pprint


class PlayerManager:

    def __init__(self):
        self.players = []
        self.backup_folder = Path.cwd().parent / "data" / "players" / "players.json"

    def add_player(self, first_name, last_name, birth_date, national_id):
        self.players.append({"first_name": first_name,
                             "last_name": last_name,
                             "birth_date": birth_date,
                             "national_id": national_id})

    def load_players(self):
        registered_players = []
        if self.backup_folder.exists():
            with open(self.backup_folder, "r") as file:
                registered_players = json.load(file)
        return registered_players

    def _update_players(self):
        new_players = self.players[:]
        registered_players = self.load_players()
        for player in self.players:
            if player in registered_players:
                new_players.remove(player)
        return new_players

    def save_players(self):
        self.backup_folder.parent.mkdir(exist_ok=True, parents=True)
        new_players = self._update_players()
        if new_players:
            with open(self.backup_folder, "a") as file:
                json.dump(new_players, file, indent=2)


class Tournament:
    def __init__(self, name, place, start_date, end_date, round_number=4):
        pass


class Rounds:
    pass


class Match:
    pass


if __name__ == "__main__":
    player_manager = PlayerManager()
    player_manager.add_player("Aylan", "BELLIL", "30/07/2023", "AB986523")
    player_manager.add_player("Mouloud", "BELLIL", "04/08/1992", "AB986523")
    player_manager.add_player("Victor", "REICHARD", "08/09/1996", "AB986523")
    #pprint(player_manager.load_players())
    player_manager.save_players()
