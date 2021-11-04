#Sujet3 exo 1
def multiplication(n1,n2):
    if n1 >= 0 and n2 >= 0:
        resultat = 0
        for i in range(n1):
            resultat = resultat + n2
        return resultat
    elif n1 < 0 and n2 < 0:
        return multiplication(-n1, -n2)
    elif n1 < 0 and n2 >= 0:
        return - (multiplication(-n1, n2))
    else:
        return -(multiplication(n1,-n2))
    
print(multiplication(-2,0))