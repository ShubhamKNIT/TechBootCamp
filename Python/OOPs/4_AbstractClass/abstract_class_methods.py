# Abstraction - It is the process of hiding the complex 
# implementation details and showing only the essential 
# features of the object.

# Abstract Class - A class that contains one or more
# abstract methods. An abstract method is a method that is declared,
# but contains no implementation.
# Inheriting from an abstract class requires the subclass
# to implement all abstract methods.

# abc = Abstract Base Class module
from abc import ABC, abstractmethod

# Abstract Vehicle class
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Car class inheriting from Vehicle
class Car(Vehicle):
    def go(self):
        print("The car is moving.")

    def stop(self):
        print("The car has stopped.")

# Bike class inheriting from Vehicle
class Bike(Vehicle):
    def go(self):
        print("The bike is moving.")

    def stop(self):
        print("The bike has stopped.")

car = Car()
bike = Bike

car.go()
car.stop()