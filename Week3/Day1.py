# OOP (Object Oriented Programming)

# class
class car:

    # Attributes
    Wheels = 4

    # Constructor
    def __init__(self,color,headlight,speed,spoiler):
        self.color = color
        self.headlight = headlight
        self.speed = speed
        self.spoiler = spoiler

    # Methods
    def accelerate(self):
        print('Car is accelerating')

    def brake(self):
        print('Car is stopped')

# creating an object of the class.
myCar = car('red','square','60 KM/H',True)

# Accessing attribute of an object
# print(myCar.color)

# changing the value of an attribute
# myCar.color = 'Red'
# print(myCar.color)

# using methods
# myCar.accelerate()
# myCar.brake()


