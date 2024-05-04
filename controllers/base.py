import random


class Controller:
    def __init__(self, tournament):
        self.tournament = tournament
        self.registered_players = tournament.registered_players
        self.played_pairs = []

    def shuffle_players(self):
        """
        :return: Liste des joueurs mélangés aléatoirement.
        """
        return random.shuffle(self.registered_players)

    def sort_players(self):
        """
        :return: Liste des joueurs trier par leurs points.
        """
        return sorted(self.registered_players, key=lambda player: player["points"])

    def registered_players_list(self):
        """
        :return: Liste des joueurs inscrit par ordre alphabétique.
        """
        registered_players = []
        for player in self.registered_players:
            registered_players.append(f"{player['first_name']} {player['last_name']}")
        registered_players = sorted(registered_players)
        return registered_players

    def genarate_pairs(self):
        players_number = len(self.registered_players)
        pairs = []
        print(self.registered_players)

        while players_number < 1:
            player_1 = self.registered_players[0]
            player_2 = None
            for player in self.registered_players[1:]:
                if (player_1, player) not in self.played_pairs or (player, player_1) not in self.played_pairs:
                    player_2 = player

            if player_2:
                pairs.append((player_1, player_2))
            else:
                print(f"The player {player_1} player against all players")

            index_player_1 = self.tournament.registered_players.index(player_1)
            index_player_2 = self.tournament.registered_players.index(player_2)
            self.registered_players.pop(index_player_1)
            self.registered_players.pop(index_player_2)
            players_number = len(self.tournament.registered_players)

        return pairs
