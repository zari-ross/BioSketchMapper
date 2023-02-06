import colorama
from colorama import Fore
lcm = input('Deine Größe in cm: ')
try:
    float(lcm)
    if 30 < float(lcm) < 300:
        l = float(lcm)*0.01
        m = input('Dein Gewicht in kg: ')
        try:
            float(m)
            if 30 < float(m) < 300:
                m = float(m)
                calc_BMI=m/(l**2)
                print("%.2f" % calc_BMI)
            else:
                print(Fore.RED + "Prüf die Eingabe und Maßeinheit") 
        except:
            print(Fore.RED + "Schlechter Eingangswert") 
    else:
        print(Fore.RED + "Prüf die Eingabe und Maßeinheit") 
except:
    print(Fore.RED + "Schlechter Eingangswert")