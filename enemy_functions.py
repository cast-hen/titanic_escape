from pauze import *
import random

def WillekeurigeAanvalKiezen(AanvallenLijst):
    OptiesAanvallen = []
    randomAanval = AanvallenLijst[random.randint(0, len(AanvallenLijst) - 1)]
    OptiesAanvallen.append(randomAanval)
    for i in range(0, 2):

        while randomAanval in OptiesAanvallen:
            randomAanval = AanvallenLijst[random.randint(0, len(AanvallenLijst) - 1)]

        OptiesAanvallen.append(randomAanval)

    return OptiesAanvallen

class Vijand:
    def __init__(self, afbeelding, naam, levens, aanvallen):
        self.Afbeelding = afbeelding
        self.naam = naam
        self.hitpoints = levens
        self.aanvallen = aanvallen

    def AanvalKiezen(self):
        return self.aanvallen[random.randint(0, len(self.aanvallen) - 1)]