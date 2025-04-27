# Perjashtimet

while True:
    try: 
        numri = int(input("Jep nje numer :"))
        assert(numri % 2 == 0) # AssertionError is thrown if the condition is false
    except AssertionError:
        print("Wow your number was not an even number!")
    else:
        print("You have dodged a bullet")
        break
    
   