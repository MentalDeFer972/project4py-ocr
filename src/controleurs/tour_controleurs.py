
class TourController:

    def __init__(self):
        pass

    @staticmethod
    def ajouter_tour(tour):
        tour.save()
