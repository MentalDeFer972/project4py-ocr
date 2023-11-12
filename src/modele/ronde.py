import datetime
import random


class Ronde:
    nbre_ronde = 4
    dh_debut = datetime.datetime.now()
    dh_fin = ""
    match = []
    liste_match = []
    liste_joueur_tournoi = []

    def __init__(self, nbre_ronde, liste_joueur_tournoi):
        self.nbre_ronde = nbre_ronde
        self.liste_joueur_tournoi = liste_joueur_tournoi

    def exec_dh_fin(self):
        self.dh_fin = datetime.datetime.now()
