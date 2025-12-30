# Method Overloading is not directly supported in Python as it is in some other languages.
# However, we can achieve similar functionality using default arguments or variable-length arguments(*args, **kwargs).

# Operator Overloading in Python
# This example demonstrates how to overload the '+' operator for a custom Complex number class.
# __magic-method__ __add__ is defined to handle the addition of two Complex objects.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

c1 = Complex(2, 3)
c2 = Complex(4, 5)
print(f"Complex Number 1: {c1.real} + {c1.imag}i")
print(f"Complex Number 2: {c2.real} + {c2.imag}i")

c3 = c1 + c2
print(f"Result of addition: {c3.real} + {c3.imag}i")
