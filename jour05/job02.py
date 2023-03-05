def puissance(x, n):
    if n == 0:
        return 1
    else:
        return x * puissance(x, n-1)
    
x = int(input("Entrez un entier : "))
n = int(input("Entrez un entier : "))
resultat = puissance(x, n)
print(f"{x} puissance {n} est {resultat}")
   