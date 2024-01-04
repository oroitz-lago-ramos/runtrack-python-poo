class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombreHabitants = nombre_habitants
    
    def getNom(self):
        return self.__nom
    def getNombreHabitants(self):
        return self.__nombreHabitants
    def addNombreHabitants(self, chiffre):
        self.__nombreHabitants += chiffre
        
class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()
        
    def getVille(self):
        return self.__ville   
    
    def ajouterPopulation(self):
        self.__ville.addNombreHabitants(1)
    
    
marseille = Ville("Marseille", 861_635)
paris = Ville("Paris", 1_000_000)
print(f"\nIl y a {marseille.getNombreHabitants()} habitants à {marseille.getNom()}")
print(f"Il y a {paris.getNombreHabitants()} habitants à {paris.getNom()}")
print()

jhon = Personne("Jhon", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)
print()
print(f"Mise à jour de la population de la ville de {marseille.getNom()}: {marseille.getNombreHabitants()} habitants")
print(f"Mise à jour de la population de la ville de {paris.getNom()}: {paris.getNombreHabitants()} habitants\n")
