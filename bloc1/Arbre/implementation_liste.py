from visualisation_arbre import *
from random import randint

# PARTIE 1 - TRAVAIL PRELIMINAIRE Question 2
arbre_cours = [2, [8, [6, [], []], [9, [], []]], [1, [7, [], []], []]]
show(arbre_cours, "mon_arbre")

# PARTIE 1 - TRAVAIL PRELIMINAIRE Question 3
arbre = [21, [], []]
show(arbre, "arbre_feuille")
# # PARTIE 2 - CODE ET TESTS A ECRIRE

arbre_vide = []
arbre_feuille = [1, [], []]
def est_vide(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Détermine si un arbre est vide
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si l'arbre est vide, False sinon
    
    TESTS :
    >>> est_vide([])
    True
    
    >>> est_vide([2, [], []])
    False
    
    >>> est_vide([3, [5, [], []], []])
    False
    '''
    if arbre == []:
        return True
    else :
        return False #return arbre == []
    
def est_feuille(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Détermine si l'arbre est une feuille
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si l'arbre est une feuille, False sinon
    
    TESTS :
    >>> est_feuille(arbre_vide)
    False
    >>> est_feuille(arbre_feuille)
    True
    >>> est_feuille(arbre_cours)
    False
    '''
    if est_vide(arbre) == True:
        return False
    return arbre[1] == [] and arbre[2] == []

def racine(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie la valeur du noeud racine
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int, str, etc...) : Valeur du noeud racine
    précondition : vérifier si l'arbre est un arbre racine
    
    TESTS :
    >>> racine(arbre_feuille)
    1
    
    >>> racine(arbre_vide)
    "L'arbre est vide"
    
    >>> racine(arbre_cours)
    2
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
    assert est_vide(arbre) == False, "L'arbre est vide" # A compléter
    # Code de la fonction à compléter
    return arbre[0]

def SAG(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie le sous-arbre gauche de l'arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (list) : sous-arbre gauche
    précondition : A compléter
    
    TESTS :
    >>> SAG(arbre_cours)
    [8, [6, [], []]
    
    >>> SAG(arbre_vide)
    "Il n'y a pas de sous-arbre gauche"
    
    >>> SAG(arbre_feuille)
    [1, [], []]
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail)
    assert est_vide(arbre) == False, "l'arbre est vide donc il n'y a pas de sous-arbre gauche" # A compléter
    # Code de la fonction à compléter
    return arbre[1]

def SAD(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Renvoie le sous-arbre droit de l'arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (list) : sous-arbre droit
    précondition : A compléter
    
    TESTS :
    >>> SAD(arbre_cours)
    [1, [7, [], []], []]
    
    >>> SAD(arbre_vide)
    "Il n'y a pas de sous-arbre droit"
    
    >>> SAD(arbre_feuille)
    [1, [], []]
    '''
    # Vérification de la précondition (voir énoncé : remarques importantes sur le travail) 
    assert est_vide(arbre) == False, "Il n'y a pas de sous-arbre droit" # A compléter
    # Code de la fonction à compléter
    return arbre[2]

def taille(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Calcule la taille d'un arbre
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int) : Taille de l'arbre
    
    TESTS :
    >>> taille(arbre_cours)
    6
    >>> taille(arbre_vide)
    0
    >>> taille(arbre_feuille)
    1
    '''
    # A compléter
    if est_vide(arbre):
        return 0
    elif est_feuille(arbre):
        return 1
    else:
        return 1 + taille(SAG) + taille(SAD) 

def hauteur(arbre):
    '''
    DOCUMENTATION :
    Description de la fontion : Calcule la hauteur d'un arbre en respectant la convention
            donnée dans l'énoncé
    arbre (list) : Arbre implémenté sous forme de listes imbriquées
    return (int) : Hauteur de l'arbre
    
    TESTS :
    >>> taille(arbre_cours)
    3
    >>> taille(arbre_vide)
    0
    >>> taille(arbre_feuille)
    0
    '''
    # A compléter
    if est_vide(arbre):
        return -1
    elif est_feuille(arbre):
        return 0
    else:
        return 1 + max(hauteur(SAG), hauteur(SAD))

def cree_arbre_complet(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre complet de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    # A compléter
    

def cree_peigne_gauche(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne gauche de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    # A compléter

def cree_peigne_droit(h, maxi):
    '''
    DOCUMENTATION :
    Description de la fontion : crée un arbre peigne droit de hauteur h
            avec des valeurs de noeud aléatoires comprises entre 0 et maxi inclus
    h (int) : hauteur de l'arbre
    maxi (int) : valeur maximale des noeuds
    return (list) : arbre créé
    '''
    # A compléter

def est_egal(arbre1, arbre2):
    '''
    DOCUMENTATION :
    Description de la fontion : détermine si deux arbres sont identiques ou différents
    arbre1 (list) : Arbre implémenté sous forme de listes imbriquées
    arbre2 (list) : Arbre implémenté sous forme de listes imbriquées
    return (bool) : True si les deux arbres sont identiques, False sinon 
    
    TESTS :
    >>> est_egal([21, [17,[15], [27]], [30, [11], [3]]], [21, [17,[15], [27]], [30, [13], [3]]])
    False
    >>> est_egal([21, [17,[15], [27]], [30, [11], [3]]], [21, [17,[15], [27]], [30, [11], [3]]])
    True
    '''
    # A compléter
    return arbre1 == arbre2

if __name__ == '__main__':
    # Lancement des tests (laisser ces deux lignes de code inchangées)
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
    
    # PARTIE 2 - Question 3
    
    # Creation d'un arbre complet de hauteur 3
        # A compléter
    
    # Creation d'un peigne gauche de hauteur 3
        # A compléter
    
    # Creation d'un peigne droit de hauteur 3
        # A compléter
   
    # PARTIE 2 - Question 4 
    # A compléter
