from models.tournament import Tournament
from utils.data_manager import save_tournaments, load_tournaments


class TournamentController:
    def __init__(self):
        self.tournaments = load_tournaments()

    def create_tournament(self, name, location, start_date, end_date, rounds_count=4, description=""):
        tournament = Tournament(name, location, start_date, end_date, rounds_count, description)
        self.tournaments.append(tournament)
        save_tournaments(self.tournaments)

    def list_tournaments(self):
        return self.tournaments

    def find_tournament_by_name(self, name):
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament
        return None

    def add_player_to_tournament(self, tournament_name, player):
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            tournament.add_player(player)
            save_tournaments(self.tournaments)
            return True
        return False

    def add_round_to_tournament(self, tournament_name, round_):
        tournament = self.find_tournament_by_name(tournament_name)
        if tournament:
            tournament.add_round(round_)
            save_tournaments(self.tournaments)
            return True
        return False
