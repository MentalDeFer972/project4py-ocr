import datetime
import random
import secrets
from random import *

import tinydb
from tinydb import *

from src.modele.partie import Partie


class Tournoi:
    db = tinydb.TinyDB("./data/tournoi.json")

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

    def __init__(self, nom, lieu, nbre_ronde, description):
        self.id_tournoi = secrets.token_hex(8)
        self.nom = nom
        self.lieu = lieu
        self.date_debut = datetime.date.today()
        self.nbre_ronde = nbre_ronde
        self.description = description

    def ajouter_date_fin(self):
        self.date_fin = datetime.date.today()

    def to_dict(self):
        return self.__dict__
        pass

    @classmethod
    def from_dict(cls, attrs):
        return Tournoi(**attrs)
        pass

    def save(self):
        self.db.insert(self.to_dict())
        pass

    def update(self):
        self.db.update(self.to_dict(), Query()["id_tournoi"] == self.id_tournoi)
        pass

    def delete(self):
        self.db.remove(Query().id_tournoi == self.id_tournoi)
        pass

    @classmethod
    def load_all(cls):
        p_list = cls.db.all()
        p_list = [cls.from_dict(p) for p in p_list]
        return p_list

    @classmethod
    def find_players(cls, key, value):
        p_list = cls.db.search(Query()[key] == value)
        p_list = [cls.from_dict(p) for p in p_list]
        return p_list
        pass

    @classmethod
    def delete_all(cls):
        cls.db.truncate()
        pass

    def __repr__(self) -> str:
        return (f"Tournoi,avec nom: {self.nom} , lieu : {self.lieu} , date de début : {self.date_debut}, "
                f"id_tournoi : {self.id_tournoi} ,"
                f"date de fin : {self.date_fin} ,"
                f"Avec nombre de tours : {self.nbre_ronde}")

    def generer_paires(self):
        joueur_o = sorted(self.liste_joueurs_tournoi, key=lambda x: x.points, reverse=True)

        for i in range(0, len(joueur_o), 2):
            joueur1 = joueur_o[i]
            joueur2 = joueur_o[i + 1] if i + 1 < len(joueur_o) else None

            couleur_joueur1 = random.choice(['Blanc', 'Noir'])
            couleur_joueur2 = 'Noir' if couleur_joueur1 == 'Blanc' else 'Blanc'
            self.liste_paires_joueurs.append((joueur1, joueur2, couleur_joueur1, couleur_joueur2))


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



