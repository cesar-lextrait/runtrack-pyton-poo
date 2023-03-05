class Vehicule:
    def __init__(self, marque, modele,année, prix):
        self.marque = marque
        self.modele = modele
        self.année = année
        self.prix = prix

    def affiche(self):
        print("Marque: ", self.marque)
        print("Modèle: ", self.modele)
        print("Année: ", self.année)
        print("Prix: ", self.prix)

    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, année, modele, prix, nbPortes):
        Vehicule.__init__(self, marque, année, modele, prix)
        self.nbPortes = nbPortes

    def informationsVehicule(self):
        Vehicule.affiche(self)
        print("Nombre de portes: ", self.nbPortes)
    
    def demarrer(self):
        print("Attention, je conduis une mercedes je connais pas les priorités")


class Moto(Vehicule):
    def __init__(self, marque, année, modele, prix):
        Vehicule.__init__(self, marque, année, modele, prix)
        self.__roue = 2

    def informationsVehicule(self):
        Vehicule.affiche(self)
        print("Nombre de roues: ", self.__roue)

    def demarrer(self):
        print("Attention, je roule sans casque en Y")




voiture1 = Voiture("Mercedes", "Classe A", 2020, 18500, 4)
voiture1.informationsVehicule()

moto1 = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto1.informationsVehicule()
moto1.demarrer()
voiture1.demarrer()
