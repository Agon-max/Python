# Funksionet ne Python
#Nje funksion ne Python i cili kryen nje 
# pune specifike
# P.SH. : Le te themi se kemi nevoje te krijojme nje program i cili krijon nje rreth 
# dhe e ngjyros ate. Ketu duhet te krijojme dy funksione/metoda per te zgjidhur kete problem.

# Ato jane : Funksioni qe krijon rrethin dhe tjetri qe vendos ngjyren e tij
# Pra, zgjidhja e problemeve me komplekse behet, duke ndare problemin ne pjese me te vogla 
# qe mundesojn kuptimin dhe programimin me te lehte te problemit dhe zgjidhjes se tij.

# Struktura e nje funksioni ne Python eshte :
def pershendetje(): # def - eshte fjala qe krijon funksionin, pershendetje(): emri i funksionit
    print("Pershendetje te gjithe juve!") # Trupi i funksionit

# pershendetje() # Thirrim funksionin
# print("Pershendetje nga jashte funksioni!")

# Funksioni me argument ne Python 
def hello(Emri):
    print("Miredita",Emri)

# hello("Agon")   


def mbledh(arg1, arg2):
    Shuma = arg1 + arg2
    print("Shuma e llogaritur eshte",Shuma)


# mbledh(150,9999)

# Detyre Ushtrimi: Gjeje Prodhimin e numrit P nga 1 deri ne 10, duke definuar 
# nje metode me emrin Prodhimi 

def Prodhimi():
    global P 
    P = 1
    for i in range(1,11):
        P = P * i
    print(P)      

# Prodhimi()        


# y = 2x+P/C, Nese P eshte 


def funksionY(x, c):
    P = 1
    for i in range(1,11):
        P = P * i
    y = 2 * x + P/c
    print(y)  


funksionY(10, 2)     

# Statement RETURN 
# Ne kthejme nje vlere nga funksioni duke perdorur gjendjen STATEMENT

def siperfaqjaEKatrorit(brinja):
    Siperfaqja = brinja * brinja
    return Siperfaqja

katrori = siperfaqjaEKatrorit(5)
print("Siperfaqja e katrorit eshte: ", katrori,"m2")


def siperfaqjaEDrejtekendshit(brinjaA,brinjaB):
    Siperfaqja = brinjaA * brinjaB
    return Siperfaqja

drejtkendeshi = siperfaqjaEDrejtekendshit(5,5)
print("Siperfaqja e drejtkendeshit eshte: ", drejtkendeshi,"m2")

def siperfaqjaETrekendeshit(brinjaA,brinjaB):
    Siperfaqja = (brinjaA * brinjaB)/2
    return Siperfaqja

trekendeshi = siperfaqjaETrekendeshit(5,3)
print("Siperfaqja e trekendeshit eshte: ", trekendeshi,"m2")


# Statement PASS
# Statement PASS sherben si nje mbajtje per kodin ne te ardhmen, per te 
# parandaluar errors prej blloqeve me kode te zbrazeta (EMPTY)

def funksioniNeZhvillim():

    pass
# Kjo ekzekutohet jashte çdo aksioni ose jashte çdo errori
funksioniNeZhvillim()
