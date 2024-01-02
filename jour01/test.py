class Etudiant:
    niveau = "prepa"
    
class Etudiant2:
    batiment = "La Plateforme"
    def __init__(self) -> None:
        self.niveau = "prepa"
    
print(Etudiant.niveau)
print(Etudiant2.batiment)
# print(Etudiant2.niveau)