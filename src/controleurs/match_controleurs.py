class MatchController:

    def __init__(self):
        pass

    @staticmethod
    def ajouter_match(match):
        match.save()
