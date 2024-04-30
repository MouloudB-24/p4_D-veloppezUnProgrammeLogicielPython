import json
from pathlib import Path


class Player:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.date_of_birth = None
        self.sex = None
        self.chess_id = None
        self.points = 0
        self.save_folder = Path.cwd().parent / "data" / "tournament"

    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def set_sex(self, sex):
        self.sex = sex

    def set_chess_id(self, chess_id):
        self.chess_id = chess_id

    def set_save_folder(self, save_folder):
        self.save_folder = save_folder

    def update_points(self, score):
        self.points += score

    def get_player(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "chess_id": self.chess_id,
            "sex": self.sex,
            "points": self.points
        }

    def update_player(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def save_player(self):
        self.save_folder.mkdir(parents=True, exist_ok=True)
        save_file = self.save_folder / "players.json"

        # Load the existing player list if there is one
        if save_file.exists():
            with open(save_file, "r") as file:
                players_list = json.load(file)
        else:
            players_list = []

        new_player = self.get_player()
        registered_player = any(new_player["chess_id"] == player["chess_id"] for player in players_list)

        # Add new player
        if not registered_player:
            players_list.append(new_player)

            # Save updated player list
            with open(save_file, "w") as file:
                json.dump(players_list, file, indent=2)
        else:
            print(f"The player {new_player} already existed in the database")


if __name__ == "__main__":
    aylan = Player()
    aylan.set_name("Aylan", "BELLIL")
    aylan.set_date_of_birth( "30/07/2023")
    aylan.set_sex("M")
    aylan.set_chess_id("AB98762")
    aylan.save_player()

