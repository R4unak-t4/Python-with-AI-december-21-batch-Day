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