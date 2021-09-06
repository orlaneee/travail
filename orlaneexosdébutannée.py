liste = (21, 30, 1, 18, 15)

def recherche1( liste , valeur ):
    '''
La fonctione cherche un chiffre demandé dans la liste
    valeur
    return bool
    '''
    for elements in liste :
        if elements == valeur:
            return True
    return False

print(recherche1(liste , 30))

#Exercice2

def recherche2 (liste, valeur):
    '''
    La fonctione cherche un chiffre demandé dans la liste
    valeur
    return bool
    '''
    for i in range(len(liste)) :
        if i == valeur :
            return True
    return False

print(recherche2(liste, 4))

#Exercice3

def recherche3 (liste , valeur):
    i = liste[0]
    while i != len(liste):
        if i != valeur:
            i =+ 1
            return False
    return True

#print(recherche3(liste , 12))

#Exercies ALgorithme dichotomique
    '''liste triée
    demande dun nb dans la liste
    parcourir liste pour chercher ce nb
    prendre moitiée de la liste
    si chiffre plus petits que le chiffre demandé -> pas chercher
    si chiffre plus grand que le ciffre demandé -> pas chercher
    return bool
    '''
    
liste  = (1, 3, 5, 7, 9, 11, 13, 15)

def recherche_dichotomique(liste, valeur):
    """
    Rôle : détermine si la valeur est présente dans la liste
    """
    
    


