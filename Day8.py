# Non-primitive Data type
# Data Type made up of multiple or same kind of primitive data types
# collection of primitive data types.

# primitive Data types

# int
# float
# str
# bool

# list

# list are enclosed in big brackets --> [ ]
# list allows multiple data types
# list is indexed data type

info = [63.4,20,"Raunak",True]
# index: 0   1      2      3

# index wise access
# print(info[3])

# for in loop in list

# info = [63.4,20,"Raunak",True] -->
# i = 63.4
# i = Raunak
# i = True

# for i in info:
#     print(i)

# Task use while loop to iterate over the info list
# Hint : use access by index

# info = [63.4,20,"Raunak",True]
# i = 0
# while i < len(info):
#     print(f'index of {info[i]} is {i}')
#     i+=1

# list operations

# .append()
# [63.4,20,"Raunak",True]--> info.append(5) --> [63.4, 20, 'Raunak', True, 5]
# info.append(5)
# print(info)

# .clear()
# [63.4,20,"Raunak",True]--> []
# info.clear()
# print(info)

# .index()
# print(info.index(63.4))

# .pop()
# [63.4,20,"Raunak",True]--> info.pop() --> [63.4, 20, 'Raunak']
# print(info.pop())
# print(info)

# replacing values in list
# [63.4,20,"Raunak",True] --> info[1] = 30 --> [63.4,30,"Raunak",True]
# info[1] = 30
# print(info)

# .insert()
# [63.4,20,"Raunak",True] --> info.insert(index_value, element) --> [63.4,"KTM",20,"Raunak",True]
#                                              1        "KTM"
# info.insert(1,"KTM")
# print(info)

# Task

# Take input from user for 5 items' price

# store those prices in a list

# run a for in loop to calculate the total price

# print the final total amount with 13% V.A.T

# Hint for VAT :
# print(100*0.13)