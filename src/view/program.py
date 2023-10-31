from src.controleurs.joueur_controleurs import *


class Program:

    def __init__(self):
        pass

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
            pass
        if choix == 3:
            pass
        if choix == 4:
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
