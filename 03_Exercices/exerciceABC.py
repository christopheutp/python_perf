from abc import ABC, abstractmethod

class Interface(ABC):
    __methods__ = ("test","__iter__","__len__")
    @classmethod
    def __subclasshook__(cls, C):
        if cls is Interface:
            if all(any(method in B.__dict__ for B in C.__mro__) for method in cls.__methods__):
                return True
        return NotImplemented


class MyClass:
    def test(self):
        return "toto"
    def __iter__(self):
        return iter([1,2,3])
    def __len__(self):
        return 42
    
class MyClass2:
    def __iter__(self):
        return iter([1,2,3])
    
print(issubclass(MyClass,Interface))
print(issubclass(MyClass2,Interface))


class Container(ABC):
    @abstractmethod
    def __contains__(self):
        pass

class Sized(ABC):
    @abstractmethod
    def __len__(self):
        pass

class SizedContainer(Container,Sized):
    def __contains__(self):
        pass

    def __len__(self):
        pass

    pass

class Iterable(ABC):
    @abstractmethod
    def __iter__(self):
        pass