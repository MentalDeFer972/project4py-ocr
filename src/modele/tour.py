from tinydb import TinyDB, Query


class Tour:

    db = TinyDB("./data/tour.json")

    def __init__(self,nom_round,dh_debut,dh_fin,statut,liste_match):
        self.nom_round = nom_round
        self.dh_debut = dh_debut
        self.dh_fin = dh_fin
        self.statut = statut
        self.liste_match = liste_match

    def to_dict(self):
        return self.__dict__
        pass

    @classmethod
    def from_dict(cls, attrs):
        return Tour(**attrs)
        pass

    def save(self):
        self.db.insert(self.to_dict())
        pass

    def update(self):
        self.db.update(self.to_dict(), Query().id_match == self.id_match)
        pass

    def delete(self):
        self.db.remove(Query().id_match == self.id_match)
        pass

    def load_all(self):
        p_list = self.db.all()
        p_list = [self.from_dict(p) for p in p_list]
        return p_list

    @classmethod
    def find_parties(cls, key, value):
        p_list = cls.db.search(Query()[key] == value)
        p_list = [cls.from_dict(p) for p in p_list]
        return p_list

    @classmethod
    def delete_all(cls):
        cls.db.truncate()


