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
            
roberto_lagrosseverge = Joueur("Roberto", 1, "Gardien")
fernando_longuebite = Joueur("Fernando", 2, "Defense")
alonso_allison = Joueur("Alonso", 3, "Attaquant")

minato_follekawazaki = Joueur("Minato", 1, "Gardien")
nazuma_sexarigato = Joueur("Nazuma", 2, "Defense")
porrete_lorenzo = Joueur("Porrete", 3, "Attaquant")

equipe_esp_gran_verga = Equipe("Real Gran Verga")
equipe_jpn_ahegao = Equipe("Miyamoto Ahegao")

equipe_esp_gran_verga.ajouterJoueur(roberto_lagrosseverge)
equipe_esp_gran_verga.ajouterJoueur(fernando_longuebite)
equipe_esp_gran_verga.ajouterJoueur(alonso_allison)


equipe_jpn_ahegao.ajouterJoueur(minato_follekawazaki)
equipe_jpn_ahegao.ajouterJoueur(nazuma_sexarigato)
equipe_jpn_ahegao.ajouterJoueur(porrete_lorenzo)



nazuma_sexarigato.recevoirUnCartonJaune()
porrete_lorenzo.marquerUnBut()
fernando_longuebite.marquerUnBut()
fernando_longuebite.marquerUnBut()
alonso_allison.marquerUnBut()
alonso_allison.recevoirUnCartonRouge()
minato_follekawazaki.marquerUnBut()

equipe_esp_gran_verga.AfficherStatistiquesJoueurs()
equipe_jpn_ahegao.AfficherStatistiquesJoueurs()