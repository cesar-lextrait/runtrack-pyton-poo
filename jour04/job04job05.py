class Forme:
    def aire(self):
        return 0
    

class Cercle(Forme):
    def __init__(self, radius):
        self.__radius = radius

    def aire(self):
        return 3.14 * self.__radius * self.__radius
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur

    def aire(self):
        return self.__largeur * self.__hauteur



rectangle1 = Rectangle(5, 6)       
print(rectangle1.aire())
cercle1 = Cercle(5)
print(cercle1.aire())