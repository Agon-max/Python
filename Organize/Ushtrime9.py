# import math ka disa metoda matematikore

import math as m

class Algebra1:
    calculations = 0
    def is_real_num(self,numri):
        if   numri > 0 and m.sqrt(numri):
             print("This is a real number...") 
             Algebra1.calculations += 1
        else:
             print("This is not a real number it has an imaginary value.")
             

# num_from_user = int(input("Provide a number to see if it is imaginary in a square root : "))

# algebra = Algebra1()

# algebra.is_real_num(num_from_user)


class Algebra2:
      
      def __init__(self, name):
          self.__name = name
          
      def get_name(self):
          print(self.__name)   
      

alg = Algebra2("Agon")

alg.get_name()