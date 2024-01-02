class Personnage:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
    
    def gauche(self):
        self.x -= 5
    def droite(self):
        self.x += 5
    def haut(self):
        self.y = -5
    def bas(self):
        self.y += 5
    
    def position(self):
        return (self.x, self.y)

mario = Personnage()
mario.bas()
mario.droite()
mario.droite()
mario.droite()
print(mario.position())