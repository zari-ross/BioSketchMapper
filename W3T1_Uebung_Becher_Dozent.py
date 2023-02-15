class Becher():
    """
    Die Klasse "Becher" repräsentiert einen Trinkbecher. Womit der Becher gefüllt ist,
    wird über den Konstruktor mitgeteilt. Die Klasse soll sowohl textbasiert, als auch
    im graphischen Kontext nutzbar sein, was die Anwendung von "input" oder "print"
    verbietet.
    """
    __inhalt = None
    __fassungsvermoegen = None
    __fuellhoehe = None

    # ---------------------------------------------------------------

    def __init__(self, inhalt, fassungsvermoegen, fuellhoehe):
        self.__inhalt = inhalt
        self.__fassungsvermoegen = fassungsvermoegen
        self.__fuellhoehe = fuellhoehe

    # ---------------------------------------------------------------

    def leertrinken(self):
        self.__inhalt = None
        self.__fuellhoehe = 0.0

    # ---------------------------------------------------------------

    def auffuellen(self):
        """
        Der Becher ist nicht leer und wird mit dem gleichen Getränk vollgemacht.
        """
        if (self.__inhalt != None):
            self.__fuellhoehe = 1.0

    # ---------------------------------------------------------------

    def nachfuellen(self, inhalt):
        """
        Der Becher ist leer und wird einem Getränk vollgemacht.
        """
        if (self.__inhalt == None):
            self.__inhalt = inhalt
            self.__fuellhoehe = 1.0

    # ---------------------------------------------------------------

    def schluck_nehmen(self):
        self.__fuellhoehe -= 20.0 / self.__fassungsvermoegen
        if self.__fuellhoehe < 0:
            self.__fuellhoehe = 0.0
            self.__inhalt = None

    # ---------------------------------------------------------------

    def __str__(self):
        back = ""
        if (self.__inhalt == None):
            back = f"Der Becher ist leer und hat ein "
            back += f"Fassungsvermögen von {self.__fassungsvermoegen} ml."
        else:
            back = f"Der Becher beinhaltet {self.__inhalt}, hat ein "
            back += f"Fassungsvermögen von {self.__fassungsvermoegen} ml "
            back += f"und ist zu {self.__fuellhoehe * 100:1.1f} % gefüllt."
        return back


# ===================================================================

if (__name__ == "__main__"):
    b = Becher(input("Getränk: "), 300, 0.8)
    print(f"(01) {b}")
    b.leertrinken()
    print(f"(02) {b}")
    b.auffuellen()
    print(f"(03) {b}")
    b.nachfuellen("Tee")
    print(f"(04) {b}")
    b.schluck_nehmen()
    print(f"(05) {b}")
    b.auffuellen()
    print(f"(06) {b}")

