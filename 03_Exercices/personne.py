class Personne:
    """representation d'une personne"""
    def __init__(self,nom: str,prenom,tel,mail):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail

    def __str__(self) -> str :
        return f"Personne : nom : {self.nom} prenom : {self.prenom} tel : {self.tel} mail: {self.mail}"
    

class Travailleur(Personne):
    def __init__(self, nom, prenom, tel, mail,nom_entreprise,adresse_entreprise,tel_professionnel):
        super().__init__(nom, prenom, tel, mail)
        self.nom_entreprise = nom_entreprise
        self.adresse_entreprise = adresse_entreprise
        self.tel_professionnel = tel_professionnel

    def __str__(self):
        return super().__str__() + f" entreprise : {self.nom_entreprise} adresse entreprise : {self.adresse_entreprise} tel pro : {self.tel_professionnel}"

class Scientifique(Travailleur):
    def __init__(self, nom, prenom, tel, mail, nom_entreprise, adresse_entreprise, tel_professionnel,disciplines,types_du_scientifique):
        super().__init__(nom, prenom, tel, mail, nom_entreprise, adresse_entreprise, tel_professionnel)
        self.disciplines = disciplines
        self.types_du_scientifique = types_du_scientifique

    def __str__(self):
        return super().__str__() + f" disciplines : {self.disciplines}, type : {self.types_du_scientifique}"
    


personne = Personne("toto","tutu","123456789","toto@tutu.com")
print(personne)
print('-'*100)
travailleur = Travailleur("toto","tutu","123456789","toto@tutu.com","Microsoft","Silicon valley","987654321")
print(travailleur)
print('-'*100)
scientifique = Scientifique("toto","tutu","123456789","toto@tutu.com","Microsoft","Silicon valley","987654321",['chimie','physique'],['experimental','informatique'])
print(scientifique)
