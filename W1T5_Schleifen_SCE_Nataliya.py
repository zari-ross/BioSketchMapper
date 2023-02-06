

def gib_bool(b):
    print(b)
    return b

def short_circuit_evaluation():
    print("(01) Resultat:", gib_bool(True) and gib_bool(False), "\n")
    print("(02) Resultat:", gib_bool(False) and gib_bool(True), "\n")
    print("(03) Resultat:", gib_bool(True) or gib_bool(False), "\n")
    print("(04) Resultat:", gib_bool(False) or gib_bool(True), "\n")
    
# short_circuit_evaluation()


# ## while-Schleifen
# Jede Schleife kann - unabhängig von ihrer Bedingung - beendet werden. \
# Ein Abbruch wird durch die Anweisung "break" verursacht. Dadurch wird die Schleife
# mit sofortiger Wirkung beendet und die nächste Anweisung nach der Schleife ausgeführt.\
# Soll aber die Schleife nicht beendet werden, sondern alle weiteren Schritte
# im Schleifenkörper übersprungen werden, dann bietet sich die Anweisung
# "continue" an. \
# Durch "continue" wird zum Schleifenkopf zurückgekehrt.

def while_schleifen_v2():
    x = 0
    while(x < 10):  # do not write "while(True)", *grusel*
        x += 1
        
        if (x % 2 == 0):
            continue
        print(x)    
        if (x >= 5):
            break

# while_schleifen_v2()


# innen = aussen = 1;
# while (aussen <= 5):
#     while (innen <= 4):
#         print("a = ", aussen, ", i = ", innen, sep="")
#         if (innen == 3):
#             break
#         innen += 1
#     aussen += 1
#     innen = 1


# #### "Mädchen"-Code
# https://www.zeit.de/zustimmung?url=https%3A%2F%2Fwww.zeit.de%2Fonline%2F2008%2F17%2Fschoener_code

# ## for-Schleifen

# for i in range (5, -5, -2):
#     print(i)


# ## Formatting output
#
# s = "wdweKKKJhy Ggy hih eedw"
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.capitalize())


# ## Übung
# Es ist eine Funktion zu schreiben, die "input_int" heißt. Diese Funktion verhält sich wie "input", ist aber darauf ausgelegt, einen int-Wert einzulesen und keine Ruhe zu geben, bis ein korrekter int-Wert eingegeben wurde. Diese Funktion darf keinen Fehler werfen, falls eine fehlerhafte Eingabe vorgenommen wird.
# Diese Funktion ist mit den Mitteln, die bisher behandelt wurden, realisierbar.
# 
# Code:
# -----
# 
# def input_int(s : str) -> int:
#    ...
#    ...
# 
# x = input_int("Zahl eingeben: ")
# print("Deine Eingabe ist:", x)
# 
# So soll es laufen:
# ------------------
# Zahl eingeben: abc\
# Das hat nicht funktioniert, bitte nochmal versuchen!\
# Zahl eingeben: 13abc\
# Das hat nicht funktioniert, bitte nochmal versuchen!\
# Zahl eingeben: 13\
# Deine Eingabe ist: 13


def input_int(inp : str) -> int:
    if inp.isdigit():
        print("Deine Eingabe ist:", inp)
    else:
        print("Das hat nicht funktioniert, bitte nochmal versuchen!") 

# input_int("abc")
# input_int("13abc")
# input_int("13")





def input_int(inp : str) -> int:
        eingabe = input(inp)
        while not eingabe.isdigit():
            print("Das hat nicht funktioniert, bitte nochmal versuchen!")
            eingabe = input(inp)
        return eingabe

# x = input_int("Zahl eingeben: ")
# print("Deine Eingabe ist:", x)


def BMI():
    l = input('Deine Größe in cm: ')
    while not l.isdigit():
        print("Das hat nicht funktioniert, bitte nochmal versuchen!")
        l = input('Deine Größe in cm: ')
    m = input('Dein Gewicht in kg: ')
    while not m.isdigit():
        print("Das hat nicht funktioniert, bitte nochmal versuchen!")
        m = input('Dein Gewicht in kg: ')
    calc_BMI = int(m) / ((int(l)*0.01) ** 2)
    return calc_BMI

# x = BMI()
# print("Deine BMI:", "%.2f" % x)


def input_int_best(inp: str) -> int:
    eingabe = input(inp)
    while ((not eingabe.isdigit()) and (not (eingabe[1:].isdigit() and eingabe[0] == "-"))):
        print("Das hat nicht funktioniert, bitte nochmal versuchen!")
        eingabe = input(inp)
    return eingabe

# x = input_int_best("Zahl eingeben: ")
# print("Deine Eingabe ist:", x)

if (__name__ != "__main__"):
    print("Diese Zeile wird gelaufen wenn zugegriffen nicht aus main:", __name__)
