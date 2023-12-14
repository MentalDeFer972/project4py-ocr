import random
from datetime import date

import tinydb
from tinydb import *

from src.modele.match import Match
from src.modele.tour import Tour


class Tournoi:
    db = tinydb.TinyDB("./data/tournoi.json", indent=4)
    db_joueur = tinydb.TinyDB("./data/player.json", indent=4)
    current_round_number = 0

    def __init__(self, id_tournoi, nom, lieu, date_debut, date_fin,
                 nbre_ronde, description,
                 liste_joueurs_tournoi, liste_tour):
        self.id_tournoi = id_tournoi
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nbre_ronde = nbre_ronde
        self.description = description
        self.liste_joueurs_tournoi = liste_joueurs_tournoi
        self.liste_tour = liste_tour

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

    @classmethod
    def find_tournoi_with_name(cls, nom):
        table = cls.db.table("_default")
        tournoi = Query()
        p_list = table.search(tournoi.nom == nom)
        p_list = [cls.from_dict(p) for p in p_list]
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
        self.finder_tour()

    def finder_tour(self):
        liste_tour = self.liste_tour
        for tour in liste_tour:
            liste_tour_final = Tour.find_tour("id_tour", tour)
            for liste in liste_tour_final:
                print(f"\n{liste.__repr__()} \n")
                for liste in liste.liste_match:
                    match = Match(liste['id_match'], liste['joueur1'],
                                  liste['joueur2'], liste['couleur_joueur1'],
                                  liste['couleur_joueur2'], liste['resultat'])
                    print(match.to_string())

    def get_current_match_list(self):
        """Trouver l'id de la current round
           Chercher dans la classe tour,le tour qu'on vient sélectionner
           Chercher dans le tour la liste des matchs
           Retourner la liste des matches
        """
        current_round_id = self.liste_tour[self.current_round_number]
        tour = Tour.find_tour("id_tour", current_round_id)
        liste_matchs = tour.liste_match
        return liste_matchs

    def update_current_round(self, list_matchs):
        current_round_id = self.liste_tour[self.current_round_number]
        tour = Tour.find_tour("id_tour", current_round_id)
        tour.liste_match = list_matchs
        tour.update()
