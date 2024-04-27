import random


class Match:
    def __init__(self, player_1, player_2, score_1=0, score_2=0):
        self.player_1 = player_1
        self.score_1 = score_1
        self.player_2 = player_2
        self.score_2 = score_2
        self.match = ([player_1, score_1], [player_2, score_2])

    def award_match_points(self):
        winner_index = random.randint(0, 1)
        if winner_index == 0:
            self.score_1 += 1
        elif winner_index == 1:
            self.score_2 += 1
        else:
            self.score_1 += 0.5
            self.score_2 += 0.5

        self.match[0][1] = self.score_1
        self.match[1][1] = self.score_2

    def __repr__(self):
        return f"{self.match}"
