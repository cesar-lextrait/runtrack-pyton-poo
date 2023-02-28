class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def get_longueur(self):
        return self._longueur

    def set_longueur(self, longueur):
        self._longueur = longueur 

    def get_largeur(self):
        return self._largeur

    def set_largeur(self, largeur):
        self._largeur =  largeur


rect = Rectangle(10, 5)
print(rect.get_longueur())
print(rect.get_largeur())
rect.set_longueur(3)
rect.set_largeur(4)
print(rect.get_longueur())
print(rect.get_largeur())
