from datetime import datetime
import json
from config import SAVE_FOLDER


class Round:
    def __init__(self):
        self.name = None
        self.start_time = None
        self.end_time = None
        self.matches = []
        self.save_folder = SAVE_FOLDER

    def set_name(self, name):
        self.name = name

    def start_round(self):
        self.start_time = datetime.now()

    def add_match(self, match):
        self.matches.append(match)

    def finish_round(self):
        self.end_time = datetime.now()

    def get_round(self):
        return {
            "name": self.name,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "matches": self.matches
        }

    def save_round(self):
        self.save_folder.mkdir(parents=True, exist_ok=True)
        save_file = self.save_folder / "rounds.json"

        # Load the existing player list if there is one
        if save_file.exists():
            with open(save_file, "r") as file:
                rounds_list = json.load(file)
        else:
            rounds_list = []

        # Check if round exists in JSON database
        registered_round = any(self.name == round["name"] for round in rounds_list)

        # Add new round
        if not registered_round:
            rounds_list.append(self.get_round())

            # Save updated round list
            with open(save_file, "w") as file:
                json.dump(rounds_list, file, indent=2)
        else:
            print(f"The round already existed in the database")


if __name__ == "__main__":
    round1 = Round()
    round1.set_name("Round 1")
    round1.start_round()
    round1.finish_round()
    round1.save_round()


