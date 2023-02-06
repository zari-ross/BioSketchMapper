#!/usr/bin/env python
# coding: utf-8

# # W1T4 while Funktionen


# ## Übung 1

# %%time
def umdrehung(inp):
    pni = inp[::-1]
    print(inp, "\n", pni, sep="")
umdrehung("Josef")

# %%time
inp = "Josef"
i = len(inp)-1
npi = ""
while i > -1:
    #print(inp[i])
    npi = npi + inp[i]
    i -= 1
print(npi)


# ## Übung 2

# %%time
import re
re.sub(' ', '', "Python     ist   toll  ") #, count=1

# %%time
inp = "Python     ist   toll  "
def leerzeichen_entfernen(inp):
    i = 0
    out = ""
    count = 0
    while i < len(inp):
        #print(inp[i])
        if inp[i] != " ":
            count += 1
            out = out + inp[i]
        i += 1
    return out


# ## Übung 3

# %%time
inp = "efwe78754we1e567wdw"
def ziffern_zahlen(inp):
    i = 0
    out = ""
    count = 0
    while i < len(inp):
    #     print(ord(inp[i]))
        if inp[i].isdigit(): # if 48 <= ord(inp[i]) <= 57:
            count += 1
            #out = out + inp[i]
        i += 1
    return count


# %%time
sum(c.isdigit() for c in inp)


# ## Übung 4
# A problem with empty line as input.

# %%time
class StopExecution(Exception):
    def _render_traceback_(self):
        pass

def weirderst_trim(inp):
    i = 0
    out1 = ""
    out2 = ""
    if ((inp[0] != " ") and (inp[len(inp)-1] != " ")):
        out2 = inp
    elif inp[0] == " ":
        while (i != len(inp)-1) and ((inp[i] == " ")):
            i += 1
        if i == len(inp)-1:
            print("empty", sep="")
            raise StopExecution
        while i < len(inp):
            out1 = out1 + inp[i]
            i += 1        
        if inp[-1] == " ":
            j = len(out1)-1 
            while out1[j] == " ":
                j -= 1
            while j >= 0:
                out2 = out1[j] + out2
                j -= 1       
        else:
            out2 = out1
    elif inp[-1] == " ":   
        j = len(inp)-1 
        while inp[j] == " ":
            j -= 1
        while j >= 0:
            out2 = inp[j] + out2
            j -= 1     
    print("check", out2, "check", sep="")
    
weirderst_trim("33333")
weirderst_trim("   33333     ")
weirderst_trim("   33333")
weirderst_trim("33333   ")
weirderst_trim("   ")

# %%time
def trimmen(inp):
    while ((len(inp) > 0) and (inp[0] == " ")):
        inp = inp[1:]
    while ((len(inp) > 0) and (inp[-1] == " ")):
        inp = inp[:-1]
    return inp
trimmen("    Python     ist   toll    ")


("    Python     ist   toll    ").strip()


# ## Übung 5 Primzahlen
# Alle Verschluessungsalgorithmen funktionieren mit Primzahlen. See RSA-Verschlüsselung.
# Um schneller zu machen, wir koennen sehen ob die Zahl gerade ist.

# wert = int(input('Wert zu Überprüfung: '))
def check_prim(wert):
    i=wert
    count = 0
    while i > 0:
        if wert%i == 0:
            count += 1
        i -= 1 
    print(count)
    if count == 2:
        return True
    else:
        return False

print(check_prim(59))


# better
# wert = int(input('Wert zu Überprüfung: '))
def check_prim(wert):
    i=wert
    count = 0
    while i > 0:
        if wert%i == 0:
            count += 1
        i -= 1 
    print(count)
    if count == 2:
        ist_prim = True
    else:
        ist_prim =  False
    return ist_prim

print(check_prim(59))

