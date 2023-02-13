# The methods like __init__ and __st__ exist, but we can overwrite them when we create new functions for them.

class Bundesland:
    # Class is not "reality", just attributes to describe the class.
    # Architect makes a plan that has all details of the future house - class,
    # with attributes: measurements, materials...
    # When the house at some address is being built it becomes an object.
    # Another house could be built at a different address with some attributes having different values.

    __name = None
    __hauptstadt = None
    __einwohner = None

    # The values of the attributes are currently made with assignment outside the class.
    # It would be better to be able to write them like this:
    # nds = Bundesland("Niedersachsen", "Hannover", 8_027_031)
    # Then we use the function "__init__"

    def __init__(self, n, h, e):  # better not to repeat the attribute names for parameters
        """ ... """
        print(f"in __init__: {id(self):016X}")
        self.name = n
        self.hauptstadt = n
        self.einwohner = n
        # self.name = "dfgwddw"

    # There are methods that are in use but not written out explicitly.
    # For example, we can initiate objects without explicitly writing__init__,
    # see later instances of nds and by, there it is hidden but present.
    # Constructor!!!
    def __str__(self):  # A method to output object as a string.
        # print(nds) explicitly is working as print(nds.__str__()
        # it is better to always write it ourselves, otherwise the output would be standard for al objects.
        return f" {self.name}: Hauptstadt = {self.hauptstadt}, Anzahl Einwohner = {self.einwohner}"


def objektorientierung_v1():
    # hier wird ein konkretes Objekt erzeugt, das die Informationen fuer Niedersachsen enthaelt.
    nds = Bundesland("Niedersachsen", "Hannover", 8_027_031)
    nds.hauptstadt = "Hannover"
    nds.einwohner = 8_027_031

    # nds.__name = "Nrdschsn"
    # print(nds.__name)
    # print(nds.name)
    # Here we have a creation of instance nds

    print(f"{nds}, id in hex: 0x{id(nds):016X}")  # before overwriting __str__ it would look different:
    # <__main__.Bundesland object at 0x00000209FE4462C0>, id in hex: 0x00000209FE4462C0
    print(f"{nds.__str__()}, id in hex: 0x{id(nds):016X}")  # same as previous

    # Now we don't need the next line because we implemented it in __str__
    print(f"{nds.name}: Hauptstadt = {nds.hauptstadt}, Anzahl Einwohner = {nds.einwohner}, id in hex: 0x{id(nds):016X}")

    # (01) < __main__.Bundesland    object    at    0x000002468FF24BE0 >, id in hex: 2468    FF24BE0
    # We are calling an object of class Bundesland. The objects person, tree or Bundesland would be output differently.
    # The developers had to find a way to do a universal output for all objects:
    # <datei.klassenname object at speicheradresse>
    # This output is not usually needed for user as it does not have information about the object.

    by = Bundesland("Bayern", "Muenchen", 13_176_989)
    by.hauptstadt = "Muenchen"
    by.einwohner = 13_176_989

    print(by)

if __name__ == "__main__":
    objektorientierung_v1()
