def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)
    

n = int(input("Entrez un entier : "))
resultat = factoriel(n)
print(f"le factoriel de {n} est {resultat}")