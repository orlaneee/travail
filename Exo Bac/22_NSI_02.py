#sujet_épreuve_2
#Exo1
def moyenne(liste):
    total_notes = 0
    total_coef = 0
    for couple in liste:
        note = couple[0]
        coef = couple[1]
        total_notes += note * coef
        total_coef += coef
    return total_notes / total_coef
#Exo 2
def pascal(n):
    T = [[0] * (n+1) for p in range (n+1)]
    for n in range(n+1):
        if n == 0:
            T[n][0] = 1
        else:
            for k in range(n+1):
                if k == 0:
                    T[n][0] = 1
                else:
                    T[n][k] = T[n-1][k-1] + T[n-1][k]
    return T
T = trianglePascal(9)
