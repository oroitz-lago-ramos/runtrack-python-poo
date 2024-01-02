class Point:
    def __init__(self) -> None:
        self.x = 10
        self.y = 4
        
    def afficherLePoint(self):
        print(f"Les coordoonnées du point sont ({self.x},{self.y})")
        
    def afficherX(self):
        print(self.x)
    def afficherY(self):
        print(self.y)
        
    def changerX(self,valeur):
        self.x = valeur
    def changerY(self,valeur):
        self.y = valeur
    
point_1 = Point()
point_1.afficherX()
point_1.afficherY()
point_1.changerX(80)
point_1.changerY(20)
point_1.afficherLePoint()
