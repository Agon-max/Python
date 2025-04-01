# Perseritje me tipet te te dhenave 
stringA = """ Ky eshte nje string me shume rreshtesh
Rreshti1
Rreshti2
Rreshti3
Rreshti4
Rreshti5 
 """

# print(stringA)


# # Selektimi i karaktereve brenda stringut
# stringC = "Jemi ne ore te Python"
# print(stringC[1],stringC[2],stringC[5])

# # Ndryshimi i karakterit me string
# myString = stringC[:2] + "5" + stringC[3:]

# print(myString)

# x = "Ramazani"
# y = 3
# print(x)

# x = 3
# y = "Python"
# print(x)
# print(y)

# Dhenia e shume vlerave per variabla

a, b ,c = "ariu", "balena", "cjapi"

# print(a,b,c)

a = b = c

# print(a, b, c)

veturat = ["BMW", "VolksWagen", "Range Rover", "Mercedes", "Audi"]

a,b,c,d,e = veturat

# print(a,b,c,d,e)

# Variablat dalese
x = "Python-i"
y = "eshte"
z = "gjuhe"
t = "e"
v = "bukur"
u = "programuese."

# print(x,y,z,t,v,u)
# print(x+y+z+t+v+u)

m = 10
n = "Python"

# Paraqet error kur dy tipe te ndryshme te te dhenave i mbledhim aritmetikisht
# print(m,n)

# Deklarimi i funksionit

def printimi(): # Definimi i funksionit dhe emertimi 
    print("Ky eshte nje funksion ne Python") # Trupi i funksionit

printimi() # Thirrja e funksionit metodes permes emrit te saj 

# Variablat globale ne Python
# Jane variabla jashte nje funksioni 
# Ato mund te perdoren nga çdokush, si brenda ashtu dhe jashte

x = "Python" # Variabla globale

def fmetoda():
    print("Lenda e jone quhet Programimi ne " + x)

# Printohet 
fmetoda()


# def fmetoda():
#     # I ndryshohet vlera
#     x = "logjike"
#     # print("Lenda e jone quhet Programimi ne " + x)

# fmetoda()

# print("Lenda e jone quhet Programimi ne " + x)

# Detyre 
# Kalkulo shumen e numrit 1 prej 1 deri ne 100, duke perdorur
# funksionin fShuma (10 min kohe)


# Deklarimi i variables globale brenda funksionit 
# Kur deklarojme variabel brenda nje metode/funksioni, atehere ajo 
# variabel quhet variabel lokale, sepse mund te perdoret vetem brenda funksionit ku eshte deklaruar

# Mirepo ne Python ne mund te deklarojme nje variabel lokale brenda metodes 
# dhe ta perdorim sikur nje variabel globale
# Kjo behet me ane te shprehjes "global"

def GinLfunksioni():
    global variablaLokale 
    variablaLokale = "Python"
    print("Gjuha programuese", variablaLokale)    

GinLfunksioni()
print("Gjuha programuese", variablaLokale)    
