# Encapsulation

class Kompjuteri:
    def __init__(self,cmimi):
        self.__cmimi = cmimi
    
    def get_price(self):
        return self.__cmimi
    
    def set_price(self, unik_cmimi):
        self.__cmimi = unik_cmimi
    
    
kmp = Kompjuteri(1000)

kmp.set_price(1500)
print(kmp.get_price())


# Trashegimia

class Vetura:
    def __init__(self, emri, viti):
        self.emri = emri
        self.viti = viti
    
    def vozis(self):
        print(f"Po vozise me {self.emri}")
        
    def prodhimi(self):
        print(f"Viti i prodhimit : {self.viti}")
        

class BMW(Vetura):
    
    def ul_dritaren(self):
        print("Dritarja po ulet")

vetura_ime = BMW("BMW", 2025)

vetura_ime.ul_dritaren()
vetura_ime.vozis()
vetura_ime.prodhimi()

# Polymorphism

class Poligoni:
    def krijimi(self):
        print("Poligoni u krijua")

class Siperfaqja(Poligoni):
    def krjimi(self):
        print("Siperfaqja u krijua")
        
class Qarku(Poligoni):
    def krijimi(self):
        print("Qarku u krijua!")  
        
qarku = Qarku()

qarku.krijimi()  


# Shume klase inheritojne nga nje klase dhe mbishkruajne njeren nga metodat qe ajo ka.
