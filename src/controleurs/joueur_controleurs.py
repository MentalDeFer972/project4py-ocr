from src.modele.joueur import Joueur


class JoueurController:

    def __init__(self):
        pass

    @staticmethod
    def ajouter_joueur(joueur):
        joueur.save()

    @staticmethod
    def choisir_joueurs():
        print("Veuillez choisir parmi les joueurs suivants : \n")
        p_list = Joueur.load_all()
        i = 1
        for p in p_list:
            print(f"""
                Numéro {i} :
                {p.__repr__()}
                """)
            i += 1
        choice = int(input("\nVeuillez chosir un numéro de joueur\n"))
        final_choice = choice - 1
        joueur = p_list[final_choice]
        print(joueur.__repr__())
        return joueur

    @staticmethod
    def modifier_joueur(joueur, choix):
        if choix == 1:
            nom = input("\nVeuillez changer le nom du joueur.")
            joueur.nom = nom
            joueur.update()
            print(joueur.__repr__())
            print("\nModification effectuée.\n")
        if choix == 2:
            prenom = input("\nVeuillez changer le prénom du joueur.\n")
            joueur.prenom = prenom
            joueur.update()
            print(joueur.__repr__())
            print("\nModification effectuée.\n")
        if choix == 3:
            date_n = input("\nVeuillez changer la date de naissance du joueur.\n")
            joueur.date_n = date_n
            joueur.update()
            print(joueur.__repr__())
            print("\nModification effectuée.\n")

    def supprimer_joueur(self):
        joueur = self.choisir_joueurs()
        joueur.delete()
        print("\nJoueur supprimé!\n")
