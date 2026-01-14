# encapsulation

# protecting the attributes

class Car:
    # Attributes
    wheels = 4
    headlight_status = False

    # Constructor
    def __init__(self,color,headlight,speed,spoiler,fuel):
        self.__color = color
        self.headlight = headlight
        self.speed = speed
        self.fuel = fuel
        self.spoiler = spoiler

    #getter (Accessor)
    def get_color(self):
        return self.__color

    #setter (Mutator)
    def set_color(self,color):
        self.__color = color

myCar = Car('red','square','60 KM/H',True,'50 L')

myCar.set_color('yellow')
print(myCar.get_color())

class BankAccount:
    def __init__(self, name, balance):
        self.__name = name          # private
        self.__balance = balance    # private
        self.__transaction = 0

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction+=1

    def withdraw(self, amount):
        if amount <= self.__balance and amount > 0:
            self.__balance -= amount
            self.__transaction+=1
        else:
            print('Invalid amount')

    def set_name(self,name):
        if type(name) == str and len(name) > 2:
            self.__name = name
        else:
            print("Invalid name")

    def get_transaction(self):
        return self.__transaction

'''
Question 1: Add Validation (Setter Method)

Create a method set_name(new_name) that:
Allows changing the name only if:
new_name is a string

Length is more than 2 characters
Otherwise print "Invalid name"
Test the method using an object.
'''
acc = BankAccount("raunak",2000)
acc.set_name('thapa')
print(acc.get_name())
'''
Modify the withdraw() method so that:

If the amount is greater than balance, print
"Insufficient balance"

If amount is zero or negative, print
"Invalid amount"

Otherwise deduct the amount normally.
'''

'''
Make the balance read-only:
Remove any way to directly change balance from outside the class.
Only deposit() and withdraw() should change the balance.
Demonstrate that trying to modify balance directly fails.
Explain why this is encapsulation.
'''

'''
Add a private variable __transactions that:
Starts from 0
Increases by 1 every time:

deposit is successful

withdraw is successful

Create a getter method get_transactions() to display the count.
'''
print(acc.get_transaction())
acc.deposit(1000)
print(acc.get_transaction())
acc.withdraw(1000)
print(acc.get_transaction())
'''
Create a new class called StudentAccount that demonstrates encapsulation.

Requirements:

Private variables:

__student_name

__marks

Constructor should initialize both variables.

Create methods:

get_name()

get_marks()

set_marks(new_marks)

Allow marks only between 0 and 100

Otherwise print "Invalid marks"
Create a method grade() that:

Returns "A" if marks ≥ 80
"B" if marks ≥ 60
"C" if marks ≥ 40
"Fail" otherwise
Create an object and demonstrate all methods.
'''