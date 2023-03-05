def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    

n = int(input("Entrez un nombre : "))
resultat = fibonnaci(n)
print(f"le fibonnaci de {n} est {resultat}")
