from src.controleurs.joueur_controleurs import JoueurController


class View:

    def __init__(self):
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



    @staticmethod
    def menu_joueur():
        print("""
            Veuillez faire votre choix dans ce menu:
                1-Ajouter un joueur
                2-Modfier un joueur
                3-Supprimer un joueur
        """)
        joueur_menu = int(input())
        if joueur_menu == 1:
            JoueurController.ajouter_joueur()
        if joueur_menu == 2:
            JoueurController.modifier_joueur()
        if joueur_menu == 3:
            JoueurController.supprimer_joueur()
