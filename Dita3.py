# Ne kete fajll pershkruhet dita e trete ku kemi vazhdu me operatoret bitwise


#Operatoret Bitwise ne Python
#Operatoret Bitwise jane operator te cilat bejne operime ne ndryshim te bitave ne menyret bit per bit
#Operatoret Bitwise jane :
#Operatori Bitwise AND    &    p.sh x & y = 0 (0000 0000)
#Operatori Bitwise OR    |   psh. x | y (0000 1110)
#Operatori Bitwise Not   ~    psh. ~x = -11 (1111 0101)
#Operatori Bitwise XOR   ^    psh. x^y = 14 (0000 1110)
#Operatori Bitwise right shift  >>  x>>2 = 2 (0000 0010)
#Operatori Bitwise left shift   << x<<2  = (0000 1000)

z = 10
h = 4

# print("Operatori bitwise AND, z & h = ", z & h)
# print("Operatori bitwise OR, z | h = ", z | h)
# print("Operatori bitwise XOR, z ^ h = ", z ^ h)
# print("Operatori bitwise NOT, ~h = ", ~h)
# print("Operatori left shift z << 2 = ", z << 2)
# print("Operatori right shift z >> 2 = ", z >> 2)


# Operatoret Special ne Python:
# Pythn ofron disa tipe te operatoreve si "IDENTITY" dhe "MEMBERSHIP", qe njihen si operatore special
# Operatori Identity, perdoret per te kontrolluar pjesen e memories nese eshte e zene apo jo,
# kur dy vlera jane te alokuara ne te njejten pjese (vend). Kjo tregon (mundëson), që te na njoftoj se
# dy variabla me vlera te njejta nuk eshte e domosdoshme qe te jen identike.

# Operatori IS   (True - nese operatoret janë identik, referohen objektit te njejte).       p.sh. : x is True

#Operatori IS NOT   (True - nese operatoret nuk jan identike, nuk i referohen objektit te njejte).        p.sh. : x is not True

x1 = 10
y1 = 10

x2 = 'Tung'
y2 = 'Tung'

x3 = [0,1,2,3,4,5]
y3 = [0,1,2,3,4,5]

# print(x1 is  y1)
# print(x2 is not y2)
# print(x3 is not y3)
#
# print(x1 is not y1)
# print(x2 is y2)
# print(x3 is y3)

# Operatori MEMBERSHIP =>  perdore dy operand:  IN dhe NOT IN
# Behet testimi se vlera e variables eshte gjetur apo nuk eshte gjetur ne nje sekuence (string, list, tuple, set dhe dictionaries)
# Operatori IN :      True - nese vlera ose variabla eshte e gjetur ne sekuence  psh: 5 in a
# Operatori NOT IN :  True - nese vlera ose variabla nuk eshte e gjetur ne sekuence  psh: 5 not in a

fjalia = 'Sot po mesojme operatoret e ndryshem ne Python'
# print(fjalia)

# print('S' in fjalia)
# print('w' in fjalia)
# print('S' not in fjalia)
# print('Agon' in fjalia)
# print('w' not in fjalia)
#
# print('python' not in fjalia)
# print('Python' in fjalian)


# Loops
# Perdoren ne python per perseritje te aksioneve apo veprimeve ne menyre efikase
# Llojet : While, For, Netstad

# While loop

#Ne python while loop perdoret per te ekzekutuar nje blloke te perseritur te gjendjes perderisa
#te plotesohet nje kushtezim i dhene. Kur kushtezimi i dhene behet False, nderpritet ekzekutimi.

# variablaC = 0
# while(variablaC < 10):
#     variablaC = variablaC+1
#     print("Unaza While", variablaC)    
    
# # While i kombinuar me else    
# variablaC = 2
# while(variablaC < 10):
#     variablaC = variablaC+1
#     print("Unaza While", variablaC) 
# else:
#     print("Ne bllokun else")
    
# variablaD = 0
# while(variablaD == 0): # Ekzekutimi i bllokut ne menyre te pa limituar i pereritur (deri ne infinit)
#     print('Pershendetje')    

# Unaza/Loopa 'for' (for loop)
# Perdoret per ezekutime te nje rangu te caktuar te vlerave, qe jan dhene, duke ditur limitet e rangut

# variablaE = 6
# for i in range(0, variablaE):
#     print(i)
    
# Perdorimi i for loop ne List, Tuple, String dhe Dictionary

##########################################    

list1 = ["Python", "per", "student", "te", "BCS-se"]

for k in list1:
    print(k)
    
##########################################    
    
tuple1 = ("Python", "per", "student", "te", "BCS-se")

for v in tuple1:
    print(v)
    
##########################################    
    
string1 = "Python"

for s in string1:
    print(s)    
    
##########################################    
    
set1 = {1,2,3,4,5,6,7,8,9}

for e in set1:
    print(e)