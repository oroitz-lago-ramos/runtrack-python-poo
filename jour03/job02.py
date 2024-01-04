class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert) -> None:
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    
    def afficher(self):
        print(f"Numero de compte: {self.__numero_compte}")
        print(f"Client: {self.__prenom} {self.__nom}")
        print(f"Solde du compte: {self.__solde} €\n")
       
    def afficherSolde(self):
        print(f"Solde actuel de {self.__prenom} {self.__nom}: {self.__solde} €\n")
        
    def versement(self, qte):
        self.__solde += qte
        print(f"Vous avez reçu {qte} €")
        print(f"Votre nouveau solde est de {self.__solde} €\n")
    
    def virement(self, compte, somme):
        if self.__solde >= somme or self.__decouvert:
            self.__solde -= somme
            compte.__solde += somme
            print(f"Le virement de {somme} € à été effectué\n")
        else:
            print("Vous n'avez pas la capacité d'effectuer ce versement\n")
        
    def retrait(self, qte):
        if self.__solde >= qte or self.__decouvert:
            self.__solde -= qte
            print(f"Vous avez retiré {qte} € de votre solde")
            print(f"Il vous reste {self.__solde} € sur votre compte\n")
        else:
            print("Vous n'avez pas assez de solde sur votre compte, retrait impossible")
    
    def agios(self):
        pass
    

            
print()      
      
mon_compte = CompteBancaire(667,"Lago Ramos", "Oroitz", 1_000_000, False)
thomas_compte = CompteBancaire(667,"Chardin", "Thomas", -100_000, True)

mon_compte.afficher()
mon_compte.afficherSolde()
mon_compte.retrait(250000)
mon_compte.versement(50)
mon_compte.retrait(2_000_000)
mon_compte.afficherSolde()
mon_compte.virement(thomas_compte, 55_000)
mon_compte.virement(thomas_compte, 45_000)
mon_compte.afficherSolde()
thomas_compte.afficherSolde()
