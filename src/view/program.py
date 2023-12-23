import datetime
import secrets
from datetime import date

import tinydb

from src.controleurs.joueur_controleurs import JoueurController
from src.controleurs.tournoi_controleurs import TournoiController
from src.modele.tour import Tour
from src.modele.tournoi import Tournoi
from src.modele.joueur import Joueur


class Program:

    @staticmethod
    def nbre_occurences_tournoi():
        db = tinydb.TinyDB("./data/tournoi.json")
        tab = db.all()
        resultat = len(tab)
        return resultat

    def menu_principal(self):
        try:
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
            else:
                raise ValueError
        except ValueError:
            print("Vous avez saisi une mauvaise valeur.")
            self.menu_principal()

    def menu_joueur(self):
        try:
            print("""
                    Veuillez faire votre choix dans ce menu:
                        1-Ajouter un joueur
                        2-Modfier un joueur
                        3-Supprimer un joueur
                        4-Retour
                """)
            joueur_menu = int(input())
            if joueur_menu == 1:
                print("-----Ajout du joueur----- \n")
                nom = input("Veuillez écrire le nom du joueur\n")
                prenom = input("Veuillez écrire le prénom du joueur\n")
                date_naissance = input("Veuillez écrire "
                                       "la date de naissance du joueur\n")
                joueur = Joueur(nom, prenom, date_naissance)
                joueurc = JoueurController()
                joueurc.ajouter_joueur(joueur)
                print("Joueur ajouté!\n")
                self.menu_principal()
            if joueur_menu == 2:
                try:
                    joueurc = JoueurController()
                    joueur = joueurc.choisir_joueurs()
                    print("Que voulez-vous modifier",
                          "sur le joueur suivant:\n",
                          f"{joueur}\n",
                          "1-Nom \n",
                          "2-Prenom \n",
                          "3-Date de naissance\n")
                    choix = int(input())
                    if choix == 1 or choix == 2 or choix == 3:
                        joueurc.modifier_joueur(joueur, choix)
                        self.menu_principal()
                    else:
                        raise ValueError
                except ValueError:
                    print("Vous avez saisi une mauvaise valeur.")
                    self.menu_joueur()
            if joueur_menu == 3:
                joueurc = JoueurController()
                joueurc.supprimer_joueur()
                self.menu_principal()
            if joueur_menu == 4:
                self.menu_principal()
            else:
                raise ValueError
        except ValueError:
            print("Vous avez saisi la mauvaise valeur")
            self.menu_joueur()

    def menu_tournoi(self):
        try:
            t_controller = TournoiController()
            print("""
                            Veuillez faire votre choix dans ce menu:
                                1-Ajouter un tournoi
                                2-Supprimer un tournoi
                                3-Retour
                        """)
            tournoi_menu = int(input())
            if tournoi_menu == 1:
                try:
                    print("-----Ajout du tournoi-----\n")
                    nom = input("Veuillez écrire le nom du tournoi \n")
                    lieu = input("Veuillez écrire le lieu du tournoi \n")
                    description = input("Veuillez saisir "
                                        "la description du tournoi \n")
                    nbre_joueurs_tournoi = int(input("Veuillez choisir "
                                                     "un nombre pair "
                                                     "de joueurs "
                                                     "qui participent dans le "
                                                     "tournoi \n"))
                    if nbre_joueurs_tournoi % 2 != 0:
                        raise ValueError
                    print("\n----Création liste de joueur du tournoi----\n")
                    occurences = self.nbre_occurences_tournoi()
                    liste_joueurs_tournoi = (
                        t_controller
                        .choice_joueurs_tournoi
                        (occurences, nbre_joueurs_tournoi))
                    print("-----Création des tours et matchs-----\n")
                    nbre_ronde = \
                        (int(input("Veuillez saisir "
                                   "le nombres de tours/rondes")))
                    liste_ronde = []
                    i = 0
                    while i != nbre_ronde:
                        liste_match = (
                            t_controller.generer_paires(liste_joueurs_tournoi))
                        tour = Tour(secrets.token_hex(8), f"Round n°{i + 1}",
                                    str(datetime.datetime.now()),
                                    str(datetime.datetime.now()),
                                    "Terminée", liste_match)
                        tour.save()
                        liste_ronde.append(tour.id_tour)
                        print(f"Tour/Round n°{i} enregistré!\n")
                        i += 1
                    tournoi = Tournoi(secrets.token_hex(6), nom, lieu,
                                      str(date.today()),
                                      "Inconnu",
                                      nbre_ronde,
                                      description, liste_joueurs_tournoi,
                                      liste_ronde)
                    t_controller.sauvegarder_tournoi(tournoi)

                    print("Tournoi ajouté!\n")
                    self.menu_principal()
                except ValueError:
                    print("Vous avez saisi la mauvaise valeur ou "
                          "le nombre choisi n'est pas pair")
                    self.menu_tournoi()
            if tournoi_menu == 2:
                tournoic = TournoiController()
                tournoic.supprimer_tournoi()
                self.menu_principal()
            if tournoi_menu == 3:
                self.menu_principal()
            else:
                raise ValueError
        except ValueError:
            print("Vous avez saisi la mauvaise valeur.")
            self.menu_tournoi()

    def menu_lancer_tournoi(self):
        tournoic = TournoiController()
        tournoi = tournoic.choisir_tournoi()
        tournoi.lancer_tournoi()
        self.menu_principal()

    def menu_lancer_rapports(self):
        try:
            print("\n-----Sélection des rapports-----\n")
            print("Veuillez choisir un rapport \n")
            choix = int(input("1-Liste de tous "
                              "les joueurs par ordre alphabétique \n"
                              "2-Liste de tous "
                              "les tournois \n"
                              "3-Nom et dates "
                              "d’un tournoi donné \n"
                              "4-Liste des "
                              "joueurs du tournoi par ordre alphabétique \n"
                              "5-Liste de "
                              "tous les tours du tournoi et "
                              "de tous les matchs du tour \n"
                              "6-Retour \n"))
            if choix == 1:
                joueur_c = JoueurController()
                print("-----Liste de "
                      "tous les joueurs par ordre alphabétique----- \n")
                joueur_c.afficher_liste_tous_joueurs()
                self.menu_lancer_rapports()
                pass
            elif choix == 2:
                tournoi_c = TournoiController()
                print("-----Liste de tous les tournois----- \n")
                tournoi_c.afficher_liste_tournoi()
                self.menu_lancer_rapports()
                pass
            elif choix == 3:
                tournoi_c = TournoiController()
                print("-----Liste de nom et dates d’un tournoi donné----- \n")
                print("Veuillez choisir le nom du tournoi")
                nom = input()
                tournoi_c.rechercher_nom_date_tournoi(nom)
                self.menu_lancer_rapports()
            elif choix == 4:
                tournoi = TournoiController.choisir_tournoi()
                print("-----Liste des joueurs "
                      "du tournoi par ordre alphabétique-----\n")
                TournoiController.afficher_liste_joueurs_tournoi(tournoi)
                self.menu_lancer_rapports()
                pass
            elif choix == 5:
                tournoi = TournoiController.choisir_tournoi()
                tournoi.finder_tour()
                self.menu_lancer_rapports()
                pass
            elif choix == 6:
                self.menu_principal()
            else:
                raise ValueError
        except ValueError:
            print("Vous avez saisi la mauvaise valeur.")
            self.menu_lancer_rapports()
