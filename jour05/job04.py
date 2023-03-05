def  plus_grand_chiffre(liste):
    if liste == []:
        return 0
    else:
        max_chiffre = plus_grand_chiffre(liste[1:])
        if liste[0] > max_chiffre:
            return liste[0]
        else:
            return max_chiffre
        

liste = [12, 34, 54, 22, 34, 23, 40]
plus_grand_chiffre(liste)
print(f"le plus grand chiffre de {liste} est {plus_grand_chiffre(liste)}")