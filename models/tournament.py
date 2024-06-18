from models.match import Match
from models.round import Round
from models.player import Player
import random


class Tournament:
    def __init__(self, name=None, location=None, start_date=None, end_date=None, rounds_count=4, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds_count = rounds_count
        self.current_round_number = 0
        self.rounds = []
        self.players = []
        self.description = description
        self.match_history = {}

    def set_name(self, name):
        self.name = name

    def set_location(self, location):
        self.location = location

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_rounds_count(self, rounds_count):
        self.rounds_count = rounds_count

    def set_description(self, description):
        self.description = description

    def add_player(self, player):
        if isinstance(player, Player):
            self.players.append(player)
            if player.chess_id not in self.match_history:
                self.match_history[player.chess_id] = []

    def add_round(self, round_):
        if isinstance(round_, Round):
            self.rounds.append(round_)
            self.current_round_number += 1

    def generate_pairs(self):
        if self.current_round_number == 0:
            random.shuffle(self.players)
        else:
            self.players.sort(key=lambda player: player.points, reverse=True)

        pairs = []
        used_players = set()

        # Gérer le cas où le nombre de joueurs est impair
        bye_player = None
        if len(self.players) % 2 != 0:
            for player in self.players:
                if player.chess_id not in self.match_history:
                    self.match_history[player.chess_id] = []
                if player not in used_players:
                    bye_player = player
                    used_players.add(player)
                    break

        for i in range(len(self.players)):
            if self.players[i] in used_players:
                continue
            for j in range(i + 1, len(self.players)):
                if self.players[j].chess_id not in self.match_history:
                    self.match_history[self.players[j].chess_id] = []
                if self.players[j] not in used_players and self.players[j].chess_id not in self.match_history[
                   self.players[i].chess_id]:
                    pairs.append((self.players[i], self.players[j]))
                    used_players.add(self.players[i])
                    used_players.add(self.players[j])
                    self.match_history[self.players[i].chess_id].append(self.players[j].chess_id)
                    self.match_history[self.players[j].chess_id].append(self.players[i].chess_id)
                    break

        if bye_player:
            print(f"{bye_player.first_name} {bye_player.last_name} do not play in this round.")

        return pairs

    def generate_round(self):
        if self.current_round_number >= self.rounds_count:
            raise Exception("The maximum number of rounds has been reached.")

        round_ = Round(name=f"Round {self.current_round_number + 1}")
        pairs = self.generate_pairs()
        for player1, player2 in pairs:
            match = Match(player1, player2)
            match.generate_random_result()
            round_.add_match(match)

        self.add_round(round_)
        return round_

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rounds_count": self.rounds_count,
            "current_round_number": self.current_round_number,
            "rounds": [round_.to_dict() for round_ in self.rounds],
            "players": [player.to_dict() for player in self.players],
            "description": self.description,
            "match_history": self.match_history,
        }

    @classmethod
    def from_dict(cls, data):
        tournament = cls(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            rounds_count=data["rounds_count"],
            description=data["description"],
        )
        tournament.current_round_number = data.get("current_round_number", 0)
        tournament.rounds = [
            Round.from_dict(round_data) for round_data in data["rounds"]
        ]
        tournament.players = [
            Player.from_dict(player_data) for player_data in data["players"]
        ]
        tournament.match_history = data.get("match_history", {})
        return tournament

    def __str__(self):
        return (
            f"Tournament: {self.name} at {self.location} from {self.start_date} to {self.end_date},"
            f"Rounds: {self.rounds_count}, Current Round: {self.current_round_number}, Players: {len(self.players)}"
        )


if __name__ == "__main__":
    pass
