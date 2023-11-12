from src.controleurs.joueur_controleurs import *
from src.controleurs.tournoi_controleurs import TournoiController
from src.modele.tournoi import Tournoi


class Program:

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
                    {joueur.__repr__()}
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
        joueurc = JoueurController()
        print("""
                        Veuillez faire votre choix dans ce menu:
                            1-Ajouter un tournoi
                            2-Supprimer un tournoi
                    """)
        tournoi_menu = int(input())
        if tournoi_menu == 1:
            print("-----Ajout du tournoi-----\n")
            nom = input("Veuillez écrire le nom du tournoi \n")
            lieu = input("Veuillez écrire le lieu du tournoi \n")
            description = input("Veuillez saisir la description du tournoi \n")
            nbre_joueurs_tournoi = int(input("Veuillez choisir un nombre pair "
                                             "de joueurs qui participent dans le "
                                             "tournoi"))
            print("\n----Création liste de joueur du tournoi----\n")
            for i in range(nbre_joueurs_tournoi):
                joueur = joueurc.choisir_joueurs()
                t_controller.ajouter_joueur_tournoi(joueur)
            nbre_ronde = input("Veuillez saisir le nombre de ronde \n")
            tournoi = Tournoi(nom, lieu, nbre_ronde, description)
            tournoi.liste_joueurs_tournoi = t_controller.liste_joueurs_tournoi
            tournoic = TournoiController()
            tournoic.ajouter_tournoi(tournoi)
            print("Tournoi ajouté!\n")
            self.menu_principal()
        if tournoi_menu == 2:
            tournoic = TournoiController()
            tournoic.supprimer_tournoi()
            self.menu_principal()

    def menu_lancer_tournoi(self):
        pass

    def menu_lancer_rapports(self):
        pass


