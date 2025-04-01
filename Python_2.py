#  Perdorimi i operatoreve aritmetik

# a = 7
# b = 2

# # Operatori i mbledhjes (addition)
# print("Shuma : ", a + b)

# # Operatori i zbritjes (subtraction)
# print("Zbritja  : ", a - b)

# # Operatori i shumëzimit (multiplication)
# print("Shumezimi : ", a * b)

# # Operatori i pjestimit (division)
# print("Pjestimi : ", a / b)

# # Operatori i mbetjes (module)
# print("Mbetja : ", a % b)

# # Operatori i pjestimit rrafshues (floor division)
# print("Floor Division : ", a // b)

# # Operatori i fuqizimit (exponent, power)
# print("Fuqizimi : ", a ** b)


##########################################################################

# Operatoret Assignment  

# Assignment operator = 

# Equals

# c = 7

# Addition operator "+=" : ((x += 1) == (x = x + 1))
# Subtraction operator "-=" : ((x -= 1) == (x = x - 1))
# Multiplication operator "*=" : ((x *= 1) == (x = x * 1))
# Division operator "/=" : ((x /= 1) == (x = x / 1))
# Remainder operator "%=" : ((x %= 1) == (x = x % 1))
# Exponent operator "**=" : ((x **= 1) == (x = x ** 1))


# Detyre perdori te gjithe operatoret e qasjes ne nje detyre te vetme.

# Two variables : 

# var1 = 5
# var2 = 9

# # Formula : 

# var1 += var2
# var1 -= var2
# var1 *= var2
# var1 /= var2
# var1 %= var2
# var1 **= var2

# print("Kalkulimi i juaj : ", var1)



# Comparison operators (Operatoret e krahasimit ne Python) 
# Perdoren per te krahasuar dy vlera variabla
# kthejne nje rezultat te tipit boolean : true apo false

# Operatoret e krahasimit jane: 

# A eshte e barabarte me (is equal to) ==
# Operatori jo i barabarte (not equal to) !=
# Operatori me i madh se (greater than) >
# Operatori me i madh se ose barazi me , >=
# Operatori me i vogel se (less than) <
# Operatori me i vogel ose barazi me, <=

# Shembuj me operatoret e krahasimit:

# y = 6
# z = 6
# t = 8

# print('A eshte "y" e barabarte me "t" : ', y == t)
# print('A eshte "y" me e vogel se "t" : ', y < t)
# print('A eshte "y" jo baraz me "t" : ', y !=t)
# print('A eshte "y" me vogel ose baraz me "t" : ', y <=t)
# print('A eshte z me e madhe se y : ', z > y)
# print('A eshte z me e madhe se ose baraz me y + t : ', z>= (y +t))


# Operatoret logjike ne Python 
# Perdoren per te kontrolluar gjendjen e vlerave per 
# shikohen kombinimet e TRUE dhe/ose FALSE

# Operatoret Logjike : 

# 1. Operatori DHE (AND) - vendimi eshte TRUE vetem nese te dy kushtet jane TRUE

# 2. Operatori OSE (OR) - vendimi eshte TRUE vetem nese njeri nga operandet eshte TRUE

# 3. Operatori i Negacionit/Mohimit (NOT) - vendimi eshte TRUE kur operandi eshte FALSE dhe anasjelltas


# Shembull operatori AND : 

# print(True and True)
# print(True and False)

# print(False and False)
# print(False and True)

# Shembull operatori OR : 

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# Shembull operatori OR : 

# print(not True)
# print(not False)

# Shembull i kombinimit te operatoreve

# print(not(True or False) and (not False or True))

# Le te jete dhene nje funksion m = 3n + k -1v
#  funksionin f(m)= m or n and m + v
#  dhe funksioni f(t) = n or m and dhe jo(v + m)
# Nese vlera e n = 5, k = 6, dhe v = 2
# A eshte funksioni f(m) dhe f(t), funksion tautologji

# m = 19 
# f(m) = 19 or 5 and 21 = false
# f(t) = 5 or 19 and not(21) = false 

# Konkluzioni : Nuk eshte tautologji (Pra, false)




