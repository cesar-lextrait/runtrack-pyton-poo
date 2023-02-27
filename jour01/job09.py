class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def obtenir_nom(self):
        return self.nom
    
    def modifier_nom(self, nom):
        self.nom = nom
    
    def modifier_prixHT(self, prixHT):
        self.prixHT = prixHT
    
    def modifier_TVA(self, TVA):
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        prix_ttc =  self.prixHT *(1+(self.TVA/100))  
        return(prix_ttc)

    def afficher(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}, Prix TTC: {self.CalculerPrixTTC()}"


   
result = Produit('Chocolat', 3, 20)
print(result.afficher())

result.modifier_nom('Place Cinema')
result.modifier_prixHT(10)
result.modifier_TVA(10)
print(result.afficher())

result.modifier_nom('Livre')
result.modifier_prixHT(8)
result.modifier_TVA(5.5)
print(result.afficher())