import abc #abstract base classes
# from abc import ABC, abstractmethod

# Pour créer une classe abstraite / interface, il nous faut hériter de la classe ABC dans le module abc
#
# Ce type de classe va nous permettre de créer des classes pouvant être héritées et forçant les
# classes qui en hériteront à implémenter les méthodes définies dans l'interface
#
# Il est ausi possible de créer une classe abstraite / interface avec la metaclass ABCMeta Dinosaure(metaclass=abc.ABCMeta)

class Dinosaure(abc.ABC):
    # Pour créer une méthode abstraite qui devra à terme être implémentée, il nous faut passer
    # par le décorateur @abc.abstractmethod
    #
    # Ces méthodes n'ont pas forcément besoin de corps, vu que leur but n'est pas d'être utilisée dans cette
    # classe mais dans celle qui en héritera
    @abc.abstractmethod
    def crier(self):
        pass

# En héritant de notre interface, on est forcé d'implémenter la méthode
# abstraite pour que notre classe puisse servir à l'instanciation
#
# Si l'on ne le fait pas, on a levée d'une exception lors de la tentative d'instanciation
class Stegosaure(Dinosaure):

    def test(self):
        print("test")

    def crier(self):
        print("Mon stego crie !")


# dino = Dinosaure() # ERREUR car la classe Dinosaure est abstraite
stego = Stegosaure() # si on ne redéfinit/surcharge pas crier, la classe Stegosaure ne poura pas être instanciée
stego.crier()