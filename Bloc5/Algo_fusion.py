#Partie 1
def tri_fusion(liste):
    '''
    description de la fonction: permet de fusionner deux listes triées dans l'ordre croissant.
    liste(list): liste donnée
    return(list): liste triée dans l'ordre croissant
    '''
    if len(liste) < 2:
        return liste
    else :
        liste1, liste2 = coupe(liste)
        liste1 = tri_fusion(liste1)
        liste2 = tri_fusion(liste2)
        return fusion (liste1, liste2)
        
def coupe(liste):
    
    
def fusion(liste1, liste2):
    
    
    
    
    
    
tri_fusion([38, 27, 43, 3, 9, 82, 10])
#partie 3


    