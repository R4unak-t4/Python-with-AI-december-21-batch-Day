# Build a CLI calculator
# 1.Take First number input from user (int)
num1 = int(input("Enter a number : "))
# 2.Take Second number input from user (int)
num2 = int(input("Enter second number : "))
# 3.Take operation input from user : +, -, *, /
operator = input("Enter the operation (+, -, *, /) : ")
# 4.Use if-else ladder to perform those operations
if operator.strip() == '+':
    print(float(num1+num2))
elif operator.strip() == '-':
    print(float(num1-num2))
elif operator.strip() == '*':
    print(float(num1*num2))
elif operator.strip() == '/':
    print(num1/num2)
# 5.if the user's operator input is invalid display appropriate message
else:
    print("Invalid operator")
# 6.Note : the output printed should be in float datatype
