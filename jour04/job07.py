import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class JeuDeCartes:
    def __init__(self) -> None:
        self.listeDeCartes = [Carte(valeur, couleur) for valeur in range(1,14) for couleur in ['pique','coeur', 'treffle','carreau']]
    
    def melanger(self):
        random.shuffle(self.listeDeCartes)
    
    def distribuer(self):
        return self.listeDeCartes.pop()
    
class Joueur:
    def __init__(self) -> None:
        self.main = []
    
    def prendre(self,listeDeCartes):
        self.main.append(listeDeCartes.distribuer())
    
    def calculValeur(self):
        valeur = 0
        ases = 0
        for carte in self.main:
            if carte.valeur > 10:
                valeur += 10
            elif carte.valeur == 1:
                ases += 1
                valeur += 11
            else:
                valeur += carte.valeur
        while valeur > 21 and ases:
            valeur -= 10
            aces -= 1
        return valeur
    
class Jeu:
    def __init__(self) -> None:
        self.listeDeCartes = JeuDeCartes()
        self.listeDeCartes.melanger()
        self.joueur = Joueur()
        self.dealer = Joueur()
            
    def jouer(self):
        for _ in range(2):
            self.joueur.prendre(self.listeDeCartes)
            self.dealer.prendre(self.listeDeCartes)
        while self.joueur.calculValeur() < 21:
            self.joueur.prendre(self.listeDeCartes)
        while self.dealer.calculValeur() < 17:
            self.dealer.prendre(self.listeDeCartes)
        valeurJoueur = self.joueur.calculValeur()
        valeurDealer = self.dealer.calculValeur()
        if valeurJoueur > 21:
            return "Le dealer gagné"
        elif valeurDealer > 21:
            return "Le joueur gagne"
        elif valeurJoueur > valeurDealer:
            return "Le joueur gagne"
        else:
            return "Le dealer gagne²"

jeu = Jeu()
resultat = jeu.jouer()
print(resultat)
