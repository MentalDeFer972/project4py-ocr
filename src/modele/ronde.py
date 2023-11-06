import datetime
import random


class Ronde:
    nbre_ronde = 4
    dh_debut = datetime.datetime.now()
    dh_fin = ""
    joueur = []
    score = [0, 0]
    match = []
    liste_match = []
    liste_joueur_tournoi = []

    def __init__(self, nbre_ronde, liste_joueur_tournoi):
        self.nbre_ronde = nbre_ronde
        self.liste_joueur_tournoi = liste_joueur_tournoi

    def exec_dh_fin(self):
        self.dh_fin = datetime.datetime.now()

    def exec_lancer_match(self):
        for i in range(self.nbre_ronde):
            for joueur_t in self.liste_joueur_tournoi:
                random.shuffle(self.liste_joueur_tournoi)
                print(f"Ronde n°{self.nbre_ronde} \n")
                self.joueur.append(joueur_t)
                if len(self.joueur) == 2:
                    self.match = [[self.joueur[0], self.score[0]],
                                  [self.joueur[1], self.score[1]]]
                    self.liste_match.append(self.match)
                self.match.clear()
