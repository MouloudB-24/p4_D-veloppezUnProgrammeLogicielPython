# models/player.py

class Player:
    def __init__(self, last_name=None, first_name=None, birth_date=None, sex=None, chess_id=None):
        """
        Initializes a new player.

        :param last_name: The player's last name
        :param first_name: The player's first name
        :param birth_date: The player's birth date
        :param sex: The player's sex
        :param chess_id: The player's national chess ID
        """
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.chess_id = chess_id
        self.points = 0

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_sex(self, sex):
        self.sex = sex

    def set_chess_id(self, chess_id):
        self.chess_id = chess_id

    def add_points(self, points):
        """
        Adds points to the player.

        :param points: The number of points to add
        """
        self.points += points

    def to_dict(self):
        """
        Converts the player's information to a dictionary for JSON storage.
        """
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'sex': self.sex,
            'chess_id': self.chess_id,
            'points': self.points
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a player from a dictionary (loaded from JSON).

        :param data: Dictionary containing the player's data
        """
        player = cls(
            last_name=data['last_name'],
            first_name=data['first_name'],
            birth_date=data['birth_date'],
            sex=data['sex'],
            chess_id=data['chess_id']
        )
        player.points = data.get('points', 0)
        return player

    def __str__(self):
        """
        Returns a string representation of the player.
        """
        return f"{self.last_name} {self.first_name} (ID: {self.chess_id}) - Birth Date: {self.birth_date} - Points: {self.points}"