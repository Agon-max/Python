# Operatoret Bitwise 

a = 5 # 0101
b = 11 # 1011

# Operatori AND (&)  

c = a & b

# Operatori OR (|)

c = a | b

# Operatori NOT (~)

c = ~a # ku ka zero, bëhet një
c = ~b # ku ka një, bëhet zero

# Operatori XOR (^)

c = a ^ b

# XOR =>
# 0 - 0 => 0
# 0 - 1 => 1
# 1 - 0 => 1
# 1 - 1 => 0

# Operatori right dhe left shift 

c = a >> 2 # 'a' esht i zhvendosur per dy bita nga ana e djathte

c = b << 2 # 'b' eshte i zhvendosur per dy bita nga ana e majte

# Operatoret special ne Python : IDENTITY dhe MEMBERSHIP, qe njihen si operatore special
# Operatori identity, perdoret per te kontrolluar pjesen e memories nese eshte e zene apo jo,
# kur dy vlera jane te alokuara ne te njejten vend memorik. Kjo tregon se dy variabla nuk eshte e 
# domosdoshme te jen identike.

# Identity -- is, is not.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) # Kjo kthen true pasi qe 'b' eshte objekt qe direkton tek 'a'- ja, e kunderta kthen false
print(a is c) # Kjo kthen false pasi qe edhepse 'a' -ja dhe 'c' -ja e kane te njejten vlere, ato direktojne ne objekte specifike te ndara ne memorie


# Membership -- in, not in

myList = [1, 2, 3, 4, 5]

print(3 in myList) # True

print(6 not in myList) # True

print(5 not in myList) # False


# Kjo punon edhe me stringje 

fjalia = "Pershendetje."

print("e" in fjalia) # True

# Print the whole string characters 

for s in fjalia:
    print(s) # 👌
    
    
    