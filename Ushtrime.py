# Ushtrimi 1 - Multistring

stringA ="""
Ky
eshte 
stringu 
im
dhe 
ai 
eshte
shume linjesh 
"""

# Ushtrimi 2 - Selektimi indeksor i stringut

stringB = "Agon"

indeksi_I = stringB[0]
indeksi_II = stringB[1]
indeksi_III = stringB[2]
indeksi_IV = stringB[3]

# Ushtrimi 3 - Manipulimi i stringut me ane te indeksit

stringC = "MyString"

shtoMeIndeks = stringC[:1] +"hey"+ stringC[2:]

# Ushtrimi 4 - Tipet e te dhenave ndryshojne ne menyre dinamike 

x = 2
y = "Hello!"

#--------------------------

x = "Hello!"
y = 2

# Ushtrimi 5 - Inicializimi i variablave "njekohesisht"

a ,b ,c ,d = "My", "age", "is", 19

# Printimi i njekohshem i variablave

# print(a,b,c,d)

# Ushtrimi 6 - Vargjet

Vetura = ["BMW", "Audi", "Mercedes", "Renault"]

k, l, m, n = Vetura

# Ushtrimi 7 - variablat dalese

fjala1 = "Python"
fjala2 = "eshte"
fjala3 = "gjuhe"
fjala4 = "programuese"

fjalia = [fjala1,fjala2,fjala3,fjala4]

# print( fjala1,fjala2,fjala3,fjala4)

# print(fjala1+fjala2+fjala3+fjala4)




def fjaliaMeVetura():
    global Une
    Une = "Agon"
    for i in Vetura:
        for j in fjalia:
            print(i,j)
            ti = 2


fjaliaMeVetura()

print(Une)