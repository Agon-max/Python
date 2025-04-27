# Klasat

class Person:
    def __init__(self, emri, mosha):
        self.emri = emri
        self.mosha = mosha
        
    def paraqitja(self):
        print(f"Pershendetje une jam : {self.emri}.")
        print(f"Kam {self.mosha} vjeç.")

person1 = Person("Agoni", 19)

person1.paraqitja()

class Gota:
    count = 0
    def __init__(self, perberja):
        self.perberja = perberja
        Gota.count += 1
        
    def shprehu(self):
        print(f"Gota e juaj eshte perbere nga {self.perberja}")

gota1 = Gota("Qelqi")
gota1.shprehu()

gota2 = Gota("Plastika")
gota2.shprehu()

print(f"Deri me tani ju keni krijuar {Gota.count} objekte per gota!")


class Rrobat:
    count = 0
    def __init__(self, tipi, ngjyra, fabrika):
        self.tipi = tipi
        self.ngjyra = ngjyra
        self.fabrika = fabrika
        Rrobat.count += 1
    
    def Merr_Tipin(self):
        return self.tipi
    
    def Merr_Ngjyren(self):
        return self.ngjyra
    
    def Merr_Fabriken(self):
         return self.fabrika

    def Merri_Te_Gjitha(self):
        print(self.Merr_Tipin(), self.Merr_Ngjyren(), self.Merr_Fabriken())
        
        
rr = Rrobat("Xhamper","Bardhe","Mendafshi")

rr.Merri_Te_Gjitha()
    