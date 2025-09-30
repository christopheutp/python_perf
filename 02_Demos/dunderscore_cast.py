class Chien:
    def __init__(self, nom:str, age:int, race:str, taille:int) -> None:
        self.nom = nom
        self.age = age
        self.race = race
        self.taille = taille
    
    def __len__(self): # correspond à la taille de l'objet chien, avec la fonction len()
        return self.taille
    
    def __str__(self) -> str: # cast/convertion du chien en chaine de caractères
        return f'{self.nom} le bon toutou est agé de {self.age} ans, est de race {self.race} et mesure {self.taille} de haut'
    
    def __repr__(self) -> str: # représentation du chien (informations pour le développeur)
        return f'Chien(nom={self.nom}, age={self.age}, race={self.race}, taille={self.taille})'

    def __int__(self) -> int: # cast/convertion en int 
        return self.age
    
    def __bool__(self) -> bool:
        return not (self.nom == "" and self.age == 0 and self.race == "" and self.taille == 0)
    

if __name__ == '__main__':
    ppt = Chien("Pepette", 2, "Rodweiller", 50)

    print(len(ppt))
    print(ppt)
    print(repr(ppt))
    print(int(ppt))
    print(bool(ppt))

    faux_chien = Chien("",0,"",0)
    print(bool(faux_chien))

    if ppt:
        print(ppt)

    if faux_chien:
        print(faux_chien)