# OOP (Object Oriented Programming)

# class
class car:
    # Attributes
    Wheels = 4
    headlight_status = False

    # Constructor
    def __init__(self,color,headlight,speed,spoiler,fuel):
        self.color = color
        self.headlight = headlight
        self.speed = speed
        self.fuel = fuel
        self.spoiler = spoiler

    # Methods
    def accelerate(self):
        print('Car is accelerating')

    def brake(self):
        print('Car is stopped')

    def increase_speed(self,speed):
        arr = self.speed.split(' ')
        curr_speed = int(arr[0])
        curr_speed = curr_speed+speed
        self.speed = f'{curr_speed} {arr[1]}'

    def drive(self,distance):
        if int(self.fuel.split(' ')[0]) * 10 >= distance:
            fuel_required = distance/10
            new_fuel = int(self.fuel.split(' ')[0]) - fuel_required
            self.fuel = f'{new_fuel} L'
            print(self.fuel)
        else:
            print("Not enough fuel")

    def toggle_headlight(self):
        if self.headlight_status:
            self.headlight_status = False
            print('Headlight is OFF')
        else:
            self.headlight_status = True
            print('Headlight is ON')

# creating an object of the class.
myCar = car('red','square','60 KM/H',True,'50 L')

# Accessing attribute of an object
# print(myCar.color)

# changing the value of an attribute
# myCar.color = 'Red'
# print(myCar.color)

# using methods
# myCar.accelerate()
# myCar.brake()

'''
increase_speed(20)
--------------------------
60 KM/H --> 80 KM/H
'''
# myCar.increase_speed(20)
# print(myCar.speed)

'''
Add a new attribute called fuel to the car class that stores fuel in liters (e.g., "50 L").
Create a method called drive(distance) that:
Takes distance in kilometers
Reduces fuel by 1 liter per 10 km

Prints:
    "Not enough fuel" if fuel is insufficient

    Otherwise updates and displays remaining fuel
    
Fuel before: 50 L
drive(100)
Fuel after: 40 L

'''
myCar.drive(100)
'''
Create a method called toggle_headlight() that:
Turns the headlight ON if it is OFF
Turns the headlight OFF if it is ON
Prints the current headlight status

Assume:
    headlight = "ON" or "OFF"
    
Headlight is ON
toggle_headlight()
Headlight is OFF

'''
myCar.toggle_headlight()
myCar.toggle_headlight()
'''
Create a separate class called Driver with the following:
Attributes:
    name
    age

Method:
    drive_car(car_object)

This method should:
    Print the driver’s name
    Call the accelerate() method of the passed car object

Example behavior:
Driver John is driving the car
Car is accelerating
'''
