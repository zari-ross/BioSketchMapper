print("W2T1")

from W1T5_Schleifen_SCE_Nataliya import input_int_best
from W2T1_imported_Nataliya import quadrat



if (__name__ == "__main__"):
    print("Das ist Hauptprogramm:", __name__)

def main():
    print("Complicated")


print("Ergebnisse", quadrat(12))
# x = input_int_best("Zahl eingeben: ")
# print("Deine Eingabe ist:", x)


def formatierte_ausgabe():
    i = 12
    l = 121212132121
    f = 12321.2331
    s = "Python"

    print("01a", i)
    print("01b", l)
    print("01c", f)
    print("01d", s)

    print("02a" + str(i))
    print("02b" + str(l))
    print("02c" + str(f))
    print("02d" + s)

    # Die Variablen werden in den String integriert. f = formatted output, geschweiften Klammern sind wichtig.
    # Eine Konvertierung in einen String ist dadurch obsolet.
    print(f"03a {i}")
    print(f"03b {l}")
    print(f"03c {f}")
    print(f"03d {s}")

    print("04a i = " + str(i) + ", l = " + str(l) + ", f = " + str(f) + ", s = " + s)

    print(f"04b i = {i}, l = {l}, f = {f}, s = {s}")

    print(f"05a {i:25}")
    print(f"05b {l:25}")
    print(f"05c {f:25}")
    print(f"05d {s:25}")

    print(f"06a {i:25d}<--")
    print(f"06b {l:25,d}<--")
    print(f"06c {f:25.3f}<--")
    print(f"06d {s:25}<--")

    print(f"06a {i:b}")
    print(f"06b {54321:x}") # hexadecimal mit kleinen Buchstaben
    print(f"06c {54321:X}") # hexadecimal mit grossen Buchstaben


formatierte_ausgabe()

"""
Die bisherige Zusammensetzung eines Strings, der aus verschiedenen Komponenten
besteht, ist mühselig: Nicht-String-Werte müssen zu String konvertiert werden
und die häufige Nutzung von '+' wird unübersichtlich.
Da kommt die formatierte Ausgabe (in Python3 eingeführt) ins Spiel.
Den einleitenden Anführungsstrichen wird ein 'f' vorgestellt. Alles, was dem String
hinzugefügt werden soll, wird einfach in geschweifte Klammern geschrieben:
Variablen, Berechnungen, ...

s - String
d - decimal (Ganzzahlen)
f - floating point number (float)
f'{s}' - String
f'{s:10s}' - String rechtsseitig mit Leerzeichen aufgefüllt, sodass insgesamt 10 Zeichen linksbündig
f'{s:10s}' - String rechtsseitig mit Leerzeichen aufgefüllt, sodass insgesamt 10 Zeichen linksbündig
f'{i}' - int
f'{i:10d}' - int linksseitig mit Leerzeichen aufgefüllt, sodass insgesamt 10 Zeichen rechtsbündig
f'{f:13.7f}' - float mit 7 Nachkommastellen, linksseitig mit Leerzeichen aufgefüllt,
sodass insgesamt 13 Zeichen rechtsbündig (inkl. Punkt)
f'{i:,d}' - int mit Tausender-Trennzeichen
f'{i:x}' - int als Hex mit kleinen Buchstaben
f'{i:X}' - int als Hex mit großen Buchstaben
f'{i:b}' - int als Binärzahl
"""

from W1T4_while_Funktionen_Nataliya import umdrehung, leerzeichen_entfernen, ziffern_zahlen, trimmen, check_prim

def menu_func(inp):
    print(f' 1 ... umdrehen \n 2 ... leerzeichen_entfernen \n 3 ... ziffern_zahlen \n 4 ... trimmen \n 5 ... beenden ')
    eingabe = input(inp)
    print(eingabe)
    while int(eingabe) != 0:
        if int(eingabe) == 1:
            print("check")
            s = input("Welcher String soll umgedreht werden? ")
            out = umdrehung(s)
        elif int(eingabe) == 2:
            s = input("Welcher String soll leerzeichen_entfernen werden? ")
            out = leerzeichen_entfernen(s)
        elif int(eingabe) == 3:
            s = input("Welcher String soll ziffern_zahlen werden? ")
            out = ziffern_zahlen(s)
        elif int(eingabe) == 4:
            s = input("Welcher String soll getrimmt werden? ")
            out = trimmen(s)
        print(out)
        eingabe = input(inp)
        return "End"

x = menu_func("Auswahl: ")
print("Ergebnisse:", x)

def prim_bis_10000():
    for i in range(0, 10001):
        if check_prim(i):
            print(f"{i:25,d}")

prim_bis_10000()