import tinydb
import secrets

from tinydb import *


class Joueur:

    db = tinydb.TinyDB('./data/player.json')

    def __init__(self, nom: str, prenom: str, date_n: str, id_joueur: str = None, points=0, couleur="None"):
        self.nom = nom
        self.prenom = prenom
        self.date_n = date_n
        self.id_joueur = secrets.token_hex(8) if not id_joueur else id_joueur
        self.couleur = couleur
        self.points = points

    def to_dict(self):
        return self.__dict__
        pass

    @classmethod
    def from_dict(cls, attrs):
        return Joueur(**attrs)
        pass

    def save(self):
        self.db.insert(self.to_dict())
        pass

    def update(self):
        self.db.update(self.to_dict(), Query()["id_joueur"] == self.id_joueur)
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
        return (f"Joueur,avec nom: {self.nom} , prénom : {self.prenom} , date de naissance : {self.date_n} , et "
                f"id_joueur : {self.id_joueur}")


