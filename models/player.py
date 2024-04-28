class Player:
    def __init__(self, first_name, last_name, date_of_birth, chess_id, sex=None):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.chess_id = chess_id
        self.sex = sex
        self.points = 0

    def add_point(self, score):
        self.points += score

    def get_player_info(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "chess_id": self.chess_id,
            "sex": self.sex,
            "points": self.points
        }

    def update_player_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return f"{self.get_player_info()}"


if __name__ == "__main__":
    aylan = Player("Aylan", "BELLIL", "30/07/2023", "AB98762", "M")
    print(aylan)
