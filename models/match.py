class Match:
    def __init__(self, player_1, score_1, player_2, score_2):
        self.player_1 = player_1
        self.score_1 = score_1
        self.player_2 = player_2
        self.score_2 = score_2
        self.match = ([player_1, score_1], [player_2, score_2])

    def __repr__(self):
        return f"{self.match}"
