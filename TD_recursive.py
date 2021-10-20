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