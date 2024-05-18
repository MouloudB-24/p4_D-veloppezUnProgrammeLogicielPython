class TournamentView:
    @staticmethod
    def display_tournament(tournament):
        """
        Displays the details of a single tournament.
        """
        print(f"Tournament Name: {tournament.name}")
        print(f"Location: {tournament.location}")
        print(f"Start Date: {tournament.start_date}")
        print(f"End Date: {tournament.end_date}")
        print(f"Number of Rounds: {tournament.rounds_count}")
        print(f"Current Round: {tournament.current_round_number}")
        print(f"Description: {tournament.description}")
        print("\nPlayers:")
        for player in tournament.players:
            print(f"{player.first_name} {player.last_name} (ID: {player.chess_id})")

    @staticmethod
    def display_tournaments(tournaments):
        """
        Displays a list of tournaments.
        """
        if not tournaments:
            print("No tournaments available.")
        else:
            for tournament in tournaments:
                print(
                    f"{tournament.name} - {tournament.location} (From {tournament.start_date} to {tournament.end_date})")

    @staticmethod
    def get_tournament_details():
        """
        Prompts the user for tournament details.
        """
        name = input("Enter tournament name: ")
        location = input("Enter tournament location: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        rounds_count = int(input("Enter number of rounds: "))
        description = input("Enter description: ")
        return name, location, start_date, end_date, rounds_count, description

    @staticmethod
    def get_tournament_name():
        """
        Prompts the user for the tournament name.
        """
        return input("Enter tournament name: ")

    @staticmethod
    def get_player_chess_id():
        """
        Prompts the user for the player's chess ID.
        """
        return input("Enter player's chess ID: ")
