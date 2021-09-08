liste = (21, 30, 15, 18, 10)

def moyenne_elements(liste):
    moyenne = 0
    Len = len(liste)
    for i in liste:
        moyenne =+ 1
    moyenne = moyenne/Len
    return moyenne

print("La moyenne est:", moyenne_elements(liste))

def moyenne_indice(liste):
    moyenne = 0
    Len = len(liste)
    long = len(liste)
    for i in range(long):
        moyenne = moyenne + liste[i]
    moyenne = moyenne / Len
    return moyenne

print("La moyenne est:", moyenne_indice(liste))

t = 0
Len = len(liste)
while t != sum(liste):
    t = t + 1
    if t == sum(liste):
        print("La moyenne est:", t/ len(liste))