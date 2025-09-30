class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)

    def show(self):
        print(self.street)
        print(self.city)


class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print(self.name + ' - ' + self.email)


class Contact(Person, Address):
    def __init__(self, name, email, street, city):
        Person.__init__(self, name, email)
        Address.__init__(self, street, city)

    def show(self):
        Person.show(self)
        Address.show(self)

class Notebook:
    def __init__(self):
        self.notebook = dict()

    def __len__(self): # len(mon_carnet)
        return len(self.notebook)

    def __getitem__(self, name): # mon_carnet[name]
        return self.notebook[name]

    def __setitem__(self, name, contact): # mon_carnet[name] = contact
        self.notebook[name] = contact

    def __delitem__(self, name): # del mon_carnet[name]
        print(name, "supprimé des contacts")
        del self.notebook[name]

    def __contains__(self, name): # name in mon_carnet
        if name in self.notebook:
            return True
        else:
            return False

    def show(self):
        print("---- Liste de contacts ----")
        for name, contact in self.notebook.items():
            print(f"=== {name.upper()} ===")
            contact.show()
        print("-" * 27)


def main():
    mon_carnet = Notebook()
    mon_carnet["Bob"] = Contact('Bob', '<bob@example.com>', 'Rtb35', 'Sthlm')
    mon_carnet['Alice'] = Contact("alice", '<alice@example.com>', 'Lv24', 'Sthlm')
    mon_carnet.show()
    print()
    print("Nombre de contacts :", len(mon_carnet))
    print()
    del mon_carnet['Bob']
    print()
    mon_carnet.show()
    print("On vérifie que 'Alice' est dans les contacts :")
    print("Alice" in mon_carnet)
    print("On vérifie que 'Bob' est dans les contacts :")
    print("Bob" in mon_carnet)


if __name__ == "__main__":
    main()
