# Exercise with classes
# 1 - Create a class Car(Name)
# 2 - Create a class Engine(Name)
# 3 - Create a class Manufaacturer(Name)
# 4 - Make the conection between Car and the Engine
# Obs.: An engine can belong to several cars
# 5 - Make the connection between Car and the Manufacturer
# Obs.: A manufacturer can produce several cars
# Print the car's name, engine and manufacturer on the screen.
class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._manufacturer = None

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value

class Engine:
    def __init__(self, name, engine=False):
        self.name = name
        self.engine = engine

    def turn_on(self):
        if self.engine:
            return f'{self.engine} is already turned on...'
        
        self.engine = True
        return f'{self.name} is turned on...'

    def turn_off(self):
        if not self.engine:
            return f'{self.engine} is already turned off...'

        self.engine = False
        return f'{self.name} is turned off...'

class Manufacturer:
    def __init__(self, name):
        self.name = name


yaris = Car('Yaris')
engine = Engine('V6')
manufacturer = Manufacturer('Toyota')
yaris.engine = engine
yaris.manufacturer = manufacturer
print(yaris.name, yaris.manufacturer.name, yaris.engine.name)
print(yaris.engine.turn_on())
print(yaris.engine.turn_off())