from tinydb import TinyDB, Query


class Tour:
    db = TinyDB("./data/tour.json", indent=4)

    def __init__(self, id_tour,
                 nom_round,
                 dh_debut,
                 dh_fin,
                 statut,
                 liste_match):
        self.id_tour = id_tour
        self.nom_round = nom_round
        self.dh_debut = dh_debut
        self.dh_fin = dh_fin
        self.statut = statut
        self.liste_match = liste_match

    def to_dict(self):
        return {"id_tour": self.id_tour,
                "nom_round": self.nom_round,
                "dh_debut": self.dh_debut,
                "dh_fin": self.dh_fin,
                "statut": self.statut,
                "liste_match": [match.to_dict() for match in self.liste_match]}

    @classmethod
    def from_dict(cls, attrs):
        return Tour(**attrs)

    def save(self):
        self.db.insert(self.to_dict())

    def update(self):
        self.db.update(self.to_dict(), Query().id_tour == self.id_tour)

    def delete(self):
        self.db.remove(Query().id_tour == self.id_tour)

    def load_all(self):
        p_list = self.db.all()
        p_list = [self.from_dict(p) for p in p_list]
        return p_list

    @classmethod
    def find_tour(cls, key, value):
        p_list = cls.db.search(Query()[key] == value)
        p_list = [cls.from_dict(p) for p in p_list]
        return p_list

    @classmethod
    def delete_all(cls):
        cls.db.truncate()

    def __repr__(self) -> str:
        return (f"Tour,avec id :{self.id_tour} \n "
                f"avec nom du round : {self.nom_round} \n"
                f"date de début : {self.dh_debut} \n"
                f"date de fin : {self.dh_fin} \n"
                f"statut : {self.statut} \n")
