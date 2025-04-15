# Shembulli 1
class Personi1: # Deklarimi i klases
    def __init__(self, emri, mosha): # Deklarimi i funksioni iniciues me dy argumente
        self.emri = emri #Inicimi i argumentit te pare
        self.mosha = mosha #Inicimi i argumentit te dyte
    def paraqitja(self): # Deklarimi i funksionit per paraqitje te te dhenave
        print("Pershendetje une jam", self.emri,"dhe jam",self.mosha,"vjeçar.") # Printimi nga funksioni i dyte
         #Atributet e objektit jan inicuar ne konstruktor, i cili eshte nje procedure specifike me emrin  __init_
        
# # Krijojme nje instance dhe perdorime ate.        
personi = Personi1("Filani Fisteku",20)

personi.paraqitja()

# Shembulli 2

class Personi:
    count = 0 # Variabel e klases
    def __init__(self, emri, mosha): 
        self.emri = emri # Eshte nje variabel instance
        self.mosha = mosha 
        Personi.count += 1 # Duke i dhene vlere me ane te emrit te klases.
 
personi1 = Personi("Filan",27)
personi2 = Personi("Filane",25)
print(Personi.count)
print(personi1.emri)
print(personi2.emri)

# Detyra 3

# Klasa per kalkulime matematikore

import math as m

class Qarku:
    def __init__(self,rrezja):
        self.r = rrezja
    def kalkulo(self):
        return round(m.pi * self.r ** 2,2)
    
    def paraqitja(self):
        print("Siperfaqja e rrethit me rreze",self.r,"eshte",self.kalkulo())
        
qarku = Qarku(9)
qarku.paraqitja()
    # Perdore shembulli 1 ose 2 per te paraqitur rezultatin
    
    # Detyra 4 : Krijimi i disa objekteve ne Python
    
class Punonjesit:
    # definojme nje veti te punonjesit
    punonjesi_id = 0
    count = 0
    def __init__(self):
        Punonjesit.count += 1
        
# Krijojme objektet 
punonjesi1 = Punonjesit()

 # Krijojme qasjen ne vetit e punonjesve te klases
punonjesi1.punonjesi_id = 1489
print(f"Punonjesi i {Punonjesit.count} ID : {punonjesi1.punonjesi_id}")

punonjesi2 = Punonjesit()

punonjesi2.punonjesi_id = 1490
print(f"Punonjesi ID {Punonjesit.count} :{punonjesi2.punonjesi_id}")

punonjesi3 = Punonjesit()

punonjesi3.punonjesi_id = 1491
print(f"Punonjesi ID i {Punonjesit.count} : {punonjesi3.punonjesi_id}")

punonjesi4 = Punonjesit()

punonjesi4.punonjesi_id = 1492
print(f"Punonjesi ID i {Punonjesit.count} : {punonjesi4.punonjesi_id}")


# Detyra 5

class Detyra:
    # Atributet e klases
    emri = ""
    mosha = 0
    
prs1 = Detyra()

prs1.emri = "Agon"
prs1.mosha = 19

# Krijojme nje objekt tjeter

prs2 = Detyra()

prs2.emri = "Enis"
prs2.mosha = 80

# Qasja ne atribute 
print(f"{prs1.emri} eshte {prs1.mosha} vjeçar")
print(f"{prs2.emri} eshte {prs2.mosha} vjeçar")

# Detyra 6: Trashegimia (Inheritance)

# Trashegimia eshte nje menyre e krijimit te nje klase ekzistuese per te perdorure detajet e nje klase ekzistuese,
# duke mos e ndryshuar ate. Klasa e re eshte klase e derivuar nga klasa tjeter (klasa prind - parent class)


# Klasa parent (klasa bazë) 

class Shtazet:
    def Ushqehem(self):
        print("Une ha ushqim!")
    def Flej(self):
        print(self,"Une munde te flej.")
        
class Tigri(Shtazet):
    emriKafshes = "Tigri"
    def Vrapon(self):
        print("Une munde te vrapoj")

tigri1 = Tigri()

tigri1.Ushqehem()
tigri1.Vrapon()
tigri1.Flej()

# Enkapsulimi eshte nje veti e programimit te orientuar ne objekte, qe i referohet izolimit te atributeve dhe metodave
# brenda nje klase te vetme

class Kompjuteri:
    def __init__(self):
        self.maxCmimi = 1000
    def shitja(self):
        print("Cmimi i shitjes: {}".format(self.maxCmimi))
    def setMaxCmimi(self, cmimi):
        self.maxCmimi = cmimi
        
kmp = Kompjuteri()

kmp.shitja()
# Ndryshojme cmimin 
kmp.maxCmimi = 1200

kmp.shitja()

kmp.setMaxCmimi(1200)
kmp.shitja()

# Polimorfizmi 
# Eshte njera nga shtyllat e OOP qe mundeson qe te kemi me shume se nje forme te prezantimit.
# Pra, mundeson performimin e operimeve te ndryshme ne skenar te ndryshem.

# Detyra 8 apo cilado me radhe 

class Poligoni:
    def krijimi(self):
        print("Poligoni u krjua")
        
class Siperfaqja(Poligoni): 
    def krijimi(self):
        print("Siperfaqja u krijua")

class Qarku(Poligoni):
        def krijimi(self):
            print("Qarku/Rrethi u krijua")
            
# Krijimi i objektit per siperfaqe

siperfaqja = Siperfaqja()

siperfaqja.krijimi()

# Krijojme objektin per qarkun 

rrethi = Qarku()
rrethi.krijimi()