from src.modele.joueur import Joueur
from datetime import datetime


class JoueurController:

    @staticmethod
    def format_date_valide(date, format_date="%d/%m/%Y"):
        try:
            datetime.strptime(date, format_date)
            return True
        except ValueError:
            return False

    def __init__(self):
        pass

    @staticmethod
    def afficher_liste_tous_joueurs():
        list_ja = Joueur.load_all()
        list_joueurs = sorted(list_ja, key=lambda joueur: joueur.nom)
        for joueurs in list_joueurs:
            print(joueurs.__repr__())

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
                {p}
                """)
            i += 1
        choice = int(input("\nVeuillez choisir un numéro de joueur\n"))
        final_choice = choice - 1
        joueur = p_list[final_choice]
        return joueur

    @staticmethod
    def modifier_joueur(joueur, choix):
        if choix == 1:
            nom = input("\nVeuillez changer le nom du joueur.")
            joueur.nom = nom
            joueur.update()
            print(joueur.__repr__)
            print("\nModification effectuée.\n")
        if choix == 2:
            prenom = input("\nVeuillez changer le prénom du joueur.\n")
            joueur.prenom = prenom
            joueur.update()
            print(joueur.__repr__)
            print("\nModification effectuée.\n")
        if choix == 3:
            date_n = input("\nVeuillez changer "
                           "la date de naissance du joueur.\n")
            if JoueurController.format_date_valide(date_n):
                joueur.date_n = date_n
                joueur.update()
                print(joueur.__repr__)
                print("\nModification effectuée.\n")
            else:
                print("\nErreur:Date non valide.")
                JoueurController.modifier_joueur(joueur, choix)

    def supprimer_joueur(self):
        joueur = self.choisir_joueurs()
        joueur.delete()
        print("\nJoueur supprimé!\n")
