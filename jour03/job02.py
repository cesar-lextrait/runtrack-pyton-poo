class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, compte_bancaire=True):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__CompteBancaire = compte_bancaire
    def afficher(self):
        print("Le compte bancaire de {} {} a pour numéro de compte {} ".format(self.__nom, self.__prenom, self.__numero_compte))


    def afficherSolde(self):
        print("Le solde du compte bancaire est de {} euros.".format(self.__solde))


    def verser(self, montant):
        self.__solde += montant
        print("Le solde du compte bancaire est de {} euros.".format(self.__solde))

    def retrait(self, montant):
        if montant > self.__solde and self.__CompteBancaire == True:
            self.__solde -= montant
            self.agios()
        else:
            print("Le colde du compte bancaire est insuffisant pour effectuer ce retrait.")
            

    def agios(self):
        if self.__solde < 0 :
            self.__solde -= 15
            print("Des agios de 15 euros ont été prélevés sur votre compte.")
        print("Le solde du compte bancaire est de {} euros.".format(self.__solde))


compte1 = CompteBancaire(3489, "John", "Doe", 400, compte_bancaire=True)
compte2 = CompteBancaire(3490, "Jane", "Doe", 100, compte_bancaire=False)
compte1.afficher()
compte1.afficherSolde()
compte1.verser(100)
compte1.retrait(600)
compte1.agios()

compte2.afficher()
compte2.afficherSolde()
compte2.verser(100)
compte2.retrait(600)
compte2.agios()