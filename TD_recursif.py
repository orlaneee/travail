#exercice1 recursivité
#Q1
def somme_recursif(n):
    if n == 0 :
        return 0
    else : 
        return n + somme_recursif(n-1)

somme_recursif(100)

def somme_iteratif(n):
    a = 0
    total = 0
    while a-1<n:
        total = total + a
        a = a+1
    return total

print(somme_iteratif(4))

#Q2a/ L'algorithme le plus proche de la formule de definiton est recursif
#Q2b/ L'avantage de la methode recursive est que c'est plus naturel/simple

#Q3