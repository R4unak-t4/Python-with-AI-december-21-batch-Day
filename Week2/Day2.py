# Functions

# Functions are reusable block of code.

# it takes input and gives certain output.

# function takes input and gives output

# The parameters are the variables that is declared when defining a function, arguments are the values that we pass when calling the function.

# g = 67
# def my_function(x, y):
#     g = x
#     print(g)
#     z = 2*x+y
#     print(f'When x is {x}, y is {y} then z is {z}')
# print(f'g is {g}')
# my_function(2,4)
# my_function(3,5)
# my_function(4,7)
# my_function(5,8)

# Task : take first name and last name as input parameters for the function and print "my name is First_name Last_name"

# def namer(firstName, lastName):
#     print(f'My name is {firstName} {lastName}')
#
# namer('raunak', 'thapa')

# return
# def namer(firstName, lastName):
#     print(f'My name is {firstName} {lastName}')
#
#
# num = len("raunak")
# print(num)

def name_length(f, l):
    total_length = len(f) + len(l)
    return total_length
num = name_length("raunak", 'Thapa')
print(num)

