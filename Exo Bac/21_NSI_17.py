# 21_NSI_01

# Exercice 1

def RechercheMin(tab):
    """
    Description de fonction : Renvoie la première occurence du minimum d'un tableau trié
    tab (list) : Tableau trié d'entiers
    return (int) : première occurence du minimum
    """
    mini = 0
    for i in range(1,len(tab)):
        if tab[i] < tab[mini]:
            mini = i
    return mini

print(RechercheMin([5]))
print(RechercheMin([2,4,1]))
print(RechercheMin([5,3,2,2,4]))

# Exercice 2

def separe(tab):
    i = 0
    j = len(tab) - 1
    while i < j :
        if tab[i] == 0 :
            i = i + 1
        else :
            tab[i], tab[j] = tab[j], tab[i]
            j = j - 1
    return tab

print(separe([1,0,1,0,1,0,1,0]))
print(separe([1,0,0,0,1,1,0,1,1,0,1,0,1,1,1,0]))