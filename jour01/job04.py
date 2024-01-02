class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
    def SePresenter(self):
        print(f"Je suis {self.prenom} {self.nom}")
        
rodolphe = Personne("Rodolphe", "Le Ru")
oroitz = Personne("Oroitz", "Lago Ramos")
john = Personne("Jhon", "Doe")

rodolphe.SePresenter()
oroitz.SePresenter()
john.SePresenter()