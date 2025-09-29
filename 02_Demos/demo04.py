class Rectangle:
    def __init__(self,largeur,hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    @classmethod
    def carre(cls,cote):
        return cls(cote,cote)
    
    @classmethod
    def avec_chaine(cls,chaine):
        l,h = map(int, chaine.split("x"))
        return cls(l,h)
    
r1 = Rectangle(3,8)
r2 = Rectangle.carre(7)
r3 = Rectangle.avec_chaine("2x7")


print(r1.__dict__)
print(r2.__dict__)
print(r3.__dict__)