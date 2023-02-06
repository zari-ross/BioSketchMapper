#!/usr/bin/env python
# coding: utf-8

# ## Aufgabe 1

#!pip install tabulate
from tabulate import tabulate

def table(): 
    ID = 12 # ID : int
    name = "Johann, Gambolputty" #ID : int
    alter = 38
    adresse = "Mühlenweg 1a, 24837 Schleswig"
    telefon = "04621 - 55 66 77"
    beruf = "Fachinformatiker"
    status = True
    lohnsteuerklasse = 2
    kinder = 2
    bruttolohn = 3800
    
    if status == True:
        statusname = "Verheiratet"
    else:
        statusname = "Ledig"
    
    #create data
    data = [["ID", ID], 
        ["name", name], 
        ["alter", alter], 
        ["adresse", adresse], 
        ["alter", alter],
        ["telefon", telefon], 
        ["beruf", beruf],
        ["statusname", statusname], 
        ["alter", alter],
        ["lohnsteuerklasse", lohnsteuerklasse],
        ["kinder", kinder],
        ["bruttolohn", bruttolohn]]
      
    #define header names
    col_names = ["Variablename", "Variable"]
    #display table
    print(tabulate(data, headers=col_names))

table()


# ## Aufgabe 2

def convert_to_str(n1):
    n2 = str(n1)
    return n2, type(n2)
def convert_to_float(t1):
    t2 = float(t1)
    return t2, type(t2)
def convert_to_int(b1):
    b2 = int(b1)
    return b2, type(b2)

print(convert_to_str(34.5))
print(convert_to_float(3))
print(convert_to_float("388"))
print(convert_to_float("55.55"))
print(convert_to_int("12"))
print(convert_to_str(12))


# ## Aufgabe 3

def func_rest(n1, n2):
    print(n1 % n2)
func_rest(123, 7)
func_rest(12345, 100)
func_rest(121, 11)
func_rest(10, 2)
func_rest(11, 2)
func_rest(12, 2)
func_rest(1, 2)

print("\n")
def func_mod(n1, n2):
    print(n1 // n2)
func_mod(123, 7)
func_mod(12345, 100)
func_mod(121, 11)
func_mod(10, 2)
func_mod(11, 2)
func_mod(12, 2)
func_mod(1, 2)


# ## Aufgabe 4
# Fun way where the operations are in a string to see the id 

def myfunc(x):
    x += 12 #24
    print(x, id(x))
    x -= 12 #12
    print(x, id(x))
    x /= 12 #1
    print(x, id(x))
    x %= 12 #1
    print(x, id(x))
    x = ((x + x) - (x * 2) / 4) # 2-2/4 
    print(x, id(x))
myfunc(12)


# ## Aufgabe 5

x1 = True
x2 = False
print(x1 and x2)
print(not x1 or x2)
print(not x1 and not x2)
print((x1 or x2) and (not x1 and x1))


# ## Aufgabe 9

hh = int(input('Stunden: '))
mm = int(input('Minuten: '))
ss = int(input('Sekunden: '))

if hh <10:
    hh_show = "0" + str(hh)
else:
    hh_show = hh
if mm <10:
    mm_show = "0" + str(mm)
else:
    mm_show = mm
if ss <10:
    ss_show = "0" + str(ss)
else:
    ss_show = ss

sec = hh*60*60 + mm*60 + ss
print("Die Zeitangabe")
print(hh_show,mm_show,ss_show, sep = ":")
print("Uhr beträgt in Sekunden")
print(sec)


# ## Aufgabe 10

preis_rot = 12.99
preis_rose = 9.98
preis_weis = 11.99

rot = int(input('Anzahl Rotwein: '))
rose = int(input('Anzahl Rosewein: '))
weis = int(input('Anzahl Weiswein: '))

gesamt = preis_rot * rot + preis_rose * rose + preis_weis * weis

print("Die Gesamtkosten betragen:", gesamt, "Euro")

