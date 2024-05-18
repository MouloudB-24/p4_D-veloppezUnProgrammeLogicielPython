from models.player import Player


class PlayerViews:
    @staticmethod
    def create_player():
        print("Incription d'un nouveau joueur")
        first_name = input("Entrez le prénom du joueur: ")
        last_name = input("Entrez le nom de famille du joueur: ")
        date_of_birth = input("Entrez la date de naissance du joueur (format YYYY-MM-DD): ")
        sex = input("Entrez le sexe du joueur: ")
        chess_id = input("Entrez l'identifiant du joueur: ")

        # Creating a player instance --> à deplacer dans la partie controller
        new_player = Player()
        new_player.set_first_name(first_name)
        new_player.set_last_name(last_name)
        new_player.set_date_of_birth(date_of_birth)
        new_player.set_sex(sex)
        new_player.set_chess_id(chess_id)

        # Player registration
        new_player.save_player()

        print(f"Le joueur {first_name} {last_name} a été inscrit avec succès!")


# Test
if __name__ == "__main__":
    PlayerViews.create_player()