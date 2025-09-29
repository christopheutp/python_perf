class CompteBancaire:

    def __init__(self,numero_compte,titulaire,solde):
      self.numero_compte = numero_compte
      self.titulaire = titulaire
      self.solde = solde

    def versement(self,montant):
       self.solde += montant

    def retrait(self,montant):
       self.solde -= montant

    def agios(self):
        if self.solde < 0:
          agios = abs(self.solde) * 0.05
          print(f"L'agios applicable est d'un  montant de : {agios}")
        else:
          print("Vous n'etes pas a decouvert")

    def afficher(self):
       print("Compte bancaire n°",self.numero_compte,":")
       print("Solde : ",self.solde)

if __name__ == '__main__':
   compte = CompteBancaire("FR123456","toto",4000000)
   compte.afficher()
   compte.versement(10)
   compte.afficher()

# compte = CompteBancaire("FR123456","toto",4000000)
# compte.afficher()
# compte.versement(10)
# compte.afficher()

print(__name__)