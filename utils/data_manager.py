import json
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match


def save_players(players, filepath='data/players.json'):
    """
    Saves a list of Player objects to a JSON file.

    :param players: List of Player objects
    :param filepath: Path to the JSON file
    """
    with open(filepath, 'w') as file:
        json.dump([player.to_dict() for player in players], file, indent=4)


def load_players(filepath='data/players.json'):
    """
    Loads a list of Player objects from a JSON file.

    :param filepath: Path to the JSON file
    :return: List of Player objects
    """
    try:
        with open(filepath, 'r') as file:
            players_data = json.load(file)
            return [Player.from_dict(player_data) for player_data in players_data]
    except FileNotFoundError:
        return []


def save_tournaments(tournaments, filepath='data/tournaments.json'):
    """
    Saves a list of Tournament objects to a JSON file.

    :param tournaments: List of Tournament objects
    :param filepath: Path to the JSON file
    """
    with open(filepath, 'w') as file:
        json.dump([tournament.to_dict() for tournament in tournaments], file, indent=4)


def load_tournaments(filepath='data/tournaments.json'):
    """
    Loads a list of Tournament objects from a JSON file.

    :param filepath: Path to the JSON file
    :return: List of Tournament objects
    """
    try:
        with open(filepath, 'r') as file:
            tournaments_data = json.load(file)
            return [Tournament.from_dict(tournament_data) for tournament_data in tournaments_data]
    except FileNotFoundError:
        return []


def save_round(round_, filepath):
    """
    Saves a Round object to a JSON file.

    :param round_: Round object
    :param filepath: Path to the JSON file
    """
    with open(filepath, 'w') as file:
        json.dump(round_.to_dict(), file, indent=4)


def load_round(filepath):
    """
    Loads a Round object from a JSON file.

    :param filepath: Path to the JSON file
    :return: Round object
    """
    with open(filepath, 'r') as file:
        data = json.load(file)
        return Round.from_dict(data)


def save_match(match, filepath):
    """
    Saves a Match object to a JSON file.

    :param match: Match object
    :param filepath: Path to the JSON file
    """
    with open(filepath, 'w') as file:
        json.dump(match.to_dict(), file, indent=4)


def load_match(filepath):
    """
    Loads a Match object from a JSON file.

    :param filepath: Path to the JSON file
    :return: Match object
    """
    with open(filepath, 'r') as file:
        data = json.load(file)
        return Match.from_dict(data)
