class Etudiant:
    niveau = "prepa"
    def print_hello():
        print("Hello!")
    
class Etudiant2:
    batiment = "La Plateforme"
    def __init__(self) -> None:
        self.niveau = "prepa"
    
print(Etudiant.niveau)
Etudiant.print_hello()
print(Etudiant2.batiment)
# print(Etudiant2.niveau)