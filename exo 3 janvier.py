#EXERCICE

def moyenne(tab):
    element = len(tab)
    if element == 0:
        return "erreur"
    else:
        moyenne = 0
        a = 0
        for e in tab:
            a =a + e
        moyenne = a/ element
        return moyenne
    
#EXERCICE2

def tri(tab):
    i = 0
    j = len(tab) - 1
    while i != j:
        if tab[i] == 0:
            i += 1
        else:
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j - 1
    return tab