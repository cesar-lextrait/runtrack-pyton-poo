class Commande:
    STATUT_EN_COURS = "en cours"
    STATUT_TERMINEE = "terminée"
    STATUT_ANNULEE = "annulée"
    
    def __init__(self, num_commande):
        self.__num_commande = num_commande
        self.__plats = {}
        self.__statut = Commande.STATUT_EN_COURS
        
    def ajouter_plat(self, nom_plat, prix):
        self.__plats[nom_plat] = {"prix": prix, "status": Commande.STATUT_EN_COURS}
        
    def annuler_commande(self):
        self.__statut = Commande.STATUT_ANNULEE
        
    def calculer_total(self):
        total = 0
        for plat in self.__plats.values():
            if plat["status"] == Commande.STATUT_EN_COURS:
                total += plat["prix"]
        return total
    
    def afficher(self):
        print("Commande #{}".format(self.__num_commande))
        for nom_plat, plat in self.__plats.items():
            print("- {} ({}): {}".format(nom_plat, plat["status"], plat["prix"]))
        print("Total : {}".format(self.calculer_total()))
        
    def calculer_tva(self, taux):
        return self.calculer_total() * taux / 100
    
    def get_num_commande(self):
        return self.__num_commande
    
    def set_num_commande(self, num_commande):
        self.__num_commande = num_commande
    
    def get_statut(self):
        return self.__statut
    
    def set_statut(self, statut):
        self.__statut = statut
        
    def changer_statut_plat(self, nom_plat, status):
        if nom_plat in self.__plats:
            self.__plats[nom_plat]["status"] = status
        else:
            print("Le plat {} n'est pas dans la commande.".format(nom_plat))

ma_commande = Commande(12345)

# Ajout de plats à la commande
ma_commande.ajouter_plat("Pizza", 10.0)
ma_commande.ajouter_plat("Pâtes", 8.0)
ma_commande.ajouter_plat("Salade", 5.0)

# Affichage de la commande
ma_commande.afficher()

# Calcul du total
total = ma_commande.calculer_total()
print("Total:", total)

# Calcul de la TVA
tva = ma_commande.calculer_tva(20)
print("TVA:", tva)

# Annulation de la commande
ma_commande.annuler_commande()

# Changement du statut de la pizza
ma_commande.changer_statut_plat("Pizza", Commande.STATUT_TERMINEE)

# Affichage de la commande après annulation et changement de statut
ma_commande.afficher()