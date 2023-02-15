def bennante_argumente(int_argument, str_argument, float_argument):
    print("Bennante Argumente")
    print("------------------")
    print("i", int(int_argument))
    print("s", str(str_argument))
    print("f", float(float_argument))


def default_werte(int_argument=12, str_argument="Moin!", float_argument=7.0):
    print("Default Werte")
    print("------------------")
    print("i", int(int_argument))
    print("s", str(str_argument))
    print("f", float(float_argument))


def beliebig_viele_Argumente(*meine_argumente):  # It is a tuple when a star is used
    print("Meine Argumente")
    print("------------------")
    print(f"{meine_argumente}, Typ: {type(meine_argumente)}")
    for i in meine_argumente:
        print(i, type(i))


def beliebig_viele_bennante_Argumente(**argument_dict):
    print("Argument Dictionary")
    print("------------------")
    print(f"{argument_dict}, Typ: {type(argument_dict)}")
    for key, value in argument_dict.items():
        print(key, type(key), value, type(value))


def argumente():
    # bennante_argumente(1, "str", 0.5)
    # bennante_argumente(int_argument=4, str_argument="why", float_argument=9.1)
    # default_werte(41)
    # default_werte(str_argument="order is important otherwise call the argument")
    # beliebig_viele_Argumente(42, "Check", 8.5, 78, "yay")
    beliebig_viele_bennante_Argumente(i=42, s="Check")


def my_func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


# ----------------------------------------- #
def addieren(*summanden):
    summe = 0

    while type(summanden[0]).__name__ == tuple.__name__:
        # would have worked easier is we did not call the other functions later
        # we need a way to say when which argument type begins/ends
        summanden = summanden[0]

    for summand in summanden:
        summe += summand
    return summe


def multiplizieren(*faktoren):
    produkt = 1

    # while type(faktoren[0]).__name__ == tuple.__name__:
    while isinstance(faktoren[0], tuple):
        faktoren = [0]

    for faktor in faktoren:
        produkt *= faktor
    return produkt


def ausgabe(funktion):
    print(funktion)
    print(funktion.__name__)


def rechnen(fkt, *zahlen):
    return fkt(zahlen)


def funktionales():
    resultat = addieren(6, 7)
    resultat = multiplizieren(6, 7, 8)

    ausgabe(addieren)
    ausgabe(multiplizieren)

    print(rechnen(addieren, 3, 4, 5, 8))


if __name__ == "__main__":
    argumente()
    # my_func(name='Alice', age=30)

    print(addieren(3, 4, 5, 8))
    funktionales()


# class book():
#     __title = None
#     def __init__(self, t):
#         self.title = t
#     def __str__(self):
#         return f"The book is {self.title}"
#
# print(book("Alice"))
