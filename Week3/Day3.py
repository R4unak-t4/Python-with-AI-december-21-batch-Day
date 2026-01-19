# inheritance

class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')


class Dog(Animal):
    def __init__(self,breed,name):
        super().__init__(name)
        self.breed = breed

    def bark(self):

        print(f'{self.name} is barking')

bruno = Dog('pug','bruno')
bruno.eat()

class GuardDog(Dog):
    def __init__(self,duty_hours,breed,name):
        super().__init__(breed,name)
        self.duty_hours = duty_hours

    def guard(self):
        super().bark()

'''
Using the same code structure you were given, complete the following tasks:

Task:

Create a new child class called GuardDog that inherits from Dog.

Add a new attribute duty_hours to the GuardDog class.

Use super() in the GuardDog constructor to initialize breed, name.

Add a method guard() that:

First calls the bark() method from the Dog class using super()

Then prints:

Guard dog is on duty for <duty_hours> hours


Create an object of GuardDog and call the guard() method.
'''

