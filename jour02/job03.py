class Livre:
    def __init__(self, titre, auteur, nb):
        self._titre = titre
        self._auteur = auteur
        self._nb= nb 
        self._disponible = True

    def get_titre(self):
        return self._titre
    
    def set_titre(self, titre):
        self._titre = titre

    def get_auteur(self):
        return self._auteur
    
    def set_auteur(self, auteur):
        self._auteur = auteur

    def get_nb(self):
        return self._nb
    
    def set_nb(self, nb):
        if isinstance(nb, int) and nb > 0:
            self._nb = nb 
        else:
            return False
    
    def verification(self):
        if self._disponible == True:
            return True
        else:
            return False
    
    def emprunter(self):
        if self.verification() == True:
            self._disponible = False 
            print("Le livre est disponible")
        else:
            print("Le livre est emprunté")
    
    def rendre_livre(self):
        if self.verification() == False:
            self._disponible = True
            print("Le livre est rendu")
        else:
            print("Le livre n'est pas rendu ")


livre = Livre("Le capital", "Marx", 3024)
print(livre.get_titre())
livre.set_titre("Snow crash")
print(livre.get_titre())
print(livre.get_nb())
livre.set_auteur("Proust")
print(livre.get_auteur())
print(livre.verification())
livre.emprunter()
livre.emprunter()
livre.rendre_livre()
livre.emprunter()
