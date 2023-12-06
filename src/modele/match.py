from tinydb import TinyDB, Query

from src.modele.joueur import Joueur


class Match:
    db = TinyDB("./data/match.json")

    def __init__(self, id_match, joueur1, joueur2, couleur_joueur1, couleur_joueur2, resultat):
        self.id_match = id_match
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.couleur_joueur1 = couleur_joueur1
        self.couleur_joueur2 = couleur_joueur2
        self.resultat = resultat

    def to_dict(self):
        return self.__dict__
        pass

    @classmethod
    def from_dict(cls, attrs):
        return Match(**attrs)
        pass

    def save(self):
        self.db.insert(self.to_dict())
        pass

    @classmethod
    def find_match(cls, key):
        p_list = cls.db.search(Query()[key])
        p_list = [cls.from_dict(p) for p in p_list]
        return p_list

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

    @staticmethod
    def resultat_repr(resultat):
        if resultat == 1:
            return "Joueur 1 gagnant"
        if resultat == 2:
            return "Joueur 2 gagnant"
        if resultat == 3:
            return "Match nul"

    def to_string(self):
        print(f"\n ID du match : {self.id_match} \n ",
              f"\n Nom du joueur 1 : {self.joueur1['nom']} \n",
              f" Prénom du joueur 1: {self.joueur1['prenom']} \n",
              f" Date de naissance du joueur 1 : {self.joueur1['date_n']} \n",
              f" ID du joueur 1 : {self.joueur2['id_joueur']} \n",
              f"\n Nom du joueur 2 : {self.joueur2['nom']} \n"
              f" Prénom du joueur 2 : {self.joueur2['prenom']} \n",
              f" Date de naissance du joueur 2 : {self.joueur2['date_n']} \n",
              f" ID du joueur 2 : {self.joueur2['id_joueur']} \n",
              f"\n Couleur du joueur n°1 choisi : {self.couleur_joueur1} \n"
              f" Couleur du joueur n°2 choisi : {self.couleur_joueur2} \n"
              f"\n Resultat du match : \n",
              f"{self.resultat_repr(self.resultat)} \n")
