
# Detyra per fajll te trete

# # Kontrolli i rrjedhjes ne Python
# # Gjendjet if/else
#
# # Nese numri eshte me i madh se 0 atehere numri eshte pozitive
# # Nese numri eshte me i vogel se 0 atehere numri eshte negativ
# # Nese numri eshte i barabarte me 0 atehere numri eshte neutral
#
# variabla = -10
#
#
#
# # Kombinimi i gjendjes if me nje kushtezim pointues
# if variabla > 0:
#     print("Variable A vlere pozitive")
#
#
# # Kombinimi i gjendjes if me gjendjen else
# if variabla > 0:
#     print("Variable A vlere pozitive")
# else:
#     print("Variabla A ka vlere negative")
#
#
# # Kombinimi i gjendjes me if me gjendjen else dhe me printimin rrjedhes - i ekzekutueshem
# if variabla > 0:
#     print("Variable A vlere pozitive")
# else:
#     print("Variabla A ka vlere negative")
# print("Kjo gjendje çdo here eshte e ekzekutueshme, behet run!!")
#
# # Perdorimi i gjendjes if, else dhe else-if
#
# variablaB = 0
#
# if variablaB > 0:
#  print('Variabla B ka vlere pozitive')
# elif variablaB < 0:
#  print('Variabla B ka vlere negative')
# else:
#  print('Variabla B ka vlere neutrale, eshte 0. Pra B - ', variablaB)
# print('Kjo gjendje eshte çdohere e ekzekutueshme!!')

x = 5

funksioniY = 2*x+3
funksioniZ = 33 - x
funksioniT = 55+(1-x)
if x > 0:
    print('x-i eshte pozitiv andaj funksioni Y = ',funksioniY)
elif x < 0:
    print('x-i eshte negativ andaj funksioni Z = ',funksioniZ)
else:
    print('x-i eshte neutral andaj funksioni Y = ',funksioniT)