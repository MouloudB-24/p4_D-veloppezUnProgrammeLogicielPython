class RoundView:
    @staticmethod
    def display_round(round_):
        """
        Displays the details of a single round.
        """
        print(f"Round Name: {round_.name}")
        print(f"Start Time: {round_.start_time}")
        print(f"End Time: {round_.end_time}")
        print("\nMatches:")
        for match in round_.matches:
            print(
                f"{match.player1.first_name} {match.player1.last_name} vs {match.player2.first_name} {match.player2.last_name} - Score: {match.score1}:{match.score2}")

    @staticmethod
    def display_rounds(rounds):
        """
        Displays a list of rounds.
        """
        if not rounds:
            print("No rounds available.")
        else:
            for round_ in rounds:
                print(f"{round_.name} (Start: {round_.start_time} - End: {round_.end_time})")
