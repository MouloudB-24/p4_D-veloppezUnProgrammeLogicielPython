class Player:
    def __init__(self, first_name, last_name, date_of_birth, chess_id, sex=None, elo_rating=None):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.chess_id = chess_id
        self.sex = sex
        self.elo_rating = elo_rating
        self.points = 0

    def add_points(self):
        self.points += 1

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.date_of_birth,
            "chess_id": self.chess_id,
            "sex": self.sex,
            "elo_rating": self.elo_rating
        }

    def update_info(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


if __name__ == "__main__":
    Aylan = Player("Aylan", "BELLIL", "30/07/2023", "AB98762", "M")
    Mouloud = Player("Mouloud", "BELLIL", "04/08/2023", "MB23452", "M")
    tournoi_ermont = Tournament("Tournoi d'Ermont", "Ermont", "25/04/2024", "30/04/2024")

