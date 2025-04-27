# Rekurzioni ne metoda

def faktorieli(x):
    """
    This is my recursion example 
    """
    if x == 1:
      return 1
    else:
      return (x * faktorieli(x - 1))

print(faktorieli(9))


""" Let's create another """

# Fn = Fn-1 + Fn-2

def fib(number):
    if number <= 1:
        return number
    return fib(number - 1) + fib(number - 2)

print(fib(3))
     

def new_fib(key, memo={}):
    if key in memo:
        return memo[key]
    if key <= 1:
        return key
    memo[key] = new_fib(key - 1, memo) + new_fib(key - 2,memo)
    return memo[key]

print(new_fib(9))

# Funksioni anonim ne Python

fun = lambda : print("Hello")

fun()


calculation = lambda x,y: print(x + y) 

calculation(1,5)