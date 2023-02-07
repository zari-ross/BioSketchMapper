from W1T4_while_Funktionen_Nataliya import umdrehung, leerzeichen_entfernen, ziffern_zahlen, trimmen, check_prim

def menu_func(inp):
    print("W2T1")
    eingabe = -1
    while int(eingabe) != 0:
        print(
            f' 1 ... umdrehen \n 2 ... leerzeichen_entfernen \n 3 ... ziffern_zahlen \n 4 ... trimmen \n 0 ... beenden ')
        eingabe = input(inp)
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
        print("---->", out, "<----", sep="")
    return "End"

def prim_bis_10000():
    for i in range(0, 10001):
        if check_prim(i):
            print(f"{i:25,d}")

def primzahlen():
    max = 10_000
    laenge = len(str(max)) + 4

    for i in range(0, max + 1):
        if check_prim(i):
            print(f"{i:{laenge},d}", end = '')

if (__name__ == "__main__"):

    print("Das ist Hauptprogramm:", __name__)

    # x = menu_func("Auswahl: ")
    # print("Ergebnisse:", x)

    # prim_bis_10000()
    primzahlen()


def main():
    eingabe = -1
    prim_max = 10000

    help = (f"{prim_max}").replace(',','.')

    while int(eingabe) != 0:
        print(
            f' 1 ... umdrehen \n 2 ... leerzeichen_entfernen \n 3 ... ziffern_zahlen \n 4 ... trimmen \n 0 ... beenden ')
        eingabe = input(inp)
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
        print("---->", out, "<----", sep="")
    return "End"
