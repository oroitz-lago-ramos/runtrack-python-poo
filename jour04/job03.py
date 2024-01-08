class Rectangle:
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
        
    def perimetre(self):
        return (self.getLongueur() + self.getLargeur()) * 2
    def surface(self):
        return self.getLargeur() * self.getLongueur()
    
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur) -> None:
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def getHauteur(self):
        return self.__hauteur
    def setHauteur(self, val):
        self.__hauteur = val
    
    def volume(self):
        return (self.getLargeur() * self.getLongueur() * self.getHauteur())
    
rectangle = Rectangle(10, 20)
parallelepipede = Parallelepipede(10,20,5)

print("Perimètre:",rectangle.perimetre())
print("Surface:",rectangle.surface())
print("Volume:",parallelepipede.volume())
    