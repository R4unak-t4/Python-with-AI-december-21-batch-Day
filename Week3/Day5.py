'''
Question 1: Class Inheritance & Method Overriding

Create a class Employee with the following:

Attributes: name, salary

Method: get_annual_salary() that returns the yearly salary

Create a subclass Manager that:

Adds an attribute bonus

Overrides get_annual_salary() to include the bonus

Task:
Write the classes and demonstrate their usage with at least one Employee and one Manager object.

Question 2: Encapsulation & Property Decorators

Create a class BankAccount that:

Has a private attribute __balance

Has methods deposit(amount) and withdraw(amount)

Prevents withdrawal if the amount is greater than the balance

Use @property to create a read-only attribute balance.

Task:
Implement the class and show how encapsulation protects the balance from direct modification.

Question 3: Polymorphism & Abstract Base Classes

Create an abstract base class Shape with an abstract method area().

Create two subclasses:

Rectangle (attributes: length, width)

Circle (attribute: radius)

Task:
Implement the area() method in each subclass and write a function that takes a list of shapes and prints their areas using polymorphism.
'''
'''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

cat = Cat()
print(cat.sound())
dog =Dog()
print(dog.sound())
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_annual_salary(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus
    def get_annual_salary(self):
        return (self.salary * 12) + self.bonus

emp = Employee("Raunak",10000)
mgr = Manager ("Abhishek",12000, 2000)
print(f"{emp.name}'s annual salary : ${emp.get_annual_salary()}")
print(f"{mgr.name}'s annual salary : ${mgr.get_annual_salary()}")