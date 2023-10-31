from src.modele.joueur import Joueur


class JoueurController:

    @staticmethod
    def ajouter_joueur():
        print("-----Ajout du joueur----- \n")
        nom = input("Veuillez écrire le nom du joueur")
        prenom = input("Veuillez écrire le prénom du joueur")
        date_naissance = input("Veuillez écrire la date de naissance du joueur")
        joueur = Joueur(nom, prenom, date_naissance)
        joueur.save()
        print("Joueur ajouté!")
        return joueur

    @staticmethod
    def choisir_joueurs():
        print("Veuillez choisir parmi les joueurs suivants : \n")
        Joueur.boot()
        p_list = Joueur.load_all()

        i = 1
        for p in p_list:
            print(f"""
                Numéro {i} :
                {p.__repr__()}
                """)
            i += 1
        choice = int(input("Veuillez chosir un numéro de joueur"))
        final_choice = choice - 1
        joueur = p_list[final_choice]
        print(joueur.__repr__())
        return joueur

    @staticmethod
    def modifier_joueur():
        joueur = JoueurController.choisir_joueurs()
        print(f""" Que voulez-vous modifier sur le joueur suivant: 
        {joueur.__repr__()}
        1-Nom
        2-Prenom
        3-Date de naissance
        """)

        choix = int(input())

        if choix == 1:
            nom = input("Veuillez changer le nom du joueur.")
            joueur.nom = nom
            joueur.update()
            print(joueur.__repr__())
        elif choix == 2:
            prenom = input("Veuillez changer le prénom du joueur.")
            joueur.prenom = prenom
            joueur.update()
            print(joueur.__repr__())
        elif choix == 3:
            date_n = input("Veuillez changer la date de naissance du joueur.")
            joueur.date_n = date_n
            joueur.update()
            print(joueur.__repr__())
        else:
            JoueurController.modifier_joueur()

    @staticmethod
    def supprimer_joueur():
        joueur = JoueurController.choisir_joueurs()
        joueur.delete()
        print("Joueur supprimé!")
