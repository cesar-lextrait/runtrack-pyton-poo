class Ville:

    def __init__(self, nom, nbHabitants):
        self.__nom= nom
        self.__nbHabitants = nbHabitants

    def get_ville(self):
        return (self.__nom, self.__nbHabitants)
    
    def ajouter_population(self, nb_nouveauHabitants):
        self.__nbHabitants += nb_nouveauHabitants

class Personne:
    def __init__(self, nom, age, ville,):
        self.__nom = nom
        self.__age = age
        self.__ville = ville


    def ajouter_population(self, nb_nouveauxHabitants):
        self.__ville.ajouter_population(nb_nouveauxHabitants)

    
    
Ville1 = Ville("Paris", 1000000)
Ville2 = Ville("Marseille", 861635)
Personne1 = Personne("John", 45, Ville1)
Personne2 = Personne("Myrtille", 4, Ville1)
Personne3 = Personne("Chloé", 18, Ville2)

nom_ville1, pop_ville1 = Ville1.get_ville()
nom_ville2, pop_ville2 = Ville2.get_ville()
print(f"La ville de {nom_ville1} a une population de {pop_ville1} habitants.")
print(f"La ville de {nom_ville2} a une population de {pop_ville2} habitants.")


Personne1.ajouter_population(1)
Personne2.ajouter_population(1)
pop_ville1 = Ville1.get_ville()[1]
print("Mise à jour de la population de la ville de Paris : {} habitants".format(pop_ville1))

Personne3.ajouter_population(1)
pop_ville2 = Ville2.get_ville()[1]
print("Mise à jour de la population de la ville de Marseille : {} habitants".format(pop_ville2))