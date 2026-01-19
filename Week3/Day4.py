# polymorphism

class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')


class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)

    def eat(self):
        print(f'{self.name} is eating a bone')

bruno = Dog('bruno')
bruno.eat()

bird = Animal('bird')
bird.eat()
'''
Create a base class called Vehicle with methods:

accelerate(self): Prints "The vehicle is accelerating."

brake(self): Prints "The vehicle is braking."

honk(self): Prints "The vehicle is honking."

Create two subclasses:

Car, which overrides the accelerate method to print "The car is speeding up!"

Bike, which overrides the honk method to print "The bike rings its bell."

Create a function called perform_actions(vehicle) that accepts a Vehicle object as an argument and calls the accelerate(), brake(), and honk() methods on it. The function should work for any Vehicle subclass.
'''

class Vehicle:

    def accelerate(self):
        print("The vehicle is accelerating.")

    def brake(self):
        print("The vehicle is braking.")

    def honk(self):
        print("The vehicle is honking.")

class Car(Vehicle):
    def accelerate(self):
        print("The car is speeding up!")

class Bike(Vehicle):
    def brake(self):
        print("The bike rings its bell.")



bk = Bike()

def perform_actions(vehicle):
    vehicle.honk()
    vehicle.brake()
    vehicle.accelerate()

perform_actions(bk)