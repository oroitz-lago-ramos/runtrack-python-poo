class Vehicule:
    def __init__(self, marque, modele, annee, prix) -> None:
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix
    
    def getMarque(self):
        return self.__marque
    def getModele(self):
        return self.__modele
    def getAnnee(self):
        return self.__annee
    def getPrix(self):
        return self.__prix
    
    def informationsVehicule(self):
        print("Information du vehicule:")
        print(f"Marque: {self.getMarque()} - Modele: {self.getModele()} - Année: {self.getAnnee()}")
        print(f"Prix: {self.getPrix()}€")
    
    def demarrer(self):
        print("Attention je roule")
        
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4) -> None:
        super().__init__(marque, modele, annee, prix)
        self.__portes = portes
        
    def getPortes(self):
        return self.__portes
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes :",self.getPortes())
    
    def demarrer(self):
        print("Le bruit du moteur ronronne")
        
ma_voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
ma_voiture.informationsVehicule()
ma_voiture.demarrer()

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2) -> None:
        super().__init__(marque, modele, annee, prix)
        self.__roues = roues
    
    def getRoues(self):
        return self.__roues
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.getRoues()}")
        
    def demarrer(self):
        print("La moto en Y")

ma_moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
ma_moto.informationsVehicule()
ma_moto.demarrer()