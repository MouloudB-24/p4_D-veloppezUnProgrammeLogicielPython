class PlayerView:
    @staticmethod
    def display_player(player):
        """
        Displays the details of a single player.
        """
        print(f"Name: {player.first_name} {player.last_name}")
        print(f"Date of Birth: {player.birth_date}")
        print(f"Sex: {player.sex}")
        print(f"Chess ID: {player.chess_id}")
        print(f"Points: {player.points}")

    @staticmethod
    def display_players(players):
        """
        Displays a list of players.
        """
        if not players:
            print("No players available.")
        else:
            for player in players:
                print(f"{player.first_name} {player.last_name} (ID: {player.chess_id})")

    @staticmethod
    def get_player_details():
        """
        Prompts the user for player details.
        """
        last_name = input("Enter last name: ")
        first_name = input("Enter first name: ")
        birth_date = input("Enter birth date (YYYY-MM-DD): ")
        sex = input("Enter sex (M/F): ")
        chess_id = input("Enter chess ID: ")
        return last_name, first_name, birth_date, sex, chess_id
