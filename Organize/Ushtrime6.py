# Definicionet apo funksionet (metodat)

def printimi():
    print("Ky mesazh vije nga nje funksion")
    
printimi()

import math as m

def teorema_e_pitagores(a,b):
    a = a ** 2
    b = b ** 2
    c = a + b
    print(m.sqrt(c))

teorema_e_pitagores(6,4)

# Variabla lokale dhe ajo globale

def local_var_function(x,y):
    formula_implicite = 2*x + y # local variable inside the function
    print(f"Drejteza e ka nje shume prej : {formula_implicite}")

local_var_function(5,9)


def global_var_function(value):
    global kontradiksion
    kontradiksion = value and True
    print(f"A eshte kontradiksion : {kontradiksion}")
    
global_var_function(True)    


def fuck_you():
    
    pass # parandalon errorat prej blloqeve me kode te zbrazeta.

fuck_you()

# Funksionet arbitrare me shume parametra

def funksionArb(*emrat):
    my_list = [emrat]
    for emer in my_list:
        print(emer)
        
funksionArb("Agon","Leart","Besim","Bahri")


