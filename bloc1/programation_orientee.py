# class CompteBancaire:
#     def __init__(self,numero,titulaire,solde):
#         self.solde = solde
#         self.numero = numero
#         self.titulaire = titulaire
#         
#     def deposer_argent(saelf, valeur):
#         self.solde = self.solde + valeur
#         return self.solde
#     def retirer_argent (self, valeur):
#         self.solde = self.solde - valeur
#         if self.solde < valeur:
#             return "Vous ne pouvez pas effectuer cette transaction"
#         else:
#             return self.solde
#         
# un_compte = CompteBancaire(12345, "Alice", 0)

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