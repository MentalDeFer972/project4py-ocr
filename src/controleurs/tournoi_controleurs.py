import random
import secrets

import tinydb
from tinydb import Query, TinyDB

from src.modele.joueur import Joueur
from src.modele.match import Match
from src.modele.tournoi import Tournoi


class TournoiController:
    liste_joueurs_tournoi = []

    db_tournoi = tinydb.TinyDB("./data/tournoi.json", indent=4)

    def __init__(self):
        pass

    def afficher_liste_tournoi(self):
        list = Tournoi.load_all()
        for tournoi in list:
            print(tournoi.__repr__())

    def afficher_liste_joueurs_tournoi(self):
        list = Tournoi.load_all()
        for tournoi in list:
            liste_joueurs_tournoi = sorted(tournoi.liste_joueurs_tournoi, key=lambda x: x['nom'])
            for joueur in liste_joueurs_tournoi:
                print(joueur.__repr__())

    def ajouter_joueur_tournoi(self, joueur):
        self.liste_joueurs_tournoi.append(joueur.id_joueur)

    @staticmethod
    def sauvegarder_tournoi(tournoi):
        tournoi.save()

    def supprimer_tournoi(self):
        tournoi = self.choisir_tournoi()
        tournoi.delete()
        print("\nTournoi supprimé!\n")

    @staticmethod
    def choice_joueurs_tournoi(num_tournoi, nbre_joueurs):
        liste_joueurs_tournoi = []
        db_joueur = Joueur.db
        for nbre in range(nbre_joueurs):
            print(f"Veuillez choisir un joueur dans le tournoi n°{num_tournoi + 1} \n")
            p_list = db_joueur.all()
            i = 0
            print("Veuillez choisir un joueur \n")
            for p in p_list:
                joueur = Joueur(**p)
                print(f"Joueur n°{i + 1}  : \n {joueur.__repr__()}")
                i += 1
            choix = int(input())
            joueur_choix = p_list[choix - 1]
            print(f"Joueur choisi n°{choix} : \n {joueur_choix.__repr__()}")
            liste_joueurs_tournoi.append(joueur_choix)
        return liste_joueurs_tournoi

    @staticmethod
    def generer_paires(liste_joueurs_tournoi):

        random.shuffle(liste_joueurs_tournoi)
        liste_match = []

        print("Génération des paires \n")
        for i in range(0, len(liste_joueurs_tournoi), 2):
            print(i)
            joueur1 = liste_joueurs_tournoi[i]
            joueur2 = liste_joueurs_tournoi[i + 1] if i + 1 < len(liste_joueurs_tournoi) else None

            couleur_joueur1 = random.choices(['Blanc', 'Noir'])
            couleur_joueur2 = 'Noir' if couleur_joueur1 == 'Blanc' else 'Blanc'

            resultat = 0

            match = Match(secrets.token_hex(8), joueur1, joueur2, couleur_joueur1, couleur_joueur2, resultat)
            match.save()
            liste_match.append(match)

        return liste_match

    @staticmethod
    def choisir_tournoi():
        print("Veuillez choisir parmi les tournoi suivants : \n")
        p_list = Tournoi.load_all()
        i = 1
        for p in p_list:
            print(f"Numéro {i}: \n {p.__repr__()}")
            i += 1
        choice = int(input())
        final_choice = choice - 1
        tournoi = p_list[final_choice]
        print(tournoi.__repr__())
        return tournoi

    def rechercher_nom_date_tournoi(self, nom):
        resultats = Tournoi.find_tournoi_with_name(nom)
        if resultats:
            for tournoi in resultats:
                print(f"Tournoi : \n {tournoi.__repr__()}")
        else:
            print("Aucun resultat trouvé")

    def tous_tour_tous_match_tour(self,tournoi):
        pass


