# Es ist eine Klasse "BecherMitAufdruck" zu schreiben, die von Becher abgeleitet ist.
# Diese Klasse soll zusätzlich einen Aufdruck verwalten, der beim Erwerb dieses Bechers
# vorhanden sein soll und nicht wieder geändert werden kann.
# Dieser muss natürlich bei der Ausgabe berücksichtigt werden!
#
# Ach ja: der Aufdruck soll "von außen" gelesen, aber nicht geändert werden können.
#
# bma = BecherMitAufdruck("Tee", 250, 0.85, "Andrés Teetasse")
# bma.leertrinken()
# print(bma) # Der Becher ... von 250 ml. Der Aufdruck ist "Andrés Teetasse"
# print(bma.get_aufdruck()) # Andrés Teetasse


from W3T1_Uebung_Becher_Dozent import Becher


class Becher_mit_Aufdruck(Becher):
    # soll von Becher vererben, in runde Klammern sollen die Klassen (comma-separated)
    # da sollen die Attributen nicht gehen
    __aufdruck = None

    def __init__(self, inhalt, fassungsvermoegen, fuellhoehe, aufdruck):  # , inhalt, fassungsvermoegen, fuellhoehe sind schon vererbt
        # super() ist in builtins festgelegt und ist einfach da
        # In diesem Beispiel ruft super().__init__(inhalt, fassungsvermoegen, fuellhoehe)
        # die __init__-Methode der Superklasse Becher auf,
        # um die inhalt, fassungsvermoegen, fuellhoehe Argumente an die Initialisierung der Basisklasse zu übergeben.

        super().__init__(inhalt, fassungsvermoegen, fuellhoehe)
        self.__aufdruck = aufdruck

    def __str__(self):
        back = super().__str__()
        back += f" Der Becher hat den Aufdruck \"{self.__aufdruck}\"."
        return back


if __name__ == "__main__":
    b = Becher_mit_Aufdruck(input("Getränk: "), 300, 0.8, "Coffee makes my day more beautiful!")
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

# super() ist eine eingebaute Funktion in Python, die eine Verbindung zur Superklasse einer Klasse herstellt.
# Durch Aufrufen der Methode super() können Sie auf
# Methoden und Eigenschaften der Superklasse zugreifen und diese verwenden.
#
# Dies ist besonders nützlich, wenn eine Klasse eine Methode überschreibt,
# die in der Superklasse definiert ist, und Sie immer noch die Funktionen der
# ursprünglichen Methode ausführen möchten. Sie können super() in der überschreibenden Methode verwenden,
# um auf die Methode der Superklasse zuzugreifen und diese in Kombination mit der überschreibenden Methode auszuführen.
# In diesem Beispiel ruft super().__init__(arg1, arg2) die __init__-Methode der Superklasse
# MyBaseClass auf, um die arg1 und arg2 Argumente an die Initialisierung der Basisklasse zu übergeben.

# "Basisklasse" und "Superklasse" sind nicht genau dasselbe,
# obwohl sie sich auf ähnliche Konzepte beziehen.
# Eine Basisklasse ist die Klasse, von der eine abgeleitete Klasse erbt,
# während eine Superklasse die Klasse ist, von der eine abgeleitete Klasse geerbt hat.
# In vielen Fällen sind Basisklassen und Superklassen dasselbe, insbesondere wenn eine einzige
# Vererbungshierarchie vorhanden ist.
# In mehrfachen Vererbungshierarchien kann es jedoch mehrere Basisklassen geben, aber nur eine Superklasse,
# die die Methode super() verwenden kann, um auf die nächste Methode in der Aufrufreihenfolge zuzugreifen.