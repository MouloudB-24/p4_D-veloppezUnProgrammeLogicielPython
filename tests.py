# main.py

from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from utils.data_manager import save_players, load_players, save_tournaments, load_tournaments, save_round, load_round

# Create players
players = [
    Player("Doe", "John", "1990-01-01", "M", "AB12345"),
    Player("Smith", "Jane", "1985-05-15", "F", "CD67890"),
    Player("Brown", "Charlie", "1992-02-20", "M", "EF12345"),
    Player("Johnson", "Emily", "1988-03-30", "F", "GH67890")
]

# Save players to JSON file
save_players(players)

# Load players from JSON file
loaded_players = load_players()

# Print loaded players
print("Loaded Players:")
for player in loaded_players:
    print(player)

# Create a tournament
tournament = Tournament("Summer Open", "New York", "2023-07-01", "2023-07-05")

# Add players to the tournament
for player in loaded_players:
    tournament.add_player(player)

# Create the first round and add matches
round1 = Round("Round 1")
pairs_round1 = tournament.generate_pairs()
for player1, player2 in pairs_round1:
    match = Match(player1, player2)
    round1.add_match(match)

# Generate random results for the first round
round1.generate_results()

# Add the first round to the tournament
tournament.add_round(round1)

# Save the first round to JSON file
save_round(round1, 'data/round1.json')

# Create the second round and add matches
round2 = Round("Round 2")
pairs_round2 = tournament.generate_pairs()
for player1, player2 in pairs_round2:
    match = Match(player1, player2)
    round2.add_match(match)

# Generate random results for the second round
round2.generate_results()

# Add the second round to the tournament
tournament.add_round(round2)

# Save the second round to JSON file
save_round(round2, 'data/round2.json')

# Save tournaments to JSON file
save_tournaments([tournament], 'data/tournaments.json')

# Load tournaments from JSON file
loaded_tournaments = load_tournaments('data/tournaments.json')

# Print loaded tournaments and their matches
print("\nLoaded Tournaments:")
for t in loaded_tournaments:
    print(t)
    for r in t.rounds:
        print(r)
        for m in r.matches:
            print(m)