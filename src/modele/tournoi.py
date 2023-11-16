from datetime import date
import random
import secrets

import tinydb
from tinydb import *

from src.modele.joueur import Joueur
from src.modele.partie import Partie


class Paire:

    db_paire = tinydb.TinyDB("./data/paire.json", indent=4)
    joueur1 = Joueur
    joueur2 = Joueur
    couleur_joueur1 = ""
    couleur_joueur2 = ""

    def __init__(self, joueur1, joueur2, couleur_joueur1, couleur_joueur2):
        self.id_paire = secrets.token_hex(6)
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.couleur_joueur1 = couleur_joueur1
        self.couleur_joueur2 = couleur_joueur2

    def to_dict(self):
        return self.__dict__
        pass

    @staticmethod
    def from_dict(attrs):
        return Paire(**attrs)

    def save(self):
        self.db_paire.insert(self.to_dict())

    def update(self):
        self.db_paire.update(self.to_dict(), Query()["id_paire"] == self.id_paire)
        pass

    def delete(self):
        self.db.remove(Query().id_paire == self.id_paire)
        pass


    def load_all(self):
        p_list = self.db_paire.all()
        p_list = [self.from_dict(p) for p in p_list]
        return p_list

    def find_players(self, key, value):
        p_list = self.db_paire.search(Query()[key] == value)
        p_list = [self.from_dict(p) for p in p_list]
        return p_list
        pass

    def delete_all(self):
        self.db_paire.truncate()
        pass




class Tournoi:
    db = tinydb.TinyDB("./data/tournoi.json", indent=4)
    db_joueur = tinydb.TinyDB("./data/player.json", indent=4)

    id_tournoi = ""
    nom = ""
    lieu = ""
    date_debut = ""
    date_fin = ""
    nbre_ronde = 4
    liste_parties = []
    liste_joueurs_tournoi = []
    liste_paires_joueurs = []
    description = ""

    def __init__(self, nom, lieu, nbre_ronde, description, occurences, nbre_joueurs):
        self.id_tournoi = secrets.token_hex(8)
        self.nom = nom
        self.lieu = lieu
        self.date_debut = str(date.today())
        self.nbre_ronde = nbre_ronde
        self.description = description
        self.liste_joueurs_tournoi = self.choice_joueurs_tournoi(occurences, nbre_joueurs)
        self.liste_paires_joueurs = self.generer_paires()

    def choice_joueurs_tournoi(self, num_tournoi, nbre_joueurs):
        liste_joueurs_tournoi = []
        db_joueur = self.db_joueur
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

    def ajouter_date_fin(self):
        self.date_fin = date.today()

    def to_dict(self):
        return self.__dict__
        pass

    @staticmethod
    def from_dict(attrs):
        return Tournoi(**attrs)

    def save(self):
        self.db.insert(self.to_dict())

    def update(self):
        self.db.update(self.to_dict(), Query()["id_tournoi"] == self.id_tournoi)
        pass

    def delete(self):
        self.db.remove(Query().id_tournoi == self.id_tournoi)
        pass


    def load_all(self):
        p_list = self.db.all()
        p_list = [self.from_dict(p) for p in p_list]
        return p_list

    def find_players(self, key, value):
        p_list = self.db_joueur.search(Query()[key] == value)
        p_list = [self.from_dict(p) for p in p_list]
        return p_list
        pass

    def delete_all(self):
        self.db.truncate()
        pass

    def __repr__(self) -> str:
        return (f"Tournoi,avec nom: {self.nom} , lieu : {self.lieu} , date de début : {self.date_debut}, "
                f"id_tournoi : {self.id_tournoi} ,"
                f"date de fin : {self.date_fin} ,"
                f"Avec nombre de tours : {self.nbre_ronde}")

    def lancer_tournoi(self):
        for paire in self.liste_paires_joueurs:
            resultat = random.randint(1, 3)
            if resultat == 1:
                paire.joueur1.points += 1
            elif resultat == 2:
                paire.joueur2.points += 1
            elif resultat == 3:
                paire.joueur1.points += 0.5
                paire.joueur2.points += 0.5

            partie = Partie(paire.joueur1, paire.joueur2, paire.couleur_joueur1, resultat)
            self.liste_parties.append(partie)
            self.save()
            print("Liste des resultat des parties : \n")
            for partie in self.liste_parties:
                print(partie.__repr__())

    def generer_paires(self):
        liste_paires_joueurs = []
        print("Génération des paires \n")
        for i in range(0, len(self.liste_joueurs_tournoi), 2):
            print(i)
            joueur1 = self.liste_joueurs_tournoi[i]
            joueur2 = self.liste_joueurs_tournoi[i + 1] if i + 1 < len(self.liste_joueurs_tournoi) else None

            couleur_joueur1 = random.choices(['Blanc', 'Noir'])
            couleur_joueur2 = 'Noir' if couleur_joueur1 == 'Blanc' else 'Blanc'

            liste_paires_joueurs.append(Paire(joueur1, joueur2, couleur_joueur1, couleur_joueur2))

        return liste_paires_joueurs
