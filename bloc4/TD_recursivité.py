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

#Exercice3

#1 la fonction de n! et fonction de (n-1)! est: n! = (n-1) x n
#2 Un + 1 = Un x (n + 1)

def factorielle_recursif(n):
    if n == 0:
        return 1
    else:
        return n * (factorielle_recursif(n-1))

#Exercice5

"""fonction récursive puissance qui :
prend deux entiers a et n (avec n >= 0)"""

def recursive(a,n):
    if n == 0:
        return 1
    else:
        
        return recursive(a,n-1) * a
    
#print(recursive(2,3))

def recursivev2(a,n):
    if n == 0:
        return 1
    elif (n % 2 == 0):
        return a*(recursivev2(a, n /2))
    else:
        
        return a * (a * (recursivev2(a, n-1)/2))
    
print(recursivev2(2,3))

# avec la fonction recursive ça sera plus long car ça fera 1-1,1-1... tandis que la fonction recursivev2 divisera par deux dès qu'on est sur un nombre paire


def recursive(a,n):
    if n == 0:
        return 1
    else:
        return a * recursive(a,n-1)

    #Exo6

#25 % 7

#Question2

def euclidienne(a,b):
    """permet de calculer le reste de la division euclidienne"""
    if b == 0:
        return a
    else:
        r = a % b
        return euclidienne(b,r)
    
#Exercie7
def nombre_de_chiffres(v):
    '''
    la fonction perme de savoir combien il y a de chiffres dans le nombre demandé.
    v: nombre demandé.
    '''
    if v < 10:
        return 1
    else:
        v = v// 10
        return 1 + nombre_de_chiffres(v)
print(nombre_de_chiffres(123456789))

#Exercice8
def appartient(v, t, i):
    if v == t[i]:
        return True
    elif t[-1] == t[i]:
        return False
    else:
        return appartient(v, t, i+1)
    
ma_liste = ['foo','bar','spam','ham','eggs']
print(appartient('spam', ma_liste, 3))

#Exercice9
def est_palindrome(chaine):
    while len(chaine) > 0:
        if chaine[0] == chaine[-1]:
            chaine = chaine[1:-1]
        else:
            return False
    return True

 def est_palindrome(chaine):
    if len(chaine) == 0:
        return True
    elif chaine[0] == chaine[-1]:
        return est_palindrome(chaine[1:-1])
    else:
        return False
    
#Exercice10
#Q1 Les fonctions trucs et bidul sont des récursives croisées car truc elles fonctionne ensemble, truc appel bidul et vice-versa
#Q2c) oui.
#Q3 truc = paire et bidul = impair
#Q4 truc et bidul sont terminales.
