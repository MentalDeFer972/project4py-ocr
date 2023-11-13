import secrets

from tinydb import TinyDB, Query


class Partie:
    db = TinyDB("./data/parties.json")

    id_partie = ""
    resultat = 0

    def __init__(self, joueur1, joueur2, couleur_joueur, resultat):
        self.id_partie = secrets.token_hex(6)
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.couleur_joueur = couleur_joueur
        self.resultat = resultat

    def to_dict(self):
        return self.__dict__
        pass

    @classmethod
    def from_dict(cls, attrs):
        return Partie(**attrs)
        pass

    def save(self):
        self.db.insert(self.to_dict())
        pass

    def update(self):
        self.db.update(self.to_dict(), Query()["id_partie"] == self.id_partie)
        pass

    def delete(self):
        self.db.remove(Query().id_partie == self.id_partie)
        pass

    @classmethod
    def load_all(cls):
        p_list = cls.db.all()
        p_list = [cls.from_dict(p) for p in p_list]
        return p_list

    @classmethod
    def find_parties(cls, key, value):
        p_list = cls.db.search(Query()[key] == value)
        p_list = [cls.from_dict(p) for p in p_list]
        return p_list

    @classmethod
    def delete_all(cls):
        cls.db.truncate()
