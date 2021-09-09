liste = [9, 15, 18, 21, 30,]

def algorithme(liste,nb):
    pivot = 0
    gauche = 0
    droite = len(liste)-1
    
    while gauche<=droite:
        pivot = (gauche + droite)//2
        if pivot == nb:
            return True
        elif pivot < nb:
            gauche = pivot + 1
        else:
            droite = pivot - 1
        return False
        
print(algorithme(liste,9))
            
