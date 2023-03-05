class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
class Parallepipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur
    
    def VolumeParallepipede(self):
        return self.__hauteur * self.surface()
    

rectangle1 = Rectangle(5, 6)
print(rectangle1.perimetre())
print(rectangle1.surface())

parallepipede1 = Parallepipède(5, 6, 7)
print(parallepipede1.VolumeParallepipede())
