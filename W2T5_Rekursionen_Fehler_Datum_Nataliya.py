from MyTools.Tools import typ # needs to be loaded in the project directory


def fakultaet_iterativ(n):
    """
    abc, acb, bac, bca, cab, cba - 6 Möglichkeiten

    Die Anzahl der Permutationen kann über die Fakultät ermittelt werden.
    0! = 1
    1! = 1
    2! = 1 * 2 = 2
    3! = 1 * 2 * 3 = 6
    4! = 1 * 2 * 3 * 4 = 24
    ...
    n! = 1 * 2 * ... * (n - 1) * n
    """
    f = 1
    for i in range(1, n + 1):
        f *= i

    return f


# -------------------------------------------------------------------

import traceback


def fakultaet_rekursiv(n):
    """
    0! = 1
    1! = 1
    2! = 2 * 1!
       = 2 * (1)
       = 2
    3! = 3 * (2!)
       = 3 * (2 * (1!))
       = 3 * (2 * (1))
       = 3 * 2
       = 6
    4! = 4 * (3!)
       = 4 * (3 * (2!))
       = 4 * (3 * (2 * (1!)))
       = 4 * (3 * (2 * (1)))
       = 4 * (3 * 2)
       = 4 * 6
       = 24

    """
    if (n == 1):
        print("1! = 1")
        return 1
    else:
        print(f"{n} * {n - 1}! = {n * (n - 1)}")  # + " --- " + str(traceback.format_stack())+"\n")
        return n * fakultaet_rekursiv(n - 1)


# -------------------------------------------------------------------

def rekursionen():
    """
    https://de.wikipedia.org/wiki/Rekursion
    Eine rekursive Funktion ruft sich selbst immer wieder auf.
    Damit keine Endlos-Schleife entsteht, muss es eine Abbruchbedingung
    geben. Mithilfe rekursiver Funktion können wiederkehrende Teilaufgaben,
    deren Tiefe nicht bekannt ist und die einem festen Schema folgen, problemlos
    bewältigt werden. Ein Beispiel dafür ist das Auslesen eines vollständigen
    Verzeichnispfades. Eine Datei wird übernommen und in ein Verzeichnis muss eingetaucht werden.
    Hier beginnt dann alles - nach dem selben Schema - von Neuem. Gibt es kein weiteres
    Unterverzeichnis, ist das Verzeichnis abgearbeitet und es wird zum letzten
    Verzeichnis zurückgesprungen (sozusagen eine Ebene zurück).
    """

    print(f"(01) 5! = {fakultaet_iterativ(5):6,d}")
    print(f"(02) 8! = {fakultaet_iterativ(8):6,d}")
    print(f"(03) 5! = {fakultaet_rekursiv(5):6,d}")
    print(f"(04) 8! = {fakultaet_rekursiv(8):6,d}")

    a = fakultaet_iterativ(995)
    b = fakultaet_rekursiv(995)
    print(a == b)


# -------------------------------------------------------------------

def gerade():
    x = 13
    if (x % 2 == 0):
        grd = True
    else:
        grd = False

    # grd = (x % 2 == 0) ? True : False

    grd = True if (x % 2 == 0) else False


# -------------------------------------------------------------------

def fehler_v1():
    """
    Die Fehler, die hier auftreten, sind Fehler, die zur Laufzeit auftreten
    können und vom Compiler/Interpreter nicht festgestellt werden können.
    Tritt ein solcher Fehler unbehandelt auf, bricht das Programm ab.
    Ein solcher Fehler wird vom Interpreter "geworfen" (wird so bezeichnet).

    Es gibt die Möglichkeit, einen geworfenen Fehler zu fangen, darauf zu reagieren
    und den Programmabbruch zu verhindern.
    Es kann dabei etwas versucht ("try") werden und wenn es schiefgeht, kann
    gegen den Fehler Widerspruch eingelegt werden ("except").
    Tritt ein Fehler im try-Block auf, wird er verlassen und der except-Block
    betreten. Es erfolgt keine Rückkehr in try!
    """
    x = 0

    print(1)
    try:
        print(2)
        print(1 / x)
        print(3)
    except:
        print(4)
        print("Ein Fehler ist aufgetreten")
        print(5)
    print(6)


# -------------------------------------------------------------------

def fehler_v2():
    """
    In einem try-Block werden häufig mehrere Zeilen abgearbeitet, die
    unterschiedliche Fehler werfen können. Auf jeden dieser Fehler soll
    unterschiedlich (individuell) reagiert werden.
    D.h. ein try mit mehreren except-Blöcken wäre praktisch, bei denen jeder
    Fehler einen eigenen except-Block hätte.
    Im Fehlerfall werden die except-Blöcke sequentiell von oben nach unten
    gecheckt, ob der angegebene Fehler vorliegt. Falls nicht, fahre mit dem
    nächsten fort. Wird ein zutreffender Fehler gefunden, werden die
    weiteren except-Blöcke übersprungen.
    Trifft aber kein except-Block zu, bleibt der Fehler unbehandelt und das
    Programm bricht ab. Deshalb ist es manchmal sinnvoll, einen "allgemeinen"
    except-Block unterzubringen, der alle nicht behandelten Fehler fängt.
    Da der Check des passenden except-Blocks von oben nach unten verläuft,
    müssen die except-Blöcke von oben nach unten allgemeiner werden.
    Was heißt allgemeiner?
    Alle diese Fehler sind Klassen. Und Klassen erben voneinander. D.h. eine
    "allgemeinere" Fehlerklasse ist eine Superklasse davon.
    """
    liste = [7, 13, 17]

    try:
        zahl = liste[11]
        # zahl = int("abc")
        # zahl = int(input("Zahl: "))
        zahl = 1 / 0
    except IndexError:
        print("IndexError ist aufgetreten")
    except ValueError:
        print('ValueError: da ist eine Konvertierung fehlgeschlagen')
    except BaseException as be:
        print("Ein anderer Fehler:", type(be).__name__)


# -------------------------------------------------------------------

def fehler_v3():
    """
    Sollen im Zusammenhang mit try-except bestimmte Anweisungen
    a) ohne Fehler oder
    b) trotz Fehler (egal, ob gefangen oder nicht)
    ausgeführt werden, ist "finally" nützlich.
    Der finally-Block darf maximal einmal vorkommen! Er wird in jedem
    Falle betreten. Tritt aber darin ein unbehandelter Fehler auf,
    knallt es natürlich trotzdem (würde es im except auch).

    Wird beispielsweise im try eine Datei geöffnet und es tritt irgendwo
    ein Fehler auf, dann drohen innerhalb der Datei Inkonsistenzen. Deshalb
    sollte die Datei in jedem Fall geschlossen werden. Tritt hingegen kein
    Fehler auf, muss die Datei ebenfalls geschlossen werden.
    Genau hier kommt "finally" ins Spiel.
    """
    zahl = 0

    try:
        zahl = 1 / 0
    except:
        print("im except")
    finally:
        print("im finally")

    try:
        # zahl = 1 / 0
        # return # Funktion vorzeitig verlassen
        zahl = 13
    finally:
        print("try-finally")

    try:
        # einen Fehler selbst werfen
        fehler = IndexError("Ist zwar kein IndexError, aber ich hatte Lust drauf :-D")
        raise fehler
    except:
        print("Yo ... Fehler")

    fehler = IndexError("V2: Ist zwar kein IndexError, aber ich hatte Lust drauf :-D")
    raise fehler

    print('Funktionsende')


# -------------------------------------------------------------------

def fehler():
    fehler_v1()
    print("-------------")
    fehler_v2()
    print("-------------")
    try:
        fehler_v3()
    except:
        print("Fehler ist aufgetreten")

    print("-------------")

    try:
        x = 1 / 1
    except:
        print("Fehler")
    else:
        print("Kein Fehler")
    finally:
        print("Egal, ob Fehler oder nicht")


# -------------------------------------------------------------------
def datum():
    from datetime import datetime, date, timedelta
    jetzt = datetime.now()
    print("(01)", jetzt)
    print("(02a)", jetzt.day)
    print("(02b)", jetzt.month)
    print("(02c)", jetzt.year)

    kursstart = date(2022, 11, 28)
    print("(03) Kursstart:", kursstart)
    print(f"(04) {kursstart.day}.{kursstart.month}.{kursstart.year}")

    # auf den Kursstart eine Zeitspanne von 3 Wochen und 4 Tagen rechnen
    kursende = kursstart + timedelta(weeks=3, days=4)
    print(f"(05) {kursende.day}.{kursende.month}.{kursende.year}")


# -------------------------------------------------------------------

def datum():
    from datetime import datetime, date, timedelta
    jetzt = datetime.now()
    print(f"(01) {jetzt}, typ = {typ(jetzt)}")
    print("(02a)", jetzt.day)
    print("(02b)", jetzt.month)
    print("(02c)", jetzt.year)

    kursstart = date(2023, 1, 30)
    print("(03) Kursstart:", kursstart)
    print(f"(04) {kursstart.day}.{kursstart.month}.{kursstart.year}")

    # auf den Kursstart eine Zeitspanne von 3 Wochen und 4 Tagen rechnen
    kursende = kursstart + timedelta(weeks=3, days=4)
    print(f"(05) {kursende.day}.{kursende.month}.{kursende.year}")


# -------------------------------------------------------------------

if (__name__ == "__main__"):
    # rekursionen()
    # fehler()
    datum()


anzahl = 0

def fibonacci(n):
    global anzahl
    anzahl += 1
    if n < 1:
        raise ValueError("Nur n >= 1 erlaubt!")
    elif n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def myinput(s):
    back = 0
    eingabe_ok = False
    while (not eingabe_ok):
        try:
            back = int(input(s))
            eingabe_ok = True
        except:
            eingabe_ok = False
            print("Das hat nicht funktioniert. Bitte nochmal versuchen!")


def BMI():
    gewicht = myinput("Dein Gewicht in kg: ")
    groesse = myinput("Deine Größe in cm:  ")

    # es wird die Größe in m benötigt
    groesse = float(groesse) / 100

    bmi = float(gewicht) / (groesse ** 2)

    # die Initialisierung der Variablen ist zwar nicht nötig, aber sinnvoll.
    kategorie = ""

    if (bmi < 18.5):
        kategorie = "Untergewicht"
    elif (bmi < 25):
        kategorie = "Normalgewicht"
    elif (bmi < 30):
        kategorie = "Übergewicht"
    else:
        kategorie = "Adipositas"

    print("Dein BMI: " + str(bmi) + " (" + kategorie + ")")


if __name__ == "__main__":
    # 9,227,465, anzahl = 18,454,929 Aufrufe der Funktion
    # print(f"{fibonacci(30):,d}, anzahl = {anzahl:,d} Aufrufe der Funktion")
    BMI()