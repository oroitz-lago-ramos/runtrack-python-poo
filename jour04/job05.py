import math

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
    
class Cercle(Forme):
    def __init__(self, radius) -> None:
        self.__radius = radius
    
    def getRadius(self):
        return self.__radius
    def setRadius(self, val):
        self.__radius = val
    
    def aire(self):
        return math.pi * (self.__radius ** 2)
    
rectangle = Rectangle(20, 45)
cercle = Cercle(5)
print("Aire du rectangle:",rectangle.aire())
print(f"Aire du cercle: {cercle.aire():.2f}")