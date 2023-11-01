import datetime
import random


class Ronde:
    number_ronde = 0
    nom_ronde = f"Ronde n°{number_ronde}"
    dh_debut = datetime.datetime.now()
    dh_fin = ""
    joueur = []
    score = []
    match = (joueur, score)
    liste_match = []

    def __init__(self,number_ronde,joueur,score=0):
        self.number_ronde = number_ronde
        self.joueur.append(joueur)
        self.score.append(score)
        self.match = (joueur, score)
        self.liste_match.append(self.match)

    def exec_dh_fin(self):
        self.dh_fin = datetime.datetime.now()

    def exec_lancer_match(self):

        for match in self.liste_match:
            random.shuffle(self.liste_match)
            print(f"Ronde n°{self.number_ronde} \n")





