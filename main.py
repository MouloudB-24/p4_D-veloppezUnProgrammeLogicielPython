from pprint import pprint

from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match

# Inscription des joueurs au club
player1 = Player("Mouloud", "ZOO", "04/08/1992", "JD12345", "M")
player2 = Player("Johnson", "Bob", "02/02/1960", "JD67890", "M")
player3 = Player("Victor", "BIZIEN", "16/05/1993", "MB87641", "M")
player4 = Player("Aylan", "BELLIL", "30/07/2023", "AB77800", "M")

# Organisation d'un Tournoi à Ermont
tournament = Tournament("Tournoi Ermont", "Centre ville", "27/04/2024", "30/04/2024", "Merci aux organisateurs")

# Enregistrement des joueurs au Tournoi d'Ermont
tournament.register_player(player1)
tournament.register_player(player2)
tournament.register_player(player3)
tournament.register_player(player4)

# Afficher les joueurs enregistrés dans le tournoi
"""print("Liste des joueurs inscrits au tournoi:")
for player in tournament.registered_players:
    print(player)"""

# Lancer le 1er round
round = Round("Round 1")
match1 = Match(player1, player3)
match2 = Match(player2, player4)
match1.award_match_points()
match2.award_match_points()
round.add_match(match1)
round.add_match(match2)

#print(f"\n{round}")
tournament.add_round(round)

# Enregistrer les points des joueurs ...

# Lancer le 2eme round
tournament.start_next_round()
round = Round("Round 2")
match1 = Match(player1, player4)
match2 = Match(player2, player3)
match1.award_match_points()
match2.award_match_points()
round.add_match(match1)
round.add_match(match2)
print()
tournament.add_round(round)
pprint(tournament.get_tournament_info())



print(player1.points)
print(player2.points)
print(player3.points)
print(player4.points)

