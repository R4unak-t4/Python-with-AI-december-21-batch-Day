# Iterative statements

# for in , while loop

# For in loop

# While
# while (condition) --> boolean value --> True/ False:
is_door_open = True
timer = 0 # seconds

# timer > 5 --> is_door_open : False
# while timer <= 5:
#     if timer == 3:
#         timer = timer + 1
#         continue
#     print(f'Time in seconds : {timer} s')
#     timer = timer + 1
#
# print("The door is now closed")

# Task
# Note : use while loop
# 1. Take input from user of two number (int)
# 2. calculate the sum of those numbers
# 3. after calculation ask for user input if they want to continue (str)
# 4. if the user input is no, break the program
# 5. if the user input is yes continue the program as it is

desc_system = True
while desc_system :
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    print(num1+num2)
    desc = input("Do you want to continue? : ")
    if desc.strip().lower() == "no":
        desc_system = False
# input --> "  no   " == "no"
# "__no___" == "no" --> "no"
# "NO".lower == "no" --> "no"

# For in loop
for i in range(5):
    print(i)

# Task door open timer program with for loop
print("Door opened!")
for timer in range(1,6):
    print(f'Timer in seconds : {timer} s')
print("Door is closed")


# range(5) --> range(0,5) --> [0,1,2,3,4]
# i = 0
# i = 1
# i = 2
# i = 3
# i = 4
# a,b  --> a : start, b-1 : end