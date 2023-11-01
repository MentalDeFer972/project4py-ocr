import datetime
import secrets

import tinydb
from tinydb import *


class Tournoi:
    db = tinydb.TinyDB("./data/tournoi.json")

    id_tournoi = ""
    nom = ""
    lieu = ""
    date_debut = ""
    date_fin = ""
    nbre_tours = 4
    numero_tour_actuel = 0
    liste_ronde = []
    liste_joueurs_tournoi = []
    description = ""

    def __init__(self, nom, lieu, nbre_tours,
                 liste_ronde,
                 liste_joueurs_tournoi,
                 description):
        self.id_tournoi = secrets.token_hex(8)
        self.nom = nom
        self.lieu = lieu
        self.date_debut = datetime.date.today()
        self.nbre_tours = nbre_tours
        self.liste_ronde = liste_ronde
        self.liste_joueurs_tournoi = liste_joueurs_tournoi
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
        self.db.update(self.to_dict(), Query()["id_tournoi"] == self.id_joueur)
        pass

    def delete(self):
        self.db.remove(Query().id_joueur == self.id_joueur)
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
                f"Avec nombre de tours : {self.nbre_tours}")

    def description_tournoi(self):
        print(self.__repr__())
        print("Liste des tours: \n")
        for liste_t in self.liste_ronde:
            print(f"list")


