from models.tournament import Tournament


class TournamentViews:
    @staticmethod
    def create_tournament():
        print("Création d'un nouveau tournoi")
        name = input("Entrez le nom du tournoi: ")
        location = input("Entrez le lieu du tournoi: ")
        start_date = input("Entrez la date de début du tournoi (format YYYY-MM-DD): ")
        end_date = input("Entrez la date de fin du tournoi (format YYYY-MM-DD): ")
        description = input("Entrez la description du tournoi: ")
        number_rounds = int(input("Entrez le nombre de rounds du tournoi: "))

        # Creating a tournament instance
        new_tournament = Tournament()
        new_tournament.set_name(name)
        new_tournament.set_location(location)
        new_tournament.set_date(start_date, end_date)
        new_tournament.set_description(description)
        new_tournament.set_number_rounds(number_rounds)

        # Tournament registration
        new_tournament.save_tournament()

        print(f"Le tournoi {name} a été créé avec succès!")


# Test
if __name__ == "__main__":
    TournamentViews.create_tournament()
