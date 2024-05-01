from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match

# Inscription des joueurs au club
player1 = Player()
player1.set_name("Aylan", "BELLIL")
player1.set_chess_id("RE26528")
player1.save_player()
player2 = Player()
player2.set_name("Victor", "BIZIEN")
player2.set_chess_id("IU87651")
player2.save_player()
player3 = Player()
player3.set_name("Jean", "ZOO")
player3.set_chess_id("NH98760")
player3.save_player()
player4 = Player()
player4.set_name("Nicolas", "CARAMEL")
player4.set_chess_id("BG87650")
player4.save_player()

# Mettre à jour le joueur1
player1.update_player(date_of_birth="30/07/2023")

# Organisation d'un Tournoi à Paris
tournament1 = Tournament()
tournament1.set_name("Tournoi de Paris")
tournament1.save_tournament()

#tournament.update_tournament(location="JO Paris")


# Enregistrement des joueurs au Tournoi de Paris
tournament1.register_player(player1.get_player())
tournament1.register_player(player2.get_player())
tournament1.register_player(player3.get_player())
tournament1.register_player(player4.get_player())
tournament1.update_tournament()

# Lancer le 1er round
round1 = Round()
round1.set_name("Round 1")
round1.start_round()
match1 = Match()
match1.set_players(player1, player4)
match1.award_points()
match2 = Match()
match2.set_players(player3, player2)
match2.award_points()
round1.add_match(match1.get_score())
round1.add_match(match2.get_score())
tournament1.add_round(round1.get_round())
round1.finish_round()
tournament1.update_tournament()


# Lancer le 2eme round
tournament1.start_next_round()
round2 = Round()
round2.start_round()
round2.set_name("Round 2")
match1 = Match()
match1.set_players(player1, player3)
match1.award_points()
match2 = Match()
match2.set_players(player4, player2)
match2.award_points()
round2.add_match(match1.get_score())
round2.add_match(match2.get_score())
tournament1.add_round(round2.get_round())
round2.finish_round()
tournament1.update_tournament()



