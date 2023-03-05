class Personne:
    def __init__(self):
        self.age = 14 # attribut d'instance

    def affiche(self):
        print("Age: ", self.age)

    def bonjour(self):
        print("Hello")

    def modif(self, age):
        self.age = age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.matiereEnseignee = matiereEnseignee

    def affichageMatiere(self):
        print("Je donne le cours de", self.matiereEnseignee)

    def affichageAge(self):
        print("J'ai", self.age, "ans")

    def bonjour(self):
        print("Bonjour")

eleve1 = Eleve()
eleve1.affiche()
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modif(15)
eleve1.affichageAge()

professeur1 = Professeur("Maths")
professeur1.bonjour()
professeur1.affichageMatiere()

