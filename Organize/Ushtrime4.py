import numpy as np
# Loops ne Python

for a in range(0,10):
   print("Good Morning!")
   
   
# Per lista

list1 = ["Agon","Ramadani","is","a","programmer"]

for str in list1:
    print(str)


# Per array -- normally they are not fixed in python ,
# the one underneath is though, cause it is special.

arr = np.array(["A","B","C","D"])

for element in arr:
    print(element)

# Per Sets -- mutable, no duplicates

my_set = {"Connection","Affection",4,True,False}

for e in my_set:
    print(e)

# Per Tuple -- immutable

my_tuple = (4,5,6,7,8,9,10,2.3)

i = 0

while i < len(my_tuple):
    
   fuckoff = my_tuple[i]
    
   print(fuckoff)
    
   i += 1
