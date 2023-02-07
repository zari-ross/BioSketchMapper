import math


def listen():
    ungerade = []
    for i in range(3, 21, 2):
        ungerade.append(i)
    print(f"Ungerade liste {ungerade}")
    print(f"List length {len(ungerade)}")
    print(f"5th element {ungerade[5]}")

    gerade = list()
    gerade = list(range(2, 7, 2))
    print(f"Gerade liste {gerade}")

    liste = gerade
    liste.append(math.pi)
    liste.append("Python")
    liste.append(ungerade)
    print(f"Liste {liste}")

    # Eine Liste ist nicht typenrein (wie alle Variablen in Python).
    for i in range(0, len(liste)):
        elmnt = liste[i]
        typ_elmnt = str(type(elmnt))
        # print(typ_elmnt)
        print(f"Liste[{i}] = {elmnt}, Typ: {typ_elmnt[8:-2]}")

    for e in liste:  # braucht
        print(f"{e}")

    liste.insert(3, "More stuff")
    liste.insert(-4, "And this stuff from the other side")
    liste.insert(-7777, "And this position number is too small so 0")
    print(f"Liste {liste}")
    liste.pop(5)
    print(f"Liste mit gelöschtem Element {liste}")


def main():
    listen()


from random import randint, seed
import time

# seed(20230207)

def zufall():
    zahl = randint(1, 100)  # Grenzen sind INKLUSIV
    print(zahl)


def lottoziehung(inp):
    liste = []
    while len(liste) != inp:
        zahl = randint(1, 49)
        if zahl not in liste:
            liste.append(zahl)
    liste.sort()
    return liste

def jackpotknacker(inp):
    tipp = lottoziehung(inp)
    print(tipp)
    tipp_check = []
    counter = 0
    while tipp != tipp_check:
        tipp_check = lottoziehung(inp)
        counter += 1
    print("Gefunden!", counter, "Ziehungen sind nötig")


if __name__ == '__main__':
    # main()
    # zufall()
    # print(lottoziehung())

    start_time = time.time()
    jackpotknacker(4)
    print("time elapsed: {:.2f}s".format(time.time() - start_time))

    start_time = time.time()
    jackpotknacker(5)
    print("time elapsed: {:.2f}s".format(time.time() - start_time))

    start_time = time.time()
    jackpotknacker(6)
    print("time elapsed: {:.2f}s".format(time.time() - start_time))
