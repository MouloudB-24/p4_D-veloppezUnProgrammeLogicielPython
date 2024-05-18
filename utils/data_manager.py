import json
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match


def load_players():
    try:
        with open('data/players.json', 'r', encoding='utf-8') as file:
            players_data = json.load(file)
            return [Player.from_dict(player) for player in players_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from players.json")
        return []


def save_players(players):
    try:
        with open('data/players.json', 'w', encoding='utf-8') as file:
            json.dump([player.to_dict() for player in players], file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving players: {e}")


def load_tournaments():
    try:
        with open('data/tournaments.json', 'r', encoding='utf-8') as file:
            tournaments_data = json.load(file)
            return [Tournament.from_dict(tournament) for tournament in tournaments_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from tournaments.json")
        return []


def save_tournaments(tournaments):
    try:
        with open('data/tournaments.json', 'w', encoding='utf-8') as file:
            json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving tournaments: {e}")


def save_round(round_, filepath):
    """
    Saves a Round object to a JSON file.

    :param round_: Round object
    :param filepath: Path to the JSON file
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(round_.to_dict(), file, indent=4)


def load_round(filepath):
    """
    Loads a Round object from a JSON file.

    :param filepath: Path to the JSON file
    :return: Round object
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return Round.from_dict(data)


def save_match(match, filepath):
    """
    Saves a Match object to a JSON file.

    :param match: Match object
    :param filepath: Path to the JSON file
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(match.to_dict(), file, indent=4)


def load_match(filepath):
    """
    Loads a Match object from a JSON file.

    :param filepath: Path to the JSON file
    :return: Match object
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return Match.from_dict(data)
