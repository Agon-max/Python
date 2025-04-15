# Perjashtimet jane ngjarje te paparashikueshme munde te ndodhe gjate ekzekutimit te kodit
# dhe japin rezultat te gabuar ose nderpresin programin. PSH. : Pjestimi me zero

# Forma bazike e perjashtimit ne Python realizohet keshtu:

# try:
    # Pjesa e kodit qe munde te ket perjashtim
# except
    # Pjesa e kodit qe ekzekutohet nese ndodh gabimi

# Detyra 1 (Metoda 2) : Exception = pjestimi me numrin zero

try:
    numeruesi = 10
    emruesi = 0
    rezultati = numeruesi / emruesi
    print(rezultati)
except ZeroDivisionError:
    # print("You cannot divide by zero!")
    print("Dividing by zero exception!")

# Detyra 2 : New Exception
try:
    numri_cift = [2,4,6,8,10]
    print(numri_cift[6])
except:
    print("You are trying to access a non existent index in the list!")
    
    
    
try: 
    nr = int(input("Jepe nje numer cift:"))
    assert (nr % 2) == 0
except :
    print("Numri qe ju dhate eshte cift")
else:
    rezultatiPjestues = 1/nr
    print(rezultatiPjestues)   
    
# Blloku finally

try:
    nr1 = 10
    nr2 = 0 
    
    result = nr1/nr2
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("Successfully handled this exception!") 