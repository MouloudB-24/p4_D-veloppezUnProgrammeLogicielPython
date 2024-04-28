import random


class Match:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = 0
        self.score_2 = 0

    def award_match_points(self):
        winner_index = random.randint(0, 2)
        if winner_index == 0:
            self.score_1 += 1
            self.player_1.add_point(1)
        elif winner_index == 1:
            self.score_2 += 1
            self.player_2.add_point(1)
        else:
            self.score_1 += 0.5
            self.score_2 += 0.5
            self.player_1.add_point(0.5)
            self.player_1.add_point(0.5)

    def get_match_score(self):
        return [self.player_1.first_name, self.score_1], [self.player_2.first_name, self.score_2]

    def __repr__(self):
        return f"{self.get_match_score()}"


if __name__ == "__main__":
    match0 = Match("Aylan", "Mouloud")
    match0.award_match_points()
    print(match0)
