ma_liste = [1,2,3]
print(ma_liste)

def modifier_liste(liste):
    liste.append(4)
 
modifier_liste(ma_liste)   
print(ma_liste)

def non_modifier_liste(liste):
    liste = [4,5,6]

non_modifier_liste(ma_liste)
print(ma_liste)
print()
class MaClasse:
    def __init__(self,val) -> None:
        self.val = val
        
        
def modifier_obj(obj):
    obj.val += 3
def non_modifier_obj(obj):
    obj.val = 30
    # ça modifie également le assignement, j'en conclut que dans les classes si on modifie un attribut est modifie
    # d'ou l'importance d'utiliser des getters et setters
    
obj = MaClasse(5)
print(obj.val)
modifier_obj(obj)
print(obj.val)
non_modifier_obj(obj)
print(obj.val)