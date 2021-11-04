# 21_NSI_01

# Exercice 1

def moyenne(couples):
    """
    Description de fonction : Renvoie une moyenne
    couples (list) : Liste contenant des tuples, d'un flotant de 0 à 20, la note, et d'un entier ,le coefficient.
    return (float) : Renvoie la moyenne
    """
    denominateur = 0
    total = 0
    for i in range(len(couples)):
        denominateur += (couples[i])[1]
        total += (couples[i])[0] * (couples[i])[1]
    return total / denominateur

# (2*15+1*9+3*12)/(2+1+3) = 12,5 et non 11,83
print(moyenne([(15,2),(9,1),(12,3)]))

# Exercice 2

def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C

print(pascal(4))
print(pascal(5))