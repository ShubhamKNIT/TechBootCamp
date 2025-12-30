# Polymorphism through Method Overriding and Abstraction
# Polymorphism allows methods to do different things based on the object
# that it is acting upon. This can be achieved through method overriding
# in inheritance and through abstraction using abstract classes.

from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
class Pizza(Circle):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius
    
shapes = [Circle(5), Square(4), Triangle(3, 6)]
for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


pizza = Pizza(7)
print(f"The area of the Pizza is: {pizza.area()}")