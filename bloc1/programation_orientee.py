class CompteBancaire:
    def __init__(self,numero,titulaire,solde):
        self.solde = solde
        self.numero = numero
        self.titulaire = titulaire
        
    def deposer_argent(saelf, valeur):
        self.solde = self.solde + valeur
        return self.solde
    def retirer_argent (self, valeur):
        self.solde = self.solde - valeur
        if self.solde < valeur:
            return "Vous ne pouvez pas effectuer cette transaction"
        else:
            return self.solde
        
un_compte = CompteBancaire(12345, "Alice", 0)

#Exercice 1

class Eleve:
    def __initi__(self, nom, classe, note):
        self.nom = nom
        self.classe = classe
        self.note = note
        
def compare(eleve1,eleve2):
    if eleve1.note == eleve2.note:
        return (eleve1.nom, eleve2.nom)
    elif eleve1.note < eleve2.note:
        return eleve1.nom
    else:
        eleve2.nom
        
PA = Eleve("Ngondji","tg",20)
Nathan = Eleve("Depaepe","tg",15)
Orlane = Eleve("Cailleux","tg",15)

#Exercice3

import random
class Personnage:

    def __init__(self, nom, points_de_vie,apt_combat):
        self.nom = nom
        self.vie = points_de_vie
        self.aptitude_combat = self.__limiter_aptitude_combat(apt_combat)
        
    def perd_vie(self):
        if random.random() < 0.5:
            nbPoint = 1
        else:
            nbPoint = 2

        self.vie = self.vie - nbPoint
        return nbPoint
    def __limiter_aptitude_combat(self, degat):
        if degat > 4:
            return 4
        else:
            return degat
        
def game(j1,j2):
    
    while j1.vie > 0 and j2.vie > 0:
        perte1 = j1.perd_vie()
        print(j1.nom + " perd "+ str(perte1) + " point de vie")
        perte2 = j2.perd_vie()
        print(j2.nom + " perd "+ str(perte2) + " point de vie")

    if j1.vie <= 0 and j2.vie > 0:
        msg = j2.nom + " est vainqueur, il lui reste encore " + str(j2.vie) + " points alors que " + j1.nom + " est mort"
    elif j2.vie <= 0 and j1.vie > 0:
        msg = j1.nom + " est vainqueur, il lui reste encore " + str(j1.vie) + " points alors que " + j2.nom + " est mort"
    else:
        msg = "Les deux combattants sont morts en même temps"

    return msg

bilbo = Personnage("Bilbo", 20, 4)
gollum = Personnage("Gollum", 20, 3)
frodon = Personnage("Frondo", 20, 6)
araignee = Personnage("Araignée", 10, 2)
aragorn = Personnage("Aragorn", 30, 7)
orc = Personnage("Orc", 10, 2)

import math
class Point:
    def __init__(self,point,coor):
        self.point1 = point[0]
        self.point2 = coor[1]
    
    def __repr__(self):
        return "(" + str(self.point1) + "," + str(self.point2) + ")"
    

#Exo5

class Fraction:
    def __init__(self,num,denom):
        self.num = num / self.__euclidienne(num, denom)
        self.denom = denom / self.__euclidienne(num,denom)
        
    def __repr__(self):
        return str(self.num) + "/" + str(self.denom)
        
    def __eq__(self,frac2):
        return self.num / self.denom == frac2.num / frac2.denom
    
    def __lt__(self,frac2):
        return self.num / self.denom < frac2.num / frac2.denom
    
    def __mul__(self,frac2):
        res = Fraction(self.num * frac2.num, self.denom * frac2.denom)
        return res
    
    def __add__(self, frac2):
        res = Fraction(self.num * frac2.denom + frac2.num * self.denom, self.denom * frac2.denom)
        return res
    
    def __euclidienne(self, a,b):
        """permet de calculer le reste de la division euclidienne"""
        if b == 0:
            return a
        else:
            r = a % b
            return self.__euclidienne(b,r)
