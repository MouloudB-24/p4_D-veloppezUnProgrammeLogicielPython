import random


class Controller:
    def __init__(self, tournament):
        self.tournament = tournament

    def shuffle_players(self):
        """
        :return: Liste des joueurs mélangés aléatoirement.
        """
        random.shuffle(self.tournament.registered_players)
        return self.tournament.registered_players

    def sort_players(self):
        """
        :return: Liste des joueurs trier par leurs points.
        """
        return sorted(self.registered_players, key=lambda player: player["points"])

    def registered_players_list(self):
        """
        :return: Liste des joueurs inscrit par ordre alphabétique.
        """
        return sorted(self.tournament.registered_players)
