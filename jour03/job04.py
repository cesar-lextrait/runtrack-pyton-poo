class Joueur:
    def __init__(self, nom, numéro, position, nbButs, nbPasses, cartonsJaunes, cartonsRouges) -> None:
        self.__nom = nom
        self.__numéro = numéro
        self.__position = position
        self.__nbButs = nbButs
        self.__nbPasses = nbPasses
        self.__cartonsJaunes = cartonsJaunes
        self.__cartonsRouges = cartonsRouges

    def marquerUnBut(self, nbButs):
        self.__nbButs += nbButs

    def effectuerUnePasseDecisive(self, nbPasses):
        self.__nbPasses += nbPasses

    def recevoirUncartonJaune(self, cartonsJaunes):
        self.__cartonsJaunes += 1

    def recevoirUncartonRouge(self, cartonsRouges):
        self.__cartonsRouges += 1
    
    def afficherStatistiques(self):
        print("Le joueur {} qui porte le numéro {} a  marqué {} buts et effectué {} passes décisive, \
               il a reçu {} cartons jaunes et {} cartons rouges".format(self.__nom, self.__numéro, self.__nbButs, self.__nbPasses, self.__cartonsJaunes, self.__cartonsRouges))
    
        



class Equipe:
    def __init__(self, nomEquipe, listeJoueurs):
        self.__nomEquipe = nomEquipe
        self.__listeJoueurs = listeJoueurs

    def ajouterJoueur(self, joueur):
        self.__listeJoueurs.append(joueur)

    def AfficherStastistiquesJoueurs(self):
        for joueur in self.__listeJoueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiques(self, joueur, nbButs, nbPasses, cartonsJaunes, cartonsRouges):
        joueur.marquerUnBut(nbButs)
        joueur.effectuerUnePasseDecisive(nbPasses)
        joueur.recevoirUncartonJaune(cartonsJaunes)
        joueur.recevoirUncartonRouge(cartonsRouges)



joueur1 = Joueur("Cantona", 7, "attaquant", 26, 3, 3, 0)
joueur2 = Joueur("Gignac", 10, "attaquant", 17, 11, 2, 0)
joueur3 = Joueur("Umtiti", 4, "défenseur", 2, 0, 2, 1)

joueur1.afficherStatistiques()
joueur2.afficherStatistiques()
joueur3.afficherStatistiques()

joueur1.marquerUnBut(34)
joueur1.effectuerUnePasseDecisive(4)
joueur1.recevoirUncartonJaune(2)
joueur1.recevoirUncartonRouge(3)
joueur1.afficherStatistiques()

equipe1 = Equipe("OM", [joueur1, joueur2, joueur3])
equipe1.AfficherStastistiquesJoueurs()