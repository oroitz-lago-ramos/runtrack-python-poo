import random
class Personnage:
    def __init__(self, nom, maxVie) -> None:
        self._nom = nom
        self._maxVie = maxVie
        self._vie = self._maxVie
        self._estVivant = True
        
    def predreDegats(self,degats):
        if self._vie > degats:
            self._vie -= degats
            print(f"{self._nom} possède maintenant {self._vie} points de vie\n")
        else:
            self._estVivant = False
            print(f"{self._nom} possède maintenant 0 points de vie\n")
        
    def attaquer(self, ennemi):
        degats = random.randint(0,20)
        print(f"{self._nom} a attaqué et à fait {degats} points de degats")
        ennemi.predreDegats(degats)

    
class Jeu:
    def __init__(self):
        self._niveau = None
        self._joueur = None
        self._ennemi = None
    
    def choisirNiveau(self):
        self._niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3): "))
        if self._niveau == 1:
            vie = 100
            vie_ennemi = 80
        elif self._niveau == 2:
            vie = 60
            vie_ennemi = 60
        else:
            vie = 30
            vie_ennemi = 40
        return vie, vie_ennemi

    def lancerJeu(self):
        vie, vie_ennemi = self.choisirNiveau()
        self._joueur = Personnage("Joueur", vie)
        self._ennemi = Personnage("Ennemi", vie_ennemi)
        self.jouer()

    def verifierSante(self):
        if not self._joueur._estVivant:  
            return False
        elif not self._ennemi._estVivant:
            return False
        return True
    
    def verifierGagnant(self):
        if not self._joueur._estVivant:
            print("Le joueur est mort")
        elif not self._ennemi._estVivant:
            print("L'ennemi est mort")

    def jouerTour(self):
        self._joueur.attaquer(self._ennemi)
        if self.verifierSante():
            self._ennemi.attaquer(self._joueur)
        self.verifierSante()
    
    def jouer(self):
        while self.verifierSante():
            self.jouerTour()
        self.verifierGagnant()
        
jeu = Jeu()
jeu.lancerJeu()
