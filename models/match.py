import random
from models.player import Player


class Match:
    def __init__(self, player1, player2, score1=0, score2=0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def set_score(self, score1, score2):
        self.score1 = score1
        self.score2 = score2

    def generate_random_result(self):
        """
        Generates a random result for the match.
        """
        result = random.choice([(1, 0), (0, 1), (0.5, 0.5)])
        self.set_score(*result)
        self.update_player_points()

    def update_player_points(self):
        """
        Updates the points of the players based on the match result.
        """
        self.player1.points += self.score1
        self.player2.points += self.score2

    def to_dict(self):
        return {
            'player1': self.player1.to_dict(),
            'score1': self.score1,
            'player2': self.player2.to_dict(),
            'score2': self.score2
        }

    @classmethod
    def from_dict(cls, data):
        player1 = Player.from_dict(data['player1'])
        player2 = Player.from_dict(data['player2'])
        return cls(player1, player2, data['score1'], data['score2'])

    def __str__(self):
        return f"{self.player1} vs {self.player2} - Score: {self.score1}:{self.score2}"


if __name__ == "__main__":
    pass
