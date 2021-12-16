##TP_sac_à_dos
##listeObjets = [[7,12],[4,11],[3,8],[3,10]]
##
##def cle_tri(objet):
##    return objet[0]/objet[1]
##
##listeObjetsTriee= sorted(listeObjets, key = cle_tri, reverse = True)
##
##
##p = 0
##sac = []
##for obj in listeObjetsTriee : #obj = liste
##    if p + obj[1] <= 30:
##        sac.append(obj)
##        p = p + obj[1]
##        
##objet = listeObjetsTriee[0]     
##while p + objet[1] <= 30:
##    sac = sac + [objet]
##    p = p + objet[1]
##    objet = listeObjetsTriee[1]

##TP_rendu_monnaie
systeme_pieces = [200, 100, 50, 20, 10, 5, 2, 1]
def rendu_monnaie(cent, systeme_pieces):
    '''
    description de fonction : elle rend la monnaie mais de manière optimisée.
    cent(entier): une valeur de centime a retirer.
    systeme_pieces(liste d'entier): pièce disponible à l'infini
    return(liste): de pièces rendues
    >>> rendu_monnaie(55, systeme_pieces)
    [50, 5]
    >>> rendu_monnaie(43, systeme_pieces)
    [20, 20, 2, 1]
    >>> rendu_monnaie(100, systeme_pieces)
    [100]
    '''
    monnaie_rendue = []
    i = 0
    argent_rendu = 0
    while argent_rendu < cent:
        if argent_rendu + systeme_pieces[i] <= cent:
            argent_rendu += systeme_pieces[i]
            monnaie_rendue.append(systeme_pieces[i])
        else:
            i = i + 1
    return monnaie_rendue

    
    
    
if __name__ == '__main__':
    # Validation des tests
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
    
