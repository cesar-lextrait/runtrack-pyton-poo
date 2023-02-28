class Voiture:
    
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir
    
    def set_marque(self, marque):
        self.__marque = marque
        
    def set_modele(self, modele):
        self.__modele = modele
        
    def set_annee(self, annee):
        self.__annee = annee
        
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
        
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche
        
    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir
        
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_en_marche(self):
        return self.__en_marche
    
    def get_reservoir(self):
        return self.__reservoir
    
    def demarrer(self):
        if self.__verifier_plein() and not self.__en_marche:
            self.__en_marche = True
            print("La voiture a démarré.")
        else:
            print("Impossible de démarrer la voiture.")
            
    def arreter(self):
        self.__en_marche = False
        print("La voiture a été arrêtée.")
        
    def __verifier_plein(self):
        return self.__reservoir > 5
    

# Instanciation d'une voiture
ma_voiture = Voiture("Renault", "Twingo", 2010, 150000)

# Affichage de l'état initial de la voiture
print("Marque:", ma_voiture.get_marque())
print("Modèle:", ma_voiture.get_modele())
print("Année:", ma_voiture.get_annee())
print("Kilométrage:", ma_voiture.get_kilometrage())
print("En marche:", ma_voiture.get_en_marche())
print("Niveau du réservoir:", ma_voiture.get_reservoir())

# Démarrage de la voiture
ma_voiture.demarrer()

# Ajout d'essence
ma_voiture.set_reservoir(10)

# Démarrage de la voiture à nouveau
ma_voiture.demarrer()

# Arrêt de la voiture
ma_voiture.arreter()