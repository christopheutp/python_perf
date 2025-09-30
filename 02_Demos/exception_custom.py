# Pour créer une exception nous-même, il nous suffit de créer une
# classe qui héritera d'Exception
class AgeInvalideException(Exception):
    pass

# class AgeInvalideException(Exception):
#     def __init__(self, *args: object) -> None:
#         super().__init__("Age invalide", *args)

# Si l'on veut lever l'exception et stopper le programme, il nous
# faut utiliser le mot-clé raise suivit du type d'exception
# raise AgeInvalideException 

# Il est possible de passer un message d'exception
# entre les parenthèse du constructeur
# raise Exception("Un problème dans le message d'exception")
# raise AgeInvalideException("Age invalide")


# def input_age():
#     try:
#         age = int(input("Saisir votre Age : "))
#         if age<= 0 or age >=120:
#             raise AgeInvalideException("Age invalide")
#     except ValueError as ve:
#         print(ve)
#         print("Saisie invalide !")
#         return -1
#     except AgeInvalideException as aie: 
#         print(aie)
#         return -1
#     else:
#         print("Age valide !")
#         return age


# if __name__ == '__main__':
#     age = -1
#     while age == -1:
#         age = input_age()

# def input_age():
#     age_local = int(input("Saisir votre Age : "))
#     if age_local<= 0 or age_local >=120:
#         raise AgeInvalideException("Age invalide")
#     return age_local

# if __name__ == "__main__":
#     age = -1
#     while age == -1:
#         try:
#             age = input_age()
#         # except ValueError as ve:
#         #     print(ve)
#         #     print("Saisie invalide !")
#         # except AgeInvalideException as aie:
#         #     print (aie)
#         except Exception as ex: # Attrape tout les types d'exception
#             print(ex)
#             print(type(ex))
#         else:
#             print("Age valide !")


class Personne:
    def __init__(self, age) -> None:
        if age<= 0 or age >=120:
            raise AgeInvalideException("Age invalide")
        self.age = age

try:
    p = Personne(3000)
except Exception:
    print('Un problème est arrivé lors de la création de mon instance de personne')

print('test')
print(p) 