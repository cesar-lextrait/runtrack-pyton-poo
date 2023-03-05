def longueur(chaine):
    if chaine  == "":
        return 0
    else:
        return 1 + longueur(chaine[1:])
    
chaine = input("Entrez une chaine : ")
resultat = longueur(chaine)
print(f"la longueur de {chaine} est {resultat}")