class Joueur:
    def __init__(self, nom , numero, position) -> None:
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nombreButs = 0
        self.passesDecisives = 0
        self.cartonsJaunes = 0
        self.cartonsRouges = 0

    def marquerUnBut(self):
        self.nombreButs += 1
    def effectuerUnePasseDecisive(self):
        self.passesDecisives += 1
    def recevoirUnCartonJaune(self):
        self.cartonsJaunes += 1
    def recevoirUnCartonRouge(self):
        self.cartonsRouges += 1
    
    def afficherStatistiques(self):
        print(f"{self.nom}")
        print(f"Numéro {self.numero} -- {self.position}")
        print(f"Buts: {self.nombreButs} -- Passes decisives: {self.passesDecisives}")
        print(f"Cartons rouges {self.cartonsRouges} -- Cartons jaunes{self.cartonsJaunes}")
        
class Equipe:
    def __init__(self, nom) -> None:
        self.nom = nom
        self.liste_joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)
    def AfficherStatistiquesJoueurs(self):
        print(f"Equipe {self.nom}")
        for item in self.liste_joueurs:
            item.afficherStatistiques()
            print()
            
roberto = Joueur("Roberto", 1, "Gardien")
fernando = Joueur("Fernando", 2, "Defense")
alonso = Joueur("Alonso", 3, "Attaquant")

minato = Joueur("Minato", 1, "Gardien")
nazuma = Joueur("Nazuma", 2, "Defense")
lorenzo = Joueur("Lorenzo", 3, "Attaquant")

equipe_esp = Equipe("Real Gran Via")
equipe_jpn = Equipe("Miyamoto Socker")

equipe_esp.ajouterJoueur(roberto)
equipe_esp.ajouterJoueur(fernando)
equipe_esp.ajouterJoueur(alonso)


equipe_jpn.ajouterJoueur(minato)
equipe_jpn.ajouterJoueur(nazuma)
equipe_jpn.ajouterJoueur(lorenzo)



nazuma.recevoirUnCartonJaune()
lorenzo.marquerUnBut()
fernando.marquerUnBut()
fernando.marquerUnBut()
alonso.marquerUnBut()
alonso.recevoirUnCartonRouge()
minato.marquerUnBut()

equipe_esp.AfficherStatistiquesJoueurs()
equipe_jpn.AfficherStatistiquesJoueurs()