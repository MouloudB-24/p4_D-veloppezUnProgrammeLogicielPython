import json
from pathlib import Path
from ..models.player import Player


class PlayerManager:
    def __init__(self, save_directory=None):
        if save_directory:
            save_directory = Path.cwd().parent / "data" / "players"
        self.save_directory = Path(save_directory)
        self.players = []

    def add_players(self, players):
        self.players.extend(players)

    def save_players(self):
        save_file = self.save_directory / "players.json"
        player_dicts = [player.get_player() for player in self.players]
        with open(save_file, "w") as file:
            json.dump(player_dicts, file)

    def load_players(self):
        save_file = self.save_directory / "players.json"
        with open(save_file, "r") as file:
            player_dicts = json.load(file)
        self.players = [Player(**player_dict) for player_dict in player_dicts]
