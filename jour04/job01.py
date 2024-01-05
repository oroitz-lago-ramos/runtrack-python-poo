class Personne:
    def __init__(self, age=14) -> None:
        self.age = age
    
    def afficherAge(self):
        print(f"L'age de la personne est {self.age}")
    def modifierAge(self, age):
        if type(age) == int and age > 0:
            self.age = age
    
    def bonjour(self):
        print("Hello")
        
class Eleve(Personne):
    def __init__(self) -> None:
        super().__init__()
    
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
        
class Professeur(Personne):
    def __init__(self, matiereEnseignee) -> None:
        super().__init__()
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")
        
personne = Personne()
eleve = Eleve()

eleve.afficherAge()