# Duck typing is a concept in Python where the type or class of an object is 
# less important than the methods it defines or the behavior it exhibits.

# The idea is summarized by the phrase "If it looks like a duck and quacks like a duck,
# it must be a duck." This allows for more flexible and dynamic code.

# In simple terms, it only checks wherether an object has the required methods and properties,
# rather than checking the actual type of the object.


class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())

