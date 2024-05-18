from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.view_players import PlayerView
from views.view_tournaments import TournamentView
from views.view_rounds import RoundView


class MainController:
    def __init__(self):
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.round_view = RoundView()

    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Manage Players")
            print("2. Manage Tournaments")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.manage_players()
            elif choice == '2':
                self.manage_tournaments()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_players(self):
        while True:
            print("\n--- Manage Players ---")
            print("1. Add Player")
            print("2. List Players")
            print("3. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_player()
            elif choice == '2':
                self.list_players()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_player(self):
        try:
            last_name, first_name, birth_date, sex, chess_id = self.player_view.get_player_details()
            self.player_controller.add_player(last_name, first_name, birth_date, sex, chess_id)
            print("Player added successfully.")
        except Exception as e:
            print(f"Error adding player: {e}")

    def list_players(self):
        players = self.player_controller.list_players()
        if players:
            self.player_view.display_players(players)
        else:
            print("No players available.")

    def manage_tournaments(self):
        while True:
            print("\n--- Manage Tournaments ---")
            print("1. Create Tournament")
            print("2. List Tournaments")
            print("3. Add Player to Tournament")
            print("4. Display Tournament Details")
            print("5. Generate Round")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_tournament()
            elif choice == '2':
                self.list_tournaments()
            elif choice == '3':
                self.add_player_to_tournament()
            elif choice == '4':
                self.display_tournament_details()
            elif choice == '5':
                self.generate_round_for_tournament()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def create_tournament(self):
        try:
            name, location, start_date, end_date, rounds_count, description = self.tournament_view.get_tournament_details()
            self.tournament_controller.create_tournament(name, location, start_date, end_date, rounds_count,
                                                         description)
            print("Tournament created successfully.")
        except Exception as e:
            print(f"Error creating tournament: {e}")

    def list_tournaments(self):
        tournaments = self.tournament_controller.list_tournaments()
        if tournaments:
            self.tournament_view.display_tournaments(tournaments)
        else:
            print("No tournaments available.")

    def add_player_to_tournament(self):
        try:
            tournament_name = self.tournament_view.get_tournament_name()
            chess_id = self.tournament_view.get_player_chess_id()
            player = self.player_controller.find_player_by_id(chess_id)
            if player:
                success = self.tournament_controller.add_player_to_tournament(tournament_name, player)
                if success:
                    print("Player added to tournament successfully.")
                else:
                    print("Tournament not found.")
            else:
                print("Player not found.")
        except Exception as e:
            print(f"Error adding player to tournament: {e}")

    def display_tournament_details(self):
        try:
            tournament_name = self.tournament_view.get_tournament_name()
            tournament = self.tournament_controller.find_tournament_by_name(tournament_name)
            if tournament:
                self.tournament_view.display_tournament(tournament)
                for round_ in tournament.rounds:
                    self.round_view.display_round(round_)
            else:
                print("Tournament not found.")
        except Exception as e:
            print(f"Error displaying tournament details: {e}")

    def generate_round_for_tournament(self):
        try:
            tournament_name = self.tournament_view.get_tournament_name()
            tournament = self.tournament_controller.find_tournament_by_name(tournament_name)
            if tournament:
                try:
                    round_ = tournament.generate_round()
                    self.round_view.display_round(round_)
                    print("Round generated successfully.")
                except Exception as e:
                    print(f"Error generating round: {e}")
            else:
                print("Tournament not found.")
        except Exception as e:
            print(f"Error generating round: {e}")


if __name__ == "__main__":
    controller = MainController()
    controller.main_menu()
