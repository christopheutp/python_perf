# Demo héritage multiple + MRO (method resolution order)

# Pas de parent commun utile

class A:
    def save(self):
        print("methode save classe A")

class B:
    def save(self):
        print("methode save classe B")

class C(A,B):
    def save(self):
        print("methode save classe C")
        # super() va au prochain dans le MRO aprec C ici A
        super().save()
        
# C().save()

# Parent commun

class Root:
    def save(self):
        print("methode save dans Root")

class Root2:
    def save(self):
        print("methode save dans Root 2")

class A2(Root):
    def save(self):
        print("debut methode save classe A2")
        super().save()
        print("fin methode save classe A2")

class B2(Root):
    def save(self):
        print("debut methode save classe B2")
        super().save()
        print("fin methode save classe B2")

class C1(A2,B2):
    def save(self):
        print("debut methode save classe C1")
        super().save()
        print("fin methode save classe C1")

class C2(B2,A2):
    def save(self):
        print("debut methode save classe C2")
        super().save()
        print("fin methode save classe C2")

print("MRO de C1 :", [cls.__name__ for cls in C1.mro()])
print("MRO de C2 :", [cls.__name__ for cls in C2.mro()])
C1().save()
# C2().save()