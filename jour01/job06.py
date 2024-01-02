class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ''
    
    def afficherAge(self):
        print(f"L'age de l'animal est {self.age} ans")
    def afficherPrenom(self):
        print(f"L'animal se nomme {self.prenom}")
        
    def viellir(self):
        self.age += 1
    def nommer(self, prenom):
        self.prenom = prenom
    
        
mon_animal = Animal()
mon_animal.afficherAge()
mon_animal.viellir()
mon_animal.afficherAge()
mon_animal.afficherPrenom()
mon_animal.nommer("Luna")
mon_animal.afficherPrenom()