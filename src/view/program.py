import datetime
import secrets
from datetime import date

import tinydb

from src.controleurs.joueur_controleurs import *
from src.controleurs.tournoi_controleurs import TournoiController
from src.modele.tour import Tour
from src.modele.tournoi import Tournoi


class Program:

    @staticmethod
    def nbre_occurences_tournoi():
        db = tinydb.TinyDB("./data/tournoi.json")
        tab = db.all()
        resultat = len(tab)
        return resultat

    def menu_principal(self):
        print(""" Bienvenue !
                    Veuillez faire votre choix:
                    1-Gérer un joueur
                    2-Gérer un tournoi
                    3-Lancer un tournoi
                    4-Rapports
                """)
        choix = int(input())
        if choix == 1:
            self.menu_joueur()
        if choix == 2:
            self.menu_tournoi()
            pass
        if choix == 3:
            self.menu_lancer_tournoi()
            pass
        if choix == 4:
            self.menu_lancer_rapports()
            pass

    def menu_joueur(self):
        print("""
                Veuillez faire votre choix dans ce menu:
                    1-Ajouter un joueur
                    2-Modfier un joueur
                    3-Supprimer un joueur
            """)
        joueur_menu = int(input())
        if joueur_menu == 1:
            print("-----Ajout du joueur----- \n")
            nom = input("Veuillez écrire le nom du joueur\n")
            prenom = input("Veuillez écrire le prénom du joueur\n")
            date_naissance = input("Veuillez écrire la date de naissance du joueur\n")
            joueur = Joueur(nom, prenom, date_naissance)
            joueurc = JoueurController()
            joueurc.ajouter_joueur(joueur)
            print("Joueur ajouté!\n")
            self.menu_principal()
        if joueur_menu == 2:
            joueurc = JoueurController()
            joueur = joueurc.choisir_joueurs()
            print(f""" Que voulez-vous modifier sur le joueur suivant: 
                    {joueur.__repr__}
                    1-Nom
                    2-Prenom
                    3-Date de naissance
                    """)
            choix = int(input())
            joueurc.modifier_joueur(joueur, choix)
            self.menu_principal()
        if joueur_menu == 3:
            joueurc = JoueurController()
            joueurc.supprimer_joueur()
            self.menu_principal()

    def menu_tournoi(self):
        t_controller = TournoiController()
        print("""
                        Veuillez faire votre choix dans ce menu:
                            1-Ajouter un tournoi
                            2-Supprimer un tournoi
                            3-Reprendre un tournoi
                    """)
        tournoi_menu = int(input())
        if tournoi_menu == 1:
            print("-----Ajout du tournoi-----\n")
            nom = input("Veuillez écrire le nom du tournoi \n")
            lieu = input("Veuillez écrire le lieu du tournoi \n")
            description = input("Veuillez saisir la description du tournoi \n")
            nbre_joueurs_tournoi = int(input("Veuillez choisir un nombre pair "
                                             "de joueurs qui participent dans le "
                                             "tournoi \n"))
            print("\n----Création liste de joueur du tournoi----\n")
            occurences = self.nbre_occurences_tournoi()
            liste_joueurs_tournoi = t_controller.choice_joueurs_tournoi(occurences, nbre_joueurs_tournoi)

            print("-----Création des tours et matchs-----\n")
            nbre_ronde = int(input("Veuillez saisir le nombres de tours/rondes"))
            liste_ronde = []
            for nbre_ronde in range(nbre_ronde):
                liste_match = t_controller.generer_paires(liste_joueurs_tournoi)
                tour = Tour(secrets.token_hex(8),f"Round n°{nbre_ronde}", str(datetime.datetime.now()), "", "Non terminée", liste_match)
                tour.save()
                liste_ronde.append(tour.id_tour)
                print(f"Tour/Round n°{nbre_ronde} enregistré!\n")
            tournoi = Tournoi(secrets.token_hex(6), nom, lieu, str(date.today()), "Inconnu", nbre_ronde,
                              description, liste_joueurs_tournoi,
                              liste_ronde)
            t_controller.sauvegarder_tournoi(tournoi)

            print("Tournoi ajouté!\n")
            self.menu_principal()
        if tournoi_menu == 2:
            tournoic = TournoiController()
            tournoic.supprimer_tournoi()
            self.menu_principal()
        if tournoi_menu == 3:
            tournoic = TournoiController()
            tournoi = tournoic.choisir_tournoi()


    def menu_lancer_tournoi(self):
        tournoic = TournoiController()
        tournoi = tournoic.choisir_tournoi()
        tournoi.lancer_tournoi()
        pass

    def menu_lancer_rapports(self):
        pass
