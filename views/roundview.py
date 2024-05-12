from models.round import Round


class RoundViews:
    @staticmethod
    def create_round():
        print("Création d'un nouveau round")
        name = input("Entrez le nom du round: ")

        #  Creating a round instance
        new_round = Round()
        new_round.set_name(name)

        # Start round
        new_round.start_round()

        # End round
        new_round.finish_round()

        # Round registration
        new_round.save_round()

        print(f"Le round {name} a été créé avec succès!")


# Test
if __name__ == "__main__":
    RoundViews.create_round()
