from src.controleurs.match_controleurs import MatchController


class TourController:

    def __init__(self):
        pass

    @staticmethod
    def ajouter_tour(tour):
        tour.save()

    """def choisir_tour(self):
        
    def supprimer_joueur(self):
        tour = self.choisir_tour()
        tour.delete()
        print("\nJoueur supprimé!\n")"""
