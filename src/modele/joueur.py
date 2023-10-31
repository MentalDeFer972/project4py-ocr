import tinydb
import secrets


class Player:
    db = tinydb.TinyDB("./data/player.json")

    def __init__(self, nom: str, prenom: str, date_n: str, id_joueur: str = None) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_n = date_n
        self.id_joueur = id_joueur

    def to_dict(self):
        return self.__dict__
        pass

    @classmethod
    def from_dict(cls, attrs):
        return Player(**attrs)
        pass

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    @classmethod
    def load_all(self):
        pass

    @classmethod
    def find_player(self,key,value):
        pass

    @classmethod
    def delete_all(self):
        pass

    @classmethod
    def bootstrap(self):
        pass

    def __repr__(self) -> str:
        return (f"Joueur,avec nom: {self.nom} , prénom : {self.prenom} , date de naissance : {self.date_n} , et "
                f"id_joueur : {self.id_joueur}")


