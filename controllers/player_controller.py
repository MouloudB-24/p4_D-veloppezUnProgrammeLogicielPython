from models.player import Player
from utils.data_manager import save_players, load_players


class PlayerController:
    def __init__(self):
        self.players = load_players()

    def add_player(self, last_name, first_name, birth_date, sex, chess_id):
        player = Player(last_name, first_name, birth_date, sex, chess_id)
        self.players.append(player)
        save_players(self.players)

    def list_players(self):
        return self.players

    def find_player_by_id(self, chess_id):
        for player in self.players:
            if player.chess_id == chess_id:
                return player
        return None

