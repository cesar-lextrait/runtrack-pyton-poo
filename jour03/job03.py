class Tache:
    def __init__(self, nom, description):
        self.__nom = nom
        self.__description = description
        self.__statut= "A faire"

    def marquer_comme_finie(self):
        self.__statut = "Terminée"

    def get_tache(self):
        return (self.__nom, self.__description, self.__statut)
    

class ListeDeTaches:
    def __init__(self):
        self.__taches = []
     
    def ajouter_tache(self, tache):
        self.__taches.append(tache)
    
    def supprimer_tache(self, tache):
        self.__taches.remove(tache)

    def marquer_tache_comme_finie(self, tache):
        tache.marquer_comme_finie()


    def afficherListe(self):
        for tache in self.__taches:
            if tache.get_tache()[2] == "A faire":
                print(tache.get_tache())

    def filterListe(self):
        for tache in self.__taches:
            if tache.get_tache()[2] == "Terminée":
                print(tache.get_tache())

    
tache1 = Tache("Faire les courses", "Acheter du café, de l'hule et de la lessive")
tache2 = Tache("Ranger la chambre", "Ranger les vêtements et le bureau, et tout le ménage même")
tache3 = Tache("Apprendre Python", "Faire des exercices et des projets")

liste_taches = ListeDeTaches()

liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)
print("Tâches à faire :")
liste_taches.afficherListe()

liste_taches.marquer_tache_comme_finie(tache1)
liste_taches.marquer_tache_comme_finie(tache3)

print("Tâches terminées :")
liste_taches.filterListe()


print("Tâches à faire :")
liste_taches.afficherListe()