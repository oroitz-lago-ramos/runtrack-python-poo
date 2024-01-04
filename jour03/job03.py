class Tache:
    def __init__(self,titre,description='') -> None:
        self.titre = titre
        self.description = description
        self.status = "à faire"
        
class ListeTaches:
    def __init__(self) -> None:
        self.taches = []
    
    def ajouterTaches(self, tache):
        self.taches.append(tache)
    def supprimerTache(self,tache):
        self.taches.remove(tache)
    def marquerCommeFinie(self,tache):
        index = self.taches.index(tache)
        self.taches[index].status = "terminée"
    def afficherListe(self, finieOuPas=None):
        liste = self.filtrerListe(finieOuPas)
        for item in liste:
            print(f"{item.titre} -- {item.description} | {item.status}")
            
    def filtrerListe(self, finieOuPas):
        '''
        Argument: Si elle est finie -> True, si à faire -> False
        Return -> list() une liste filtrée
        Si en argument finiOuPas = None retourne la liste entière
        '''
        if finieOuPas is None:
            return self.taches
        
        if finieOuPas:
            liste_filtre = []
            for item in self.taches:
                if item.status == "terminée":
                    liste_filtre.append(item)
            return liste_filtre
        elif not finieOuPas: 
            liste_filtre = []
            for item in self.taches:
                if item.status == "à faire":
                    liste_filtre.append(item)
            return liste_filtre
        
tache1 = Tache("Nettoyer salle de bain")
tache2 = Tache("Appeller assurence", "Leur demander un devis de remboursement")
tache3 = Tache("Veto vendredi 12/05/2012")
tache4 = Tache("Acheter cadeaux noël")
tache5 = Tache("Organiser mariage")

liste_taches = ListeTaches()

for i in range(1,6):
    nom_variable = f"tache{i}"
    tache = eval(nom_variable)
    liste_taches.ajouterTaches(tache)

print()
liste_taches.afficherListe()
print()

liste_taches.marquerCommeFinie(tache1)
liste_taches.marquerCommeFinie(tache3)
liste_taches.supprimerTache(tache4)

liste_taches.afficherListe()
print()
liste_taches.afficherListe(True)
print()
liste_taches.afficherListe(False)
print()

    