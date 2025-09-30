class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        return (self.largeur + self.longueur) *2
    
    def surface(self):
        return self.largeur * self.longueur
    
  
    
class Parallepipede(Rectangle):
    def __init__(self, longueur, largeur,hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        return super().surface() * self.hauteur
        # return self.largeur * self.longueur * self.hauteur
    
    def perimetre(self):
        return 2 * super().perimetre() + 4 * self.hauteur
        # return 4 * (self.hauteur + self.largeur + self.longueur)
    
    def surface(self):
        return 2 * super().surface() + 2 * self.longueur * self.hauteur + 2 * self.largeur * self.hauteur
        #return 2 * self.largeur * self.longueur + 2 * self.longueur * self.hauteur + 2 * self.largeur * self.hauteur

print("Rectangle de 10 par 5 : ")   
rec = Rectangle(10,5)
print(rec.perimetre())
print(rec.surface())

print("Parallepipede de 10 par 5 par 4: ")   
para = Parallepipede(10,5,4)
print(para.perimetre())
print(para.surface())
print(para.volume())






