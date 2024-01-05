class Forme:
    
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, longueur, largeur) -> None:
        self.__longueur = longueur
        self.__largeur = largeur
    
    def getLongueur(self):
        return self.__longueur
    def getLargeur(self):
        return self.__largeur
    
    def setLongueur(self, val):
        self.__longueur = val
    def setLargeur(self, val):
        self.__largeur = val
        
    def aire(self):
        return (self.getLongueur() * self.getLargeur())
    
rectangle = Rectangle(20, 45)
print("Aire du rectangle:",rectangle.aire())