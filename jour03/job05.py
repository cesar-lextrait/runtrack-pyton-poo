class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def estVivant(self):
        return self.vie > 0

    def attaquer(self, personnage, degats):
        personnage.vie -= degats

    
    def getNom(self):
        return self.nom
    
class Jeu:
    def __init__(self):
        self.niveau = 0
        self.__personnages = []
    
    def getPersonnages(self):
        return self.__personnages

    def getNom(self, nom):
        self._nom = nom
        return self._nom
    
    def choisirNiveau(self):
        self.niveau = input("Choisissez un niveau de difficulté (1, 2 ou 3): ")
        if self.niveau == "1":
            self.__personnages.append(Personnage("Néo", 100))
            self.__personnages.append(Personnage("Agent Smith", 100))
        elif self.niveau  == "2":
            self.__personnages.append(Personnage("Néo", 150))
            self.__personnages.append(Personnage("Agent Smith", 100))
            self.__personnages.append(Personnage("Trinity", 120))
            self.__personnages.append(Personnage("Morpheus", 130))
        elif self.niveau  == "3":
            self.__personnages.append(Personnage("Néo", 150))
            self.__personnages.append(Personnage("Agent Smith", 100))
            self.__personnages.append(Personnage("Trinity", 120))
            self.__personnages.append(Personnage("Morpheus", 130))
            self.__personnages.append(Personnage("Cypher", 80))
        else:
            print("Choix incorrect")
            self.choisirNiveau()

    def lancerJeu(self):
        self.choisirNiveau()
        print("Le jeu commence")
        print("Le niveau choisi est le niveau", self.niveau)
        print("Les personnages sont:")
        for personnage in self.__personnages:
             print(personnage.getNom())

        joueur = self.__personnages[0]
        ennemi = self.__personnages[1]

        while joueur.estVivant() and ennemi.estVivant():
            joueur.attaquer(ennemi, 10)
            ennemi.attaquer(joueur, 10)
            print(f"Vie de {joueur.nom} : {joueur.vie}")
            print(f"Vie de {ennemi.nom} : {ennemi.vie}")

        if joueur.estVivant():
            print("Vous avez gagné !")
        else:
            print("Vous avez perdu...") 


jeu = Jeu()
jeu.lancerJeu()

joueur = jeu.getPersonnages()[0]
ennemi = jeu.getPersonnages()[1]

while joueur.vie > 0 and ennemi.vie > 0:
    print(joueur.nom, ":", joueur.vie, "points de vie")
    print(ennemi.nom, ":", ennemi.vie, "points de vie")
    joueur.attaquer(ennemi, 10)
    if ennemi.vie > 0:
        ennemi.attaquer(joueur, 10)

if joueur.vie > 0:
    print("Bravo, vous avez vaincu l'ennemi !")
else:
    print("Dommage, vous avez été vaincu...")
