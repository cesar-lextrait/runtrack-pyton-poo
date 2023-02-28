class Livre:
    def __init__(self, titre, auteur, nb):
        self._titre = titre
        self._auteur = auteur
        self._nb= nb 

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
        
livre = Livre("Le capital", "Marx", 3024)
print(livre.get_titre())
livre.set_titre("Snow crash")
print(livre.get_titre())
print(livre.get_nb())
livre.set_auteur("Proust")
print(livre.get_auteur())

