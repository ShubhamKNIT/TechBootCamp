# super() - Used to call a method from the parent class.
# It is commonly used in the __init__ method to initialize
# attributes of the parent class in the child class.
# It can also be used to call other methods from the parent class.

# Use case: 
# 1. To avoid redundancy when initializing attributes in child classes.
# 2. To extend the functionality of inherited methods.

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"A {self.color} shape that is {'filled' if self.is_filled else 'not filled'}.")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"\nIt is circle with area {3.14 * self.radius * self.radius}.")
        return super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, side_length):
        super().__init__(color, is_filled)
        self.side_length = side_length

    def describe(self):
        print(f"\nIt is square with area {self.side_length * self.side_length}.")
        return super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height
    
    def describe(self):
        print(f"\nIt is triangle with area {0.5 * self.base * self.height}.")
        return super().describe()

circle = Circle("Red", True, 5)
square = Square("Blue", False, 4)
triangle = Triangle("Green", True, 3, 6)

print(f"Circle: Color={circle.color}, Filled={circle.is_filled}, Radius={circle.radius}")
print(f"Square: Color={square.color}, Filled={square.is_filled}, Side Length={square.side_length}")
print(f"Triangle: Color={triangle.color}, Filled={triangle.is_filled}, Base={triangle.base}, Height={triangle.height}")

circle.describe()
square.describe()
triangle.describe()