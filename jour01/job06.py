class Animal:
    def __init__(self, age, prenom):
        self.age = age
        self.prenom = prenom

    def vieux(self):
        print("L'age de l'animal est", self.age, "ans")
        while self.age <= 10:
            self.age += 1
            print("L'age de l'animal est", self.age, "ans")
            


    def nommer(self, prenom):
        self.prenom = prenom
        print("L'animal se nomme", self.prenom)


A = Animal(3, '')
A.vieux()
A.nommer("Luna")