#     Es empfiehlt sich, Attribute als "privat" zu kennzeichnen, sodass
#     von außerhalb der Klasse nicht direkt auf sie zugegriffen werden kann.
#     Diese Kennzeichnung erfolgt durch zwei führende Unterstriche.
#     Das Attribut 'name' soll von außen nicht geändert werden können. Die einzige
#     Möglichkeit des Auslesens und der Änderung des Namens soll eine Methode sein.
#     Denn dann kann einem Attribut kein beliebiger Phantasieinhalt gegeben werden,
#     sondern es kann eine Plausibilitätsprüfung stattfinden. Bei Vornamen z.B.
#     ein Zugriff auf ein Register gültiger Namen.

# Die Becherklasse ist

class Becher:
    __inhalt = None
    __fassungsvermoegen = None
    __fuellhoehe = None

    def __init__(self, what, vol, height):
        # print(f"in __init__: {id(self):016X}")
        self.__inhalt = what  # "__" macht privat, nicht veraenderbar von aussen
        # aber kann veraendert werden durch Methoden, die inhaltlich sind in der Klasse
        self.__fassungsvermoegen = vol
        self.__fuellhoehe = height

    def __str__(self):
        if self.__fuellhoehe == 0:
            print("The cup is empty.")
        if self.__fuellhoehe == 0.5:
            print("The cup is either half empty or half full.")
        return f"Was ist drin: {self.__inhalt}, Fassungsvermoegen = {self.__fassungsvermoegen} ml" \
               f", Fuellhoehe = {self.__fuellhoehe:.0%}"

    def auffuelen(self):
        self.__fuellhoehe = 1
        # return f" Was ist drin: {self.__inhalt}, Fassungsvermoegen = {self.__fassungsvermoegen} ml,
        # Fuellhoehe = {self.__fuellhoehe:.0%}"
    #
    def leertrinken(self):
        self.__fuellhoehe = 0
        print("The cup is empty.")

    def schluckNehmen(self):
        if (self.__fassungsvermoegen * self.__fuellhoehe - 20) / self.__fassungsvermoegen > 0:
            self.__fuellhoehe = (self.__fassungsvermoegen * self.__fuellhoehe - 20) / self.__fassungsvermoegen
        else:
            print("The cup would be empty, are you sure you want to drink it? Press 4.")

def objektorientierung_becher_uebung():
    tasse_1 = Becher("Tee", 200, 0.2)
    tasse_2 = Becher("Kaffee", 300, 0.7)

    print(f"{tasse_1}, id in hex: 0x{id(tasse_1):016X}")
    tasse_1.auffuelen()
    print(f"{tasse_1}, id in hex: 0x{id(tasse_1):016X}")
    tasse_1.schluckNehmen()
    print(f"{tasse_1}, id in hex: 0x{id(tasse_1):016X}")
    tasse_1.schluckNehmen()
    tasse_1.schluckNehmen()
    print(f"{tasse_1}, id in hex: 0x{id(tasse_1):016X}")
    tasse_1.leertrinken()
    print(f"{tasse_1}, id in hex: 0x{id(tasse_1):016X}")

    print(f"\n{tasse_2}, id in hex: 0x{id(tasse_2):016X}")
    tasse_2.auffuelen()
    print(f"{tasse_2}, id in hex: 0x{id(tasse_2):016X}")
    tasse_2.schluckNehmen()
    print(f"{tasse_2}, id in hex: 0x{id(tasse_2):016X}")
    tasse_2.schluckNehmen()
    tasse_2.schluckNehmen()
    print(f"{tasse_2}, id in hex: 0x{id(tasse_2):016X}")
    tasse_2.leertrinken()
    print(f"{tasse_2}, id in hex: 0x{id(tasse_2):016X}")


from W1T5_Uebung_Schleifen_Dozent import input_int


def main():
    """
    Liegt das Hauptprogramm in einer eigenen Funktion, besteht später die Möglichkeit,
    es aus einer anderen Datei zu starten.
    """
    auswahl = -1
    tasse_1 = Becher("Tee", 200, 0.2)

    while (auswahl != 0):
        print("1 ... output")
        print("2 ... auffuelen")
        print("3 ... schluckNehmen")
        print("4 ... leertrinken")
        print("0 ... Beenden")

        auswahl = input_int("Bitte Auswahl treffen: ")
        if (auswahl >= 1) and (auswahl <= 4):
            if (auswahl == 1):
                print(f"{tasse_1}")
            elif (auswahl == 2):
                tasse_1.auffuelen()
            elif (auswahl == 3):
                tasse_1.schluckNehmen()  # how to check that is not empty afterwards
            elif (auswahl == 4):
                tasse_1.leertrinken()


if __name__ == "__main__":
    # objektorientierung_becher_uebung()
    main()
