import random

from src.modele.tournoi import Tournoi


class TournoiController:
    liste_joueurs_tournoi = []

    def __init__(self):
        pass

    def ajouter_joueur_tournoi(self,joueur):
        self.liste_joueurs_tournoi.append(joueur)

    @staticmethod
    def sauvegarder_tournoi(tournoi):
        tournoi.save()

    @staticmethod
    def choisir_tournoi():
        print("Veuillez choisir parmi les tournoi suivants : \n")
        p_list = Tournoi.load_all()
        i = 1
        for p in p_list:
            print(f"""
                Numéro {i} :
                {p.__repr__()}
                """)
            i += 1
        choice = int(input())
        final_choice = choice - 1
        tournoi = p_list[final_choice]
        print(tournoi.__repr__())
        return tournoi

    def supprimer_tournoi(self):
        tournoi = self.choisir_tournoi()
        tournoi.delete()
        print("\nTournoi supprimé!\n")





