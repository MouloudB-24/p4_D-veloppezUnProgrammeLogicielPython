import json
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from config import save_folder


def load_players():
    try:
        with open(save_folder / "players.json", 'r', encoding='utf-8') as file:
            players_data = json.load(file)
            return [Player.from_dict(player) for player in players_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from players.json")
        return []


def save_players(players):
    try:
        with open(save_folder / "players.json", 'w', encoding='utf-8') as file:
            json.dump([player.to_dict() for player in players], file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving players: {e}")


def load_tournaments():
    try:
        with open(save_folder / 'tournaments.json', 'r', encoding='utf-8') as file:
            tournaments_data = json.load(file)
            return [Tournament.from_dict(tournament) for tournament in tournaments_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from tournaments.json")
        return []


def save_tournaments(tournaments):
    try:
        with open(save_folder / 'tournaments.json', 'w', encoding='utf-8') as file:
            json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving tournaments: {e}")


def load_rounds():
    try:
        with open(save_folder / "rounds.json", 'r', encoding='utf-8') as file:
            rounds_data = json.load(file)
            return [Round.from_dict(round_) for round_ in rounds_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from rounds.json")
        return []


def save_rounds(rounds):
    try:
        with open(save_folder / "rounds.json", 'w', encoding='utf-8') as file:
            json.dump([round.to_dict() for round in rounds], file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving rounds: {e}")


def load_matches():
    try:
        with open(save_folder / "matchs.json", 'r', encoding='utf-8') as file:
            matches_data = json.load(file)
            return [Match.from_dict(match) for match in matches_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from matchs.json")
        return []


def save_matches(matches):
    try:
        with open(save_folder / "matchs.json", 'w', encoding='utf-8') as file:
            json.dump([match.to_dict() for match in matches], file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving matches: {e}")


if __name__ == "__main__":
    # Créer des joueurs
    player1 = Player("Syfax", "BEL", "2003-01-01", "M", "AB12345")
    player2 = Player("Victor", "BIZ", "2000-05-15", "F", "CD67890")
    match = Match(player1, player2)
    match.generate_random_result()

    round_ = Round("Round 1")
    round_.add_match(match)

    # Sauvegarder et charger les rounds
    save_rounds([round_])
    loaded_rounds = load_rounds()
    print(loaded_rounds)

    # Sauvegarder et charger les matchs
    save_matches([match])
    loaded_matches = load_matches()
    print(loaded_matches)