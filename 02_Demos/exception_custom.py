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


def input_age():
    try:
        age = int(input("Saisir votre Age : "))
        if age<= 0 or age >=120:
            raise AgeInvalideException("Age invalide")
    except ValueError as ve:
        print(ve)
        print("Saisie invalide !")
        return -1
    except AgeInvalideException as aie: 
        print(aie)
        return -1
    else:
        print("Age valide !")
        return age


if __name__ == '__main__':
    age = -1
    while age == -1:
        age = input_age()