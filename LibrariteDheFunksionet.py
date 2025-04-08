
## Funksionet e librarive ne Python 
# Python-i perkrahe disa zhvillime te funksonieve te cilat perdoren 
# drejtperdrejt ne programin e juaj. Pra, ne disa raste ne nuk kemi nevoje te krijojme
# nje funksion por vetem e thirrim ate, do te thote e therrasim librarine 

# Disa nga funksionet e librarise jane : 
# 1. print() - printon apo shfaq stringun brenda thonjezave
# 2. sqrt() - kthen rrenjezimine e nje numri 
# 3. pow() - kthen fuqizimin e nje numri
# etj.

# Keto funskione te librarise jane te definuara brenda modulit, 
# prandaj per t'i perdorur ato ne duhet te perfshijme modulin ne programin tone.
 
# Funksioni SQRT dhe POW

import math # importon librarin Math

rrenjezimi = math.sqrt(81) # Deklarojme variablen per rrenjezim
print("Rrenja katrore e numrit 81 eshte :",rrenjezimi)

fuqizimi = math.pow(5,2)
print("Vlera e numrit 5 te rritur ne katror eshte : ",fuqizimi)

# Funksioni me argumente ne Python
# Nje argument ne programim eshte nje vlere (value) qe eshte e qasshme nga nje funksion.

def mbledhja(a,b):
    S = a + b
    print("Shuma S =",S)

mbledhja(1,2)    

# Funksion me shkronja ne argumente 

def stringjet(emri, mbiemri):
    print('Emri i studentit : ',emri)
    print('Mbiemri i studentit :',mbiemri)

stringjet(emri='Agon',mbiemri='Ramadani')

# Funksioni ne Python me Argumente Arbitrare
# Ndonjeher kemi nevoje qe mos te dijme numrin e arg. 
# qe do te kalohen neper funksion. Ne kete rast en perdorim arg. arbitrar
# per ta bere duhet te perdoret shenja * para parametrit.

# Nje program per gjetjen e shumes se shume numrave 

def funksioniArbitrar(*numrat): # Pranon shume vlera per nje variabel, asteriksi(*) i vendosur tregon se kemi all apo te gjitha 
    rezultati = 0
    for nr in numrat:
        rezultati += nr
    print("Shuma = ",rezultati)

# Funksioni therret tri argumente
funksioniArbitrar(1,2,3)

# Funksioni therret dy argumente
funksioniArbitrar(5,3)


# Rekurzioni 
# Rekurzioni eshte proces i definimit te ndonje gjeje ne kuptimin e vet saj.
# Ne Python, ekziston mundesia e qe nje funksion therret 
# funksione te tjera, me kete edhe thirrjen e vetvetes.

# Le te kalkulohet faktorieli i nje numri, qe eshte produkt i te gjithe
# numrave integjer nga 1 deri tek ai numer, psh: 6! = 6*5*4*3*2*1 = 720
# Zakonisht ne Python limiti i funksionit maksimal rekurziv eshte 1000
# Ne raste tjera kemi, RecursionError.

def faktorieli(x):
    """Ky funksion eshte rekurziv pasi 
    qe per te gjetur faktorielin 
    therret vetveten.
    """
    if x == 1:
        return 1
    else:
        return (x * faktorieli(x-1))
numri = 6
print("Faktorieli i numrit",numri,"eshte", faktorieli(numri))

# Funksioni anonim ne Python
# nje lloj specifik i funksionit ne Python eshte funksioni anonim apo 
# "LAMBA", i cili punon pa emer.

# lambda:print("Hello people!")

per = lambda : print("Hey there")

per() # Dieses ist ein fuktionen


# Variablat lokale, globale dhe nonlocal variable lexoni me heret!!!

# Global keyword
# Ne Python global keyword lejojne qe te modifikoni variablat e jashtme te skopit aktual.

# Qasja dhe modifikimi i variables globale 

# -------------------------------------------------------------
b = 11 # variabel globale

def shto():
    # b = b + 2 -- aktualisht nuk mund ta ndryshojme variablen globale nga brenda 
    # per ta ndryshuar ate veprojme keshtu:

    global b
    b = b + 2
    print(b)

shto()   

# Kete munde ta realizojme edhe me ane te funksionit Nested()

def funksioni_i_jashtem():
    nr = 22
    def funksioni_i_brendshem():
        global nr 
        nr = 33
    print("Para se te thirret funksioni i brendshem :",nr)
    funksioni_i_brendshem()
    print("Pas thirrjes se funksionit te brendshem :",nr)

funksioni_i_jashtem()
print("Pas thirrjes se dy funksioneve: ",nr)

#Importimi i librarive (modulet)

import math

print("Vlera e numrit PI eshte",math.pi)

# Kur importojme librari/module ne Python, ato ne programin tone munde t'i riemertojme, p.sh:

import math as m

print(m.pi)

# Importimi i statement ne modul (librari)

from math import pi

print(pi)

# Importimi i te gjithe statements nga libraria e caktuar

from math import*

print("Pi ka vleren : ",pi)

#--------------------------------------------------------

# Perdorimi i funksionit dir()

# z = 1
# t = "Pershendetje"
# import math

# dir()
# ['z','t','math']

# --------------------------------------------------------

# Nje pakete eshte konteiner qe permban nje variacion te funksioneve te 
# funksioneve per nje performim te nje pune specifike.

# Psh: Paketa math permban funksionin sqrt() per te performuar 
# kalkulimin e rrenjezimit te nje numri 
