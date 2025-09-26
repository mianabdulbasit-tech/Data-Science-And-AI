# A functions is a block of code which only runs when it is called 
# You can  pass data ,known as parameters, into a function.
# Function can return data as a result.
# In Python ,a function is defined using the def keyword

# define a functions
def greed_user():
    print("hello world")
#greed_user()

def aoa():
    print("Aslam o alikom")
#aoa()

def aoa(name):
    print(f"aslam o alikom",name)

# aoa("MAB")

# Recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
# print(factorial(3))

# lambda functions

x = lambda a: a + 10
print(x(5))












