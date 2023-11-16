import random
import secrets
from datetime import date

import tinydb
from tinydb import *

from src.modele.partie import Partie


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

    def __init__(self, id_tournoi, nom, lieu, date_debut, date_fin, nbre_ronde, description, liste_joueurs_tournoi,
                 liste_paires_joueurs):
        self.id_tournoi = id_tournoi
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nbre_ronde = nbre_ronde
        self.description = description
        self.liste_joueurs_tournoi = liste_joueurs_tournoi
        self.liste_paires_joueurs = liste_paires_joueurs

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

    @staticmethod
    def load_all():
        p_list = Tournoi.db.all()
        p_list = [Tournoi.from_dict(p) for p in p_list]
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
        return (f"Tournoi,avec id_tournoi : {self.id_tournoi} \n"
                f"avec nom: {self.nom} , \n"
                f"lieu : {self.lieu} , \n"
                f"date de début : {self.date_debut}, \n"
                f"date de fin : {self.date_fin} , \n"
                f"Avec nombre de tours : {self.nbre_ronde} \n")

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

            partie = Partie(secrets.token_hex(6), paire.joueur1, paire.joueur2, paire.couleur_joueur1, resultat)
            self.liste_parties.append(partie)
            self.save()
            print("Liste des resultat des parties : \n")
            for partie in self.liste_parties:
                print(partie.__repr__)

