from math import pi

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.rayon = rayon
        return self.rayon

    def afficherInfos(self):
        return self.rayon
    
    def circonference(self):
        c  = (self.rayon+self.rayon) * pi
        return c
    
    def aire(self):
        a = self.rayon**2 *pi
        return a
    
    def diametre(self):
        d = self.rayon+self.rayon
        return d
     

cercle = Cercle(4)
print("le rayon est : ", cercle.afficherInfos())
print("l'aire est : ", cercle.aire())
print("la circonference est : ", cercle.circonference())
print("le diametre est : ", cercle.diametre(), end='\n\n')

cercle.changerRayon(7)
print("le rayon est  : ", cercle.afficherInfos())
print("l'aire est : ", cercle.aire())
print("la circonference est : ", cercle.circonference())
print("le diametre est  : ", cercle.diametre())
