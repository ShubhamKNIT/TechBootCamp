# @property - Property Decorator is used to define methods as a property in a class that can be accessed like attributes.
# It helps define getter, setter and deleter methods in a class.
# Usage: It allows to manage the access to private attributes of a class.

# Naming Conventions:
# variable - Public Variable Naming Convention
# _variable - Protected Variable Naming Convention
# __variable - Private Variable Naming Convention


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    @property # Getter method for width
    def width(self):
        return f"{self._width:.2f} units"

    @property # Getter method for height
    def height(self):
        return f"{self._height:.2f} units"
    
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Width cannot be negative.")
        self._width = value

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative.")
        self._height = value

    @width.deleter
    def width(self):
        del self._width
        print("Width attribute deleted.")

    @height.deleter
    def height(self):
        del self._height
        print("Height attribute deleted.")


if __name__ == "__main__":
    # Creating an instance of Rectangle
    rect = Rectangle(5, 10)
    print(f"Width: {rect.width}")
    print(f"Height: {rect.height}")

    # Updating width and height using setter methods
    rect.width = 15
    rect.height = 20
    print(f"Updated Width: {rect.width}")
    print(f"Updated Height: {rect.height}")

    # Commenting out deleter methods to demonstrate AttributeError
    try:
        del rect.width
        del rect.height
    except AttributeError as e:
        print("AttributeError: Delete method for the property is undefined") 